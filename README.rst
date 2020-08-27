########################################################################################
### LogTool applies you to export all ERRORs/WARINGS from log files located locally. ###
#######################################################################################

Let's say that you have log files under: /var/log path directory on your host and that you might want
to export all Errors happened after some timestamp, for example after: 2020-08-25 12:00:00.

For that purpose you'll need to edit conf.ini file and to provide:
1) time_grep=2020-08-25 12:00:00
2) log_root_dir=['var/log']
Note: there are additional parameters in conf.ini file and each of them 

Once conf.ini is ready you can start LogTool process by: python LogTool.py conf.ini

After 
 







