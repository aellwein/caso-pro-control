# -*- coding: utf-8 -*-
import asyncio
import logging

import RPi.GPIO as GPIO
from tornado.web import StaticFileHandler, RequestHandler

log = logging.getLogger('handlers')


class CustomStaticFileHandler(StaticFileHandler):
    def parse_url_path(self, url_path):
        _path = url_path
        if url_path.strip() == '':
            _path = './index.html'
        if url_path.endswith('/'):
            _path = url_path + 'index.html'
        return super(CustomStaticFileHandler, self).parse_url_path(_path)


class RestHandler(RequestHandler):
    def initialize(self):
        self.channels = self.settings["channels"]

    async def get(self, *args, **kwargs):
        if len(args) < 2:
            self.send_error(500)
            return
        _action = args[1]
        result = await self.handle_action(_action)
        self.write(result)

    async def handle_action(self, action):
        GPIO.output(self.channels[action], GPIO.HIGH)
        await asyncio.sleep(0.05)
        GPIO.output(self.channels[action], GPIO.LOW)
        return '%s executed' % action
