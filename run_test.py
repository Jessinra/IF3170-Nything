import unittest
import os

"Script to run all test in unit_test folder"

loader = unittest.TestLoader()
start_dir = 'unit_test'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
os.system("pause")