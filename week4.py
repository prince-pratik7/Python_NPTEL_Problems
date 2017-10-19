Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d={}
>>> for l in"qwertyuiop":
	d[l]=l

	
>>> d["q"]
'q'
>>> d.keys()
dict_keys(['q', 'u', 'y', 'r', 'p', 'i', 'e', 't', 'o', 'w'])
>>> list(d.keys())
['q', 'u', 'y', 'r', 'p', 'i', 'e', 't', 'o', 'w']
>>> d.values()
dict_values(['q', 'u', 'y', 'r', 'p', 'i', 'e', 't', 'o', 'w'])
>>> total=0
>>> total=total+d.values()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    total=total+d.values()
TypeError: unsupported operand type(s) for +: 'int' and 'dict_values'
>>> sorted(l)
['p']
>>> l.sort()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l.sort()
AttributeError: 'str' object has no attribute 'sort'
>>> sort(d.values())
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    sort(d.values())
NameError: name 'sort' is not defined
>>> d.values().sort()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d.values().sort()
AttributeError: 'dict_values' object has no attribute 'sort'
>>> d[10]=a
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d[10]=a
NameError: name 'a' is not defined
>>> d[10]=1
>>> d.values()
dict_values(['q', 'u', 'y', 'r', 'p', 'i', 'e', 't', 1, 'o', 'w'])
>>> sorted(d.keys())
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    sorted(d.keys())
TypeError: unorderable types: int() < str()
>>> d.keys()=["q,w,e,r,t,y,u,i,o,p"]
SyntaxError: can't assign to function call
>>> d[10]
1
>>> d[10]=a
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d[10]=a
NameError: name 'a' is not defined
>>> d[10]="a"
>>> sorted(d.keys())
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    sorted(d.keys())
TypeError: unorderable types: int() < str()
>>> 
