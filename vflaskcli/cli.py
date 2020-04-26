from .groups import VFlask
from .utils import get_full_location, set_environment
import click
from flask.cli import run_command

@click.group("vflask" ,cls=VFlask, commands={})
def vflask_cli():
    '''
        CLI for VFlask
    '''

#callbacks
#uwsgi CB
def get_file_location(ctx, params, value):
    if not value:
        click.echo("Please specifiy the filename", err=True)
        ctx.exit()
    else:
        location = get_full_location(value, vflask_cli.state.get("parent_dir"))
        if location:
            vflask_cli["uwsgi"] = location
        else:
            click.echo("No such file found under location {}".format(vflask_cli.state.get('parent_dir')), err=True)
            ctx.abort()

#--version CB
def show_version(ctx,params,value):
    if not value or ctx.resilient_parsing:
            return
    click.echo("Version 1.0.0")
    ctx.exit()
#callbacks ends here

@vflask_cli.command("deploy",short_help="Run the server based on the flavour specification", epilog="VRAJ Incorporation Initiative")
@click.option(
    "prod_env", "--isproduction", "-PD", 
    type=bool, default=False, flag_value=True,
    help="Specify the environment, defaults to developement env", 
    is_flag=True, 
    show_default=True
)
@click.option(
    "app_dir", "--app-directory", "-A", 
    type=str, 
    default=vflask_cli.state.get('parent_dir'),
    help="Name of the app directory",
    show_default=True,
)
@click.option(
    "uwsgi","--uwsgi-config", "-U", 
    type=str,
    help="Configuration file location of uWSGI for production environment"
)
@click.option(
    "host", "--host", "-H",
    type=str,
    default=vflask_cli.state.get("host"),
    help="Name of the host to deploy the server",
    show_default=True
)
@click.option(
    "port", "--port", "-P",
    type=int,
    default=vflask_cli.state.get("port"),
    help="Port Value for running the server",
    show_default=True
)
@click.option(
    "--version", "-V", 
    is_eager=True, 
    is_flag=True, 
    expose_value=False,
    callback=show_version,
    flag_value=True
)
@click.pass_context
def delpoy_server(ctx, prod_env, app_dir, uwsgi, host, port):
    app_loc = get_full_location("__init__.py", app_dir)
    if app_loc:
        set_environment(FLASK_APP=app_loc, FLASK_ENV="production" if prod_env else "development")
        if prod_env:
            if uwsgi:
                #get_file_location
                click.echo("Under construction")
            else:
                click.echo("Kindly use uWSGI implementation and Nginx for production deployment")
        ctx.invoke(run_command, host=host, port=port)
    else:
        click.echo("Kindly specify a proper location or name of app directory")
        ctx.exit()