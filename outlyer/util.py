import os
import sys
import yaml


def load_file_config(instance_config_path):
    if instance_config_path:
        return read_config_file(instance_config_path)
    else:
        return load_global_config()


def load_global_config():
    path = global_config_path()

    if path:
        return read_config_file(path)
    else:
        return {}


def read_config_file(config_path):
    try:
        with open(config_path, 'r') as f:
            return yaml.load(f)

    except Exception as err:
        # print 'Error: failed to read config file: %s' % config_path
        sys.exit(err)


def global_config_path():
    # config location in preference order
    settings_path = [
        os.path.expanduser("~") + '/.outlyer-cli.yaml',
        os.path.expanduser("~") + '/outlyer-cli.yaml',
        os.getcwd() + '/outlyer-cli.yaml',
        # legacy
        os.path.expanduser("~") + '/.dlcli.yaml',
        os.path.expanduser("~") + '/dlcli.yaml',
        os.getcwd() + '/dlcli.yaml',
    ]

    # return the first file that exists
    for path in settings_path:
        if os.path.exists(path):
            return path


def merge_config(base, update):
    c = base.copy()
    sanitized_update = {k:v for k,v in update.items() if v is not None}
    c.update(sanitized_update)
    return c
