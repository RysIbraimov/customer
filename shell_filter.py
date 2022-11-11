from django.db.models import Subquery
from my_app.models import Accaunt,Customer,Work


customers_email = Customer.objects.filter(email__icontains='icloud.com')
# ltd_customer = Work.objects.filter(company__icontains='ltd')
# accaunt = Accaunt.objects.filter(customer__email_in=Subquery(Customer.objects.filter(email_icontains='protonmail')))
# print(accaunt)