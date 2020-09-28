import pygame 

class PygView(object):
    def __init__(self, width=640, height=400, fps=30):  
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((255,255,255))
        self.clock = pygame.time.Clock()
        self.fps =fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold = True)

    def paint(self):
        pygame.draw.rect(self.background,(0,0,0), (50,150,100,25) )
        myBall = Ball(color=(255,255,0), a=200, b=150,c=100, d=90)
        myBall.blit(self.background)





    def run(self):
        

        self.paint()
        mainloop = True

        while mainloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mainloop = False
            milliseconds = self.clock.tick(self.fps)
            self.playtime +=milliseconds / 1000.0
             
            self.draw_text(f"FPS:{self.clock.get_fps():2.0f}, Playtime:{self.playtime:2.0f}")
            pygame.display.flip()
            self.screen.blit(self.background, (0,0))
           
        pygame.quit()
    def draw_text(self, text):

        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 255,0))
        self.screen.blit(surface, (0 , 0 ))


class Ball(object):
    def __init__(self, color=(0,0, 255), a=100, b=100, c=3, d=3):

        self.color = color
        self.a = a
        self.b = b 
        self.c = c
        self.d = d

        self.surface = pygame.Surface((max(4*self.a, 4*self.b), max(4*self.c, 4*self.d )))
        pygame.draw.rect(self.surface, color, (a, b, c, d))
        self.surface = self.surface.convert()
        self.surface.set_colorkey((0,0,0))
        self.surface = self.surface.convert_alpha()
    def blit(self, background):
        background.blit(self.surface, (max(self.a, self.b), max(self.c, self.d))) 

if __name__ == '__main__':
    PygView(640, 400).run()