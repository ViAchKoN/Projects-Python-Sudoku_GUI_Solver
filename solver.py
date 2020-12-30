from grid import Grid


class Solver:
    '''
    Class which defines solver for sudoku
    '''
    def solver(self, grid: Grid) -> Grid:
        '''
        Solve sudoku
        :param grid: Grid's exemplar
        :return: Solved Grid's exemplar
        '''
        grid.get_empty_cells()
        grid.get_subgrids()

        available_numbers = {}

        for cell in grid.empty_cells:
            available_numbers[cell] = list(range(1, grid.size+1))

        i = 0
        try:
            while i < len(grid.empty_cells):
                cell = grid.empty_cells[i]
                j = 1
                while j < grid.size + 1 or (i != 0 and j != 0):

                    if j in available_numbers[cell]:
                        if grid.check_row_unique(cell[0], j) and grid.check_column_unique(cell[1], j) \
                                and grid.check_subgrid_unique(cell, j):
                            grid.update_cell_value(cell, j)
                            break

                        available_numbers[cell].remove(j)

                    if len(available_numbers[cell]) == 0:
                        cell, n, j, available_numbers = grid.rollback_cell_value(cell, available_numbers)
                        i -= n
                    j += 1
                i += 1
        except RecursionError:
            print('This grid cant be solved')
            raise RecursionError
        else:
            grid.print_grid()
            return grid
