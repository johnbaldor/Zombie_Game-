import pygame
from random import randint
from sys import exit 
pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Ethan")


def zombie_movement(zombie_list):
    if zombie_list:
        
        for zombie1_rect in zombie_list:
            zombie1_rect.x -= Change_Zombie1_x
            
            
            screen.blit(zombie1_surface,zombie1_rect)
            if zombie1_rect.x <= 150:
                global game_active 
                game_active = 2
                zombie_list.clear()
            if timer <= 0:
                game_active = 3
                zombie_list.clear()
            mouse_pos = pygame.mouse.get_pos()
            pressed_key = pygame.key.get_pressed()
            if zombie1_rect.collidepoint(mouse_pos) and pressed_key[pygame.K_a]:
                zombie1_rect.y = 3000 
                zombie1_rect.x = 100000 
                global actual_score
                actual_score += 1
                screen.blit(text_hit,mouse_pos)

                
        zombie_list = [zombie for zombie in zombie_list if zombie.x < -100 or zombie.y > 2000]
        return zombie_list  
    else: return []



            
            


# basic varibles 
start_time = 0
game_active = 1
actual_score = 0
timer = 2
Change_Zombie1_x = randint(2,9)
highest_score= 0



# pygame varibles
test_font = pygame.font.Font('fonts/Font.ttf',50)
test_font2 = pygame.font.Font('fonts/Font.ttf',160)
clock = pygame.time.Clock()
get_ticks = pygame.time.get_ticks()


# text varibles
hit = pygame.font.Font(None,50)
s_quit = pygame.font.Font(None,40)
a_shoot = pygame.font.Font(None,40)
score = pygame.font.Font(None,150)
play_again = pygame.font.Font(None, 75)
win = pygame.font.Font(None, 250)
highest = pygame.font.Font(None, 150)
time_left = pygame.font.Font(None, 160)

# text rendering
text_hit = hit.render("HIT",True,"white")
text_quit = s_quit.render("Click S to quit",True,"black")
text_shoot = a_shoot.render("Click A to shoot",True,"black")
text_play = play_again.render("click D to play again",True, "White")
text_win = win.render("YOU WIN!",True,"white")


# image varibles
field = pygame.image.load("images/field.jpg").convert()
aim_surface = pygame.image.load("images/aim.png").convert_alpha()
menu_background = pygame.image.load("images/black.jpg").convert_alpha()
zombie1_surface = pygame.image.load("images/zombie1.png").convert_alpha()
zombie2_surface = pygame.image.load("images/zombie1.png").convert_alpha()
cabin_surface = pygame.image.load("images/cabin.png").convert_alpha()


# making rectangles
zombie1_rect = zombie1_surface.get_rect(bottomright = (750,600))
zombie2_rect = zombie1_surface.get_rect(center = (1050,190))
play_rect = text_play.get_rect(center = (600,500))
win_rect = text_win.get_rect(center =(600, 380))
quit_rect = text_quit.get_rect(center = (600,70))
shoot_rect = text_shoot.get_rect(center = (600,35))

#mob spawning
Zombie_rect_list = []
zombie_timer = pygame.USEREVENT + 1
pygame.time.set_timer(zombie_timer, 900)




while True:
    

    for event in  pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        

        if event.type == pygame.KEYDOWN and event.key ==pygame.K_s:
            game_active = 2

         
    
        if game_active == 2 or 3: 
            if event.type == pygame.KEYDOWN and event.key ==pygame.K_d:
                game_active= 1
                start_time = pygame.time.get_ticks()
                actual_score = 0
                print("false")
        

        if event.type == zombie_timer and game_active == 1:
            
            Zombie_rect_list.append(zombie1_surface.get_rect(bottomright = (randint(1100,1200),randint(450,750))))
           
    if actual_score > highest_score:
        highest_score = actual_score    
        
    

    if game_active == 1: 
        
       
        #field 
        screen.blit(field,(0,0))


        # score 
        
        text_score = test_font.render("Score:"f'{actual_score}', True, "Black")
        screen.blit(text_score, (20,20))

        # cabin

        cabin_rect = cabin_surface.get_rect(bottomright = (280,740))
        screen.blit(cabin_surface,cabin_rect)

        # timer
        
        current_time = pygame.time.get_ticks() - start_time
        timer = round (60 - current_time/1000, 2)
        timer_surface = test_font.render(f'{timer}', True,"Black")
        screen.blit(timer_surface, (1020,20))
        
    
        
        #options
        screen.blit(text_quit,quit_rect)
        screen.blit(text_shoot,shoot_rect)

        
        # aim
        mouse_pos = pygame.mouse.get_pos()
        zombie1_rect = zombie1_surface.get_rect(bottomright = (700,600))
        aim_rect = aim_surface.get_rect(center = (mouse_pos))

        screen.blit(aim_surface,aim_rect)

        
        if timer > 52:
            Change_Zombie1_x = randint(2,7)
        if timer<= 52 and timer >= 40:
            Change_Zombie1_x = randint(5,12)
        if timer< 40 and timer >= 30:
            Change_Zombie1_x = randint(12,17)
        if timer<30 and timer >= 23:
            Change_Zombie1_x = randint(17,22)
        if timer<23 and timer >= 15:
            Change_Zombie1_x = randint(22,25)    
        if timer<15 and timer >= 10:
            Change_Zombie1_x = randint(25,29)
        if timer< 10 and timer >=6:
            Change_Zombie1_x = randint(29,32)
        if timer< 6 and timer >=0.02:
            Change_Zombie1_x = randint(32,38)
    
                
        
        # Zombies 
        zombie_rect_list = zombie_movement(Zombie_rect_list)
        
       
    

    # losing screen
    elif game_active == 2: 
         screen.blit(menu_background,(0,0))
         text_score = test_font2.render("Score:"f'{actual_score}', True, "white")
         text_score_rect = text_score.get_rect(center =(600,200))
         screen.blit(text_score, text_score_rect)
         screen.blit(text_play, play_rect)
         text_highest = highest.render("highest score: "f'{highest_score}',True,"white")
         text_time_left = time_left.render("Time left: "f'{timer}'"sec",True,"white")
         time_left_rect = text_time_left.get_rect(center =(600, 380))
         highest_rect = text_highest.get_rect(center = (600,700))

         screen.blit(text_time_left,time_left_rect)
         screen.blit(text_highest, highest_rect)
         screen.blit(zombie2_surface,zombie2_rect)


    # win screen
    elif game_active == 3:    

        screen.blit(menu_background,(0,0))

        screen.blit(text_play, play_rect)

        text_score = test_font2.render("Score:"f'{actual_score}', True, "white")
        text_score_rect = text_score.get_rect(center =(600,200))
        screen.blit(text_score, text_score_rect)

       
        
        
        text_win = win.render("YOU WIN!",True,"white")
        screen.blit(text_win, win_rect)
        text_highest = highest.render("Highest score: "f'{highest_score}',True,"white")
        highest_rect = text_highest.get_rect(center = (600,680))

        screen.blit(text_highest,highest_rect)
         

    pygame.display.update()
    clock.tick(120)































































