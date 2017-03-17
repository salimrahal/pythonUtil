'''
Created on Jul 5, 2016

@author: salim
'''

class ComputeMargin(object):
    '''
    classdocs
    '''
    
    
    def __init__(self, price_subtotal, margin):
        '''
        Constructor
        '''
        self.price_subtotal = price_subtotal
        self.margin = margin
    
    def _compute_margin_percent(self):
        print("_compute_margin_percent self.price_subtotal :{}, margin: {}".format(self.price_subtotal, self.margin))
        self.margin_percent = 100 * (self.price_subtotal and
                self.margin / self.price_subtotal or 0.0)
        print("_compute_margin_percent self.margin_percent:{}".format(self.margin_percent))
    
    def _compute_margin_percentV2(self):
        print("_compute_margin_percentV2 self.price_subtotal :{}, margin: {}".format(self.price_subtotal, self.margin))
        quotion = self.price_subtotal and self.margin
        dividend = self.price_subtotal or 0.0
        marginRate =(float(quotion) / dividend)
        print("_compute_margin_percentV2 q = {} div = {} => marginRate q/div = {}".format(quotion, dividend, marginRate))
        marginPerc = marginRate * 100
        print("_compute_margin_percentV2 marginPerc = {}".format(marginPerc))

    def substractTest(self):
        res = (1000 - (50*3.12))/1000    
        print("substractTest: res: {}".format(res))
        
    def convertToDollar(self, lbp):
        res = (lbp/1507.5)  
        print("convertToDollar: res: {}".format(res))
        print("---".format(type(res)))
        print(type(res))
        #259753.018992
        return res
    '''
    _andOperatorTest: logical and test
    in case an operand is ZERO then the result will be zero. In case two operand are
    diff  than Zero so the result is the second argument
   logical:
     0 and 1 = 0
     1 and 0 = 0
     1 and 1 = 1
      
1 and 2 = 2
2 and 0 = 0
0 and 2 = 0

2 and 100 =100
200 and False = False
-1 and 100 = 100
0.95  and 100 = 100
100 and 0.95 = 0.95
    '''
        
    def _andOperatorTest(self, num1, num2):
        res = (num1 and num2)
        print("_andOperatorTest = {}".format(res))
        
        
    '''
    _orOperatorTest: it do a logical or: gets the first true result starting from left
    0 or 0.0 = 0.0
     1 or 2 = 1
     1.6666 or 2 = 1.6666
     2 or 1.6666 = 2
     0 or 2 = 2
     0.15 or 2 = 0.15
    -100 or 2 = -100
    False or True    =  True
    True or False = True
     0 or 1 = 1
     1 or 0 = 1
     1 or 1 = 1
     0 or 0 = 0
    '''   
    def _orOperatorTest(self, num1, num2):
        res = (num1 or num2)
        print("_orOperatorTest = {}".format(res))
        
#77.76, margin: 28.548

computeMargin = ComputeMargin(2544.0, 25.1321)
computeMargin.convertToDollar(376547901.13)
'''
computeMargin._compute_margin_percent()
computeMargin._compute_margin_percentV2() 
'''

'''
computeMargin.substractTest()
'''

'''
AND OR Test
'''

'''
print "+++++++++++++ AND OR Test 1+++++++++++++++"
computeMargin._andOperatorTest(0,2)
computeMargin._andOperatorTest(1,0)
computeMargin._andOperatorTest(1,1)
computeMargin._orOperatorTest(0, 0.0)
'''
