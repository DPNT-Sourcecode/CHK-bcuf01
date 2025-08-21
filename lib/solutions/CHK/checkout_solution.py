
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        result=0
        illegal_input=0
        prices={'A':50, 'B':30, 'C':20,'D':15}
        for item in prices.keys():
            x=skus.count(item)
            illegal_input+=x
            if item == 'A':
                result+=x%3*prices[item]+int(x/3)*130
            elif item == 'B':
                result+=x%2*prices[item]+int(x/2)*45
            else:
                result+=x*prices[item]
        if len(skus)-illegal_input>0:
            result=-1
        return result


print(CheckoutSolution.checkout(1,'f'))