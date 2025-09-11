def filter_by_state(items: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция, возвращающая список словарей,
    в которых ключ 'state' = 'EXECUTED'
    """
    list_executed = []
    for item in items:
        if item["state"] == state:
            list_executed.append(item)
    return list_executed


def sort_by_date(items: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция, сортирующая список словарей по дате,
    начиная с последних операций
    """
    sorted_list = sorted(items, key=lambda x: x["date"], reverse=reverse)
    return sorted_list
