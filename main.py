
# print(grid)

# mini_grid = (
#     [2, 0, 3],
#     [1, 0, 0],
#     [0, 0, 1]
# )


class Grid:
    def __init__(self: object, grid: tuple):
        self.grid = grid
        self.size = len(grid[0])
        self.subgrid_coordinates = {}

    def get_subgrid_coordinates(self: object) -> None:
        '''
        Get the coordinates of cells in subgrids and add them
        to the attributes of a Grid's exemplar
        :return:
        '''
        size = int(self.size/3)
        for k in range(size):
            for x in range(0, size):
                rows = tuple([i, 0] for i in range(0+3*k, size+3*k))
                self.subgrid_coordinates[(k, x)] = tuple((i[0], i[1]) for i in rows for i[1] in range(0+size*x, 3+size*x))

    def update_cell_value(self: object, cell: tuple, number: int) -> None:
        '''
        Update a cell value to a given number
        :param cell: Coordinates of a cell
        :param number: A number with which update a cell
        :return: None
        '''
        self.grid[cell[0]][cell[1]] = number

    def rollback_cell_value(self: object, cell: tuple) -> None:
        '''
        Placeholder fot the function to go back to a previous cell and restore its last value
        :param cell: Coordinates of a cell
        :return: None
        '''
        pass

    def get_cell_value(self: object, cell: tuple) -> int:
        '''
        Get the value of a required cell
        :param cell: Coordinates of a cell
        :return: The value in a cell
        '''
        return self.grid[cell[0]][cell[1]]

    def get_row(self: object, row_number: int) -> list:
        '''
        Get the values of a required row
        :param row_number: Number of a row (values start from 0)
        :return: List of the values in a row
        '''
        return self.grid[row_number]

    def get_column(self: object, column_number: int) -> list:
        '''
        Get the values of a required column
        :param column_number: Number of a column (values start from 0)
        :return: List of the values in a column
        '''
        return [row[column_number] for row in self.grid]

    def get_empty_cells(self: object) -> list:
        '''
        Get the coordinates of cells which need to be filled
        :return: List of a cells which need to be filled
        '''
        empty_cells = []
        for row in range(self.size):
            empty_cells += [(row, i) for i in [col for col, x in enumerate(self.grid[row]) if x == 0]]
        return empty_cells

    def get_sum_subgrid(self: object) -> int:
        '''
        Get the total sum of the values of a subgrid
        :return: Sum of the values
        '''
        return sum([sum(i) for i in zip(*self.grid)])

    def copy_grid(self: object) -> tuple:
        '''
        Get the copy of a grid
        :return: The copy of a grid
        '''
        return self.grid

    def check_row_unique(self: object, row_number: int, num: int) -> bool:
        '''
        Check if a given number already exists in a row
        :param row_number: Number of a row
        :param num: Checked number
        :return: True/False
        '''
        return not num in set(self.get_row(row_number))

    def check_column_unique(self: object, column_number: int, num: int) -> bool:
        '''
        Check if a given number already exists in a column
        :param column_number: Number of a column
        :param num: Checked number
        :return: True/False
        '''
        return not num in set(self.get_column(column_number))


    def check_subgrid_unique(self: object, cell: tuple) -> tuple:
        self.get_subgrid_coordinates()


        rows = tuple([i, 0] for i in range(3))
        subgrid1 = tuple((i[0], i[1]) for i in rows for i[0] in range(3))




        subgrid01 = tuple((j[0], j[1]) for j in a for j[0] in range(3))



class Solver:

    def solver(grid: object):
        empty_cells = grid.get_empty_cells()
        available_numbers = {}
        for cell in empty_cells:
            available_numbers[cell] = list(range(1, grid.size+1))

        try:
            i = 0
            while i < len(empty_cells):
                cell = empty_cells[i]
                j = 1
                while j < grid.size + 1:

                    if j in available_numbers[cell]:
                        if grid.check_row_unique(cell[0], j) and grid.check_column_unique(cell[1], j):
                            grid.update_cell_value(cell, j)
                            break

                        available_numbers[cell].remove(j)

                    if len(available_numbers[cell]) == 0:
                        available_numbers[cell] = list(range(1, grid.size + 1))
                        cell = empty_cells[empty_cells.index(cell)-1]

                        i -= 1
                        j = grid.get_cell_value(cell)
                        available_numbers[cell].remove(j)

                    j += 1
                i += 1
        except ValueError:
            print('This Sudoku board can not be solved')
        else:
            print('Done')


if __name__ == "__main__":

    grid = (
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    )

    # grid = (
    #     [2, 0, 3],
    #     [1, 0, 0],
    #     [0, 0, 1]
    # )

    grid = Grid(grid)
    grid.get_subgrid_coordinates()

    a = grid.get_empty_cells()

    a = grid.get_cell_value((1, 1))

    a = grid.get_sum_subgrid()

    a = grid.get_column(1)

    a = grid.get_row(1)

    a = grid.check_row_unique(1, 1)

    Solver.solver(grid)

    #sudoku.solver()

    print('\n'.join(' '.join(str(col) for col in row) for row in grid.grid))
    # a = sudoku.check_row_unique()
