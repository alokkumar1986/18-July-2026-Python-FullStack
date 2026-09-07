default parameter

\#==========================



When we call a function, we pass parameters to function body. If we don't pass then we get error. 



There is one way to avoid this error by assigning a default value in the function body.



This parameter is called default parameter.





def sayHello(name='Alice'):

&#x20;  print('Hello', name)



sayHello()



\#output : Hello Alice





def sayHello(name='Alice'):

&#x20;  print('Hello', name)



sayHello('Tom')



\#output  : Hello Tom



Here the default value "Alice" is assigned to name and if we don't pass any parameter the default value will be printed.



If we pass a value as parameter, then default will be overwritten and the passed value will be printed. 







def sayHello(name='Alice', age):

&#x20;  print('Hello', name)

&#x20;  print('Your age :', age)



sayHello(20)



\#output : Error



def sayHello(age, name='Alice'):

&#x20;  print('Hello', name)

&#x20;  print('Your age :', age)



sayHello(20)



\#output : Hello Alice 

&#x20;         Your age : 20





Note: default values should be assigned from right





def sayHello(course='Python', age, name='Alice'):

&#x20;  print('Hello', name)

&#x20;  print('Your age :', age)

&#x20;  print('Course : ', course)

sayHello(20)



Output : Error



def sayHello(age, course='Python', name='Alice'):

&#x20;  print('Hello', name)

&#x20;  print('Your age :', age)

&#x20;  print('Course : ', course)

sayHello(20)



Output : Hello Alice 

&#x20;        Your age : 20

&#x20;        Course : Python





positional arguments

\#=============================



When we pass values are parameter in function, these values are assigned to the arguments in the function body. The assignment is always follow an order.



The assignment is always left to right. This is called positional arguments.



example :



def sayHello(course, age, name):

&#x20;  print('Hello', name)

&#x20;  print('Your age :', age)

&#x20;  print('Course : ', course)



sayHello('Python', 20, 'Alice')



keyword Arguments :

=========================



Unlike positional arguments, the values passed as parameter with the key name of the arguments of the function call. Here changing order will not change the value. This is called keyword arguments



def sayHello(course, age, name):

&#x20;  print('Hello', name)

&#x20;  print('Your age :', age)

&#x20;  print('Course : ', course)



sayHello(course='Python', age=20, name='Alice')



mixed keyword and positional arguments:



def sayHello(course, age, name):

&#x20;  print('Hello', name)

&#x20;  print('Your age :', age)

&#x20;  print('Course : ', course)



sayHello(course='Python', 20, name='Alice')



Note : Always have to remember that in function call Keyword arguments should follow positional arguments and in function body no arguments get multiple value from function call.







user defined vs predefined functions



user defined functions are the functions written by programmers



While predefined functions are the functions already written and as a programmer we use them in our program.



when we write functions in a file and we can use that file as a module.





















