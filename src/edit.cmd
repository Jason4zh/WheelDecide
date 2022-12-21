@echo off
cd C:\Users\zrz19\Desktop\Python整活\我的pypi包\WheelDecide
python setup.py sdist build
twine upload dist/*
start https://github.com/Jason4zh/WheelDecide/
start https://pypi.org/project/WheelDecide/
pause