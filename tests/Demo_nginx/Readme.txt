This is a Demo scenario.
Python Unittest and NGINX server are used to demonstrate the ability of LogTool.

1) setUp - is used to set the "time_grep" in *.ini file
2) test_restart_nginx - is supposed to reboot NGINX, but "nginx stop" is commented out.
   means that the nbginx will try to start and bind the same port again and again.
   As the result Errors are logged in its log file under /var/log/nginx
3) tearDown - here is where LogTool is activated and digging into the logs.
   We need to get the Error logged in NGINX /var/log/nginx/error.log for example:

    [stack@undercloud-0 tests]$ cat Test_Restart_Errors.log

    #################### Exported unique messages, per STANDARD OSP log file since: 2020-11-24 08:21:16####################

    ------------------------------ LogPath: /var/log/nginx/error.log ------------------------------
    IsTracebackBlock:False
    UniqueCounter:1
    AnalyzedBlockLinesSize:12
    BlockDate:2020-11-24 08:20:04
    Log:/var/log/nginx/error.log
    1:2020/11/24 08:20:04 [emerg] 687399#0: bind() to 0.0.0.0:8888 failed (98: Address already in use)
    2:2020/11/24 08:20:04 [emerg] 687399#0: bind() to [::]:80 failed (98: Address already in use)
    3:2020/11/24 08:20:04 [emerg] 687399#0: bind() to 0.0.0.0:8888 failed (98: Address already in use)
    4:2020/11/24 08:20:04 [emerg] 687399#0: bind() to [::]:80 failed (98: Address already in use)
    5:2020/11/24 08:20:04 [emerg] 687399#0: bind() to 0.0.0.0:8888 failed (98: Address already in use)
    ...
    ...
    ...
    zahlabut --> THIS BLOCK IS TOO LONG!
    zahlabut --> POTENTIAL BLOCK'S ISSUES:
    08:20:04 [emerg] 687399#0: bind() to 0.0.0.0:8888 failed (98: Address already in use)
                                                  ^^^^^^