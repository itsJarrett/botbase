from botbase.core.bot import Red
from .dataconverter import DataConverter


def setup(bot: Red):
    bot.add_cog(DataConverter(bot))
