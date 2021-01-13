import random
import pickle
class Sudoku:
    def __init__(self, mode, num_cell):
        self.mode = mode
        self.num_cell = num_cell
        self.board = [[0]*9 for _ in range(9)]
        self.def_board = [[0] * 9 for _ in range(9)]
        self.cord = []
        for i in range(9):
            for j in range(9):
                self.cord.append([i,j])
        random.shuffle(self.cord)
        for j in range(self.num_cell):
            self.board[self.cord[j][0]][self.cord[j][1]] = self.def_board[self.cord[j][0]][self.cord[j][1]] = random.randint(1,9)

        self.mode_game()

    def print_def_board(self):
        self.def_bo = self.board
        for i in range(len(self.def_bo)):
            if i % 3 == 0 and i != 0:
                print("----------------------------------")
            for j in range(len(self.def_bo[i])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end=' ')
                if j == 8:
                    print(self.def_bo[i][j])
                else:
                    print(str(self.def_bo[i][j]) + ' ', end=' ')





    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def valid(self, num, pos):
        bo = self.board
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(bo[0])):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if bo[i][j] == num and (i, j) != pos:
                    return False
        return True

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find
        for i in range(1, 10):
            if self.valid( i, (row, col)):
                self.board[row][col] = i

                if self.solve():
                    return True

                self.board[row][col] = 0
        return False

    def manual_game(self):
        print('Хотите ли вы загрузить старую игру или начать новую?')
        print('Введите 1 для продолжения старой игры или 2 для начала новой:')
        if int(input()) == 1:
            pkl_file = open('data.pkl', 'rb')
            self.board = pickle.load(pkl_file)
            pkl_file.close()


        self.print_def_board()
        cont = True
        while cont:
            print('Введите Строку(От 1 до 9), Колонку(От 1 до 9), Число(От 1 до 9):')
            row, col, num = map(int, input().split())
            self.board[row-1][col-1] = num
            print("_______________________________________")
            self.print_def_board()


            cont = False
            for i in range(9):
                for j in range(9):
                    if self.valid(self.board[i][j], (i, j)) == False:
                        cont = True
            print('Введите 1 для сохранения игры или 2 для продолжения:')
            if int(input()) == 1:
                output = open('data.pkl', 'wb')
                pickle.dump(self.board, output)
                output.close()
                return
        print('Вы решили!!!')

    def mode_game(self):
        if self.mode == 'manual':
            self.manual_game()
        elif self.mode == 'computer':
            self.print_def_board()
            self.solve()
            print("_______________________________________")
            if self.board == self.def_board:
                print('нет решения!')
            else:
                self.print_def_board()


a = Sudoku('manual', 5)
