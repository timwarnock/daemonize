daemonize
=========
python daemon with thread-safe logging handlers

See
http://www.anattatechnologies.com/q/2011/09/python-daemon/

The test_daemon.py script can be used to demonstrate a fully detatched thread-safe process that maintains logging (to file, syslog, or whatever the logging facility). The only logging facility that wouldn't work is (naturally) the terminal itself, this is demonstrated in the test_daemon.py script