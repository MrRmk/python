# coding=utf-8

# a = 0
try:
    a
except Exception as e:
    print("catch Error:", e)
print("exec over")