import logging
from oslo_utils import strutils

from cw.common import exception
from cw.common import timeutils
from cw.common import models
from cw.common import utils
from cw.db import db_query
from cw.db.sqlalchemy import api as db_api

LOG = logging.getLogger(__name__)


class DatabaseModelBase(models.ModelBase):
    _auto_generated_attrs = ['id']

    @classmethod
    def create(cls, **values):
        init_vals = {
            'id': utils.generate_uuid(),
            'created': timeutils.utcnow(),
        }
        if hasattr(cls, 'deleted'):
            init_vals['deleted'] = False
        init_vals.update(values)
        instance = cls(**init_vals)
        if not instance.is_valid():
            raise exception.InvalidModelError(errors=instance.errors)
        return instance.save()

    @property
    def db_api(self):
        return db_api

    @property
    def preserve_on_delete(self):
        return hasattr(self, 'deleted') and hasattr(self, 'deleted_at')

    @classmethod
    def query(cls):
        return db_api._base_query(cls)

    def save(self):
        if not self.is_valid():
            raise exception.InvalidModelError(errors=self.errors)
        self['updated'] = timeutils.utcnow()
        LOG.debug("Saving %(name)s: %(dict)s",
                  {'name': self.__class__.__name__,
                   'dict': strutils.mask_dict_password(self.__dict__)})
        return self.db_api.save(self)

    def delete(self):
        self['updated'] = timeutils.utcnow()
        LOG.debug("Deleting %(name)s: %(dict)s",
                  {'name': self.__class__.__name__,
                   'dict': strutils.mask_dict_password(self.__dict__)})

        if self.preserve_on_delete:
            self['deleted_at'] = timeutils.utcnow()
            self['deleted'] = True
            return self.db_api.save(self)
        else:
            return self.db_api.delete(self)

    def update(self, **values):
        for key in values:
            if hasattr(self, key):
                setattr(self, key, values[key])
        self['updated'] = timeutils.utcnow()
        return self.db_api.save(self)

    def __init__(self, **kwargs):
        self.merge_attributes(kwargs)
        if not self.is_valid():
            raise exception.InvalidModelError(errors=self.errors)

    def merge_attributes(self, values):
        """dict.update() behaviour."""
        for k, v in values.items():
            self[k] = v

    @classmethod
    def find_by(cls, context=None, **conditions):
        model = cls.get_by(**conditions)

        if model is None:
            raise exception.ModelNotFoundError("{} Not Found with conditions:{}".format(cls.__name__, conditions))

        if ((context and not context.is_admin and hasattr(model, 'tenant_id')
             and model.tenant_id != context.tenant)):
            msg = "Tenant %(s_tenant)s tried to access %(s_name)s, owned by %(s_owner)s." % {
                "s_tenant": context.tenant, "s_name": cls.__name__,
                "s_owner": model.tenant_id}

            LOG.error(msg)
            raise exception.ModelNotFoundError(msg)

        return model

    @classmethod
    def find_by_filter(cls, **kwargs):
        return db_query.find_by_filter(cls, **cls._process_conditions(kwargs))

    @classmethod
    def get_by(cls, **kwargs):
        return db_api.find_by(cls, **cls._process_conditions(kwargs))

    @classmethod
    def find_all(cls, **kwargs):
        return db_query.find_all(cls, **cls._process_conditions(kwargs))

    @classmethod
    def _process_conditions(cls, raw_conditions):
        """Override in inheritors to format/modify any conditions."""
        return raw_conditions


    @classmethod
    def get_dict_by(cls, **kwargs):
        db_info = cls.find_by(**kwargs)
        return dict((k, db_info[k]) for k in cls._data_fields)
