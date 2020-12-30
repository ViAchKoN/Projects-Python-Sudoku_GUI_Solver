import pygame

from grid import Grid

# SETTING GLOBAL VARIABLES
# Setting number of frames per second
FPS = 60

# Setting color variables
COLORS = {
        'RED': (255, 0, 0),
        'GREEN': (0, 255, 0),
        'WHITE': (255, 255, 255),
        'BLACK': (0, 0, 0),
        'LIGHT_GRAY': (200, 200, 200)
        }

# Setting the screen size
WIDTH = 270
HEIGHT = 270
# Setting koef to increase the screen size
SCREEN_KOEF = 2

# Setting the final width/height of the screen
SCREEN_WIDTH = WIDTH*SCREEN_KOEF
SCREEN_HEIGHT = HEIGHT*SCREEN_KOEF

# Setting the size of a subgrid
SUBGRID_SIZE = (WIDTH // 3)*SCREEN_KOEF
# Setting the size of a cell
CELL_SIZE = SUBGRID_SIZE // 3


class GUI:
    '''
    Class which defines all actions with the display
    '''
    def __init__(self):
        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   # Initialize a window for display
        self.display.fill(COLORS['WHITE'])
        self.font = pygame.font.SysFont('arial', 50)
        self.clock = pygame.time.Clock()                                        # Initialize clock
        self.selected = ()
        self.variants = {}

    def wait(self) -> None:
        '''
        Wait before updating the display
        :return:
        '''
        # Set number of frames per second
        self.clock.tick(FPS)

    def draw_grid(self) -> None:
        '''
        Draw grid on the display
        :return:
        '''
        ### Draw Minor Lines
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):  # draw vertical lines
            pygame.draw.line(self.display, COLORS['LIGHT_GRAY'], (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):  # draw horizontal lines
            pygame.draw.line(self.display, COLORS['LIGHT_GRAY'], (0, y), (SCREEN_WIDTH, y))

        ### Draw Major Lines
        for x in range(0, SCREEN_WIDTH, SUBGRID_SIZE):  # draw vertical lines
            pygame.draw.line(self.display, COLORS['BLACK'], (x, 0), (x, SCREEN_WIDTH))
        for y in range(0, SCREEN_HEIGHT, SUBGRID_SIZE):  # draw horizontal lines
            pygame.draw.line(self.display, COLORS['BLACK'], (0, y), (SCREEN_HEIGHT, y))

    def display_cell_value(self, cell: tuple, value: int) -> None:
        '''
        Display value in a cell
        :param cell: Coordinates of a cell
        :param value: Value to display
        :return:
        '''
        x = cell[1] * CELL_SIZE + CELL_SIZE / 3
        y = cell[0] * CELL_SIZE + CELL_SIZE / 5
        if value != 0:
            text = self.font.render(str(value), True, COLORS['BLACK'])
            self.display.blit(text, (x, y))
        elif cell in self.variants:
            x = cell[1]
            y = cell[0]
            text = self.font.render(str(self.variants[cell]), True, COLORS['LIGHT_GRAY'])
            self.display.blit(text, (x * CELL_SIZE + CELL_SIZE - CELL_SIZE / 3, y * CELL_SIZE))
        else:
            pygame.draw.rect(self.display, COLORS['WHITE'], (x, y, CELL_SIZE/2, CELL_SIZE/2))

    def display_grid_values(self, grid: Grid) -> None:
        '''
        Display all grid values
        :param grid: Grid object
        :return:
        '''
        size = len(grid.grid)
        for j in range(size):
            for i in range(size):
                cell = (i, j)
                self.display_cell_value(cell, grid.get_cell_value(cell))

    def update_display(self) -> None:
        '''
        Clear the display of all data by filling it with white color
        :return:
        '''
        self.display.fill(COLORS['WHITE'])

    def get_selected_cell(self, pos: tuple) -> tuple or None:
        '''
        Get a cell which is selected by mouse
        :param pos: Position of a mouse
        :return: Coordinates of a selected cell or None
        '''
        if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
            x = int(pos[1] // CELL_SIZE)
            y = int(pos[0] // CELL_SIZE)
            cell = (x, y)
            return cell
        else:
            return None

    def select_cell(self, cell: tuple) -> None:
        '''
        Display that cell was selected
        :param cell: Coordinates of a selected cell
        :return:
        '''
        self.selected = cell
        y, x = self.selected
        pygame.draw.rect(self.display, COLORS['RED'], (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

    def add_variant(self, value: int) -> None:
        '''
        Add variant to cell dictionary
        :param value: Chosen user variant for selected cell
        :return:
        '''
        self.variants[self.selected] = value

    def display_message(self, text_type: str) -> None:
        '''
        Display text to display
        :param text_type: Chosen type of text to show on the display
        :return:
        '''
        text = ''
        self.display.fill(COLORS['WHITE'])
        if text_type == 'victory':
            text = 'Sudoku is completed!'
        elif text_type == 'bad_grid':
            text = 'Board cant be solved!'
        text = self.font.render(text, True, COLORS['BLACK'])
        self.display.blit(text, (SCREEN_WIDTH/5, SCREEN_HEIGHT/2))
