import random


# options to choose in the game 
rps_options = ["Камень", "Ножницы", "Бумага"]

# dict with rules of the game
rules: dict = {
    "Камень": "Ножницы",
    "Ножницы": "Бумага",
    "Бумага": "Камень"
}

# function that generates option made by bot 
def bot_generate_option(list) -> str:
    bot_choice = random.choice(list)
    return bot_choice


# function that decides if player has won or not
# returns True if player won and False if lost
def decide_winner(player_choice:str) -> bool:
    """
    returns True if player won
    and False if bot won
    """
    bot_choice:str = bot_generate_option(rps_options)
    print(f'bot choice: {bot_choice}, player choice: {player_choice}')
    if player_choice == bot_choice:
        # if choices are the same - call func again 
        return decide_winner(player_choice=player_choice)
    win_result = rules[player_choice] == bot_choice
    return win_result