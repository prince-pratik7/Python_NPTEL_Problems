Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s="            hello         "
>>> s
'            hello         '
>>> s.rstrip()
'            hello'
>>> s.lstrip()
'hello         '
>>> s.strip()
'hello'
>>> s="brown fox red dog brown fox"
>>> 
>>> s.find("dog")
14
>>> s.find("d")
12
>>> s.find("cat")
-1
>>> s.index("cat")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.index("cat")
ValueError: substring not found
>>> s
'brown fox red dog brown fox'
>>> s.replace("brown","black")
'black fox red dog black fox'
>>> s
'brown fox red dog brown fox'
>>> s.replace("brown","black",1)
'black fox red dog brown fox'
>>> s="asasasas"
>>> s.replace("as",DD)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.replace("as",DD)
NameError: name 'DD' is not defined
>>> s.replace("as","DD")
'DDDDDDDD'
>>> date="12"
>>> month="3"
>>> year="2017"
>>> today="_".join([date,month,year])
>>> today
'12_3_2017'
>>> today="-".join([date,month,year])
>>> today
'12-3-2017'
>>> s="hello"
>>> s.ljust(10,-)
SyntaxError: invalid syntax
>>> s.ljust(10,'-')
'hello-----'
>>> s.center(50)
'                      hello                       '
>>> s.rjust
<built-in method rjust of str object at 0x02D915E0>
>>> s.rjust(25,'*')
'********************hello'
>>> s
'hello'
>>> s.isalpha()
True
>>> s.numeric()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.numeric()
AttributeError: 'str' object has no attribute 'numeric'
>>> 
