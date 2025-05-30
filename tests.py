# # user_data: dict = {
# #     'in_game': False,
# #     'secret_number': None,
# #     'attempts': None,
# #     'total_games': 0,
# #     'wins': 0
# # }

# # print(user_data.get('in_game'))


# user_data: dict = {}

# user_data["123"] = {
#     "in_game": False,
#     "secret_number": None,
#     "attempts": None,
#     "total_games": 0,
#     "wins": 0,
# }

# user_data["124"] = {
#     "in_game": False,
#     "secret_number": None,
#     "attempts": None,
#     "total_games": 0,
#     "wins": 0,
# }

# print(user_data)


# some_list = [7, 14, 28, 32, 32, '56']


# def custom_filter(list) -> bool:
#     list_of_integers: list = []
#     for _ in range(len(some_list)):
#         if type(some_list[_]) == int:
#             list_of_integers.append(some_list[_])
#         # elif type(some_list[_]) == str:
#         #     try:
#         #         list_of_integers.append(int(some_list[_]))
#         #     except:
#         #         continue
#         else:
#             continue
#     print(list_of_integers)
#     approved_integers: list = []
#     valiadtion_var = 7
#     # test_counter = 0
#     threshold = 83
#     for _ in range(len(list_of_integers)):
#         if list_of_integers[_] % valiadtion_var == 0:
#             approved_integers.append(list_of_integers[_])
#     print(approved_integers)
#     return sum(approved_integers) < threshold


# print(custom_filter(some_list))

# print(2 + some_list[0])


# some_srting = "яяяяяяяяяяяяяяяяяяяяяя"

# anonymous_filter = lambda x: x.lower().count('я') >= 23

# print(anonymous_filter(some_srting))
