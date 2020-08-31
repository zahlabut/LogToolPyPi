
### LogTool applies you to export all ERRORs/WARINGS from log files located locally.
## General
Let's say that you have log files under: /var/log path directory on your host and that you might want to export all Errors happened after some timestamp, for example after: 2020-08-25 12:00:00.
For that purpose you'll need to edit conf.ini file and to provide:
1) time_grep=2020-08-25 12:00:00
2) log_root_dir=['var/log']
<br>**Note:** there are additional parameters in conf.ini with detailed explanation comments. 
## Instalation
    pip install LogTool
## Configuration file
Create conf.ini file basing on example provided in GitHub: https://github.com/zahlabut/LogToolPyPi/blob/master/conf.ini 
<br>**Note:** change the configuration accordingly.
## Usage
    from LogTool import *
    load_conf_file('conf.ini') # To load cnfiguration file.
    start_analyzing() # To start analyzing log files.







