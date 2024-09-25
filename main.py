import pygame
pygame.init()
img  = pygame.image.load(r"D:\deadline\f03ac0c34cedeab3b3fc.jpg")
d, c = img.get_size()
img = pygame.transform.smoothscale(img , (d/1.6, c/1.6))
d, c = img.get_size()
screen = pygame.display.set_mode((d,c))


box1  =pygame.Rect(580,150,400,75)
box2  =pygame.Rect(495,230,500,230)

run = True

text = "thầy Nguyễn Văn B"
lc = "    zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zipzipzipzipzipzipzipzipzipzip zip zip"

def tudongdieuchin(text, box_width, initial_size=45, min_size=10):
    size = initial_size
    font = pygame.font.Font("D:\deadline\SedgwickAve-Regular.ttf", size)
    dai, _ = font.size(text)
    while dai > box_width and size > min_size:
        size -= 1
        font = pygame.font.Font("D:\deadline\SedgwickAve-Regular.ttf", size)
        dai, _ = font.size(text)
    return font

def tudongngatdong(lc, box_width, box_height, initial_size=25, min_size=10):
    size = initial_size
    font = pygame.font.Font("D:\deadline\SedgwickAve-Regular.ttf", size)
    while True:
        chu = lc.split(' ')
        lines = []
        current_line = ""
        cao = 0
        for tu in chu:
            
            linet = current_line + tu + " "
            rongt, caot = font.size(linet)
            
            if rongt <= box_width:
                current_line = linet
            else:
                lines.append(current_line)
                current_line = tu + " "
                cao += caot
        lines.append(current_line)
        cao += caot
        if cao <= box_height or size <= min_size:
            break
        else:
            size -= 1
            font = pygame.font.Font(None, size)

    return font, lines
while run:
    screen.fill((255,0,0))
    screen.blit(img,(0,0))
    font = tudongdieuchin(text, box1.width)
    font2, lines = tudongngatdong(lc, box2.width, box2.height)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    dong1 = pygame.Surface((box1.width, box1.height))
    dong1.set_alpha(0)
    dong1.fill((0,0,0))
    pygame.draw.rect(dong1, (0,0,0), box1)
    #pygame.draw.rect(screen, (0,0,0), box2)
    d1 = font.render(text, True, (166,90,116))
    #d1o = font.render(text1, True,(166,90,116))
    d1r = d1.get_rect()
    #d1r = d1.get_rect(bottom= (box1.x + 5, box1.y + (box1.height - d1.get_height()) // 2))
    #screen.blit(d1o, d1r)
    screen.blit(d1, (box1.x + 5, box1.y + (box1.height - d1.get_height()) // 2))
    y_offset = box2.y + 5
    for line in lines:
        text_surface = font2.render(line, True,(73,31,56))
        line_width = text_surface.get_width()
        x_offset = box2.x + (box2.width - line_width) // 2
        screen.blit(text_surface, (x_offset,y_offset))
        y_offset += text_surface.get_height()


    #pygame.draw.rect(screen, (255,255,255), box2)
    #pygame.image.save(screen, "abc.png",)
    pygame.display.update()