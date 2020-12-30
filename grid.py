class Grid:
    '''
    Class which defines a sudoku board
    '''
    def __init__(self, grid: tuple):
        self.grid = grid
        self.size = len(grid[0])
        self.empty_cells = []
        self.subgrids = {}

    def get_subgrids(self) -> None:
        '''
        Get the coordinates of cells in subgrids and add them
        to the attributes of a Grid's exemplar
        :return: Filled attribute of a grid with coordinates of cells which are in subgrids
        '''
        size = int(self.size/3)
        for k in range(size):
            for x in range(0, size):
                rows = tuple([i, 0] for i in range(0+3*k, size+3*k))
                self.subgrids[(k, x)] = tuple((i[0], i[1]) for i in rows for i[1] in range(0+size*x, 3+size*x))

    def get_empty_cells(self) -> None:
        '''
        Get the coordinates of cells which need to be filled
        :return: Filled attribute of a grid with the list of cells which are empty
        '''
        empty_cells = []
        for row in range(self.size):
            empty_cells += [(row, i) for i in [col for col, x in enumerate(self.grid[row]) if x == 0]]
        self.empty_cells = empty_cells

    def update_cell_value(self, cell: tuple, number: int) -> None:
        '''
        Update a cell value to a given number
        :param cell: Coordinates of a cell
        :param number: A number with which update a cell
        :return: None
        '''
        self.grid[cell[0]][cell[1]] = number

    def zero_cell_value(self, cell: tuple) -> None:
        '''
        Set a cell value as 0
        :param cell: Coordinates of a cell
        :return: None
        '''
        self.grid[cell[0]][cell[1]] = 0

    def rollback_cell_value(self, cell: tuple, available_numbers: dict):
        '''
        Update a cell value to a given number
        :param cell: Coordinates of a cell
        :param number: A number with which update a cell
        :return: None
        '''
        n = 0

        def rollback(grid: Grid, cell: tuple = cell, n = n ):
            available_numbers[cell] = list(range(1, grid.size + 1))
            cell = grid.empty_cells[grid.empty_cells.index(cell) - 1]

            n += 1
            j = grid.get_cell_value(cell)

            try:
                grid.zero_cell_value(cell)
                available_numbers[cell].remove(j)
                if len(list(available_numbers.values())[0]) == 0:
                    print('done')
                if len(available_numbers[cell]) == 0:
                    return rollback(grid, cell, n)
            except ValueError:
                return rollback(grid, cell, n)
            else:
                return cell, n, j,  available_numbers

        return rollback(self, cell, n)

    def get_cell_value(self, cell: tuple) -> int:
        '''
        Get the value of a required cell
        :param cell: Coordinates of a cell
        :return: The value in a cell
        '''
        return self.grid[cell[0]][cell[1]]

    def get_row(self, row_number: int) -> list:
        '''
        Get the values of a required row
        :param row_number: Number of a row (values start from 0)
        :return: List of the values in a row
        '''
        return self.grid[row_number]

    def get_column(self, column_number: int) -> list:
        '''
        Get the values of a required column
        :param column_number: Number of a column (values start from 0)
        :return: List of the values in a column
        '''
        return [row[column_number] for row in self.grid]

    def get_subgrid(self) -> int:
        '''
        Get the total sum of the values of a subgrid
        :return: Sum of the values
        '''
        return sum([sum(i) for i in zip(*self.grid)])

    def check_row_unique(self, row_number: int, num: int) -> bool:
        '''
        Check if a given number already exists in a row
        :param row_number: Number of a row
        :param num: Checked number
        :return: True/False
        '''
        return not num in set(self.get_row(row_number))

    def check_column_unique(self, column_number: int, num: int) -> bool:
        '''
        Check if a given number already exists in a column
        :param column_number: Number of a column
        :param num: Checked number
        :return: True/False
        '''
        return num not in set(self.get_column(column_number))

    def check_subgrid_unique(self, cell: tuple, num: int) -> bool:
        '''
        Check if a given number already exists in a subgrid
        :param cell: Coordinates of a cell
        :param num: Checked number
        :return: True/False
        '''
        subgrid_values = []
        for subgrid in self.subgrids:
            if cell in self.subgrids[subgrid]:
                for subcell in self.subgrids[subgrid]:
                    subgrid_values.append(self.get_cell_value(subcell))
            if len(subgrid_values) > 0:
                break
        return num not in set(subgrid_values)

    def check_grid_complete(self) -> bool:
        '''
        Check of the grid is completed
        :return: True/False
        '''
        return not any(0 in line for line in self.grid)

    def print_grid(self) -> None:
        '''
        Print grid in console
        :return:
        '''
        print('\n'.join(' '.join(str(col) for col in row) for row in self.grid))
