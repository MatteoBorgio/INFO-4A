import pygame
import sys

# ------------------------------------------------------------------ #
# COSTANTI                                                             #
# ------------------------------------------------------------------ #

SCREEN_W = 800
SCREEN_H = 600
FPS      = 60

BALL_RADIUS = 30
BALL_SPEED  = 4 # pixel per frame (tastiera)
speed       = BALL_SPEED

BG_COLOR   = ( 30,  30,  30)
TEXT_COLOR = (200, 200, 200)

# Colori disponibili per il cambio al clic
COLORS = [
    (220,  80,  80),   # rosso
    ( 80, 180, 220),   # azzurro
    ( 80, 220, 120),   # verde
    (220, 200,  80),   # giallo
    (180,  80, 220),   # viola
]

# ------------------------------------------------------------------ #
# INIZIALIZZAZIONE                                                     #
# ------------------------------------------------------------------ #

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Pallina interattiva")
clock  = pygame.time.Clock()
font   = pygame.font.SysFont("Arial", 22)

# ------------------------------------------------------------------ #
# STATO                                                                #
# ------------------------------------------------------------------ #

ball_x      = SCREEN_W // 2
ball_y      = SCREEN_H // 2
color_index = 0                      # indice corrente in COLORS
ball_color  = COLORS[color_index]

# ------------------------------------------------------------------ #
# FUNZIONI DI SUPPORTO                                                 #
# ------------------------------------------------------------------ #

def clamp(value: int, min_val: int, max_val: int) -> int:
    """
    Restituisce value se è compreso tra min_val e max_val,
    altrimenti restituisce il limite più vicino.

    Esempi:
        clamp(10, 0, 100)  → 10
        clamp(-5, 0, 100)  → 0
        clamp(150, 0, 100) → 100
    """
    return max(min_val, min(value, max_val))


def point_in_circle(px: int, py: int,
                    cx: int, cy: int, radius: int) -> bool:
    """
    Suggerimento: usa il teorema di Pitagora per calcolare
    la distanza tra il punto e il centro, poi confrontala
    con il raggio.
    Ricorda: puoi evitare la radice quadrata confrontando
    i quadrati delle distanze.
    """

    dx = px - cx
    dy = py - cy
    return dx * dx + dy * dy <= radius * radius

def next_color(current_index: int) -> tuple:
    """
    Parametri:
        current_index: indice attuale in COLORS

    Valore restituito:
        una tupla (int, tuple) con il nuovo indice e il colore
        corrispondente.

    Suggerimento: l'operatore % (modulo) è utile per il
    comportamento circolare.
    """
    index = (current_index + 1) % len(COLORS)
    return index, COLORS[index]

# ------------------------------------------------------------------ #
# LOOP PRINCIPALE                                                      #
# ------------------------------------------------------------------ #

running = True
move_right = True
move_down  = True
AUTO_SPEED = 4

while running:

    # Esperimento 4
    if move_right:
        ball_x += AUTO_SPEED
    else:
        ball_x -= AUTO_SPEED

    if move_down:
        ball_y += AUTO_SPEED
    else:
        ball_y -= AUTO_SPEED

    if ball_x + BALL_RADIUS >= SCREEN_W:
        move_right = False
    elif ball_x - BALL_RADIUS <= 0:
        move_right = True

    if ball_y + BALL_RADIUS >= SCREEN_H:
        move_down = False
    elif ball_y - BALL_RADIUS <= 0:
        move_down = True

    # Controllo rimbalzi sui bordi
    if ball_x + BALL_RADIUS >= SCREEN_W:
        move_right = False
    elif ball_x - BALL_RADIUS <= 0:
        move_right = True

    if ball_y + BALL_RADIUS >= SCREEN_H:
        move_down = False
    elif ball_y - BALL_RADIUS <= 0:
        move_down = True

    # ---- 1. EVENTI ------------------------------------------------ #

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if point_in_circle(x, y, ball_x, ball_y, BALL_RADIUS):
                color_index, ball_color = next_color(color_index)
        # Esperimento 2
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            ball_x, ball_y = SCREEN_W // 2, SCREEN_H // 2
        # Esperimento 3
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            x, y = event.pos
            if point_in_circle(x, y, ball_x, ball_y, BALL_RADIUS):
                ball_x, ball_y = x, y

    # ---- 2. AGGIORNA ---------------------------------------------- #

    # -- Tastiera --
    # pygame.key.get_pressed() restituisce una sequenza di booleani
    # indicizzata dai codici dei tasti. Esempio:
    #   keys[pygame.K_LEFT]  → True se il tasto ← è premuto ora
    #
    # A differenza degli eventi (che arrivano una volta sola),
    # get_pressed() fotografa lo stato istantaneo della tastiera
    # ed è pensato per il movimento continuo.

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= speed
    if keys[pygame.K_RIGHT]:
        ball_x += speed
    if keys[pygame.K_UP]:
        ball_y -= speed
    if keys[pygame.K_DOWN]:
        ball_y += speed
    # Esperimento 1
    speed = BALL_SPEED * 2 if keys[pygame.K_LSHIFT] else BALL_SPEED

    # Dopo aver aggiornato la posizione, usa clamp() per impedire
    # alla pallina di uscire dallo schermo. Ricorda di tenere conto
    # di BALL_RADIUS!
    #   ball_x = clamp(ball_x, ..., ...)
    #   ball_y = clamp(ball_y, ..., ...)

    ball_x = clamp(ball_x, BALL_RADIUS, SCREEN_W - BALL_RADIUS)
    ball_y = clamp(ball_y, BALL_RADIUS, SCREEN_H - BALL_RADIUS)

    # ---- 3. DISEGNA ----------------------------------------------- #

    screen.fill(BG_COLOR)
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), BALL_RADIUS)

    # HUD: istruzioni a schermo (già fornito)
    hints = [
        "Frecce / WASD: muovi la pallina",
        "Clic sinistro sulla pallina: cambia colore",
    ]
    for i, line in enumerate(hints):
        surf = font.render(line, True, TEXT_COLOR)
        screen.blit(surf, (10, 10 + i * 28))

    pygame.display.flip()
    clock.tick(FPS)

# ------------------------------------------------------------------ #
# USCITA                                                               #
# ------------------------------------------------------------------ #

pygame.quit()
sys.exit()
