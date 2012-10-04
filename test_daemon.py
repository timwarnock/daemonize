#!/usr/bin/env python
# vim: set tabstop=4 shiftwidth=4 autoindent smartindent:
import os, sys
import logging

#
import Daemon
import Log

if __name__ == "__main__":

	#initialize file and console logging
	Log.init('test_daemon.log', True)

	logging.info('daemonize?')
	retCode = Daemon.daemonize()

	# we are now detatched, but logging to file should still be working
	logging.info('daemonized! we are now safely detached with thread-safe logging')
	procParams = "return code = %s, process ID = %s, parent process ID = %s, process group ID = %s, session ID = %s, user ID = %s, effective user ID = %s, real group ID = %s, effective group ID = %s" % (retCode, os.getpid(), os.getppid(), os.getpgrp(), os.getsid(0), os.getuid(), os.geteuid(), os.getgid(), os.getegid())
	spam = logging.getLogger('spam')
	spam.info(procParams)

	sys.exit(retCode)

