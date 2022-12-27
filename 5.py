Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=========== RESTART: C:/Users/User/Desktop/pythonpractice/day 6/4.py ===========
3

================================ RESTART: Shell ================================
import math
math.sqrt(2)
1.4142135623730951
math.gcd(24,40)
8

from math import  *
sqrt(2)
1.4142135623730951
gcd(24,40)
8

from math import  sqrt,ged
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    from math import  sqrt,ged
ImportError: cannot import name 'ged' from 'math' (unknown location)
from math import  sqrt,gcd
sqrt(2)
1.4142135623730951
gcd(20,40)
20

================================ RESTART: Shell ================================
fromfrom math import  sqrt,gcd
SyntaxError: invalid syntax




================================ RESTART: Shell ================================

================================ RESTART: Shell ================================
from math import sqrt,gcd
sqrt(2)
1.4142135623730951
gcd(24,40)
8

============================================== RESTART: Shell =============================================
from math import  *
sqrt(2)
1.4142135623730951
gcd(24,40)
8

============================================== RESTART: Shell =============================================
import math
math.sqrt(2)
1.4142135623730951
math.gcd(24,40)
8

============================================== RESTART: Shell =============================================
import math as m
m.sqrt(4)
2.0
>>> m.gcd(24,50)
2
>>> 2
2
>>> 
>>> 
>>> 
>>> m. truncate(4.6)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    m. truncate(4.6)
AttributeError: module 'math' has no attribute 'truncate'
>>> m.floor(9.8)
9
>>> m.ceil(4.6)
5
>>> 
>>> 
>>> m.log(5656,88)
1.9298240372794866
>>> 
>>> 
>>> 
>>> pi=3.14159
>>> r=2.5
>>> h=10**0.5
