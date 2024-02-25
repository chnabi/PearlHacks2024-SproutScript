import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 883
screen_height = 674
screen = pygame.display.set_mode((screen_width, screen_height))

#button class
class Button():

    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False # buttons starts as unclicked

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos): # is the mouse cursor colliding with mouse button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # [0] is left mouse button
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
#exit button
exit_img = pygame.image.load('exitbutton.png').convert_alpha()    
buttons = ["b1.jpg", "next.jpg","next.jpg","next.jpg", "b3.jpeg", "check.png", "sunflower.JPG", "check.png", "water.jpeg", "b3.jpeg", "check.png", "clock.png", "run.png", "check.png", "run.png"]
def load_images(input):
    return pygame.image.load(buttons[input]).convert_alpha()
    
mouse_position = pygame.mouse.get_pos()
print(mouse_position)

#initialize buttons
start_button = Button(700,511, load_images(0), 0.5)
exit_button = Button(770, 10, exit_img, 0.25)
next = Button(680,581, load_images(1), 0.25)
next2 = Button(750,631, load_images(4), 0.05)
b3 = Button(750,601, load_images(4), 0.08)
check = Button(550,611, load_images(5), 0.35)
sunflower = Button(60,250, load_images(6), 0.10)
water = Button(60,250, load_images(8), 0.10)
clock = Button(80,70, load_images(11), 0.35)
run = Button(550,611, load_images(12), 0.35)

buttonList = [b3, next, next, next, b3,check, sunflower, check, water, b3, check, clock,next2, check, run,exit_button]

#draw button method
def draw_button(num):
    buttonList[num].draw(screen)


screens = ["0.jpg","r1.jpg","r2.jpg", "r3.jpg", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png", "10.png", "11.png", "12.png"]
def draw_screen(input):
    original_image = pygame.image.load(screens[input]).convert_alpha()
    scaled_image = pygame.transform.scale(original_image, (883, 674))
    screen.blit(scaled_image, (0,0))
   
#change screen 
def change_screen(num):
    draw_screen(num)
    draw_button(num)
    exit_button.draw(screen)
    pygame.display.flip()
    
current_button = buttonList[0]
count =1
# Game loop
running = True
current_screen = "main_menu"  # Initial screen

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif current_button.draw(screen):  #next button is clicked transition screen empty to seed 
                current_screen = "not first"
                change_screen(count)  
                current_button = buttonList[count]
                count = count + 1

        if exit_button.draw(screen):
             running = False

     # Update the screen based on the current state
    if current_screen == "main_menu":
        change_screen(0)
    #elif current_screen == "seed":
        #seed_screen()

    # Limit the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
