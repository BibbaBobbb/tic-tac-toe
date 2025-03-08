from typing import TypeAlias


Board: TypeAlias = tuple[list[str], ...]


def print_board(board: Board) -> None:
    """Функция для вывода игрового поля в консоль"""
    print("\n   0   1   2\n")
    for index, row in enumerate(board):
        print(f'{index}  {"   ".join(row)} \n')


def check_winner(board: Board) -> str | None:
    """Функция для проверки завершенности игры"""
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            return board[0][i]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]

    # Проверка на ничью
    if all(cell != "-" for row in board for cell in row):
        return "Draw"

    return None


def is_valid_move(board: Board, row: int, col: int) -> bool:
    """Функция проверки корректности ввода"""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "-"


def get_player_move(board: Board) -> tuple[int, int]:
    """Функция получения хода от игрока"""
    while True:
        try:
            move = input("Введите ваш ход (строка и столбец через пробел): ")
            row, col = map(int, move.split())
            if is_valid_move(board, row, col):
                return (row, col)
            else:
                print("Некорректный ход. Попробуйте снова.")
        except ValueError:
            print("Введите два числа через пробел.")


def tic_tac_toe() -> None:
    """Основная игровая функция"""
    board = tuple(["-" for _ in range(3)] for _ in range(3))
    current_player = "X"

    while True:
        print_board(board)
        print(f"Ход игрока {current_player}")
        row, col = get_player_move(board)
        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "Draw":
                print("Игра окончена. Ничья!")
            else:
                print(f"Поздравляем! Победил игрок {winner}!")
            return

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
