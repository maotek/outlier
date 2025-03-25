import pygame
import random

# Constanten
WIDTH, HEIGHT = 800, 600
FPS = 60
COLOR_BACKGROUND = (240, 240, 240)
COLOR_TEXT = (0, 0, 0)
COLOR_CORRECT = (0, 255, 0)
COLOR_WRONG = (255, 255, 0)
COLOR_INCORRECT = (255, 0, 0)
FONT_SIZE = 36

# Initialisatie van Pygame (voor gebruik van fonts)
pygame.init()

# Nu kan de font veilig worden gedefinieerd
FONT = pygame.font.SysFont('Arial', FONT_SIZE)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Lingo Spel')

def load_words():
    try:
        with open('woordenlijst.txt', 'r', encoding='utf-8') as file:
            woorden = file.read().splitlines()
            # Filter woorden die exact 5 letters lang zijn
            return [woord for woord in woorden if len(woord) == 5]
    except FileNotFoundError:
        print("Bestand 'woordenlijst.txt' niet gevonden. Gebruik standaard woordenlijst.")
        # Standaard woordenlijst (alle woorden zijn 5 letters)
        return ['appel', 'mango', 'druif']

def get_random_word(words):
    return random.choice(words)

def draw_text(text, color, x, y):
    label = FONT.render(text, True, color)
    screen.blit(label, (x, y))

def draw_grid(word, guesses):
    for i in range(5):
        col = COLOR_BACKGROUND
        if guesses[i] != '' and word[i] == guesses[i]:
            col = COLOR_CORRECT
        elif guesses[i] != '' and word[i] in guesses:
            col = COLOR_WRONG
        draw_text(word[i] if guesses[i] else '_', col, (i + 1) * 60 + 10, 100)

def game_loop():
    words = load_words()
    word = get_random_word(words)
    guesses = [''] * 5
    attempts = 6
    running = True

    while running:
        screen.fill(COLOR_BACKGROUND)
        draw_text(f"Attempts: {attempts}", COLOR_TEXT, 10, 50)
        draw_grid(word, guesses)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_RETURN) and attempts == 0:
                    game_loop()
                elif event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in (pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e,
                                  pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j,
                                  pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o,
                                  pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t,
                                  pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z):
                    letter = chr(event.key)
                    # Zorg dat we binnen de indexen blijven (de huidige poging is de rij index: 6 - attempts)
                    rij = 6 - attempts
                    if rij < 5 and guesses[rij] == '':
                        guesses[rij] = letter
                        attempts -= 1

        if attempts == 0:
            draw_text(f"Je hebt verloren! Het woord was: {word}", COLOR_INCORRECT, 30, 300)
            pygame.display.flip()
            pygame.time.wait(2000)

        if all(guesses[i] == word[i] for i in range(5)):
            draw_text("Gefeliciteerd! Je hebt gewonnen!", COLOR_CORRECT, 30, 300)
            pygame.display.flip()
            pygame.time.wait(2000)
            game_loop()

    pygame.quit()

if __name__ == "__main__":
    game_loop()