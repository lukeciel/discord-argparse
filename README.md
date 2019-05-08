discord_argparse
================

Provides support for arbitrarily ordered arguments in commands for the
[discord.py](https://github.com/Rapptz/discord.py/) library.

```python
param_converter = ArgumentConverter(
    turns = RequiredArgument(
        int,
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


# The command below can be called by ...
# !quiz pokemon
# !quiz pokemon turns=12
# !quiz pokemon images=false turns=12

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


Installation
------------

Simply drop the source file anywhere in your project. Installation via `pip` is
not available at the moment.


Documentation
-------------

Initialize an `ArgumentConverter` as in the example above, annotate a
keyword-only function argument in your command with the instance and,
optionally, set its default value by using the `.defaults()` method. Setting a
default value can be omitted if you use required arguments (otherwise it will
raise a `MissingRequiredArgument` exception).

Inside the command, you can access the arguments as a dict.
