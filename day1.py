Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('qwerty')
qwerty
>>> 7+6
13
>>> 6.3/3
2.1
>>> (4+8)/2
6.0
>>> (-5+2)+1
-2
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> 2^2
0
>>> 2**3
8
>>> 9**(1/2)
3.0
>>> //
SyntaxError: invalid syntax
>>> \\
SyntaxError: unexpected character after line continuation character
>>> 7//2
3
>>> "he\'s a boy"
"he's a boy"
>>> """today is friday"""
'today is friday'
>>> """"today is friday""""
SyntaxError: EOL while scanning string literal
>>> today
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    today
NameError: name 'today' is not defined
>>> """today...is...friday"""
'today...is...friday'
>>> print(1+2)
3
>>> print(today\nis\nfriday)
SyntaxError: unexpected character after line continuation character
>>> print("today\nis\nfriday")
today
is
friday
>>> input("enter the\ninput")
enter the
inputthis is inpt
'this is inpt'
>>> print("addition"+"of"+'strings'+"is"+'called'+"concatenation")
additionofstringsiscalledconcatenation
>>> print("addition\n"+"of\n"+'strings\n'+"is\n"+'called\n'+"concatenation.")
addition
of
strings
is
called
concatenation.
>>> 2+2
4
>>> "2"+'2'
'22'
>>> 2+'2'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    2+'2'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> clrscr
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    clrscr
NameError: name 'clrscr' is not defined
>>> "one"+'2'
'one2'
>>> "string*3"
'string*3'
>>> print("string*3")
string*3
>>> printf("string"*3)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    printf("string"*3)
NameError: name 'printf' is not defined
>>> print("string"*3)
stringstringstring
>>> 2+3
5
>>> "2"+"3"
'23'
>>> int("2")+int("3")
5
>>> float(input("enter a no."))+float(input("enter another no."))
enter a no.4
enter another no.6
10.0
>>> x=7
>>> print(x)
7
>>> print(x*3)
21
>>> x="this is string"
>>> print("x"+!)
SyntaxError: invalid syntax
>>> print(x+"!")
this is string!
>>> foo="a string"
>>> foo
'a string'
>>> bar
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    bar
NameError: name 'bar' is not defined
>>> del bar
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    del bar
NameError: name 'bar' is not defined
>>> del foo
>>> foo
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    foo
NameError: name 'foo' is not defined
>>> foo=input("enter a no.")
enter a no.6
>>> foo
'6'
>>> x="strings"
>>> x+="eggs"
>>> x
'stringseggs'
>>> 
