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


from ..config import ENV
from typing import Union
from ..logger import logger
from pyrogram import filters as f
from pyrogram.methods.decorators.on_callback_query import OnCallbackQuery


class Callback(OnCallbackQuery):
    @staticmethod
    def callback(
        query: Union[str, list[str]] = None,
        startswith: bool = False,
        owner_only: bool = False,
        sudo_only: bool = False,
        group: int = 0,
        filters=None
    ):
        """This decorator is used to handle callback queries. All arguments are optional.

        Parameters:

            query (str | list[str], optional): Query on which your function is called. Defaults to None, to handle all queries if your function handles all or if using 'filters'

            startswith (bool, optional): Set to True if you want your function to handle all queries starting with the query_string. Defaults to False.

            owner_only (bool, optional): Allow only owner to use this command. Defaults to False.

            sudo_only (bool, optional): Allow only sudos to use this command. Includes owner as sudo automatically. Defaults to False.

            group (int, optional): Define a group for this handler. Defaults to 0. [Read More](https://docs.pyrogram.org/topics/more-on-updates#handler-groups)

            filters (pyrogram.filters, optional): Extra filters to apply in your function. Import ``filters`` from pyrogram or pyweb to use this. See example below.

        Examples:

            ```python
            from pyweb import Web

            # The normal and easiest way.
            # Bot will execute function, if button with callback_data 'first_button' is pressed/clicked.
            @Web.callback('first_button')

            # Handle multiple callback queries in one function. Mainly used to show same result or do some other pythonic thing, like if-else loop.
            # Bot will execute same function, if 'first_button' or 'second_button' is pressed/clicked.
            @Web.callback(['first_button', 'second_button'])

            # Function will only be triggered if owner presses the button, that is, the user whose id is set as OWNER_ID in environment variables.
            # Others will be ignored.
            @Web.callback('first_button', owner_only=True)

            # Function will only be triggered if sudo users or owner presses the button, that is, users set as SUDO_USERS or OWNER_ID in environment variables.
            # Others will be ignored.
            @Web.callback('first_button', sudo_only=True)

            # Filter/Handle all queries.

            # Use positive integer to execute after executing another function in default group that also filtered this query.
            @Web.callback(group=1)

            # or Use negative integer to execute before executing another function in default group that also filtered this query.
            @Web.callback(group=-1)

            # Don't use this as other functions that handle queries won't work.
            @Web.callback()

            # Filter other type of queries using 'filters' argument.

            # Import filters from pyrogram or pyweb.
            from pyweb import filters

            # Filter only queries by 'TheHamkerXD' and 'xD_Anonymous'.
            @Web.callback(filters=filters.user(['TheHamkerXD', 'xD_Anonymous']))

            # Filter only queries done in 'pyweb_chat'
            @Web.callback(filters=filters.chat('pyweb_chat'))

            # Filter only queries ending with the word 'baby'.
            @Web.callback(filters=filters.regex(r'baby$'))

            # Filter all queries with the word 'hello' AND which are done in 'pyweb_chat'.
            @Web.callback(filters=filters.chat('pyweb_chat') & filters.regex('hello'))
            # or
            @Web.callback('hello', filters=filters.chat('pyweb_chat'))

            # Filter all queries with the word 'bots' OR which are done in 'pyweb_chat'
            @Web.callback(filters=filters.chat('pyweb_chat') | filters.regex('hello'))

            # Filter all queries with the word 'bots' BUT which are NOT done in 'pyweb_chat'
            @Web.callback(filters=~filters.chat('pyweb_chat') & filters.regex('hello'))
            # or
            @Web.callback(filters=filters.regex('hello') & ~filters.chat('pyweb_chat'))
            ```
        """
        # ToDo:
        #   case_sensitive argument
        if isinstance(query, list):
            cmd_filter = f.create(lambda _, __, query_: query_.data.lower() in query)
        elif isinstance(query, str):
            query = query.lower()
            if not startswith:
                cmd_filter = f.create(lambda _, __, query_: query_.data.lower() == query)
            else:
                cmd_filter = f.create(lambda _, __, query_: query_.data.lower().startswith(query))
        elif not query:
            cmd_filter = None
        else:
            logger.warn(f'Callback: query cannot be of type {type(query)} - {query}]')
            return
        if filters:
            filters_ = cmd_filter & filters
        else:
            filters_ = cmd_filter
        if sudo_only:
            filters_ = filters_ & f.user(ENV().SUDO_USERS+ENV().OWNER_ID)
        elif owner_only:
            filters_ = filters_ & f.user(ENV().OWNER_ID)
        decorator = OnCallbackQuery.on_callback_query(filters_, group)
        return decorator

    cb = callback  # alias
