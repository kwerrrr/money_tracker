# Список для хранения финансовых операций
transactions = []


# Функция добавления расхода
def add_expense():
    print("\n--- Добавление расхода ---")
    amount = input("Введите сумму расхода: ")
    category = input("Введите категорию (еда, транспорт, развлечения): ")
    description = input("Введите описание: ")

    new_transaction = {
        "type": "расход",
        "amount": amount,
        "category": category,
        "description": description
    }

    transactions.append(new_transaction)
    print("✅ Расход добавлен!")


# Функция показа всех операций
def show_all():
    if len(transactions) == 0:
        print("\n📭 Список операций пуст.")
        return

    print("\n--- Все финансовые операции ---")
    for i, transaction in enumerate(transactions, 1):
        print(
            f"{i}. {transaction['type']}: {transaction['amount']} руб. - {transaction['category']} ({transaction['description']})")
    print("--------------------------------")


# Главное меню
def main():
    while True:
        print("\n=== 💰 МОИ ФИНАНСЫ ===")
        print("1. Добавить расход")
        print("2. Показать все операции")
        print("3. Выйти")

        choice = input("Выберите пункт меню (1-3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_all()
        elif choice == "3":
            print("Выход из программы. До свидания! 👋")
            break
        else:
            print("❌ Неверный выбор! Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main()
