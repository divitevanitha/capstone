class product:
    def __init__(self,name,price,deal_price,rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating
    def display(self):
        print('name:',self.name)
        print('price:', self.price)
        print('deal_price:', self.deal_price)
        print('rating:',self.rating)
class electronic_items(product):
    def __init__(self,name,price,deal_price,rating,warranty):
        product.__init__(self,name,price,deal_price,rating)
        self.warranty=warranty
    def getwarranty(self):
        print('warranty',self.warranty)
class grocery_items(electronic_items):
    def __init__(self,name,price,deal_price,rating,warranty,expiry_date):
        electronic_items.__init__(self,name,price,deal_price,rating,warranty)
        self.expiry_date=expiry_date
    def getexpiry_date(self):
        print('expiry_date',self.expiry_date)
obj = product("charger",550,450,4.5)
obj.display()
obj1 = electronic_items("charger",550,450,4.5,12)
obj1.getwarranty()
obj2 = grocery_items("charger",550,450,4.5,12,2030)
obj2.getexpiry_date()









class product:
    def __init__(self,name,price,deal_price,rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating
    def display(self):
        print("name: {}".format(self.name))
        print('price:', self.price)
        print('deal_price:', self.deal_price)
        print('rating:',self.rating)
class electronic_items(product):
    def __init__(self,warranty):
        self.warranty=warranty
    def getwarranty(self):
        print('warranty',self.warranty)
class grocery_items(product):
    def __init__(self,name,price,deal_price,rating,expiry_date):
        super().__init__(name,price,deal_price,rating)
        self.expiry_date=expiry_date
    def groceryitems(self):
        super().display()
        print('expiry_date',self.expiry_date)
obj = product("charger",550,450,4.5)
obj.display()
obj1 = electronic_items(12)
obj1.getwarranty()
obj2 = grocery_items("charger",550,450,4.5,2030)
obj2.groceryitems()



class order:
    def __init__(self,items,):

for i in range(0,4):
    for j in range(0,3):
        print(j)
    print(i)














