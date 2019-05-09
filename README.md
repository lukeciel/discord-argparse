discord_argparse
================

Provides support for arbitrarily ordered arguments in commands for the
[discord.py](https://github.com/Rapptz/discord.py/) library.

```python
param_converter = ArgumentConverter(
    turns = RequiredArgument(
        int, # follows the rules of a converter in discord.py
        doc="The number of turns this quiz has.",
        default=10
    ),
    images = OptionalArgument(
        bool,
        doc="(Dis-)allow image questions.",
        default=True
    ),
    voice_channel = OptionalArgument(
        discord.VoiceChannel
    )
)


@bot.command()
async def quiz(ctx, name:str, *, params:param_converter=param_converter.defaults()):
    await ctx.send("Turns: {0}".format(params['turns']))


@quiz.error
async def quiz_error(ctx, error):
    if isinstance(error, InvalidArgumentValueError):
        await ctx.send(
            "Invalid argument value for parameter {0}".format(error.name)
        )
    elif isinstance(error, UnknownArgumentError):
        await ctx.send(
            "Unknown argument {0}".format(error.name)
        )
```

On your discord server, the commands can be invoked like this:

```
!quiz pokemon
    → will raise a MissingRequiredArgument exception

!quiz pokemon turns=2
    → args["images"] will be True

!quiz pokemon turns=2 images=false
```


Installation
------------

Installation is available via pip:

```
pip install discord_argparse
```


Documentation
-------------

Initialize an `ArgumentConverter` as in the example above, annotate a
keyword-only function argument in your command with the instance and,
optionally, set its default value by using the `.defaults()` method. Setting a
default value can be omitted if you use required arguments (otherwise it will
raise a `MissingRequiredArgument` exception).

Inside the command, you can access the arguments as a dict.


Custom help formatter
---------------------

By using a custom help formatter, you can send a list of all arguments to the
users of your bot. An example output, after sending `!help quiz` to the bot,
might look like this:

```
!quiz <name> <params>

Starts a quiz.
This command will start a quiz.

Example usage: !quiz pokemon turns=12 images=false

Arguments:
    turns           The number of questions this quiz has.
    images          (Dis-)allow image questions.
    voice_channel
```

To make use of the argument list, create a custom [help
command](https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.HelpCommand)
and override the `send_command_help` function like this:

```python
async def send_command_help(self, command):
    self.add_command_formatting(command)
    for name, param in command.clean_params.items():
        if isinstance(param.annotation, da.ArgumentConverter):
            arguments = param.annotation.arguments
            if not arguments:
                continue
            self.paginator.add_line("Arguments:")
            max_size = max(len(name) for name in arguments)

            for name, argument in arguments.items():
                entry = "{0}{1:<{width}} {2}".format(self.indent * " ", name, argument.doc, width=max_size)
                self.paginator.add_line(self.shorten_text(entry))
    self.paginator.close_page()
    await self.send_pages()
```

You might also want to set the `usage` parameter of the `command()` function
decorator to display a better usage string, especially when using the
`ArgumentConvert.defaults()` method.