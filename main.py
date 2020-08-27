# grid = (
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# )
#
# print(grid)


class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid

    def update_cell_value(self: object, cell: tuple, number: int):
        self.grid[cell[0]][cell[1]] = number

    def rollback_cell_value(self: object, cell: tuple):
        pass

    def get_cell_value(self: object, cell: tuple) -> int:
        return self.grid[cell[0]][cell[1]]

    def get_row(self: object, row_number: int) -> list:
        return self.grid[row_number]

    def get_column(self: object, column_number: int) -> list:
        return [row[column_number] for row in self.grid]

    def get_empty_cells(self: object) -> list:
        empty_cells = []
        for row in range(len(self.grid)):
            empty_cells += [(row, i) for i in [col for col, x in enumerate(mini_grid[row]) if x == 0]]
        return empty_cells

    def get_sum_subgrid(self: object) -> int:
        return sum([sum(i) for i in zip(*self.grid)])

    def copy_grid(self: object) -> tuple:
        return self.grid

    def check_row_unique(self: object, row_number: int, num: int) -> bool:
        return not num in set(self.get_row(row_number))

    def check_column_unique(self: object, column_number: int, num: int) -> bool:
        return not num in set(self.get_column(column_number))

    def solver(self: object):
        empty_cells = self.get_empty_cells()
        size = len(self.grid[0])
        available_numbers = {}
        for cell in empty_cells:
            available_numbers[cell] = list(range(1, size+1))

        try:
            i = 0
            while i < len(empty_cells):
                cell = empty_cells[i]
                j = 1
                while j < 4:

                    if j in available_numbers[cell]:
                        if self.check_row_unique(cell[0], j) and self.check_column_unique(cell[1], j):
                            self.update_cell_value(cell, j)
                            break

                        available_numbers[cell].remove(j)

                    if len(available_numbers[cell]) == 0:
                        available_numbers[cell] = list(range(1, size + 1))
                        cell = empty_cells[empty_cells.index(cell)-1]

                        i -= 1
                        j = self.get_cell_value(cell)
                        available_numbers[cell].remove(j)

                    j += 1
                i += 1
        except ValueError:
            print('This Sudoku can not be solved')
        else:
            print('done')


if __name__ == "__main__":
    mini_grid = (
        [2, 0, 3],
        [1, 0, 0],
        [0, 0, 2]
    )

    sudoku = SudokuSolver(mini_grid)

    a = sudoku.get_empty_cells()

    a = sudoku.get_cell_value((1, 1))

    a = sudoku.get_sum_subgrid()

    a = sudoku.get_column(1)

    a = sudoku.get_row(1)

    a = sudoku.check_row_unique(1, 1)

    sudoku.solver()

    print('\n'.join(' '.join(str(col) for col in row) for row in sudoku.grid))
    # a = sudoku.check_row_unique()
