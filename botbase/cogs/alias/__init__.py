from .alias import Alias
from botbase.core.bot import Red


def setup(bot: Red):
    bot.add_cog(Alias(bot))
