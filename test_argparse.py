import pytest
import discord_argparse as da
from discord.ext import commands

def custom_converter(s):
    return int(s)

@pytest.mark.asyncio
async def test_argparse():
    converter = da.ArgumentConverter(
        str1 = da.RequiredArgument(str),
        int1 = da.OptionalArgument(int, default=1),
        bool1 = da.OptionalArgument(bool),
        int2 = da.OptionalArgument(custom_converter)
    )

    with pytest.raises(da.InvalidArgumentValueError):
        await converter.convert(None, "str1=test int1=abc")
    
    with pytest.raises(da.InvalidArgumentValueError):
        await converter.convert(None, "str1=test bool1=abc")

    with pytest.raises(da.InvalidArgumentValueError):
        await converter.convert(None, "str1=test int2=abc")
    
    with pytest.raises(da.InvalidArgumentValueError):
        await converter.convert(None, "str1=test int2=2.71")
    
    with pytest.raises(commands.MissingRequiredArgument):
        await converter.convert(None, "int2=1")
    
    with pytest.raises(da.UnknownArgumentError):
        await converter.convert(None, "unknown=true")
    
    args = await converter.convert(None, "str1='test abc'")
    assert(args["str1"] == "test abc")

    args = await converter.convert(None, "str1=test int1=12 bool1=true int2=-1")
    assert(args["str1"] == "test")
    assert(args["int1"] == 12)
    assert(args["bool1"] == True)
    assert(args["int2"] == -1)

    args = await converter.convert(None, "str1=test")
    assert(args["int1"] == 1)