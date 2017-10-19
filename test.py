Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d={}
>>> d[[1,2]]=5
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    d[[1,2]]=5
TypeError: unhashable type: 'list'
>>> d[(1,2)]=5
>>> d["1,2"]=5
>>> d
{(1, 2): 5, '1,2': 5}
>>> d[12]=5
>>> pairs = [ (x,y) for x in range(4) for y in range(3) if (x+y)%2 != 0 ]
>>> pairs
[(0, 1), (1, 0), (1, 2), (2, 1), (3, 0), (3, 2)]
>>> marks=[1,2,3,4,5,6]
>>> d
