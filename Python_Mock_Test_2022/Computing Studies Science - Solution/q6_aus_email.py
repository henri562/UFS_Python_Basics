"""
A program to check for a valid Australian email address
"""

first_name = input('Enter your first name: ')
email = input('Enter proposed email: ')

if not (email[0].islower() or email[0].isupper()):
    print('Email must begin with a lower case letter')
elif ' ' in email:
    print('Email may not contain any spaces')
elif first_name[0].lower() not in email.lower():
    print('Email must contain first letter of first name')
elif '@' not in email:
    print('Email must contain @ symbol')
elif email[-3:] != '.au':
    print('Email must end in .au')
else:
    print('Email correctly formatted')
