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

from pyrogram.types import InlineKeyboardButton


START = """
Hey {user}

Welcome to {bot}

I can {1}
Use below buttons to learn more.

By @pywebv
"""

HELP = """
{1}

✨ **Available Commands** ✨

{commands}
"""

ABOUT = """
**About This Bot** 

A telegram bot to {1}{2}

Library : [PyWeb](https://github.com/pywebv/pyweb)

Language : [Python](www.python.org)

Developer : @TheHamkerXD
"""

HOME_BUTTON = [
    [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
]

MAIN_BUTTONS = [
    [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/pywebv")],
    [
        InlineKeyboardButton("How to Use ❔", callback_data="help"),
        InlineKeyboardButton("🎪 About 🎪", callback_data="about")
    ],
    [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/pywebv")],
]
