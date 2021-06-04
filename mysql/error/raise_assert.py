# coding=utf-8
'''
python中assert和raise语句
'''
try:
    raise IOError("File No Exit")
except Exception as e:
    print("IOError:", e)

try:
    assert 7==6, "test assert"
except AssertionError as e:
    print("AssertionError:", e)