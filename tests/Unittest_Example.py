from zahlabut.LogTool import *
import os
from configparser import SafeConfigParser
from datetime import datetime
import unittest

class NginxTestCases(unittest.TestCase):
    def setUp(self):
        test_start_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        parser = SafeConfigParser()
        parser.read('conf_unittest.ini')
        parser.set('Settings', 'time_grep', test_start_time)
        parser.set('Settings', 'log_tool_result_file', 'Test_Restart_Errors.log')


    def test_restart_nginx(self):
        for x in range(0, 5):
            # os.system('nginx stop')
            os.system('nginx')

    def tearDown(self):
        load_conf_file('conf_home_stack.ini')
        result = start_analyzing()
