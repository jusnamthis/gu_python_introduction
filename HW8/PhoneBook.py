from Contact import Contact
from FileHandler import FileHandler
from UserCommunicator import UserCommunicator
from UserCommunicator import ACTS, FIELDS


FILE_NAME = 'test'
FILE_EXT = 'txt'


class PhoneBook:
    def start_app(self):
        act = self._get_action()

        if act == ACTS['FIND_CONTACT_ACT_ID']:
            self._print_suitable_contacts(*self._get_fields_to_find())
        elif act == ACTS['ADD_CONTACT_ACT_ID']:
            self._add_contact()
        elif act == ACTS['GET_ALL_CONTACTS_ACT_ID']:
            self._print_all_contacts(self._get_all_contacts())
        elif act == ACTS['REMOVE_CONTACT_ACT_ID']:
            self._remove_contact()
        elif act == ACTS['EDIT_CONTACT_ACT_ID']:
            self._edit_contact()
        else:
            print('op doesn\'t support')


    def _get_action(self):
        return UserCommunicator.get_action()
    

    def _get_fields_to_find(self):
        return UserCommunicator.get_fileds_to_search_by()


    def _add_contact(self):
        contact_data = UserCommunicator.get_contact_data()
        contact = Contact(*contact_data)
        self._save_contact(contact, FILE_NAME, FILE_EXT)


    def _save_contact(self, contact, filename='test', file_ext='txt'):
        FileHandler().save_contacts((contact, ), filename, file_ext)

    
    def _rewrite_contacts(self, contacts, filename='test', file_ext='txt'):
        FileHandler().rewrite_contacts(contacts, filename, file_ext)


    def _get_all_contacts(self):
        contacts = FileHandler().get_contacts(FILE_NAME, FILE_EXT)
        return contacts


    def _print_all_contacts(self, contacts):
        for contact in contacts:
            print(contact)


    def _print_suitable_contacts(self, phone_number="", name="", lastname="", middlename="", birthdate=""):
        contacts = self._get_all_contacts()
        
        def compare_contact(contact):
            if name:
                return name.lower() in contact.name.lower()
            elif middlename:
                return middlename.lower() in contact.middlename.lower()
            elif lastname:
                return lastname.lower() in contact.lastname.lower()
            elif phone_number:
                return phone_number.lower() in contact.phoneNumber.lower()
            elif birthdate:
                return birthdate.lower() in contact.birthdate.lower()

        filtered_contacts = filter(compare_contact, contacts)

        self._print_all_contacts(filtered_contacts)


    def _remove_contact(self):
        contacts = self._get_all_contacts()
        self._print_all_contacts(contacts)
        fieldId = UserCommunicator.get_field_to_remove_or_edit_by()

        if fieldId == FIELDS['NAME']:
            value = UserCommunicator.get_field_value_to_remove('name')
            for i in range(len(contacts)):
                if (contacts[i].name == value):
                    contacts.remove(contacts[i])
                    break
        elif fieldId == FIELDS['LAST_NAME']:
            value = UserCommunicator.get_field_value_to_remove('last name')
            for i in range(len(contacts)):
                if (contacts[i].lastname == value):
                    contacts.remove(contacts[i])
                    break
        elif fieldId == FIELDS['MIDDLE NAME']:
            value = UserCommunicator.get_field_value_to_remove('middle name')
            for i in range(len(contacts)):
                if (contacts[i].middlename == value):
                    contacts.remove(contacts[i])
                    break
        else:
            value = UserCommunicator.get_field_value_to_remove('phone number')
            for i in range(len(contacts)):
                if (contacts[i].phoneNumber == value):
                    contacts.remove(contacts[i])
                    break

        self._rewrite_contacts(contacts)


    def _edit_contact(self):
        contacts = self._get_all_contacts()
        self._print_all_contacts(contacts)
        fieldId = UserCommunicator.get_field_to_remove_or_edit_by()

        if fieldId == FIELDS['NAME']:
            value = UserCommunicator.get_field_value_to_remove('name')
            for i in range(len(contacts)):
                if (contacts[i].name == value):
                    val = UserCommunicator.get_new_value_for_field('name')
                    contacts[i].name = val
                    break
        elif fieldId == FIELDS['LAST_NAME']:
            value = UserCommunicator.get_field_value_to_remove('last name')
            for i in range(len(contacts)):
                if (contacts[i].lastname == value):
                    val = UserCommunicator.get_new_value_for_field('last name')
                    contacts[i].lastname = val
                    break
        elif fieldId == FIELDS['MIDDLE NAME']:
            value = UserCommunicator.get_field_value_to_remove('middle name')
            for i in range(len(contacts)):
                if (contacts[i].middlename == value):
                    val = UserCommunicator.get_new_value_for_field('middle name')
                    contacts[i].middlename = val
                    break
        else:
            value = UserCommunicator.get_field_value_to_remove('phone number')
            for i in range(len(contacts)):
                if (contacts[i].phoneNumber == value):
                    val = UserCommunicator.get_new_value_for_field('phone number')
                    contacts[i].phoneNumber = val
                    break

        self._rewrite_contacts(contacts)