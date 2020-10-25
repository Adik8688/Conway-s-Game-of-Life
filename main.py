import pygame


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 5
        self.live = -1
        self.next = 0

    def is_pressed(self, x, y):
        if x > self.x and x < self.x + self.size and y > self.y and y < self.y + self.size:
            return True
        return False

    def draw(self, window):
        if self.live == 1:
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)
        pygame.draw.rect(window, color, (self.x, self.y, self.size, self.size))





class Game:
    cells = []
    for x in range(0, 700, 5):
        cell1 = []
        for y in range(0, 1000, 5):
            cell1.append(Cell(y, x))
        cells.append(cell1)

    window = pygame.display.set_mode((1000, 700))


    @classmethod
    def initialize_game(cls, delay):
        run = True
        while run:
            if cls.isQuit():
                run = False
            if pygame.mouse.get_pressed()[0]:
                for l in cls.cells:
                    for c in l:
                        if c.is_pressed(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                            c.live = 1
            if pygame.mouse.get_pressed()[2]:
                for l in cls.cells:
                    for c in l:
                        if c.is_pressed(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                            c.live = -1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                run = False
            cls.update(cls.window, delay, 1)

    @classmethod
    def run_game(cls, delay):
        run = True
        while run:
            if cls.isQuit():
                run = False
            cls.survived()
            cls.update(cls.window, delay)

    @staticmethod
    def isQuit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

    @classmethod
    def update(cls, window, delay, mode=0):
        window.fill((0, 0, 0))
        for l in cls.cells:
            for c in l:
                c.draw(window)
        if mode == 1:
            cls.draw_lines(window)
        pygame.display.update()
        pygame.time.delay(delay)
        pygame.time.Clock().tick(60)

    @staticmethod
    def draw_lines(window):
        for i in range(5, 1000, 5):
            pygame.draw.line(window, (192, 192, 192), (i, 0), (i, 700))
        for i in range(5, 700, 5):
            pygame.draw.line(window, (192, 192, 192), (0, i), (1000, i))

    @classmethod
    def survived(cls):
        cls.neighbours(cls.cells)
        for x in range(len(cls.cells)):
            for y in range(len(cls.cells[0])):
                cls.cells[x][y].live = cls.cells[x][y].next

    @staticmethod
    def neighbours(cells):
        for x in range(len(cells)):
            for y in range(len(cells[0])):
                n = 0
                for x1 in range(3):
                    for y1 in range(3):
                        try:
                            if x1 == 1 and y1 == 1:
                                pass
                            elif x - 1 + x1 < 0 or y - 1 + y1 < 0:
                                pass
                            elif cells[x - 1 + x1][y - 1 + y1].live == 1:
                                n += 1
                        except IndexError:
                            pass
                if cells[x][y].live == 1:
                    if n != 2 and n != 3:
                        cells[x][y].next = -1
                    else:
                        cells[x][y].next = 1
                elif cells[x][y].live == -1:
                    if n == 3:
                        cells[x][y].next = 1
                    else:
                        cells[x][y].next = -1


def main(delay):
    Game.initialize_game(delay)
    Game.run_game(delay)


main(1)
