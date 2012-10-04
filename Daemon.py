# vim: set tabstop=4 shiftwidth=4 autoindent smartindent:
'''
Daemon (python daemonize function)

Detach process through double-fork (to avoid zombie process), close all
file descriptors, and set working directory to root (to avoid umount problems)
'''

import os, resource
import logging

# target environment
UMASK = 0
WORKINGDIR = '/'
MAXFD = 1024
if (hasattr(os, "devnull")):
	REDIRECT_TO = os.devnull
else:
	REDIRECT_TO = "/dev/null"

def daemonize():
	'''Detach this process and run it as a daemon'''

	try:
		pid = os.fork() #first fork
	except OSError, e:
		raise Exception, "%s [%d]" % (e.strerror, e.errno)

	if (pid == 0): #first child
		os.setsid()
		try:
			pid = os.fork() #second fork
		except OSError, e:
			raise Exception, "%s [%d]" % (e.strerror, e.errno)

		if (pid == 0): #second child
			os.chdir(WORKINGDIR)
			os.umask(UMASK)
		else:
			os._exit(0)
	else:
		os._exit(0)

	#close all file descriptors except from non-console logging handlers
	maxfd = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
	if (maxfd == resource.RLIM_INFINITY):
		maxfd = MAXFD
	filenos = []
	for handler in logging.root.handlers:
		if hasattr(handler, 'stream') and hasattr(handler.stream, 'fileno') and handler.stream.fileno() > 2:
			filenos.append( handler.stream.fileno() )
	for fd in range(0, maxfd):
		try:
			if fd not in filenos:
				os.close(fd)
		except OSError:
			pass

	#redirect stdin, stdout, stderr to null
	os.open(REDIRECT_TO, os.O_RDWR)
	os.dup2(0, 1)
	os.dup2(0, 2)

	return(0)

