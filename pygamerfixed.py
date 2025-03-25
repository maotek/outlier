import pygame
import random

# Constanten
WIDTH, HEIGHT = 800, 600
FPS = 60
COLOR_BACKGROUND = (240, 240, 240)
COLOR_TEXT = (0, 0, 0)
COLOR_CORRECT = (0, 128, 0)  # Letter op de juiste positie
COLOR_WRONG = (255, 165, 0)  # Letter komt voor, maar op andere positie
COLOR_NOT_IN_WORD = (192, 192, 192)  # Letter komt niet voor
COLOR_CELL_BORDER = (0, 0, 0)
COLOR_CELL_EMPTY = (255, 255, 255)  # Celachtergrond

# Layout instellingen
SIDE_PADDING = 50  # Witruimte aan beide zijden
TOP_PADDING = 100  # Witruimte boven 't grid (onder de pogingenteller)
BOTTOM_PADDING = 50  # Witruimte onder 't grid

GRID_COLS = 5
GRID_ROWS = 6  # Maximum pogingen verhogen naar 6
GRID_HEIGHT = HEIGHT - TOP_PADDING - BOTTOM_PADDING
GRID_WIDTH = WIDTH - 2 * SIDE_PADDING
CELL_WIDTH = GRID_WIDTH / GRID_COLS
CELL_HEIGHT = GRID_HEIGHT / GRID_ROWS

# Dynamische fontgrootte gebaseerd op de hoogte van de cellen
FONT_SIZE = int(CELL_HEIGHT * 0.6)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("5 Letter Lingo Game")
FONT = pygame.font.SysFont('Arial', FONT_SIZE)


def load_words():
    try:
        with open('woordenlijst.txt', 'r', encoding='utf-8') as file:
            words = file.read().splitlines()
            return [word.strip().lower() for word in words if len(word.strip()) == 5]
    except FileNotFoundError:
        print("Bestand 'woordenlijst.txt' niet gevonden. Gebruik standaard woordenlijst.")
        return ["appel", "mango", "druif"]


def get_random_word(words):
    return random.choice(words)


def draw_text(text, color, center):
    label = FONT.render(text, True, color)
    text_rect = label.get_rect(center=center)
    screen.blit(label, text_rect)


def draw_grid(secret_word, guesses, current_guess):
    cell_margin = 5
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = SIDE_PADDING + col * CELL_WIDTH
            y = TOP_PADDING + row * CELL_HEIGHT
            rect = pygame.Rect(x + cell_margin, y + cell_margin, CELL_WIDTH - 2 * cell_margin, CELL_HEIGHT - 2 * cell_margin)
            pygame.draw.rect(screen, COLOR_CELL_EMPTY, rect)
            pygame.draw.rect(screen, COLOR_CELL_BORDER, rect, 2)

            letter = ""
            letter_color = COLOR_TEXT

            if row < len(guesses):
                guess = guesses[row]
                letter = guess[col]
                if letter == secret_word[col]:
                    letter_color = COLOR_CORRECT
                elif letter in secret_word:
                    letter_color = COLOR_WRONG
                else:
                    letter_color = COLOR_NOT_IN_WORD
            elif row == len(guesses) and col < len(current_guess):
                letter = current_guess[col]
                letter_color = COLOR_TEXT

            if letter:
                text_surface = FONT.render(letter.upper(), True, letter_color)
                text_rect = text_surface.get_rect(center=rect.center)
                screen.blit(text_surface, text_rect)


def game_loop():
    words = load_words()
    secret_word = get_random_word(words)
    guesses = []
    current_guess = ""
    running = True
    game_over = False
    clock = pygame.time.Clock()

    while running:
        screen.fill(COLOR_BACKGROUND)

        attempts_text = f"Pogingen over: {GRID_ROWS - len(guesses)}"
        attempts_surface = FONT.render(attempts_text, True, COLOR_TEXT)
        attempts_rect = attempts_surface.get_rect(center=(WIDTH / 2, TOP_PADDING / 2))
        bg_rect = pygame.Rect(attempts_rect.x - 5, attempts_rect.y - 5, attempts_rect.width + 10, attempts_rect.height + 10)
        pygame.draw.rect(screen, COLOR_CELL_EMPTY, bg_rect)
        pygame.draw.rect(screen, COLOR_CELL_BORDER, bg_rect, 2)
        screen.blit(attempts_surface, attempts_rect)

        grid_container_rect = pygame.Rect(SIDE_PADDING - 5, TOP_PADDING - 5, GRID_WIDTH + 10, GRID_HEIGHT + 10)
        pygame.draw.rect(screen, COLOR_CELL_EMPTY, grid_container_rect)
        pygame.draw.rect(screen, COLOR_CELL_BORDER, grid_container_rect, 2)

        draw_grid(secret_word, guesses, current_guess)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_BACKSPACE:
                    current_guess = current_guess[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(current_guess) == 5:
                        guesses.append(current_guess)
                        if current_guess == secret_word:
                            game_over = True
                        current_guess = ""
                elif len(current_guess) < 5 and event.unicode.isalpha():
                    current_guess += event.unicode.lower()

        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    game_loop()