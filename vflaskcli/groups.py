import click

class VFlask(click.Group):
    def __init__(self, name, commands, **attrs):
        super().__init__(name, commands, **attrs)
        self.state = {"parent_dir":"app", "host":"localhost", "port":5000}

    def get_command(self, ctx, cmd_name):
        cmd =click.Group.get_command(self,ctx,cmd_name)
        if cmd:
            return cmd
        else:
            matches = [matching_cmds for matching_cmds in self.list_commands(ctx) if matching_cmds.startswith(cmd_name)]
            if matches:
               if len(matches) == 1:
                    return click.Group.get_command(self, ctx, matches[0])
            else:
                return None
        ctx.fail("Check these similar commands {}".format('\n'.join(sorted(matches))))
                

            

