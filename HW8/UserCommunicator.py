ACTS = {
    'FIND_CONTACT_ACT_ID' : 1,
    'ADD_CONTACT_ACT_ID' : 2,
    'GET_ALL_CONTACTS_ACT_ID' : 3,
    'REMOVE_CONTACT_ACT_ID' : 4,
    'EDIT_CONTACT_ACT_ID' : 5,
}

FIELDS = {
    'NAME' : 1,
    'LAST_NAME': 2,
    'MIDDLE NAME': 3,
    'PHONE_NUMBER': 4
}


class UserCommunicator:
    @staticmethod
    def get_action():
        print('''
            Choose action type:
            1. Find contact.
            2. Add contact.
            3. Get all contacts.
            4. Remove contact.
            5. Edit contact.
            ''')
        return int(input('Enter number in range 1-3: '))

    @staticmethod
    def get_contact_data():
        name = input('Enter contact name: ')
        middlename = input('Enter contact middlename: ')
        lastname = input('Enter contact lastname: ')
        birthdate = input('Enter contact birtday: ')
        phone_number = input('Enter contact phone number: ')

        return (phone_number, name, lastname, middlename, birthdate)
    
    @staticmethod
    def get_fileds_to_search_by():
        name = input('Enter name to search by: ')
        lastname = input('Enter lastname to search by: ')
        middlename = input('Enter middlename to search by: ')
        birthdate = input('Enter birthdate to search by: ')
        phone_number = input('Enter phone_number to search by: ')
        return (phone_number, name, lastname, middlename, birthdate)
    
    @staticmethod
    def get_field_to_remove_or_edit_by():
        print('''
        Choose one of the variants to choose field to remove or edit by:
            1. name;
            2. last name;
            3. middle name;
            4. phone number
            :
        ''', end='')
        return int(input())
    
    
    @staticmethod
    def get_field_value_to_remove(msg):
        return input(f'Enter the {msg} of the contact to remove: ')
    

    @staticmethod
    def get_new_value_for_field(field_name):
        return input(f'Enter new value for {field_name} field: ')