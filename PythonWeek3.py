Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
a=100
b=50
result=a+b
print(result)
150
a=100
b=50
result=a+c
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    result=a+c
NameError: name 'c' is not defined
print(a '+' b '=', result))
SyntaxError: unmatched ')'
a=100
b=50
result = a+b
print(result)
150
>>> print (a, '+', b, '=', result)
100 + 50 = 150
>>> print(a '+' b '=', res\
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(a, '+', b, '=', result))
SyntaxError: unmatched ')'
>>> print(a, '+', b, '=', result)
100 + 50 = 150
>>> result=a-b
>>> print (a, '-', b, '=', result)
100 - 50 = 50
>>> result(a*b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    result(a*b)
TypeError: 'int' object is not callable
>>> result(a*b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    result(a*b)
TypeError: 'int' object is not callable
>>> result(a＊b)
SyntaxError: invalid character '＊' (U+FF0A)
>>> result(a﹡b)
SyntaxError: invalid character '﹡' (U+FE61)
>>> result= a*b
>>> print (a, '*', b, '=', result)
100 * 50 = 5000
>>> result = a/b
>>> print(a, '/', b, '=', rsult)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(a, '/', b, '=', rsult)
NameError: name 'rsult' is not defined. Did you mean: 'result'?
>>> print(a, '/', b, '=', result)
100 / 50 = 2.0
>>> exit()
>>> exit()
