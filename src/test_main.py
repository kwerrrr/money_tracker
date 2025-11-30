from main import transactions

def test_add_expense_increases_list():
    start_count = len(transactions)
    transactions.append({
        "type": "расход",
        "amount": "1000",
        "category": "еда",
        "description": "продукты"
    })
    assert len(transactions) == start_count + 1

def test_transactions_not_empty_after_add():
    transactions.clear()
    transactions.append({
        "type": "расход",
        "amount": "500",
        "category": "транспорт",
        "description": "бензин"
    })
    assert len(transactions) > 0