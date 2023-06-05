def is_unique(item_id, items):
    for item in items:
        if item['id'] == item_id:
            return False
    return True
