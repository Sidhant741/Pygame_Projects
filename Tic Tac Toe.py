# Importing the Libraries
import pygame

# Initializing the Pygame
pygame.init()
window_width = 500
window_height = 550
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
run = True


class Player:
    def __init__(self, mark, color):
        self.mark = mark
        self.loc_marks = []
        self.color = color

    def draw(self, loc):
        font = pygame.font.SysFont('Arial', 150, True)
        text = font.render(self.mark, True, self.color)
        text_rect = text.get_rect()
        text_rect.centerx, text_rect.centery = (2*loc[0] + 1)*80 + 5, (2*loc[1] + 1)*80 + 5
        game.window.blit(text, text_rect)


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((window_width, window_height))
        self.run = True
        self.title_screen = True
        self.playing_screen = False
        self.choosing_screen = False
        self.result_screen = False
        self.won = 0

    def gameloop(self):
        while self.run:
            if self.title_screen:
                self.title_screen_func()
            elif self.playing_screen:
                self.playing_screen_func()
            elif self.choosing_screen:
                self.choosing_screen_func()
            elif self.result_screen:
                self.result_screen_func(self.won)

    def title_screen_func(self):
        temp_run = True
        self.window.fill(white)
        self.msg_blit(msg='Tic Tac Toe', font_size=60, font_color=red, y_change=-150, bold_=True)
        self.msg_blit(msg='Play', font_size=40, font_color=black, bold_=True, italic_=True, bg=yellow)
        pygame.display.update()
        while temp_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    self.title_screen = False
                    temp_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 215 < pos[0] < 285 and 252 < pos[1] < 299:
                        print('lets play')
                        self.title_screen = False
                        self.choosing_screen = True
                        temp_run = False

    def msg_blit(self, msg, font_size, font_color, bg=None, x_change=0, y_change=0, bold_=False, italic_=False):
        font = pygame.font.SysFont('Arial', font_size, bold_, italic_)
        text = font.render(msg, True, font_color, bg)
        rect = text.get_rect()
        rect.centerx, rect.centery = self.window.get_rect().centerx + x_change, self.window.get_rect().centery + y_change
        self.window.blit(text, rect)

    def choosing_screen_func(self):
        temp_run = True
        self.window.fill(white)
        self.msg_blit(msg='Player 1 Choose', font_size=50, font_color=black, y_change=-150, bold_=True, italic_=True)
        self.msg_blit(msg='X', font_size=50, font_color=white, bg=black, x_change=-100, bold_=True)
        self.msg_blit(msg='O', font_size=50, font_color=white, bg=black, x_change=100, bold_=True)
        pygame.display.update()
        while temp_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    self.choosing_screen = False
                    temp_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 136 < pos[0] < 164 and 246 < pos[1] < 304:
                        print('Player 1 Chooses X')
                        self.player1, self.player2 = Player('X', red), Player('O', blue)
                        self.playing_screen, self.choosing_screen = True, False
                        temp_run = False
                    elif 334 < pos[0] < 366 and 246 < pos[1] < 304:
                        print('Player 1 Chooses O')
                        self.player1, self.player2 = Player('O', red), Player('X', blue)
                        self.playing_screen, self.choosing_screen = True, False
                        temp_run = False

    def playing_screen_func(self):
        temp_run = True
        turn = 0
        while temp_run:
            new_turn = turn
            self.window.fill(white)
            self.boundary()
            for i in self.player1.loc_marks:
                self.player1.draw(i)
            for i in self.player2.loc_marks:
                self.player2.draw(i)
            if not turn:
                self.msg_blit(msg='Player 1 Turn', font_size=40, font_color=blue, y_change=240)
            else:
                self.msg_blit(msg='Player 2 Turn', font_size=40, font_color=blue, y_change=240)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    self.playing_screen = False
                    temp_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    temp = []
                    for i in pos:
                        if 15 <= i <= 165:
                            temp.append(0)
                        elif 175 <= i <= 325:
                            temp.append(1)
                        elif 335 <= i <= 485:
                            temp.append(2)
                    new_turn = self.place_marks(tuple(temp), turn)

                    if not new_turn == turn:
                        if turn == 0:
                            if self.gameover(self.player1.loc_marks):
                                self.playing_screen, self.result_screen = False, True
                                self.won = 1
                                temp_run = False
                        else:
                            if self.gameover(self.player2.loc_marks):
                                self.playing_screen, self.result_screen = False, True
                                self.won = 2
                                temp_run = False
                        turn = new_turn

            count = 0
            for i in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]:
                if i in self.player1.loc_marks or i in self.player2.loc_marks:
                    count += 1
            if count == 9:
                self.playing_screen = False
                self.result_screen = True
                temp_run = False

            pygame.display.update()

    def boundary(self):
        for i in [165, 325]:
            pygame.draw.rect(self.window, black, (i, 0, 10, window_height - 60))
            pygame.draw.rect(self.window, black, (0, i, window_width, 10))
        for i in [0, 485]:
            pygame.draw.rect(self.window, black, (0, i, window_width, 15))
            pygame.draw.rect(self.window, black, (i, 0, 15, window_height - 60))

    def gameover(self, markers):
        left_to_right_diag = 0
        right_to_left_diag = 0

        for row_col in [0, 1, 2]:
            row_check = 0
            col_check = 0
            for i in markers:
                if row_col == i[0]:
                    row_check += 1
                if row_col == i[1]:
                    col_check += 1
            if row_check == 3 or col_check == 3:
                print('Won')
                return True
        print(markers)
        for i in markers:
            if i in [(0, 0), (1, 1), (2, 2)]:
                left_to_right_diag += 1
            if i in [(2, 0), (1, 1), (0, 2)]:
                right_to_left_diag += 1
        if left_to_right_diag == 3 or right_to_left_diag == 3:
            print('Won')
            return True

        return False

    def place_marks(self, loc, turn):
        if not turn:
            if loc in self.player2.loc_marks or loc in self.player1.loc_marks:
                print('You cant place your mark here')
                return 0
            else:
                self.player1.loc_marks.append(loc)
                self.player1.draw(loc)
                return 1
        else:
            if loc in self.player1.loc_marks or loc in self.player2.loc_marks:
                print('You cant place your mark here')
                return 1
            else:
                self.player2.loc_marks.append(loc)
                self.player2.draw(loc)
                return 0

    def result_screen_func(self, winner):
        temp_run = True
        self.window.fill(white)
        if winner == 1:
            self.msg_blit(msg='Player 1 Wins!!!', font_size=60, font_color=red, y_change=-150, bold_=True)
        elif winner == 2:
            self.msg_blit(msg='Player 2 Wins!!!', font_size=60, font_color=red, y_change=-150, bold_=True)
        else:
            self.msg_blit(msg='Huh Draw, You both are equally bad lol!!', font_size=30, font_color=red, y_change=-150, bold_=True)

        self.msg_blit(msg='Want to play again?', font_size=60, font_color=red, bold_=True)
        self.msg_blit(msg='YES', font_size=60, font_color=red, x_change=150, y_change=+150, bold_=True)
        self.msg_blit(msg='   NO  ', font_size=60, font_color=red, x_change=-150, y_change=+150, bold_=True)
        pygame.display.update()
        while temp_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    self.result_screen = False
                    temp_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 350 <= pos[0] <= 450 and 390 <= pos[1] <= 460:
                        self.result_screen = False
                        self.choosing_screen = True
                        temp_run = False
                    elif 28 <= pos[0] <= 172 and 390 <= pos[1] <= 460:
                        self.result_screen = False
                        self.run = False
                        temp_run = False


game = Game()
game.gameloop()
