class ProductOfNumbers(object):
    listProd=[]
    def __init__(self):        
        self.listProd.append(1)

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num==0:
            self.listProd=[]  
            self.listProd.append(1)
        else:
            self.listProd.append(self.listProd[-1]*num)
        

    def getProduct(self, k):
        if k>len(self.listProd)-1:
            return 0
        else:
            return self.listProd[-1]/self.listProd[-1-k]