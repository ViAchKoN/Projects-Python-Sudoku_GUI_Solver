import sys
import copy
import pygame

from solver import Solver
from grid import Grid
from gui import GUI


def run(grid: tuple):
    pygame.init()
    pygame.display.set_caption('Sudoku')  # Setting screen caption name

    grid_obj = Grid(grid)
    solved_grid_obj = copy.deepcopy(grid_obj)

    gui = GUI()
    gui.draw_grid()
    gui.display_grid_values(grid_obj)

    running = True
    value = None
    cell = None
    complete = False
    bad_grid = False

    try:
        solved_grid_obj = Solver().solver(solved_grid_obj)
    except RecursionError:
        bad_grid = True

    while running:  # main game loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    value = 1
                if event.key == pygame.K_2:
                    value = 2
                if event.key == pygame.K_3:
                    value = 3
                if event.key == pygame.K_4:
                    value = 4
                if event.key == pygame.K_5:
                    value = 5
                if event.key == pygame.K_6:
                    value = 6
                if event.key == pygame.K_7:
                    value = 7
                if event.key == pygame.K_8:
                    value = 8
                if event.key == pygame.K_9:
                    value = 9
                if event.key == pygame.K_RETURN:
                    variants_dict = gui.variants
                    for key in variants_dict:
                        variant = variants_dict[key]
                        if variant == solved_grid_obj.get_cell_value(key):
                            grid_obj.update_cell_value(key, variant)
                            if grid_obj.check_grid_complete():
                                complete = True
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                cell = gui.get_selected_cell(pos)
                if cell:
                    value = None

            if gui.selected and value != None:
                gui.add_variant(value)

            gui.update_display()
            gui.draw_grid()
            gui.display_grid_values(grid_obj)
            if cell:
                gui.select_cell(cell)

            if complete:
                gui.display_message('victory')
            elif bad_grid:
                gui.display_message('bad_grid')

            pygame.display.update()


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

    run(grid)
    pygame.quit()
    sys.exit()

    # grid = (
    #     [5, 3, 1, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
    # )


    # grid = (
    #     [4, 0, 3, 0, 0, 2, 0, 0, 0],
    #     [5, 0, 0, 0, 6, 0, 1, 2, 0],
    #     [9, 0, 0, 0, 0, 0, 0, 0, 4],
    #     [0, 0, 8, 0, 7, 0, 0, 0, 0],
    #     [0, 0, 0, 2, 0, 3, 0, 0, 8],
    #     [0, 3, 6, 0, 0, 0, 7, 0, 0],
    #     [0, 7, 0, 9, 2, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 5, 0, 9, 6],
    #     [0, 0, 0, 8, 0, 4, 5, 0, 0]
    # )

    # grid = (
    #     [2, 0, 3],
    #     [1, 0, 0],
    #     [0, 0, 1]
    # )
