from botbase.core.bot import Red
from .modlog import ModLog


def setup(bot: Red):
    bot.add_cog(ModLog(bot))
