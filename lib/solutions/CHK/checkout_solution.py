
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        result=0
        prices={'A':50, 'B':30, 'C':20,'D':15}
        for item in prices.keys():
            x=skus.count(item)
            
        result+=x*prices[item]
        a=skus.count('A')             
        b=skus.count('B')
        c=skus.count('C')
        d=skus.count('D')
        a3=int(a/3)
        b2=int(b/2)
        a=a-a3
        b=b-b2
        return 50*a+30*b+20*c+15*d+130*a3+45*b2
    
