#Followed the youtube video of Code Bucket to learn PyGame and make the Replica of the Dino game - made by Ramtin Alikhani
import pygame # to create the game
import os #for file navigation purposes
import random #random number generation for how much and when obstacles show up 
import sys


pygame.init() #initialize the pygame suite 

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

#characteristics of the dino character
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
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS


    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1
 
    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


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


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)
        pygame.draw.rect(SCREEN, (255,0,0), self, 2) 
        


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
        pygame.draw.rect(SCREEN, (255,0,0), self, 2)
        self.index += 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True #swtich for the while loop to start - pygame mainly works by 
    clock = pygame.time.Clock()
    player = Dinosaur() # player is the dinosaur class and everything in it
    cloud = Cloud() 
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0
    dinosaurs = [Dinosaur()]

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        SCREEN.fill((255, 255, 255))

        
        
        userInput = pygame.key.get_pressed() #user input for every instance a key is pressed

        player.draw(SCREEN) #draw dino on screen
        player.update(userInput) #update the dino on screen on every while loop iteration

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
            if player.dino_rect.colliderect(obstacle.rect):    
                pygame.draw.rect(SCREEN, (255,0,0), player.dino_rect, 2)
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)
                sys.exit()




        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    global points
    run = True
    while run: #while the game is going on - the main operation of pygame
        SCREEN.fill((255, 255, 255)) # in wvery while loop iteration, fill the screen with white
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
            text = font.render("Use Arrow keys to play", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()


        for event in pygame.event.get(): #what happens when you click on something
            if event.type == pygame.QUIT: #quit the game when....
                run = False #press x on the window to exit the game 
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)