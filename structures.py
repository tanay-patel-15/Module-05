# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:30:32 2024

Created for SDEV 220 Fall 2024

@author: c.s.francis

"""



class MyList:
    def __init__(self, element):
        self.element = element
        self.next = None

    def get_element(self):
        return self.element
    
    def set_element(self, element):
        self.element = element

    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
        
    def add(self, el):
        current = self
        while current.next != None:
            current = current.next
        current.next = MyList(el)
        
    def remove(self, el):
        current = self
        
        if el == current.element:
            temp = current.next
            self = temp
            
        while current.next.element != el and current.next != None:
            current = current.next
         
        if current.next == None:
            return
        else:
            temp = current.next.next
            current.next = temp
            return
            
        
    def __repr__(self):
        current = self
        string = "["
        while current != None:
            string += str(current.element) + ", "
            current = current.next
            
        string += "]"
        return string
    
    
class MyStack(MyList):
    def  __init__(self):
        super().__init__(None)
        self.is_empty =  True
    ##  end of constructor
        

    def push(self, element):
        if self.get_element() == None:
            self.is_empty = False
            super().__init__(element)
            return
        self.is_empty =  False
        self.add(element)
        return



    def pop(self):
        current = self
        if current.get_next() == None:
            self.is_empty = True
            temp = current.get_element()
            return temp
        while current.get_next() != None:
            current = current.get_next()
        temp = current.get_element()
        self.remove(current.get_element())
        return temp

class MyQueue(MyList):
    def __init__(self):
        super().__init__(None)
        self.is_empty = True

    def offer(self, element):
        if self.get_element() == None:
            self.is_empty = False
            super().__init__(element)
            return
        self.is_empty =  False
        self.add(element)
        return
      
    def  poll(self):
        current = self
        if current.get_next() == None:
            self.is_empty = True
            return current.get_element()
        current = self.get_next()
        temp = self.get_element()
        self.set_element(current.get_element())
        self.set_next(current.get_next())
        return temp
        




if __name__=="__main__":
   q1 = MyQueue()
   q1.offer(3)
   q1.offer(5)
   q1.offer(7)
   print(q1)
   x = q1.poll()
   print("3 times as much as the first element in the queue is " + str(3*x))
   print(q1)
    
    
    
    