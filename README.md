# Django PTVSD Debug

A little manage.py tweak to attach a PTVSD debugger during runserver. 
Built with WSL development in mind since we have to treat it like remote in apps like VSCode (for now...)

## Usage


1. Add django_ptvsd to your INSTALLED_APPS _above_ Django

```
INSTALLED_APPS = (
    'django_ptvsd',
    ...
)
```

2. pass `--ptvsd` flag to runserver command

```
django-admin runserver --ptvsd
```

## Django Settings

`PTVSD_ENABLE = False` Attach PTVSD by default. No need for `--ptvsd` flag

`PTVSD_REMOTE_ADDRESS = '0.0.0.0'` - Which address to listen on

`PTVSD_REMOTE_PORT = 5678` - Which port to listen on

`PTVSD_WAIT_FOR_ATTACH = False` - Whether or not to wait for attach before continuing
