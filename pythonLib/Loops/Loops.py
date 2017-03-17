'''
Created on Oct 12, 2016

@author: salim

https://wiki.python.org/moin/ForLoop
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    
    def forTest(self):
        collection = ['hey', 5, 'd']
        for x in collection:
            print x   
            
    def joinTest(self):
        str="fr"
        collection = ['hey', 5, 'd']
        print(str)
        
        
myClass = MyClass("params")
myClass.forTest()
myClass.joinTest()