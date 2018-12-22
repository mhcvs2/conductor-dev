from cw.db.models import DatabaseModelBase


class DBUser(DatabaseModelBase):
    _data_fields = ['id', 'name', 'age']
