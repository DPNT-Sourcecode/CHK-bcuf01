
class CheckoutSolution:

    # skus = unicode string
    def new_item(self,key,price):
        self.key=key
        self.price=price
        self.rules=None 
    def add_items(self, keys, prices,rules=None):
        for i in range(len(keys)):
            self.new_item(keys[i],p[i])
            if rules[i] is not None:
                for item in rules[i]:
                    self.add_rule(rules[i])
    def add_rule(key,fun):
        if self.rules is None:
            self.rules=[fun]
        else:
            self.rules.append(fun)    

    def checkout(self, skus):
        result=0
        illegal_input=0
        prices={'A':50, 'B':30, 'C':20,'D':15, 'E':40, 'F':10}
        for item in prices.keys():
            x=skus.count(item)
            print('x', x)
            print('item', item)
            illegal_input+=x
            if item == 'A':
                if int(x/5)>0:
                    remainder=x%5
                    result+=remainder%3*prices[item]+int(remainder/3)*130+int(x/5)*200  
                else:    
                    result+=x%3*prices[item]+int(x/3)*130
            elif item == 'B':
                discount=int(skus.count('E')/2)
                if x>0:
                    x-=discount
                print('x', x)
                result+=x%2*prices[item]+int(x/2)*45
            else:
                if item == 'F':    
                    x-=int(x/3)
                result+=x*prices[item]
            print('result', result)    
        if len(skus)-illegal_input>0:
            result=-1
        return result

f=open("challenges/CHK_R4.txt")
for line in f:
    if line.startswith("|"):
        print(line)
