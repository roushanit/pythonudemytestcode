from collections import Counter
import  re

inventory = Counter(apple=50,
    banana=30,
    orange= 20,
    grapes= 15,
    watermelon= 5)
def update_inventory(order):
    inventory.subtract(order)

order = Counter(apple=10, banana=2, watermelon=1)
update_inventory(order)

print("Updated list:", inventory)