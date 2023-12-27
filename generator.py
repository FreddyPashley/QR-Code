message = "ABCDEFGA"

import pygame

width = 700
bg = "white"

character_set = {
    " ": [0, 0, 0, 0, 0],
    "A": [1, 0, 0, 0, 0],
    "B": [0, 1, 0, 0, 0],
    "C": [0, 0, 1, 0, 0],
    "D": [0, 0, 0, 1, 0],
    "E": [0, 0, 0, 0, 1],
    "F": [1, 1, 0, 0, 0],
    "G": [1, 0, 1, 0, 0]
}

# bars = [0]
bars = []
anchor = 0
for character in message:
    if anchor not in range(width//10): break
    if character in character_set:
        set = character_set[character]
        set.insert(0, "/")
        # set.append("/")
        for x in set:
            if x == 1:
                bars.append(anchor)
            if x == "/":
                bars.append("/"+str(anchor))
            anchor += 1
# bars.append((width/10)-1)

remainder = [i for i in range(width//10) if i not in bars and "/"+str(i) not in bars]

pygame.init()
screen = pygame.display.set_mode([width, 100])
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("white")

    for x in bars:
        if type(x) == str and x.startswith("/"):
            pygame.draw.rect(screen, "black", pygame.Rect(int(x.replace("/", ""))*10, 0, 10, 50))  
            pygame.draw.rect(screen, bg, pygame.Rect(int(x.replace("/", ""))*10, 50, 10, 50))  
        else:  
            pygame.draw.rect(screen, "black", pygame.Rect(x*10, 0, 10, 100))
    for x in remainder:
        pygame.draw.rect(screen, bg, pygame.Rect(x*10, 0, 10, 100))

    pygame.display.update()