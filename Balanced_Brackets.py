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
## Let's use the concept of stack to solve a problem:
## Problem: Check if the brackets are balanced or not?
## example of balanced brackets : (({})) , ()()
## example of unbalanced brackets : ()) , }}

#This problem can be solved using the concept of stack because of the LIFO property.
# Step1: Every time we encounter an open bracket, we will push it into the stack
# Step2: Everytime we encounter a close bracket, we pop the element from the stack
# Step3: Since the last opened bracket will be closed first, the brackets should form a pair

## Defining the function

def isempty(ls):
    """
This function takes the list/string as parameter and returns the binary outcome indicating whether the list is empty or not
    :param ls: list
    :return: True/False
    """
    if len(ls) ==0:
        return True
    else:
        return False


def isbalanced(ip_str):
    s = stack()
    balanced_flag = True
    i=0
    while i<len(ip_str) and balanced_flag:
        if ip_str[i] in list(["(" , "[" , "{"]):
            s.push(ip_str[i])

        if ip_str[i] in list([")", "]", "}"]):
            if isempty(s.get_stack()) ==True:
                balanced_flag = False

            else:
                if s.pop()+ ip_str[i] in list(["[]" , "()" , "{}"]):
                    balanced_flag=True

                else:
                    balanced_flag = False

        i+=1

    list_empty_flag = isempty(s.get_stack())
    balanced_flag_2 = list_empty_flag and balanced_flag

    return balanced_flag_2

test_str ="[][][][][][][][][]((()))"
print(isbalanced(test_str))
