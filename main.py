import pygame
import random

#Initialize PyGame
pygame.init()

#Game Constants
WIDTH,HEIGHT=800,600

#Creating window
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#Title of window
pygame.display.set_caption("Fruit Ninja")

#Load Image
bg=pygame.image.load('assets/background.png')

fruit_images={
    'fruit1':pygame.image.load('assets/fruit1.png'),#Apple
    'fruit2':pygame.image.load('assets/fruit2.png'),#Pineapple
    'fruit3':pygame.image.load('assets/fruit3.png')#Watermelon
}

bomb_image=pygame.image.load('assets/bomb.png')

#Transform 
fruit_sizes={'fruit1':50,'fruit2':100,'fruit3':90}

for fruit in fruit_images:
    fruit_images[fruit]=pygame.transform.scale(fruit_images[fruit],(fruit_sizes[fruit],fruit_sizes[fruit]))

bomb_image=pygame.transform.scale(bomb_image,(60,60))

class GameObject:
    def __init__(self,fruit_type,is_bomb):
        self.x=random.randint(100,WIDTH-100)
        self.y=HEIGHT
        self.speed_x=(WIDTH/2-self.x)/40
        self.speed_y=random.randint(14,18)
        self.gravity=0.4
        self.fruit_type=fruit_type
        self.is_bomb=is_bomb

    #Drawing the object on screen
    def draw(self):    
        if self.is_bomb:
            screen.blit(fruit_images[self.fruit_type],(self.x,self.y))
        else:
            screen.blit(bomb_image,(self.x,self.y))

    def move(self):
        self.x +=self.speed_x
        self.y -=self.speed_y
        self.speed_y -=self.gravity


running=True

objects=[]

spawn_interval=2000

last_spawn_time=0

while running:

    screen.blit(bg,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    current_time=pygame.time.get_ticks()

    if (current_time-last_spawn_time)>spawn_interval or last_spawn_time==0:

        fruit_type = random.choice(["fruit1", "fruit2", "fruit3"])  
        is_bomb=random.randint(0,1)==1
        
        obj=GameObject(fruit_type,is_bomb)

        objects.append(obj)

        last_spawn_time=current_time

    objects = [game_object for game_object in objects if not game_object.y>HEIGHT]

    for game_object in objects:
        game_object.draw()
        game_object.move()
        

    pygame.display.update()

pygame.quit()










