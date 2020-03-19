from client.models import *

city1 = City.objects.create(postal_code='50-370', city='Wrocław')
address1 = Address.objects.create(street="wybrzeże Stanisława Wyspiańskiego",
                                  house_nr=27, city=city1)
su = CustomUser.objects.create_superuser(password='testing321', username='jakub', first_name='jakub', last_name='brela',
                                         email='jakub@gmail.com', pesel=1234267891, telephone=123256789, address=address1, birth_day='2000-11-11 11:11')
account = Account.objects.create(
    user=su, balance=100.40, account_type='Saving account')
account2 = Account.objects.create(
    user=su, balance=0.40, transaction_limit='10', currency='JPY')
card = Card.objects.create(account_number=account)

transaction = TransactionHistory.objects.create(
    source_bank_account=account, destination_bank_account_number=account2.account_number, title='tytul', amount=10.40)
request = Request.objects.create(
    client_data=su, request_title="asd", is_verified=True)
print(Request.objects.all())
print(VerifiedRequestsView.objects.all())
