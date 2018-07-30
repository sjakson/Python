'''
Created on Jul 27, 2018

@author: Scott Jackson
'''

class Q1(object):
    
    #Constructor (initializes list)
    def __init__(self, *args):
        self.l = list()
        for i in args:
            self.l += i
    
    #Returns list of unique items
    def unique(self):
        s = set(self.l)
        return list(s)
    
    #Returns dictioary with items and frequency
    def frequency(self):
        d = {x:self.l.count(x) for x in self.l}
        return d

    #Appends item to the list
    def append_list(self, item):
        self.l.append(item)
        return self.l

#Test the functions
q1 = Q1([1, 3, 2, 3])
print("Initialized list:", q1.l)
print("Unique items:",q1.unique())
print("Item:frequency:",q1.frequency())
print("Appended list:",q1.append_list(10))
print()
q2 = Q1([4, 2, 3, 3, 1])
print("Initialized list:", q2.l)
print("Unique items:",q2.unique())
print("Item:frequency:",q2.frequency())
print("Appended list:",q2.append_list(20))
print()
q3 = Q1([6, 5, 4, 5, 5])
print("Initialized list:", q3.l)
print("Unique items:",q3.unique())
print("Item:frequency:",q3.frequency())
print("Appended list:",q3.append_list(15))