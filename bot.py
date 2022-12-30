#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import pyromod.listen

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from config import LOGGER
from user import User

from plugins.webcode import bot_run
from os import environ
from aiohttp import web as webserver

PORT_CODE = environ.get("PORT", "8080")

class Bot(Client):
    USER: User = None
    USER_ID: int = None

def __init__(self):
        super().__init__(
            Config.BOT_SESSION,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            plugins={
                "root": "plugins"
            },
            workers=4,
            bot_token=Config.BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        print(f"{usr_bot_me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on @{usr_bot_me.username}.")
         
        client = webserver.AppRunner(await bot_run())
        await client.setup()
        bind_address = "0.0.0.0"
        await webserver.TCPSite(client, bind_address, PORT_CODE).start()

        self.bot_info = usr_bot_me
        self.set_parse_mode("html")
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        usr_bot_me = await self.get_me()
        msg = f"@{usr_bot_me.username} stopped. Bye."
        await super().stop()
        print(msg)
