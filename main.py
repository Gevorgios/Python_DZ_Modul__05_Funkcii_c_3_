# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
# a = 24
# b = 36
# result = gcd(a, b)
# print("Наибольший общий делитель чисел", a, "и", b, ":", result)



# import random
#
# def generate_number():
#     
#     digits = list(range(10))
#     random.shuffle(digits)
#     number = digits[:4]
#     return number
#
# def get_user_input():
#     
#     while True:
#         user_input = input("Введите четырехзначное число: ")
#         if user_input.isdigit() and len(user_input) == 4:
#             return [int(digit) for digit in user_input]
#         else:
#             print("Пожалуйста, введите правильное четырехзначное число.")

# def count_bulls_and_cows(secret_number, user_number):
#     bulls = 0
#     cows = 0
#
#     for i in range(len(secret_number)):
#         if secret_number[i] == user_number[i]:
#             bulls += 1
#         elif user_number[i] in secret_number:
#             cows += 1
#
#     return bulls, cows
#
# def play_game(secret_number, attempts):
#     user_number = get_user_input()
#     bulls, cows = count_bulls_and_cows(secret_number, user_number)
#     attempts += 1
#
#     if bulls == 4:
#         print("Поздравляю, вы угадали число!")
#         print("Количество попыток:", attempts)
#     else:
#         print("Быки:", bulls)
#         print("Коровы:", cows)
#         play_game(secret_number, attempts)
#
#
# print("Добро пожаловать в игру 'Быки и коровы'!")
#
# secret_number = generate_number()
# attempts = 0
#
# play_game(secret_number, attempts)

# def is_valid_move(x, y, board):
#
#     if x >= 0 and x < len(board) and y >= 0 and y < len(board) and board[x][y] == -1:
#         return True
#     return False
#
# def find_knight_tour(board, x, y, move_count):
#
#     if move_count == len(board) * len(board[0]):
#         return True
#
#
#     row_moves = [2, 1, -1, -2, -2, -1, 1, 2]
#     col_moves = [1, 2, 2, 1, -1, -2, -2, -1]
#
#
#     for i in range(8):
#         next_x = x + row_moves[i]
#         next_y = y + col_moves[i]
#
#
#         if is_valid_move(next_x, next_y, board):
#
#             board[next_x][next_y] = move_count
#
#
#             if find_knight_tour(board, next_x, next_y, move_count + 1):
#                 return True
#
#
#             board[next_x][next_y] = -1
#
#     return False
#
# def print_board(board):
#     for row in board:
#         for cell in row:
#             print(str(cell).rjust(2), end=" ")
#         print()
#
#
# n = 6
# board = [[-1 for _ in range(n)] for _ in range(n)]
#
# start_x = int(input("Введите начальную координату X (от 0 до {}): ".format(n-1)))
# start_y = int(input("Введите начальную координату Y (от 0 до {}): ".format(n-1)))
#
# board[start_x][start_y] = 0
#
# if find_knight_tour(board, start_x, start_y, 1):
#     print("Путь коня:")
#     print_board(board)
# else:
#     print("Путь не найден.")




# import random
#
# def create_board():
#     board = [[0 for _ in range(4)] for _ in range(4)]
#     numbers = list(range(1, 16))
#     random.shuffle(numbers)
#
#     for i in range(4):
#         for j in range(4):
#             if numbers:
#                 board[i][j] = numbers.pop()
#
#     return board
#
# def print_board(board):
#     for row in board:
#         for cell in row:
#             print(str(cell).rjust(2), end=" ")
#         print()
#
# def find_empty_cell(board):
#     for i in range(4):
#         for j in range(4):
#             if board[i][j] == 0:
#                 return i, j
#
# def move(board, direction):
#     i, j = find_empty_cell(board)
#
#     if direction == "влево" and j > 0:
#         board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
#     elif direction == "вправо" and j < 3:
#         board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
#     elif direction == "вверх" and i > 0:
#         board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
#     elif direction == "вниз" and i < 3:
#         board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
#
# def is_solved(board):
#     numbers = [board[i][j] for i in range(4) for j in range(4)]
#     return numbers == list(range(1, 16))
#
# board = create_board()
# print("Игра \"Пятнашки\"")
# print_board(board)
#
# while True:
#     move_direction = input("Введите направление (влево, вправо, вверх, вниз): ")
#     move(board, move_direction)
#     print_board(board)
#
#     if is_solved(board):
#         print("Поздравляю! Вы решили головоломку \"Пятнашки\"!")
#         break