import csv

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook():
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):

        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self, name):
        for contact in self._contacts:

            if contact.name.lower() == name.lower():
                self._print_contact(contact)

                for idx, contact in enumerate(self._contacts):
                    if contact.name.lower() == name.lower():
                        del self._contacts[idx]

                print(' ')
                print('UPDATE DATA')
                name = str(input('Contact name: '))
                phone = str(input('Contact phone : '))
                email = str(input('Email: '))
                # Se guardan los datos nuevos
                contact = Contact(name, phone, email)
                self._contacts.append(contact)
                self._save()
                break
        else:
            
            self._not_found()

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * ---')
        print('Name: {}'.format(contact.name))
        print('telephone number: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        print('***************')
        print('Not found!')
        print('***************')


def run():
    contact_book = ContactBook()
    with open('contacts.csv', 'w+') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            elif row == []:
                continue
            else:
                contact_book.add(row[0], row[1], row[2])
    while True:
        command = str(input('''
            What do you want to do?
            [a]add contact
            [ac]to update contact
            [b]search for contact
            [e]remove contact
            [l]present contact
            [s]exit
        '''))
        if command == 'a':
            name = str(input('Contact name: '))
            phone = str(input('Contact phone : '))
            email = str(input('Email : '))
            contact_book.add(name, phone, email)
        elif command == 'ac':
            name = str(input('Contact name: '))
            contact_book.update(name)
        elif command == 'b':
            name = str(input('Contact name: '))
            contact_book.search(name)
        elif command == 'e':
            name = str(input('Contact name: '))
            contact_book.delete(name)
        elif command == 'l':
            contact_book.show_all()
        elif command == 's':
            break
        else:
            print('command not found')


if __name__ == '__main__':
    run()