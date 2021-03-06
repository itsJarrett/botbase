from pathlib import Path
import asyncio

from botbase.core import checks, commands
from botbase.core.bot import Red
from botbase.core.i18n import Translator, cog_i18n
from botbase.cogs.dataconverter.core_specs import SpecResolver
from botbase.core.utils.chat_formatting import box

_ = Translator("DataConverter", __file__)


@cog_i18n(_)
class DataConverter:
    """
    Cog for importing Red v2 Data
    """

    def __init__(self, bot: Red):
        self.bot = bot

    @checks.is_owner()
    @commands.command(name="convertdata")
    async def dataconversioncommand(self, ctx: commands.Context, v2path: str):
        """
        Interactive prompt for importing data from Red v2

        Takes the path where the v2 install is

        Overwrites values which have entries in both v2 and v3,
        use with caution.
        """
        resolver = SpecResolver(Path(v2path.strip()))

        if not resolver.available:
            return await ctx.send(
                _(
                    "There don't seem to be any data files I know how to "
                    "handle here. Are you sure you gave me the base "
                    "installation path?"
                )
            )
        while resolver.available:
            menu = _("Please select a set of data to import by number, or 'exit' to exit")
            for index, entry in enumerate(resolver.available, 1):
                menu += "\n{}. {}".format(index, entry)

            menu_message = await ctx.send(box(menu))

            def pred(m):
                return m.channel == ctx.channel and m.author == ctx.author

            try:
                message = await self.bot.wait_for("message", check=pred, timeout=60)
            except asyncio.TimeoutError:
                return await ctx.send(_("Try this again when you are more ready"))
            else:
                if message.content.strip().lower() in ["quit", "exit", "-1", "q", "cancel"]:
                    return await ctx.tick()
                try:
                    message = int(message.content.strip())
                    to_conv = resolver.available[message - 1]
                except (ValueError, IndexError):
                    await ctx.send(_("That wasn't a valid choice."))
                    continue
                else:
                    async with ctx.typing():
                        await resolver.convert(self.bot, to_conv)
                    await ctx.send(_("{} converted.").format(to_conv))
            await menu_message.delete()
        else:
            return await ctx.send(
                _(
                    "There isn't anything else I know how to convert here."
                    "\nThere might be more things I can convert in the future."
                )
            )
