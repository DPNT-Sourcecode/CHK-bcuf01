import numpy as np

def read_items_from_file(f,o):
    for line in f:
        if line.startswith("|"):
            if line.__contains__('Item'):
                continue     
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
                        new_value=int(new_value)     
                    o.add_offer(f_type,offer_key,int(n),offer_key[-1],new_value)
            o.new_item(line[2], int(line[9:12]))

def order_keys(key):
    '''order keys by the number part of the order key'''
    while key[-1].isdigit() == False:
        key=key[-1] 
    return(int(key))    


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
        self.counts=dict(zip(u,counts))

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
        items_discount_key=items
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
        #print('executing offer 1')
        discount=int(self.counts[key_item]/n_items)
        self.counts[key_item]-=n_items*discount
        self.price[offer_key]=new_value
        self.counts[offer_key]=discount


    def get_offer(self,f_type, offer_key):
        input=self.offers[f_type][offer_key]
        if f_type == 0:
            return(self.offer_0(input['n_items'], input['k'], input['new_val'], input['offer']))
        if f_type == 1:
            return(self.offer_1(input['n_items'], input['k'], input['new_val'], input['offer']))


    def checkout(self, skus):
        result=0
        self.count_chars(skus)
        
        #execute all offers of type zero first
        for offer in self.offers[0].keys():
            k=self.offers[0][offer]['k']
            if k in self.counts.keys():
                if self.offers[0][offer]['new_val'] in self.counts.keys():
                    self.get_offer(0, offer)
        
        #execute all offers of type one next
        for offer in sorted(self.offers[1].keys(), reverse = True, key=order_keys):
            k=self.offers[1][offer]['k']
            if k in self.counts.keys():
                    self.get_offer(1, offer)
        
        for k in self.counts.keys():
            if k not in self.price.keys():
               return -1   
            result+=self.counts[k]*self.price[k] 
        return int(result)         

c=CheckoutSolution()
print(c.checkout('HHHHH') == 45)
print(c.checkout('HHHHHHHHHH') == 80)
