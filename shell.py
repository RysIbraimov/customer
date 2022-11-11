import json
from my_app.models import Accaunt,Work,Customer

with open('data.json', 'r') as file:
    data = json.load(file)

for dict in data:
    customer = Customer.objects.create(name=dict['name'], email=dict['email'], phone=dict['phone'])
    work = Work.objects.create(address=dict['address'], city=dict['city'], company=dict['company'], postalZip=dict['postalZip'],customer=customer)
    accaunt = Accaunt.objects.create(pin=dict['pin'], acc_num=dict['acc_num'],pan=dict['pan'],cvv=dict['cvv'],customer=customer)

