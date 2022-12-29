class product:
    def __init__(self,name,price,deal_price,rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating

    def display_product_details(self):
        print('name:',self.name)
        print('price:', self.price)
        print('deal_price:', self.deal_price)
        print('rating:',self.rating)

    def get_deal_price(self):
        return self.deal_price
class electronic_items(product):
    def set_warranty(self, warannty):
        self.warranty=warranty
    def get_warranty(self):
        print('warranty',self.warranty)
class grocery_items(product):
    pass
class order:
    def __init__(self,delivery_speed,delivery_address):
        self.items_in_cart=[]
        self.delivery_speed=delivery_speed
        self.delivery_address = delivery_address
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_order_details(self):
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print('quantity',quantity)
    def display_total_bill(self):
        total_bill=0
        for produt, quantity in self.items_in_cart:
            price=product.get_deal_price()*quantity
            total_bill +=price
        print('total_bill',total_bill)


milk=grocery_items("milk",40,25,3.5)
tv=electronic_items("tv",45000,40000,3.5)
Order=order("prime delivery","hyderabad")
Order.add_item(milk,2)
Order.add_item(tv,1)
print('============')
Order.display_order_details()
print('=================')
Order.display_total_bill()





