# BANK

class Bank:
    def __init__(self, name):
        # хранилище переменных
        self.name = name
        self.clients = {'дмитрий':120000, 'анна':10000, 'иван':70000}
        self.credits = {}
    
    def add_client(self):
        # добавляет клиента
        self.clients.update({add_name: add_balance})
        return self.clients
    
    def delete_client(self):
        # удаляет клиента
        result = self.clients.pop(remove_client, 'клиент не найден')
        return self.clients if result != 'клиент не найден' else result
    
    def replenish_balance(self):
        # меняет баланс клиента
        if replenish_client in self.clients:
            self.clients[replenish_client] = balance_replenish
            return self.clients
        else:
            return 'клиент не найден'
    
    def credit_system(self):
        # кредитная система
        replenish_credit = int(input('введите сумму кредита > '))

# проверка
while True:
    finances = Bank("Мой банк")

    print('добав.клиента(add)/удал.клиента(re)/поменять баланс(repl)')
    user_choice = input('> ')

    if user_choice == 'add':
        add_name = input('введите имя > ')
        add_balance = int(input('введите баланс > '))
        print(finances.add_client())
    elif user_choice == 're':
        remove_client = input('введите имя клиента которого надо удалить > ')
        print(finances.delete_client())
    elif user_choice == 'repl':
        replenish_client = input('введите имя клиента у которого надо поменять баланс > ')
        balance_replenish = int(input('введите новый текущий баланс > '))
        print(finances.replenish_balance())
