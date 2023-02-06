Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
print("Rosewater")
Rosewater
type("Rosewater")
<class 'str'>
type(0.001)
<class 'float'>
type(37)
<class 'int'>
type(False)
<class 'bool'>

#problem2
egg = 2
cake = 5
print ("with", egg, "eggs" + cake, "cakes")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print ("with", egg, "eggs" + cake, "cakes")
TypeError: can only concatenate str (not "int") to str
print ("with", egg, "eggs", cake,"cakes")
with 2 eggs 5 cakes
first = "Krista"
last = "Dockery"
print(first + last)
KristaDockery
>>> 
>>> #problem3
>>> int(42.6)
42
>>> float(34)
34.0
>>> str(2)
'2'
>>> bool(2)
True
>>> 
>>> print("hello\n new")
hello
 new
>>> #problem4
...  
>>> print("hello\nnew\nworld\nsunny\ndays\nahead")
hello
new
world
sunny
days
ahead
>>> 
>>> #problem5
>>> flour = 2
>>> milk = 1
>>> egg = 4
>>> oil = 0.4
>>> vanilla = 0.012
>>> 
>>> cake = 2 * flour + 0.5 (milk - egg + vanilla) + oil**2
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    cake = 2 * flour + 0.5 (milk - egg + vanilla) + oil**2
TypeError: 'float' object is not callable
>>> cake = 2 * flour + 0.5 * (milk - egg +vanilla) + oil**2
>>> print(cake)
2.6660000000000004
