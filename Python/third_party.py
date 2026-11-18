#Third Party modules
'''
pip install modules_name

pip show modules_name

requests

'''

from faker import Faker
fake=Faker()

print(fake.name())
print(fake.name_nonbinary())
print(fake.email())