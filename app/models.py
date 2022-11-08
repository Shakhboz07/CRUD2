from django.db.models import Model, CharField, DateField, BooleanField, EmailField
from django.utils.timezone import now


# Create your models here.

class Employee(Model):
    status_choice = [
        (1, 'Active'),
        (2, 'Inactive')
    ]

    name = CharField(max_length=255)
    email = EmailField()
    age = DateField()
    address = CharField(max_length=255)
    status = BooleanField(choices=status_choice, default=False)
    phone = CharField(max_length=255)

    @property
    def age_year(self):
        return now().year - self.age.year

    def __str__(self):
        return f'{self.id} - {self.name}'
