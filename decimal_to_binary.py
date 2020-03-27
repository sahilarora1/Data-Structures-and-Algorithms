## The stack is an abstract data type. It follows the principle of LIFO i.e. last in first out.
## Let's define an Abstract data type called stack using the class feature of Python
class stack:
    ## Defining the constructor
    def __init__(self):
        self.item = list([]) ## Creates an attribute of the instance called as 'item'
    ## Defining additional method of the class stack
    def pop(self):
        return self.item.pop()

    def push(self,a):
        return self.item.append(a)

    def get_stack(self):
        return self.item
###################################################################################################################################################################
## Q2: Let's try and convert the Decimal number to binary number using the concepts of stack

def binary_conversion(decimal):
    s= stack()

    while decimal != 0:
        rem =decimal%2
        s.push(rem)
        decimal = decimal // 2

    return (s.get_stack())

print(binary_conversion(20))



