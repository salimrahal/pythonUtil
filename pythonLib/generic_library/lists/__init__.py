import ListUtils

__all__ = ["ListUtils"]

class ListUtils(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def ensure_same_values_in_array(self,array_param):
        print("test for same value")
        arrayLen= len(array_param)
        all_same = True
        for idx, val in enumerate(array_param):
            print(idx, val)
            if(idx != 0):
                if(array_param[idx] != array_param[idx-1]):
                    all_same = False
                    print("distinct value found")
                    break
            #todo check whether all the ccy are the same
        return all_same