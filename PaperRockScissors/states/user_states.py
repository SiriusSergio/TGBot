# dict with user date
user_data: dict = {}

def start_game(user_id:int):
    user_data[user_id] = {'in_game': True}

def end_game(user_id:int):
    user_data[user_id] = {'in_game': False}

def is_in_game(user_id:int) -> bool:
    return user_id in user_data
