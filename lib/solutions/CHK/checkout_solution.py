
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        a=skus.count('A')             
        b=skus.count('B')
        c=skus.count('C')
        d=skus.count('B')
        a3=int(a/3)
        b2=int(b/2)
        a=a-a3
        b=b-b2
        return 50*a+30*b+20*c+15*d+130*a3+45*b2
    