#!/bin/python
from twitter.common import app
from mworker.common.common import log
from mworker.extend.metedata import MetadataEx
from mworker.extend.workflow import WorkflowEx

sub_commands = ['start', 'get_run', 'stop', 'get', 'get_status']


def help():
    for sc in sub_commands:
        print '- {}'.format(sc)


def proxy_main():
    app.add_option(
        '-s',
        '--server',
        dest='server',
        default='109.105.30.118:8080',
        help='Address for the condustor server')

    @app.command
    @app.command_option(
        '-n',
        '--name',
        dest='name',
        help='')
    @app.command_option(
        '-v',
        '--version',
        dest='version',
        default=1,
        help='')
    @app.command_option(
        '-i',
        '--input',
        dest='input',
        default='{}',
        help='')
    def start(args, options):
        wfc = WorkflowEx("http://%s/api" % options.server)
        if not options.name:
            app.error('lack --name')
        wfc.start(options.name, options.version, options.input)

    @app.command
    @app.command_option(
        '-n',
        '--name',
        dest='name',
        help='')
    @app.command_option(
        '-v',
        '--version',
        dest='version',
        default=1,
        help='')
    @app.command_option(
        '-i',
        '--id',
        dest='id',
        help='')
    @app.command_option(
        '-r',
        '--reason',
        dest='reason',
        default='user terminate',
        help='')
    @app.command_option(
        '-a',
        '--all',
        dest='all',
        type=int,
        default=0,
        help='')
    def stop(args, options):
        url = "http://%s/api" % options.server
        wfc = WorkflowEx(url)
        if options.id:
            wfc.terminateWorkflow(options.id, options.reason)
        elif options.name:
            wfc.stop_by_name(options.name, options.version)
        elif options.all:
            sure = raw_input('Sure to terminate all running workflow? y/n\n')
            if sure.lower() == 'y':
                wf = MetadataEx(url)
                wf_dfs = wf.getAllWorkflowDefs()
                names = [wf_df["name"] for wf_df in wf_dfs]
                for name in names:
                    wfc.stop_by_name(name, options.version)
            else:
                print "Operation canceled"
        else:
            log.error('Nothing to do')

    @app.command
    @app.command_option(
        '-n',
        '--name',
        dest='name',
        help='')
    @app.command_option(
        '-v',
        '--version',
        dest='version',
        default=1,
        help='')
    def get_run(args, options):
        wfc = WorkflowEx("http://%s/api" % options.server)
        if options.name:
            wfc.list_running(options.name, options.version)
        else:
            log.error('lack --name')

    @app.command
    @app.command_option(
        '-i',
        '--id',
        dest='id',
        help='')
    @app.command_option(
        '-t',
        '--task',
        type=int,
        default=0,
        dest='task',
        help='')
    def get_status(args, options):
        wfc = WorkflowEx("http://%s/api" % options.server)
        if options.id:
            wfc.get_workflow(options.id, True if options.task else False)
        else:
            log.error('lack --id')

    @app.command
    @app.command_option(
        '-n',
        '--name',
        dest='name',
        help='')
    @app.command_option(
        '-d',
        '--detail',
        type=int,
        dest='detail',
        help='')
    @app.command_option(
        '-k',
        '--keyword',
        dest='keyword',
        help='')
    def get(args, options):
        url = "http://%s/api" % options.server
        wf = MetadataEx(url)
        name = options.name
        keyword = options.keyword if options.keyword else None
        if name:
            wf.list_a_workflow_detail(name)
        elif options.detail:
            wf.list_workflow_detail(keyword)
        else:
            wf.list_workflow(keyword)

    def main(args, options):
        help()

    app.main()

if __name__ == '__main__':
    proxy_main()
