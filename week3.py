Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1=[1,2,3,4,5]
>>> list2=[6,7,8,9]
>>> list1.extend(list2)
>>> list1
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list1.remove(9)
>>> list1
[1, 2, 3, 4, 5, 6, 7, 8]
>>> list3=[4,5,6,7,8]
>>> list1=list1+list3
>>> list1
[1, 2, 3, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8]
>>> while 4 in list1:
	list1.remove(4)

	
>>> list1
[1, 2, 3, 5, 6, 7, 8, 5, 6, 7, 8]
>>> list1.index(6)
4
>>> 
