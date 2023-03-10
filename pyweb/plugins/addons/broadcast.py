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

from pyweb import Web, Message
from pyweb.plugins.helpers import db


@Web.cmd("broadcast", owner_only=True)
async def broadcast(bot: Web, msg: Message):
    if not msg.reply_to_message and len(msg.command) == 1:
        await msg.reply("Please reply to a message or pass some text", quote=True)
        return
    text = msg.reply_to_message.text if msg.reply_to_message else msg.text[len("/broadcast "):]
    users = await db.get_all_primary_keys("users")
    await msg.reply_text("Starting Broadcast...")
    count = 0
    for user in users:
        try:
            await bot.send_message(user, text)
            count += 1
        except Exception as e:
            Web.log(f"Exception occurred while sending message to user with id {user}: {e}", "warning")
    await msg.react(f"Broadcast done successfully to {count} users out of {len(users)}")
