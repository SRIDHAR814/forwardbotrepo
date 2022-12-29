from aiohttp import web as webserver

async def bot_run():
    _app = web.Application(client_max_size=30000000)
    _app.add_routes(routes)
    return _app
