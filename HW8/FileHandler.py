from Contact import Contact

class FileHandler:
    def save_contacts(self, contacts, filename, file_ext):
        file = f'{filename}.{file_ext}'
        with open(file, 'a') as f:
            prepared_contacts = list(map(lambda contact: repr(contact), contacts))
            for contact in prepared_contacts:
                f.write(contact)
                f.write('\n')


    def get_contacts(self, filename, file_ext):
      delim = '--'
      contacts = []
      file = f'{filename}.{file_ext}'
      with open(file, 'r') as f:
        for line in f:
            contact = line.strip().split(delim)
            contacts.append(Contact(*contact))
      return contacts
            

    def rewrite_contacts(self, contacts, filename, file_ext):
        file = f'{filename}.{file_ext}'
        with open(file, 'w') as f:
            prepared_contacts = list(map(lambda contact: repr(contact), contacts))
            for contact in prepared_contacts:
                f.write(contact)
                f.write('\n')