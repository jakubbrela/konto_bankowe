# Generated by Django 2.2.7 on 2019-12-02 11:37

import client.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifiedRequestsView',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('request_title', models.CharField(max_length=40)),
                ('request_text', models.TextField()),
                ('credit_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('send_date', models.DateTimeField()),
                ('is_verified', models.BooleanField()),
                ('is_accepted', models.BooleanField()),
                ('request_type', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'client_verifiedrequests',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('pesel', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Niewlasciwy PESEL!', regex='^\\d{11}$')])),
                ('mothers_maiden_name', models.CharField(blank=True, max_length=32, validators=[django.core.validators.RegexValidator(code='nomatch', message='Niewlasciwe nazwisko!', regex='^[a-zA-Z-]*$')])),
                ('birth_day', models.DateTimeField(help_text='Data w formacie dd/mm/yyyy')),
                ('telephone', models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Niewlasciwy numer telefonu', regex='^\\d{9}$')])),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(default=client.models.Account.rand_account_number, max_length=26, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('transaction_limit', models.IntegerField(default=10)),
                ('currency', models.CharField(choices=[('EUR', 'EUR'), ('PLN', 'PLN'), ('USD', 'USD'), ('JPY', 'JPY'), ('GBP', 'GBP'), ('CHF', 'CHF'), ('SAR', 'SAR'), ('RUB', 'RUB'), ('KRW', 'KRW')], default='PLN', max_length=3)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('account_type', models.CharField(choices=[('Normal account', 'Normal account'), ('Saving account', 'Saving account')], default='Normal account', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(code='nomatch', message='Niewlasciwy kod pocztowy! Uzyj formatu XX-XXX.', regex='^\\d{2}-{1}\\d{3}$')])),
                ('city', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Creditworthiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earnings_per_month', models.IntegerField(null=True)),
                ('contract_type', models.CharField(choices=[('Umowa o prace na czas nieokreslony', 'Umowa o prace na czas nieokreslony'), ('Umowa o prace na czas okreslony', 'Umowa o prace na czas okreslony'), ('Umowa o dzielo', 'Umowa o dzielo'), ('Umowa Zlecenie', 'Umowa Zlecenie'), ('Umowa Agencyjna', 'Umowa Agencyjna')], max_length=35, null=True)),
                ('working_time', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_bank_account_number', models.CharField(max_length=26, validators=[django.core.validators.RegexValidator(code='nomatch', message='Wrong account number!', regex='^[0-9]{26}$')])),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('title', models.CharField(max_length=20)),
                ('send_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('source_bank_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='source_bank_account', to='client.Account')),
            ],
        ),
        migrations.CreateModel(
            name='SavingAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.DecimalField(decimal_places=2, max_digits=2)),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_title', models.CharField(max_length=40, null=True)),
                ('request_text', models.TextField()),
                ('credit_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('send_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_accepted', models.BooleanField(null=True)),
                ('request_type', models.CharField(choices=[('Normal request', 'Normal request'), ('Credit request', 'Credit request'), ('Credit card request', 'Credit card request')], default='Normal request', max_length=20)),
                ('client_data', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_data', to=settings.AUTH_USER_MODEL)),
                ('credit_account_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.Account')),
                ('worker_data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='worker_data', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.DecimalField(decimal_places=2, max_digits=2)),
                ('credit_limit', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(code='nomatch', message='Bledna wartosc', regex='^\\d{0,7}$')])),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(default=client.models.Card.rand_card_number, max_length=16)),
                ('cvv', models.CharField(default=client.models.Card.rand_cvv, max_length=3)),
                ('is_nfc', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('transaction_limit', models.IntegerField(default=50)),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=64)),
                ('house_nr', models.IntegerField()),
                ('apartment_nr', models.IntegerField(blank=True, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.City')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.Address'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='creditworthiness',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='client.Creditworthiness'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
