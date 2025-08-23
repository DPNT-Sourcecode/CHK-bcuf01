import numpy as np
def buy_x_get_y_free(num,x):
    if int(num/x)>0:
        discount=int(num/x)
    return(discount)
def read_items_from_file(f,o):
    for line in f:
        if line.startswith("|"):
            if line.__contains__('Item'):
                continue     
            print('17',line[17])
            if line[17]!=' ':
                offers=line[17:]
                offers=offers[:-2].strip()
                offers=offers.split(', ')
                for item in offers:
                    n=item[:2]
                    if n[-1].isdigit() == False:
                        n=n[:-1]  
                    offer_key=item[:3].strip()
                    if 'get one ' in item:
                        f_type=0
                        new_value=item[-6]
                    if 'for' in item:
                        f_type=1
                        new_value=item[-3:]  
                        if new_value[0].isdigit() == False:
                             new_value=new_value[1:] 
                    o.add_offer(f_type,offer_key,n,offer_key[-1],new_value)
            o.new_item(line[2], int(line[9:12]))
class CheckoutSolution:

    # skus = unicode string
    def __init__(self):
        self.price={}
        self.offers={0:{}, 1:{}} 
        self.counts=None
        f=open("challenges/CHK_R4.txt")
        read_items_from_file(f, self)
    
    def count_chars(self, string):
        u, counts = np.unique(list(string), return_counts=True)
        print(u, counts)
        self.counts=dict(zip(u,counts))
        print(self.counts)

    def new_item(self,key,price):
        self.price[key]=price
    
    def get_price(self,key):
        return(self.price[key])
    
    def add_offer(self,fun_type, offer_key, n_items, key, new_val):
        self.offers[fun_type][offer_key]= {'n_items':n_items, 'k':key, 'new_val':new_val, 'offer':offer_key}

    def offer_0(self, n_items, key_item, key_discount, offer_key ):
        items=self.counts
    def get_offer(self,key, val):
        for offer in self.offers[key]:
            print(offer(val))

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


#f=open("challenges/CHK_R4.txt")
c=CheckoutSolution()


        
print(c.get_price('X'))        
print(buy_x_get_y_free(5,3))
print(c.price)
print(c.offers)
print(c.count_chars('ABBBC'))
print(c.count_chars('ABBBC') == {np.str_('A'): np.int64(1), np.str_('B'): np.int64(3), np.str_('C'): np.int64(1)})