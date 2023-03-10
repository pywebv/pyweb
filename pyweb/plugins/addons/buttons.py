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
from pyweb.plugins.web import HOME_BUTTON, MAIN_BUTTONS
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery
from pyweb.plugins.helpers import replace, module, replace_commands


@Web.callback(query=['home', 'about', 'help'])
async def basic_cb(bot: Web, cb: CallbackQuery):
    # No Warns Cuz Personalized
    chat_id = cb.from_user.id
    message_id = cb.message.message_id
    if cb.data == 'home':
        text = await replace(module.START, cb.message, bot)
        buttons = MAIN_BUTTONS
    elif cb.data == 'about':
        text = await replace(module.ABOUT, cb.message, bot)
        buttons = HOME_BUTTON
    else:
        text = str(module.HELP)
        if "{commands}" in text:
            text = await replace_commands(bot, text)
        text = await replace(text, cb.message, bot)
        buttons = HOME_BUTTON
    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True,
    )
