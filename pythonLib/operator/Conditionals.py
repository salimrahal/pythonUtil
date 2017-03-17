'''
Created on Aug 9, 2016

@author: salim
'''

class ConditionalsClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def _ifTest(self, param):
        if param:
            print("_ifTest({}) = true".format(param))
        else:
            print("_ifTest({}) = false".format(param))
            
 
    def _numberComparision(self, param1,param2):
        if param1 == param2:
            print("_numberComparision({} {}) are equals".format(param1,param2))
        if param1 != param2:
            print("_numberComparision({} {}) are diff".format(param1,param2))
            
    def _numberwithAND(self, param1,param2):
        if  len(param1)>0 & len(param1)>0:
            print("_numberwithAND({} {}) length are > 0".format(param1,param2))
        else :
            print("_numberwithAND({} {}) length <0".format(param1,param2))
            
    def _stringwithAND(self, param1,param2):
        print len(param1) 
        print len(param2) 
        if  len(param1)>0 and len(param2)>0:
            print("_stringwithAND({} {}) length are > 0".format(param1,param2))
        else :
            print("_stringwithAND({} {}) length <0".format(param1,param2))
       
condObj =  ConditionalsClass()

condObj._numberComparision(0, 0)

condObj._stringwithAND('sfas', '')

#condObj._numberwithAND(1, 2)
condObj._ifTest(None)#false
condObj._ifTest(False)#false
condObj._ifTest(True)
condObj._ifTest('')
condObj._ifTest('heloo')
condObj._ifTest(25252)
condObj._ifTest(-25252)
condObj._ifTest(0)

'''+++++++++++Output+++++++++++++
_ifTest(None) = false
_ifTest(False) = false
_ifTest(True) = true
_ifTest() = false
_ifTest(heloo) = true
_ifTest(25252) = true
_ifTest(-25252) = true
_ifTest(0) = false
'''
