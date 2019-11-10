import pygame
import random


class Food:
	def __init__(self,win):
		self.win = win
		self.x = random.randint(0,50)
		self.y = random.randint(0,50)
	def generate_food(self):

		pygame.draw.rect(self.win,(0,255,255),(self.x*10,self.y*10,10,10))

class Snake:
    def __init__(self,win):
        self.head = [3,4]
        self.tail = []
        self.previous = []
        self.up = (-1,0)
        self.down = (1,0)
        self.right = (1,1)
        self.left = (-1,1)
        self.width = 10
        self.height = 10
        self.win = win
        self.direction = self.right
        

    def print_Head_And_Tail_Position(self):
        print(self.head,self.tail)

    def move_snake(self):
        self.previous = list(self.head)
        self.head[self.direction[0]] += self.direction[1]
        # Now we must loop backward on the tail and get the position of it's precedence
        i = len(self.tail) -1
        while i>=1:
            self.tail[i] = list(self.tail[i-1])
            i-=1

        try:
	        self.tail[0] = list(self.previous)
        except:
        	pass

    def draw(self):
        cellW = 10

        pygame.draw.rect(self.win,(0,0,255),(self.head[0]*cellW,self.head[1]*cellW,self.width,self.height))
        for cell in self.tail:
            pygame.draw.rect(self.win,(250,164,255),(cell[0]*cellW,cell[1]*cellW,self.width,self.height))

    def self_collided(self):

    	if(self.head[0] > 50 or self.head[0] < 0):
    		return True
    	if(self.head[1] > 50 or self.head[1] < 0):
    		return True

    	for cell in self.tail:
    		if(self.head[0] == cell[0] and self.head[1] == cell[1]):
    			print("Collided!!!!!!!!!!!!!!!!!")
    			return True

    def grow(self):

    	if(len(self.tail) < 1):
    		self.tail.append(list([self.head[0],self.head[1]-1]))
    	else:
	    	self.tail.append(list([self.tail[-1][0],self.tail[-1][1]-1]))



pygame.init()
win_height = 500
win_width = 500
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Snake")


is_stopped = False
snake = Snake(win)
food = Food(win)
food.generate_food()

def eat():
	if( ((snake.head[0]*10) == food.x*10) and ((snake.head[1]*10) == food.y*10)):
		return True


while not is_stopped:
    pygame.time.delay(100)
    win.fill((0,0,0))
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            is_stopped = True

    keys = pygame.key.get_pressed()
    if(snake.self_collided()):
    	is_stopped = True
    if(snake.direction == (-1,-1) or snake.direction == (1,1)):
        if(keys[pygame.K_RIGHT]):
            snake.direction = (0,1)
        elif(keys[pygame.K_LEFT]):
            snake.direction = (0,-1)
    if(snake.direction == (0,1) or snake.direction == (0,-1) ):
        if(keys[pygame.K_UP]):
            snake.direction = (-1,-1)
        elif(keys[pygame.K_DOWN]):
            snake.direction = (1,1)
    if(keys[pygame.K_s]):
    	snake.grow()
    if(eat()):
    	food.x = random.randint(0,50)
    	food.y = random.randint(0,55)
    	snake.grow()

    
    snake.print_Head_And_Tail_Position()
    snake.move_snake()

    snake.draw()
    food.generate_food()
    pygame.display.update()
    
pygame.quit()

