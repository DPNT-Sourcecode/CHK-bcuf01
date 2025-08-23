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
            #print('17',line[17])
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
                             new_value=int(new_value[1:])
                    o.add_offer(f_type,offer_key,int(n),offer_key[-1],new_value)
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
        #print(u, counts)
        self.counts=dict(zip(u,counts))
        #print(self.counts)

    def new_item(self,key,price):
        self.price[key]=price
    
    def get_price(self,key):
        return(self.price[key])
    
    def add_offer(self,fun_type, offer_key, n_items, key, new_val):
        self.offers[fun_type][offer_key]= {'n_items':n_items, 'k':key, 'new_val':new_val, 'offer':offer_key}

    def offer_0(self, n_items, key_item, key_discount, offer_key ):
        '''
        X get Y free
        '''
        items=self.counts[key_discount]
        items_discount_key=items[key_discount]
        if items_discount_key>0:
            max_discount=items_discount_key
        if key_item == key_discount:
            n_items+=1
        discount=int(self.counts[key_item]/n_items)
        if discount>max_discount:
            discount=max_discount
        self.counts[key_discount]-=discount    
    
    def offer_1(self, n_items, key_item, new_value, offer_key ): 
        '''
        Buy X for Y
        '''
        discount=int(self.counts[key_item]/n_items)
        self.counts[key_item]-=n_items*discount
        self.price[offer_key]=new_value
        self.counts[offer_key]=discount

    def get_offer(self,f_type, offer_key):
        input=self.offers[f_type][offer_key]
        if f_type == 0:
            return(self.offer_0(input['n_items'], input['k'], input['new_val'], input['offer']))
        elif f_type == 1:
            return(self.offer_1(input['n_items'], input['k'], input['new_val'], input['offer']))


    def checkout(self, skus):
        result=0
        #illegal_input=0
        self.count_chars(skus)
        #prices={'A':50, 'B':30, 'C':20,'D':15, 'E':40, 'F':10}
        
        #execute all offers of type zero first
        for offer in self.offers[0].keys():
            k=self.offers[0][offer]['k']
            if k in self.counts.keys():
                if self.offers[0][offer]['new_val'] in self.counts.keys():
                    self.get_offer(0, offer)
        
        #execute all offers of type one next
        for offer in sorted(self.offers[1].keys(), reverse = True):
            k=self.offers[1][offer]['k']
            if k in self.counts.keys():
                    self.get_offer(1, offer)
        
        for k in self.counts.keys():
            if k not in self.price.keys():
               return -1   
            print(self.counts[k]*self.price[k] ) 
            print('key',k, self.price[k])             
            result+=self.counts[k]*self.price[k] 
        return result           
'''

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
            result=-1'''
     


#f=open("challenges/CHK_R4.txt")
c=CheckoutSolution()


        
print(c.get_price('X'))        
print(buy_x_get_y_free(5,3))
print(c.price)
#print(c.offers)
#print(c.count_chars('ABBBC'))
c.count_chars('ABBBC')
counts=c.counts
print(c.counts['A'] == 1)
print(c.counts['B'] == 3)
print(c.counts['C'] == 1)
print(c.checkout('BB') == 45)
print(c.checkout('AAA') == 130)
print(c.checkout('AAAAA') == 200)
print(c.checkout('EEB') == 80)
print(c.checkout('EE') == 80)
print(c.checkout('FFF') == 20)
print(c.checkout('FFFFFF') == 40)


