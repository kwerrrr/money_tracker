import json

DATA_FILE = "finance_data.json"
transactions = []


def load_data():
    global transactions
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            transactions = json.load(f)
        print("✅ Данные загружены!")
    except FileNotFoundError:
        print("📁 Файл данных не найден. Начинаем с чистого листа.")
        transactions = []
    except Exception as e:
        print(f"❌ Ошибка загрузки: {e}")
        transactions = []


def save_data():
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(transactions, f, ensure_ascii=False, indent=4)
        print("💾 Данные сохранены!")
    except Exception as e:
        print(f"❌ Ошибка сохранения: {e}")


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


def show_all():
    if len(transactions) == 0:
        print("\n📭 Список операций пуст.")
        return

    print("\n--- Все финансовые операции ---")
    for i, transaction in enumerate(transactions, 1):
        print(
            f"{i}. {transaction['type']}: {transaction['amount']} руб. - {transaction['category']} ({transaction['description']})")
    print("--------------------------------")


def main():
    load_data()

    while True:
        print("\n=== 💰 МОИ ФИНАНСЫ ===")
        print("1. Добавить расход")
        print("2. Показать все операции")
        print("3. Выйти и сохранить")

        choice = input("Выберите пункт меню (1-3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_all()
        elif choice == "3":
            save_data()
            print("Выход из программы. До свидания! 👋")
            break
        else:
            print("❌ Неверный выбор! Попробуйте снова.")


# Исправленная строка
if __name__ == "__main__":
    main()
