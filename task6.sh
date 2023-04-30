#!/bin/bash

# Run test suite
/usr/bin/python3 "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py" --path /Users/Stacey/PycharmProjects/quantium-starter-repo/task5.py

pytest_exit = $?

# Check exit code and return appropriate value
if [ $pytest_exit -eq 0 ]; then
  echo "All tests passed!"
  exit 0
else
  echo "Something went wrong"
  exit 1
fi
