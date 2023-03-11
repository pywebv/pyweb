# Import class 'Web' in every plugin
from pyweb import Web, Message


# use 'Web.cmd' decorator to create commands
# @Web.cmd(cmd=None, description=None, owner_only=False, extra_filters=None, group=0, private=False) - defaults

@Web.cmd('sample', "Sample command for bot")  # or @Web.command('sample', description="...")
async def sample_function(bot: Web, msg: Message):
    # 'msg.react()' is 'msg.reply()' with del_in added argument
    await msg.react('This will be the reply when /sample is sent.')
