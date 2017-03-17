'''
Created on Dec 16, 2016

@author: salim
'''

class NumbersTest():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
      
    
    def roundNum(self, number):
        print("run function Test")
        number = round(number, 2)
        return number

myClassInstance = NumbersTest()
res = myClassInstance.roundNum(12.55555555)
print res