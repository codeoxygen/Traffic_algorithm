import pygame
import random
import time

width = 1400
height = 1400

pygame.init()

# Set up display
screen_width = 1400
screen_height = 1400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Vehicle Simulation")


# Load images
intersection_image = pygame.image.load("images/intersection.png")
ver_vehicle_image = pygame.image.load("images/down/car.png")
hor_vehicle_image = pygame.image.load("images/right/car.png")

traffic_light_red_up_down = pygame.image.load("images/signals/down/red.png")
traffic_light_green_up_down = pygame.image.load("images/signals/down/green.png")
traffic_light_yellow_up_down = pygame.image.load("images/signals/down/yellow.png")

traffic_light_red_left = pygame.image.load("images/signals/left/red.png")
traffic_light_green_left = pygame.image.load("images/signals/left/green.png")
traffic_light_yellow_left = pygame.image.load("images/signals/left/yellow.png")

traffic_light_red_right = pygame.image.load("images/signals/right/red.png")
traffic_light_green_right = pygame.image.load("images/signals/right/green.png")
traffic_light_yellow_right = pygame.image.load("images/signals/right/yellow.png")

clock = pygame.time.Clock()


class Vehicle:
    def __init__(self, position ,height,width):
        self.speed = 2
        self.position = position
        

        if self.position == 'up':
            self.image = ver_vehicle_image
            self.rect = self.image.get_rect(midbottom=((width//2)-60, height))
            self.dir = 0,-self.speed
            
        elif self.position == 'down':
            self.image = ver_vehicle_image
            self.rect = self.image.get_rect(midtop=(height//2, 0))
            self.dir = 0,self.speed
            
        elif self.position == 'left':
            self.image  = hor_vehicle_image
            self.rect = self.image.get_rect(midleft=(0, (height-620)//2))
            self.dir = self.speed,0
            
        elif self.position == 'right':
            self.image = hor_vehicle_image
            self.rect = self.image.get_rect(midright=(width, (height-440)//2))
            self.dir = -self.speed,0
            
        
    def move(self):
        
        self.rect.move_ip(self.dir)
        

    def pause(self):
        self.rect.move_ip(0,0)
        

    def draw(self):
        screen.blit(self.image, self.rect)
    
    def get_position(self):
        x = self.rect.x
        y = self.rect.y
        return x , y
    
    def crossed(self):
        pass 

    



def spawn_vehicles(directions):
    for direction, count in directions.items():
        for _ in range(count):
            vehicles[direction].append(Vehicle(direction, 1400,1400))
            

            """
        elif direction == "down":
            for _ in range(count):
                vehicles.append(Vehicle(random.randint(100, screen_width - 100), screen_height))
        elif direction == "left":
            for _ in range(count):
                vehicles.append(Vehicle(0, random.randint(100, screen_height - 100)))
        elif direction == "right":
            for _ in range(count):
                vehicles.append(Vehicle(screen_width, random.randint(100, screen_height - 100)))
"""

def vehicle_stop(flag,  width= 1400, height=1400):
    

    if flag == 1 :
        return True
    else:
        return False
    
def switch_to_red(red_lights , direction):

   return red_lights[direction]

def switch_to_green(green_lights , direction):

   return green_lights[direction]

spawn_directions = {
    "up": 2,
    "down": 3,
    "left": 2,
    "right": 1
}
lights_cordinates = {
    "up": (550 , 540),
    "down": (790,240),
    "left": (500,300),
    "right": (800,530)
}

vehicles = {
    "up" : [] , 
    "down" : [] ,
    "left" : [] , 
    "right" : [] ,
    }

red_lights = {
   "up" : screen.blit(traffic_light_red_up_down, lights_cordinates["up"]),
   "down" : screen.blit(traffic_light_red_up_down, lights_cordinates["down"]),
   "left" : screen.blit(traffic_light_red_left, lights_cordinates['left']),
    "right" : screen.blit(traffic_light_red_right, lights_cordinates['right'])
   }
green_lights = {
   "up" : screen.blit(traffic_light_green_up_down, lights_cordinates["up"]),
   "down" : screen.blit(traffic_light_green_up_down, lights_cordinates["down"]),
   "left" : screen.blit(traffic_light_green_left, lights_cordinates['left']),
    "right" : screen.blit(traffic_light_green_right, lights_cordinates['right'])
   }

spawn_frequency = 1  # Adjust this value to control spawn frequency (lower values mean slower spawning)
spawn_timer = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(intersection_image, (0, 0))
    #screen.blit(traffic_light_green_up_down, lights_cordinates["up"])
    #screen.blit(traffic_light_green_up_down, lights_cordinates["down"])
    #screen.blit(traffic_light_green_left, lights_cordinates['left'])
    #screen.blit(traffic_light_green_right, lights_cordinates['right'])
    #screen.blit(traffic_light_green, (800,350))
    #screen.blit(traffic_light_green, (800,350))
    

    # Spawn vehicles based on the defined directions and counts
    spawn_timer += clock.get_time()  # Measure time passed since last frame

    if spawn_timer >= 1000 / spawn_frequency:  # Convert spawn frequency to milliseconds
        spawn_vehicles(spawn_directions)
        spawn_timer = 0

    algorithm_directions = {
            "up": 0,
            "down": 1,
            "left": 1,
            "right": 0
    }
    # Move and draw vehicles
    for direction , vehicle_count in vehicles.items():
        flag = algorithm_directions[direction]
        for vehicle in vehicle_count:

            if vehicle_stop(flag):
            
                vehicle.pause()
                vehicle.draw()
                match direction:

                    case "up" : 
                        screen.blit(traffic_light_red_up_down, lights_cordinates["up"]),
                    case "down" : 
                        screen.blit(traffic_light_red_up_down, lights_cordinates["down"]),
                    case "left" : 
                        screen.blit(traffic_light_red_left, lights_cordinates['left']),
                    case "right" : 
                        screen.blit(traffic_light_red_right, lights_cordinates['right'])

                
            else:
                #screen.blit(traffic_light_green, (800,350))
                vehicle.move()
                vehicle.draw()
                match direction:

                    case "up" : 
                        screen.blit(traffic_light_green_up_down, lights_cordinates["up"]),
                    case "down" : 
                        screen.blit(traffic_light_green_up_down, lights_cordinates["down"]),
                    case "left" : 
                        screen.blit(traffic_light_green_left, lights_cordinates['left']),
                    case "right" : 
                        screen.blit(traffic_light_green_right, lights_cordinates['right'])
                
                

            if vehicle.rect.y > screen_height or vehicle.rect.x < 0 or vehicle.rect.x > screen_width:
                vehicles[direction].remove(vehicle)
        

    pygame.display.flip()
    screen.fill((0, 0, 0)) 

    clock.tick(100)


pygame.quit()