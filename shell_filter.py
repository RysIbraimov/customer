from django.db.models import Subquery
from my_app.models import Accaunt,Customer,Work

#1
customers_email = Customer.objects.filter(email__icontains='icloud.com')

#2
ltd_customer = Customer.objects.filter(work__company__icontains='ltd')
3print(ltd_customer)
#3
proton_customer = Accaunt.objects.filter(customer__email__icontains='protonmail')
print(proton_customer)

