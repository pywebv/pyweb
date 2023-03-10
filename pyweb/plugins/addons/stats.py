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

from pyrogram.types import Message
from pyweb import Web, filters
from pyweb.plugins.helpers import db


@Web.cmd(extra_filters=~filters.edited & ~filters.service, group=2)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = await db.get("users", msg.from_user.id)
        if not q:
            await db.set("users", msg.from_user.id)


@Web.cmd('stats', owner_only=True)
async def stats(_, msg: Message):
    users = await db.count("users")
    await msg.reply(f"Total Users : {users}", quote=True)
