# PyWeb - Python add-on extension to Pyrogram
# Copyright (C) 2023-2024 PyWebV <https://github.com/pywebv>
#
# This file is part of PyWeb.
#
# PyWeb is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyWeb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyWeb. If not, see <https://www.gnu.org/licenses/>.

from pyweb import Web
from pyweb.plugins.web import MAIN_BUTTONS
from pyrogram.types import InlineKeyboardMarkup
from pyweb.plugins.helpers import replace, send_buttons, module, LOADED_BUT_EMPTY


@Web.cmd('start', description="Start the bot", private_only=True)
async def start_func(bot: Web, msg):
    try:
        if not module.START:
            Web.log(LOADED_BUT_EMPTY.format("start", "start"), "warn")
            return
        text = await replace(module.START, msg, bot)
        if await send_buttons():
            await msg.react(text, reply_markup=InlineKeyboardMarkup(MAIN_BUTTONS))
        else:
            await msg.react(text)
    except AttributeError:
        pass


@Web.cmd('start', description="Start the bot", group_only=True)
async def start_in_groups_func(bot: Web, msg):
    try:
        if not module.START_IN_GROUPS:
            return  # No warning
        text = await replace(module.START_IN_GROUPS, msg, bot)
        await msg.react(text)
    except AttributeError:
        pass
