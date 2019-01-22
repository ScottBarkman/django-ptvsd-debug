import os 

from django.contrib.staticfiles.management.commands import runserver
from django.conf import settings


class Command(runserver.Command):
    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument('--ptvsd', action='store_true', dest='use_ptvsd',
            help='Enable PTVSD at runtime',
        )

    def run(self, *args, **options):
        if getattr(settings, 'PTVSD_ENABLE', False) or options['use_ptvsd'] :
            if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):
                ptvsd_address = getattr(settings, 'PTVSD_REMOTE_ADDRESS', '0.0.0.0')
                ptvsd_port = getattr(settings, 'PTVSD_REMOTE_PORT', '5678')
                
                import ptvsd
                ptvsd.enable_attach(address=(ptvsd_address, ptvsd_port))
                print('PTVSD: Enabled Attach ({0}:{1})'.format(ptvsd_address, ptvsd_port))
                if getattr(settings, 'PTVSD_WAIT_FOR_ATTACH', False):
                    print('PTVSD: Waiting for attach...')
                    ptvsd.wait_for_attach()

        super().run(*args, **options)
