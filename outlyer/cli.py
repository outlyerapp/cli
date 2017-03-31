import click
from outlyer import __version__, __title__
from outlyer import api


@click.group()
@click.option('--debug', default=False)
@click.pass_context
@click.version_option(prog_name=__title__, version=__version__)
def cli(ctx, debug):
    ctx.obj['DEBUG'] = debug


############################################################
# AGENT GROUP
############################################################
@cli.group()
@click.pass_context
def agent(ctx):
    pass


@agent.command("list")
@click.pass_context
def agent_list(ctx):
    agents = api.list_agents()
    click.echo('list agents %s' % agents)


@agent.command("get")
@click.pass_context
@click.argument('name')
def agent_get(ctx, name):
    agent = api.get_agent(name)
    click.echo('get agent: %s' % agent)


############################################################
# ENTRY POINT
############################################################
def main():
    cli(obj={})
