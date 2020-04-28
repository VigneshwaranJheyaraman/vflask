import os, click, subprocess
def get_full_location(filename, parent_dir_name):
    current_working_dir = os.getcwd()
    if parent_dir_name in current_working_dir:
        path= os.path.join(current_working_dir, filename)
    else:
        path= os.path.join(current_working_dir, parent_dir_name, filename)
    return path if os.path.exists(path) else None

def set_environment(**kwargs):
    for key, value in kwargs.items():
        os.environ[key] = value

def error(msg):
    ctx = click.get_current_context()
    click.secho(msg, fg="red", bold=True, blink=True)
    ctx.abort()

def style_msg(msg,**kwargs):
    click.secho(msg, **kwargs)