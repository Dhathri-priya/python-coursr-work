Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#printing text
print("heloo")
heloo
#printing numltiple items

name= priya
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    name= priya
NameError: name 'priya' is not defined. Did you mean: 'print'?
name = "priya
SyntaxError: unterminated string literal (detected at line 1)
name = "priya"
age= 25
print("name:",name, "age:",age)
name: priya age: 25


#seperator
print("2024", "02", "07", sep="-")
2024-02-07

#end
print("Hello,", end=" ")
Hello, 
print("world!")
world!


#new line
print("Line 1/nLine 2")
Line 1/nLine 2
print("Line 1\nLine 2")
Line 1
Line 2


#tab

print("Name:\taLice")
Name:	aLice
>>> 
>>> 
>>> 
>>> #using commas
>>> 
>>> name = "priya"
>>> age = 25
>>> score = 34.4
>>> print("Name:", name, "Age:", age, "Score:", score)
Name: priya Age: 25 Score: 34.4
>>> 
>>> 
>>> 
>>> #using % operator
>>> 
>>> name = "Bob"
... age = 30
... score = 88.75print("Name: %s | Age: %d | Score: %.2f" % (name, age, score))
SyntaxError: multiple statements found while compiling a single statement
>>> name = "Bob"
>>> age = 30
>>> score = 88.75print("Name: %s | Age: %d | Score: %.2f" % (name, age, score))
SyntaxError: invalid decimal literal
>>> score = 88.75print("Name: %s | Age: %d | Score: %.2f" % (name, age, score))
SyntaxError: invalid decimal literal
>>> score = 88.75
>>> print("Name: %s | Age: %d | Score: %.2f" % (name, age, score))
Name: Bob | Age: 30 | Score: 88.75
>>> 
>>> 
>>> 
>>> #using f string
>>> name = "Bob"age = 30
SyntaxError: invalid syntax
>>> name = "priya"
>>> age = 12
>>> score = 495.4
>>> print(f"Name: {name} | Age: {age} | Score: {score:.2f}")
Name: priya | Age: 12 | Score: 495.40
