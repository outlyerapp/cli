import click
from outlyer import __version__, __title__


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
    click.echo('list agents %s' % ctx.obj['DEBUG'])


@agent.command("get")
@click.pass_context
@click.argument('name')
def agent_get(ctx, name):
    click.echo('get agent: %s' % name)



def main():
    cli(obj={})