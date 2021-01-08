# Write a method called `print_contacts` that takes a
# dictionary of key-value pairs for names and phone numbers,
# then outputs the `name` with the contact info.
#
# Try iterating over a dictionary with a for loop and printing
# out what values come back.
#
# Example method call:
#
# print_contacts(contacts)
#
# > Brian has a phone number of 333-333-3333
# > Lenny has a phone number of 444-444-4444
# > Daniel has a phone number of 777-777-7777
#
# Use the contacts below

contacts = {
  'Brian': '333-333-3333',
  'Lenny': '444-444-4444',
  'Daniel': '777-777-7777'
}
def print_contacts(dict):
  for person in dict:
    print('{} has a phone number of {}'.format(person, dict[person]))

print(print_contacts(contacts))

def print_contacts1(contacts):
    for person in contacts:
      print(f"{person} has a phone number of {contacts[person]}")

print(print_contacts1(contacts))