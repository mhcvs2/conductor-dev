from oslo_config import cfg

CONF = cfg.CONF


class GetAllWorkflowDefs(object):

    @staticmethod
    def args(args):
        args.append('includeTasks')

    @staticmethod
    def run(func, kw_dict):
        res = func(**kw_dict)
        new_res = []
        for wf in res:
            new_wf = dict(
                    name=wf['name']
                )
            if CONF.command.includeTasks:
                new_wf['tasks'] = [t['name'] for t in wf['tasks']]
            new_res.append(new_wf)
        return new_res
