@echo off
cd C:\Users\zrz19\Desktop\Python����\�ҵ�pypi��\WheelDecide
python setup.py sdist build
twine upload dist/*
start https://github.com/Jason4zh/WheelDecide/
start https://pypi.org/project/WheelDecide/
pause