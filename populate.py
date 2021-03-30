from faker import Faker
import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
import django
django.setup()
from AppTwo.models import User
fakegen = Faker()

def populate(N=5):
  for entry in range(N):

    fake_first = fakegen.first_name()
    fake_last = fakegen.last_name()
    fake_email = fakegen.email()

    fn = User.objects.get_or_create(first_name=fake_first, last_name=fake_last, email=fake_email)[0]

if __name__ == '__main__':
  print ('populating')
  populate(20)
  print('complete')