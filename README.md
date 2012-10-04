daemonize
=========
python daemon with thread-safe logging handlers

See
http://www.anattatechnologies.com/q/2011/09/python-daemon/

The test_daemon.py script can be used to demonstrate a fully detatched thread-safe process (with no terminal output) but that maintains logging to file (or syslog, or whatever the logging facility). The only logging facility that shouldn't work is (naturally) the terminal itself.