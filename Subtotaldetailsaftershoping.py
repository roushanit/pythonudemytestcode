from collections import Counter

price = {'apple': 50, 'banana': 30, 'orange': 20, 'grapes': 150.50, 'watermelon': 15.99}

def generate_bill(cart):
    total = 0
    print('Product      Price      Quantity     Subtotal')
    for item, qty in cart.items():
        print(f'{item:2} {price[item]:3} * {qty:2} = {price[item] * qty}')
        total += price[item] * qty

        print('Total:', total)

cart =  Counter(apple=1, banana=2, orange=3, grapes=4, watermelon=5)   
generate_bill(cart)