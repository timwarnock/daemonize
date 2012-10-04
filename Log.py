# vim: set tabstop=4 shiftwidth=4 autoindent smartindent:
'''
simple thread-safe logging adapter

Assigns log handlers to the logging module, you can use logging module methods directly or
create additional loggers that will inherit these handlers, e.g.,

import Log, logging
logging.info('hello world')

import Log, logging
spam = logging.getLogger('spam')
spam.info('hello from spam')

import Log, logging as log
log.info('hello world')

'''
import logging

def init(LOG_FILE=False, LOG_CONSOLE=False, LOG_SYSLOG=False):

	# remove all root handlers
	for handler in logging.root.handlers:
		logging.root.removeHandler(handler)

	# Log to file
	if LOG_FILE:
		logging.basicConfig(
			filename=LOG_FILE,
			level=logging.INFO,
			format='%(asctime)-15s %(levelname)s:%(filename)s:%(lineno)d -- %(message)s'
		)

	# Log to console
	if LOG_CONSOLE:
		console = logging.StreamHandler()
		console.setLevel(logging.DEBUG)
		console.setFormatter(logging.Formatter('%(levelname)s:%(filename)s:%(lineno)d -- %(message)s'))
		logging.getLogger().addHandler(console)

	# Log to syslog
	if LOG_SYSLOG:
		from logging.handlers import SysLogHandler
		syslog = SysLogHandler(address='/dev/log')
		syslog.setFormatter(logging.Formatter('%(asctime)-15s %(levelname)s:%(filename)s:%(lineno)d -- %(message)s'))
		logging.getLogger().addHandler(syslog)

