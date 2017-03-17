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
    def joinTest(self):
        s="-"
        collection = ['hey', "hello", 'd']
        res = s.join(collection)
        return res
      
    def splitStr(self, strparam, delimiter):
        arr = strparam.split(delimiter)
        print arr
        return arr  
        
myClass = MyClass("params")
print(myClass.joinTest())   
str_param = "[50FIT STL GV 530S 90D] SINGLE TH.NIPPLE 1/2  X 90CM STL"
if "[" in str_param and "]" in str_param:
    arr = myClass.splitStr(str_param,"]")
    print "res->"+arr[0] + "/"+arr[1]
    
    res = myClass.splitStr(arr[0],"[")
    print "res->"+res[1]

