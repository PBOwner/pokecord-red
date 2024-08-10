from redbot.core import commands


@commands.group(name="pcord")
async def pcord(self, ctx: commands.Context):
    """
    Pokecord commands
    """


class PokeMixin:
    """This is mostly here to easily mess with things..."""

    c = poke
