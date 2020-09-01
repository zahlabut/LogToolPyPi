
### LogTool - is a tool that extracts all ***UNIQUE ERRORS*** from log files and provides statistics.
## General
Let's say that you have log files located on your host under some path, for example: /var/log/containers
and that you might want to export all Errors happened after some times in order to investigate/debug some problem
happened after some time, for example: 2020-08-25 12:00:00
For that purpose you'll need to set proper values in "conf.ini" file and to provide:
1) time_grep=2020-08-25 12:00:00
2) log_root_dir=['var/log/containers']
<br>**Note:** there are additional parameters in conf.ini with detailed explanation comments. 
## Instalation
    pip install LogTool
## Configuration file
Create **"conf.ini"** file basing on example provided in GitHub: https://github.com/zahlabut/LogToolPyPi/blob/master/conf.ini 
<br>**Note:** change the configuration accordingly.
## Usage
    from LogTool.LogTool import *
    load_conf_file('conf.ini')                   # To load cnfiguration file.
    result=start_analyzing()                     # To start analyzing log files.
    print(result['Standard_Log_Results'])        # Result dictionary for Standard Logs
    print(result['Not_Standard_Log_Results'])    # Result dictionary for Not Standard logs
## Created result files
Result files will be generated according to the settings given in **"conf.ini"** file.

    create_logtool_result_file=yes
    log_tool_result_file = ResultFile.log
    save_standard_logs_raw_data_file='Standard_Logs_Output.log'
    save_not_standard_logs_raw_data_file='Not_Standard_Logs_Output.log'
**Note:** there is detailed explanation per parameter provided in ***"conf.ini"** file.