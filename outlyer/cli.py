import click
from outlyer import __version__, __title__
from outlyer import api
from outlyer import util


@click.group()
@click.pass_context
@click.version_option(prog_name=__title__, version=__version__)
@click.option('--debug', help='Debug mode', default=False, is_flag=True)
@click.option('--config', help='Config YAML File', type=str)
@click.option('--url', help='API Endpoint', type=str)
@click.option('--org', help='Organization Name', type=str)
@click.option('--account', help='Account Name', type=str)
@click.option('--key', help='API Key', type=str)
def cli(ctx, debug, config, url, org, account, key):
    file_config = util.load_file_config(config)
    ctx.obj = util.merge_config(ctx.obj, file_config)

    cmd_config = {
        'DEBUG': debug,
        'url': url,
        'org': org,
        'account': account,
        'key': key
    }
    ctx.obj = util.merge_config(ctx.obj, cmd_config)


############################################################
# AGENT GROUP
############################################################
@cli.group("agents")
@click.pass_context
def agent_cmd(_):
    pass


@agent_cmd.command("list")
@click.pass_context
def agent_list(ctx):
    agents = api.list_agents()
    click.echo('list agents %s' % agents)


@agent_cmd.command("get")
@click.pass_context
@click.argument('name')
def agent_get(ctx, name):
    agent = api.get_agent(name)
    click.echo('get agent: %s' % agent)


############################################################
# ENTRY POINT
############################################################
def main():
    cli(obj={
        'api_url': 'https://app.dataloop.io/api/v1',
    })
