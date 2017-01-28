# -*- coding: utf-8 -*-
import os

from tornado.options import parse_command_line, define, options
from tornado.platform.asyncio import AsyncIOMainLoop
from tornado.web import Application
import RPi.GPIO as GPIO

from handlers import *

log = logging.getLogger('casopro')

define('port', type=int, default=8080, help='port to listen on')
define('address', default='0.0.0.0', help='network address to listen on')
define('debug', type=bool, default=False, help='enable debug mode')
define('switchtime', type=float, default=0.05, help='time in seconds for switching on relays')


def handlers():
    return [
        (r'/rest(/(up|down|watt|power))', RestHandler),
        (r'/(.*)', CustomStaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'static')}),
    ]


def setup_gpio():
    _channels = dict(power=12,
                     watt=16,
                     up=18,
                     down=22)
    log.debug('GPIO version: %s' % str(GPIO.VERSION))
    _chans = [i for i in _channels.values()]
    log.debug('using channels: {}'.format(_chans))
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(_chans, GPIO.OUT, initial=GPIO.HIGH)
    return _channels


def init_app():
    app = Application(handlers=handlers(),
                      debug=options.debug,
                      channels=setup_gpio(),
                      switchtime=options.switchtime,
                      )

    log.info('Application will listen on %s:%d' % (options.address, options.port))
    app.listen(options.port, options.address)
    log.info('READY.')


def main():
    AsyncIOMainLoop().install()

    parse_command_line()

    if options.debug:
        log.debug('Debug mode enabled')

    log.debug('Effective command line options: %s' % options.as_dict())

    log.info('Using delay of %d seconds to switch on GPIO' % options.switchtime)
    setup_gpio()
    init_app()

    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
        log.debug("Cleaning up GPIO")
        GPIO.cleanup()


if __name__ == '__main__':
    main()
