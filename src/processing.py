def filter_by_state(items: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, возвращающая список словарей, в которых ключ 'state' = 'EXECUTED'"""
    executed_item = []
    for item in items:
        if item["state"] == state:
            executed_item.append(item)
    return executed_item


def sort_by_date(items: list[dict], reverse: bool = True) -> list[dict]:
    """Функция, сортирующая список словарей по дате, начиная с последних операций"""
    sorted_list = sorted(items, key=lambda x: x["date"], reverse=reverse)
    return sorted_list
