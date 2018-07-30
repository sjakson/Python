'''
Created on Jul 27, 2018

@author: Scott Jackson
'''
#Q2. Convert string to int/float (if possible)
def convert(a=''):
    try:
        b = int(a)
        return b
    except ValueError:
        pass
    
    try:
        b = float(a)
        return b
    except ValueError:
        pass
        
    return a

print("Q2")
print(type(convert('1')))
print(type(convert('1.0')))
print(type(convert('asd')))
print()

#Q3 Reformat
animal,name,age = ['dog', 'Fido', 10]
output = ('{name} the {animal} is {age} years old'.format(
animal=animal, name=name, age=age))

print("Q3")
print(output)
print()

#Q4 Find the minimum of 3 numbers       
def find_min(a, b, c):
    minimum = a
    
    if minimum > b:
        minimum = b
    if minimum > c:
        minimum = c
        
    return minimum

print("Q4")
print(find_min(1,2,3))
print(find_min(2,3,1))
print(find_min(3,2,1))
print()

#Q5 Reformat
def apply_operation(left_operand, right_operand, operators):
    import operator
    ops = { '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv }

    return (ops[operators](left_operand, right_operand))

print("Q5")
print(apply_operation(5, 4, '+'))
print(apply_operation(5, 4, '-'))
print(apply_operation(5, 4, '*'))
print(apply_operation(5, 4, '/'))

    
    
    
    
    
