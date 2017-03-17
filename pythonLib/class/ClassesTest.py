'''
Created on Oct 12, 2016

@author: salim
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        print("run constructor params="+params)
    def test(self):
        print("run function Test")

myClassInstance = MyClass("Param1")
myClassInstance.test()