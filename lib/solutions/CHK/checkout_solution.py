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
                    offer_key=item[:3].strip()
                    if offer_key[-1].isdigit() == False:
                        key=offer_key[-1]
                        n=offer_key[:-1]
                    else:
                        key=None
                        n=offer_key   
                    #print('key', key)        
                    #print('n',n)

                    #print('offer key', offer_key)
                    #print(len(offer_key))
                    
                    if 'get one ' in item:
                        f_type=0
                        new_value=item[-6]
                    if 'for' in item:
                        f_type=1
                        new_value=item[-3:] 
                        #print('new_value',new_value) 
                        if new_value[0].isdigit() == False:
                             new_value=new_value[1:]
                        new_value=int(new_value.strip())
                        #print('new', new_value) 
                        #print('item',item)  
                        if 'buy any' in item:
                            #print('buy any') 
                            f_type=2
                            n=item[7:9].strip()
                            print('special offer n', n)
                            offer_key=item.split('(')[-1]
                            offer_key=offer_key.split(')')[0]
                            offer_key=offer_key.replace(',', '')
                            #offer_key=offer
                            key=offer_key
                            #print('offer', offer_key)
                            #print('key', key)
                            #print(item)
                            #print('n', n)
                    o.add_offer(f_type,offer_key,int(n),key,new_value)
            o.new_item(line[2], int(line[9:12]))

def order_keys(key):
    '''order keys by the number part of the order key'''
    while key[-1].isdigit() == False:
        if len(key)<2:
            return
            print(key)
        key=key[:-1] 
        print(key)
    return(int(key))    


class CheckoutSolution:

    # skus = unicode string
    def __init__(self):
        self.price={}
        self.offers={0:{}, 1:{}, 2:{}} 
        self.counts=None
        f=open("challenges/CHK_R5.txt")
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

    def offer_2(self, n_items, key_item, new_value, offer_key ): 
        '''
        Buy any 3 for X
        '''
        #key_item=['S','T','X','Y','Z']
        #print('executing offer 2')
        total=0
        remove_keys={}
        for k in key_item:
            if k in self.counts.keys():
                remove_keys[k]=self.counts[k]
                total+=self.counts[k]
        discount=int(total/n_items)        
        
        if discount>0:
            self.price[offer_key]=new_value
            self.counts[offer_key]=discount
            remove_keys=sorted(remove_keys, key=lambda x: self.price[x], reverse=True)
            val=discount*n_items
            print(val)
            while val>0:
                print('counts', self.counts)
                for key in remove_keys:
                    print('val', val)
                    print('key', key)
                    if val<self.counts[key]:
                        print('')
                        print('if')
                        print(self.counts[key])
                        self.counts[key]-=val
                        print(key)
                        print(self.counts[key])
                        break
                    else:
                        print('')
                        print('else')
                        print('counts', self.counts[key])
                        print('key', key)
                        val-=self.counts[key]
                        print('val', val)
                        self.counts[key]=0
                        print(key)
                        print(self.counts[key])
                        if val==0:
                            break
                        continue
                    if val==0:
                         break     
            print(self.counts)
            print(self.price)
        #           self.counts[key]-=n_items*discount
 

    def get_offer(self,f_type, offer_key):
        print(self.counts.keys())
        print(offer_key)

        #if offer_key in self.counts.keys() or f_type==2:
        input=self.offers[f_type][offer_key]
        print('input', input)
        if input['k'] in self.counts.keys() or f_type==2:
            if f_type == 0:
                if input['new_val'] in self.counts.keys():
                    return(self.offer_0(input['n_items'], input['k'], input['new_val'], input['offer']))
            elif f_type == 1:
                return(self.offer_1(input['n_items'], input['k'], input['new_val'], input['offer']))
            elif f_type == 2:
                print('f 2')
                print(input)
                return(self.offer_2(input['n_items'], input['k'], input['new_val'], input['offer']))
            

    def checkout(self, skus):
        result=0
        self.count_chars(skus)
        
        #execute all offers of type zero first
        for f_type in self.offers.keys():
            print(f_type)
            offers=self.offers[f_type].keys()
            print(offers)
            print(f_type)
            if f_type == 1:
                offers = sorted(offers, reverse=True, key=order_keys)
            for offer in offers:
                print(offer)
                k=self.offers[f_type][offer]['k']
                self.get_offer(f_type, offer)
        '''        
        #execute all offers of type one next
        for offer in sorted(self.offers[1].keys(), reverse = True, key=order_keys):
            k=self.offers[1][offer]['k']
            if k in self.counts.keys():
                    self.get_offer(1, offer)
        '''
        for k in self.counts.keys():
            if k not in self.price.keys():
               return -1   
            result+=self.counts[k]*self.price[k] 
        return int(result)         

c=CheckoutSolution()
print(c.offers)
print(c.checkout('XTYXX')==79)
print(c.counts)


