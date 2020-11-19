# install the package with "pip3 install zahlabut"
# Edit conf.ini file according your needs
from zahlabut.LogTool import *               # To import all from zahlabut LogTool package
load_conf_file('conf.ini')                   # To load the cofiguration file (conf.ini).
result=start_analyzing()                     # Start analyzing log files.
print(result['Standard_Log_Results'][0])     # First item in result list (raw data) for Standard logs.
print(result['Not_Standard_Log_Results'][0]) # First item in result list (raw data) for Not Standard logs.