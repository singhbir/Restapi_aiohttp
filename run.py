"""
used to run app
"""
from aiohttp import web
from views import AgentMethods, SystemMethods

APP = web.Application()
APP.router.add_view("/agent", AgentMethods)
APP.router.add_view("/system", SystemMethods)
web.run_app(APP)
