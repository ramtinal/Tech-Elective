import pygame
import os
import random
import math
import sys
import neat

pygame.init()

# Global Constants
SCREEN_HEIGHT = 600 #screen size of the game when it launches height
SCREEN_WIDTH = 1100 #screen size of the game when it launches width
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
#A list of different sprites of the character running. It uses os.path.join to navigate the file directory and fetch the needed pictures
RUNNING = [pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets\Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Dino", "DinoRun2.png"))]

#sprite of the character Jumping
JUMPING = pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Dino", "DinoJump.png"))

#A list of different sprites of the character Ducking. It uses os.path.join to navigate the file directory and fetch the needed pictures
DUCKING = [pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Dino", "DinoDuck2.png"))]

#A list of different sprites of the cacti of various lengths. It uses os.path.join to navigate the file directory and fetch the needed pictures
SMALL_CACTUS = [pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Cactus", "LargeCactus3.png"))]

#A list of different sprites of the bird flying. It uses os.path.join to navigate the file directory and fetch the needed pictures
BIRD = [pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Bird", "Bird2.png"))]

#the sprites of the background clouds 
CLOUD = pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Other", "Cloud.png"))

#the background of the game and the ground 
BG = pygame.image.load(os.path.join("d:\Onedrive\OneDrive - Conestoga College\Conestoga\YEAR 4\SEMESTER 2\Artificial Intelligence\Project\Assets/Other", "Track.png"))

FONT = pygame.font.Font('freesansbold.ttf', 20)


class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        #hit box below 
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, self.image.get_width(), self.image.get_height()) 
        #self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.step_index = 0
       

    def update(self):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel <= -self.JUMP_VEL:
            self.dino_jump = False
            self.dino_run = True
            self.jump_vel = self.JUMP_VEL

    def run(self):
        self.image = RUNNING[self.step_index // 5]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1
    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        

class Obstacle:
    def __init__(self, image, number_of_cacti):
        self.image = image
        self.type = number_of_cacti
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

def remove(index):
    dinosaurs.pop(index)
    

def main():
    global game_speed, x_pos_bg, y_pos_bg, obstacles, dinosaurs, points
    points = 0
    obstacles = []
    dinosaurs = [Dinosaur()]
    cloud = Cloud() 
    clock = pygame.time.Clock()
    x_pos_bg = 0
    y_pos_bg = 380
    game_speed = 20

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        text = FONT.render(f'Points:  {str(points)}', True, (0, 0, 0))
        SCREEN.blit(text, (950, 50))

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.fill((255, 255, 255))  
        for dinosaur in dinosaurs:
            dinosaur.update()
            dinosaur.draw(SCREEN)  

        if len(dinosaurs) == 0:
            break

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            for i, dinosaur in enumerate(dinosaurs):
                if dinosaur.rect.colliderect(obstacle.rect):
                    remove(i)

        userInput = pygame.key.get_pressed()       
        for i, dinosaur in enumerate(dinosaurs):
            if userInput[pygame.K_UP] and not dinosaur.dino_jump:
                dinosaur.dino_duck = False
                dinosaur.dino_run = False
                dinosaur.dino_jump = True
            elif userInput[pygame.K_DOWN] and not dinosaur.dino_jump:
                dinosaur.dino_duck = True
                dinosaur.dino_run = False
                dinosaur.dino_jump = False
            elif not (dinosaur.dino_jump or userInput[pygame.K_DOWN]):
                dinosaur.dino_duck = False
                dinosaur.dino_run = True
                dinosaur.dino_jump = False
        
        
        
        score()
        background()
        cloud.draw(SCREEN)
        cloud.update()
        clock.tick(30)
        pygame.display.update()
main()

