Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> "First:{0},Second:{1}".format
<built-in method format of str object at 0x030C30B0>
>>> information.
>>> "First:{0},Second:{1}".format(42,11)
SyntaxError: invalid syntax
>>> "First:{0},Second:{1}".format(42,11)
'First:42,Second:11'
>>> "First:{1},Second:{0}".format(42,11)
'First:11,Second:42'
>>> "one:{f},two:{s}".format(f=11,s=47)
'one:11,two:47'
>>> "one:{f},two:{f}".format(f=11,s=47)
'one:11,two:11'
>>> "one:{s},two:{f}".format(f=11,s=47)
'one:47,two:11'
>>> "one:{f},two:{s}".format(s=47,f=11)
'one:11,two:47'
>>> "value:{0:3d}".format(4)
'value:  4'
>>> "value: {0:3d}".format(4)
'value:   4'
>>> "value:{0:3f}".format(4)
'value:4.000000'
>>> "value:{0:6.2f}".format(47.235)
'value: 47.23'
>>> "value:{0:6.3f}".format(47.235)
'value:47.235'
>>> "value:{0:6.4f}".format(47.2365)
'value:47.2365'
>>> "value:{0:5.4f}".format(47.2365)
'value:47.2365'
>>> "value:{0:3.4f}".format(47.2365)
'value:47.2365'
>>> "value:{0:0.4f}".format(47.2365)
'value:47.2365'
>>> "value:{0:6.2f}".format(47.2365)
'value: 47.24'
>>> 
