Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> nested=[[2,[37]],4,["bruce"]]
>>> nested[0]
[2, [37]]
>>> nested[2][0][3]
'c'
>>> nested[2][0:3]
['bruce']
>>> nested[2][1:3]
[]
>>> nested[0][1:2]
[[37]]
>>> nested[1]=7
>>> nested
[[2, [37]], 7, ['bruce']]
>>> list1=[1,3,5,7]
>>> list2=list1
>>> list1[2]=4
>>> list1
[1, 3, 4, 7]
>>> list2
[1, 3, 4, 7]
>>> del(list1)
>>> del(list2)
>>> list1
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> list1=[1,3,5,7]
>>> list2=list1[:]
>>> list1[2]=4
>>> list1
[1, 3, 4, 7]
>>> list2
[1, 3, 5, 7]
>>> list1=[1,3,5,7]
>>> list2=[1,3,5,7]
>>> list3=list2
>>> list1==list2
True
>>> list2==list3
True
>>> list1 is list2
False
>>> list2 is list3
True
>>> 
