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

import os
from pyweb import Web, Message


@Web.cmd("json", owner_only=True)
async def json(_, msg: Message):
    if not msg.reply_to_message:
        await msg.reply("Please reply to a message", quote=True)
        return
    data = str(msg.reply_to_message)
    if len(data) > 4096:
        with open("message.json", "w", encoding="utf-8") as f:
            f.write(data)
        await msg.reply_document("message.json", quote=True)
        os.remove("message.json")
    else:
        await msg.react(data)


@Web.cmd("jsondoc", owner_only=True)
async def jsondoc(_, msg: Message):
    if not msg.reply_to_message:
        await msg.reply("Please reply to a message", quote=True)
        return
    data = str(msg.reply_to_message)
    with open("message.json", "w", encoding="utf-8") as f:
        f.write(data)
    await msg.reply_document("message.json", quote=True)
    os.remove("message.json")
