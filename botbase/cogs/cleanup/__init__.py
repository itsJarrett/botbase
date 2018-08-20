from .cleanup import Cleanup
from botbase.core.bot import Red


def setup(bot: Red):
    bot.add_cog(Cleanup(bot))
