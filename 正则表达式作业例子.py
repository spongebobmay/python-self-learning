import re

email11 = 'someone@gmail.com'
email12 = 'bill.gates@microsoft.com'
email2 = r'<Tom Paris> tom@voyager.org'

version11 = re.match(r'^([a-zA-z\_]+[a-zA-Z0-9\_]+)@([0-9a-zA-Z]+)\.([a-zA-Z]{3})$', email11)
print version11.groups()
version12 = re.match(r'^([a-zA-z\_]+[a-zA-Z0-9\_]+\.[0-9a-zA-z]+)@([0-9a-zA-Z]+)\.([a-zA-Z]{3})$', email12)
print version12.groups()
version2 = re.match(r'^<([a-zA-Z\s]+)>\s+([0-9a-zA-Z]+@[a-zA-Z0-9]+\.[a-zA-Z]{3})$', email2)
print version2.groups()
