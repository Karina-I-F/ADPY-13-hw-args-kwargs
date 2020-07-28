class Contact:
    def __init__(self, name, last_name, phone_number, favorite=False, *args, **kwargs):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorite = favorite
        self.args = args
        self.kwargs = [f'{key}: {item}' for key, item in kwargs.items()]

    def __str__(self):
        my_n = '\n\t'
        return \
            f'Имя: {self.name}\n' \
            f'Фамилия: {self.last_name}\n' \
            f'Телефон: {self.phone_number}\n' \
            f'Избранный: {"да" if self.favorite else "нет"}\n' \
            f'Дополнительная информация:{my_n.join(self.args) if self.args else ""}' \
            f'{my_n + my_n.join(item for item in self.kwargs) if self.kwargs else ""}' \
            f'{my_n + "нет" if not self.args and not self.kwargs else ""}'


class PhoneBook:
    def __init__(self, book_name):
        self.book_name = book_name
        print(f'Телефонная книга "{self.book_name}".')
        self.contact_list = []

    def show_contacts(self):
        for contact in self.contact_list:
            print(contact)

    def add_new_contact(self, contact):
        self.contact_list.append(contact)

    def del_contact_by_number(self, phone_number):
        for Contact in self.contact_list:
            if Contact.phone_number == phone_number:
                self.contact_list.remove(Contact)
                print(f'Данный номер {phone_number} успешно удалён.')
        else:
            print(f'Данный номер {phone_number} не найден.')

    def search_all_favorite_numbers(self):
        for Contact in self.contact_list:
            if Contact.favorite:
                print(Contact.phone_number)
                break
        else:
            print('Вы ещё не добавили никого в "Избранные".')

    def search_contact_by_full_name(self, name, last_name):
        for Contact in self.contact_list:
            if Contact.name == name and Contact.last_name == last_name:
                print(Contact.phone_number)
                break
        else:
            print(f'Контакт {name} {last_name} не найден.')


if __name__ == '__main__':
    test_book = PhoneBook('Тык')
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    lilo = Contact('Lo', 'Li', '+79876543210', favorite=True, email='lo@li.com')
    kinfa = Contact('Fa', 'Kin', '+78971234560', favorite=True)
    test_book.add_new_contact(jhon)
    test_book.search_all_favorite_numbers()
    test_book.add_new_contact(kinfa)
    test_book.show_contacts()
    test_book.search_all_favorite_numbers()
    test_book.del_contact_by_number('+78971234560')
    test_book.search_contact_by_full_name('Fa', 'Kin')
    test_book.add_new_contact(lilo)
    test_book.show_contacts()
    test_book.search_contact_by_full_name('Lo', 'Li')
