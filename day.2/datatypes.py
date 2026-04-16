Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Data typess

#numerical types
"int-integer"
'int-integer'
product_quality = 3
order_id = 10987432


#float-floating point
product_price = 749.99
discount_percentage = 15.5
average_rating = 4.3


#complex- complex numbers
z = 5 + 2j

#sequence Types
#str-string
customer_name = "rohit sharma"
delivery_address = "Banglore, karnataka"
product_category = "Electronics"


#list-List

cart_items=["shoes", "T-shirt", "headphones"]
top_categories = ["mobile"," Fashion", "Home","beauty"]


#tuple- Tuple
warehouse_location = (12.9716, 77.5946)
Longitude
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    Longitude
NameError: name 'Longitude' is not defined
product_dimensions  = (12.5, 9.8, 2.2) #heights


#set types
#set-set
available_sizes  = {"S", "M", "XL"}












#Frozenset- immmutable set
frozen_tags =  frozenset(["sale", "Limited edition","Trending"])



#mapping type
#dict-dictionary
product_details = {
    "name":"wireless Mouse",
    "brand":"Logitech",
    "price": 899.99,
    "rating": 4.5
...     }
>>> customer_profile = {
...     "name": "anjali verma",
...     "email":"anjali@example.com",
...     "prime_member":True
...     }
>>> 
>>> 
>>> #Boolean Type
>>> #bool- boolean
>>> is_logged_in = True
>>> is_payment_successful = false
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    is_payment_successful = false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> is_payment_successful = Fals
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    is_payment_successful = Fals
NameError: name 'Fals' is not defined. Did you mean: 'False'?
>>> is_payment_successful = False
>>> is_in_stock = True
>>> 
>>> #none type
>>> tracking_number = None
>>> delivery_partner = None
>>> 
>>> 
>>> #checking type in python
>>> 
>>> 
>>> 
>>> print(type(product_price))
<class 'float'>
>>> print(type(cart_items))
<class 'list'>
>>> print(type(is_in_stock))
<class 'bool'>
