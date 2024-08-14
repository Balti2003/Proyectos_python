#Importamos los modulos necesarios
import pygame
import random

#Creamos variables de ancho, alto y colores
width = 800
height = 600
black = (0,0,0)
white = (255, 255, 255, 255)
green = (0, 255, 0)

pygame.init() #Iniciamos pygame
pygame.mixer.init() #Linea de codigo para el sonido

screen = pygame.display.set_mode((width, height)) #Creamos la ventana
pygame.display.set_caption("Game Shooter") #Colocamos un titulo a la ventana
clock = pygame.time.Clock() #Reloj para controlar fps 

#Funcion para pantalla de game over
def show_go_screen():
    screen.blit(background, [0,0]) #Una vez que pierdo, el fondo se vuelve negro
    draw_text(screen, "Game Shooter", 65, width // 2, height // 4) #Texto de juego de tiros en la pantalla de go
    draw_text(screen, "Intrucciones", 27, width // 2, height // 2) #Texto de instrucciones en la pantalla de go
    draw_text(screen, "Press Key", 20, width // 2, height // 1.5) #Texto de presiona aqui en la pantalla de go
    pygame.display.flip() #Mostrar en pantalla
    waiting = True #Variable para saber si estoy esperando
    
    while waiting: #Mientras estoy esperando
        clock.tick(60) #Reloj a 60 fps
        for event in pygame.event.get(): #Chequeo si esta pasando algo en mi ventana, o si quiero salir del juego
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYUP: #Chequeo si alguna tecla fue presionada
                waiting = False
 
#Funcion para la barra de salud
def draw_shield_bar(surface, x, y, percentage):
    barra_length = 100 #Longitud de la barra
    barra_height = 10 #Altura de la barra
    fill_calculator = (percentage / 100) * barra_length #Calculamos para llenar la barra segun en el porcentaje
    border = pygame.Rect(x, y, barra_length, barra_height) #Borde para cubrir la barra
    fill = pygame.Rect(x, y, fill_calculator, barra_height) #LLenamos la barra
    pygame.draw.rect(surface, green, fill) #Pintamos la barra de salud en pantalla
    pygame.draw.rect(surface, white, border, 2) #Dibujamos el borde de la barra
    
#Funcion para crear meteoritos
def create_meteor():
    meteor = Meteor() #Creamos la instancia de meteor
    all_sprites.add(meteor) #Añadimos meteor a la lista all_sprites
    meteor_list.add(meteor) #Añadimos meteor a la lista meteor_list

#Funcion para dibujar texto
def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size) #Fuente
    text_surface = font.render(text, True, white) #Lugar donde pintar el texto, el true es para que salga bien definido
    text_rect = text_surface.get_rect() #Obtenemos la recta 
    text_rect.midtop = (x, y) #Donde colocamos el texto, coordenadas
    surface.blit(text_surface, text_rect) #Ponemos el texto en la pantalla 
    
#Clase jugador, subclase de sprite
class Player(pygame.sprite.Sprite):
    def __init__(self): #Iniciamos la clase
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert() #Cargamos la imagen de la nave
        self.image.set_colorkey(black) #Sacar el color negro que aparece al cargar la imagen de la nave
        self.rect = self.image.get_rect() #Obtenemos la recta o cuadro del sprite
        self.rect.centerx = width // 2 #Poner la recta en pantalla
        self.rect.bottom = height - 10 #Poner la recta en pantalla
        self.speed_x = 0 #Variable que es la velocidad con la cual se va a mover el jugador
        self.shield = 100 #Variable para la barra de salud del jugador

    def update(self): #Funcion/metodo para mover el jugador
        
        self.speed_x = 0 #Velocidad del jugador
        keystate = pygame.key.get_pressed() #metodo que obtiene una lista de teclas que son pulsadas
    
        if keystate[pygame.K_LEFT]: #Si se pulso la flecha izquierda, la velocidad disminuye en 5 para moverme hacia la izquierda
            self.speed_x = -5
        
        if keystate[pygame.K_RIGHT]: #Si se pulso la flecha derecha, la  velocidad aumenta en 5 para moverme hacia la derecha
            self.speed_x = 5
            
        self.rect.x += self.speed_x

        #Esto es para que no salga la nave de la pantalla
        if self.rect.right > width:
            self.rect.right = width
    
        if self.rect.left < 0:
            self.rect.left = 0
    
    def shoot(self): #Funcion/metodo para disparar balas
        bullet = Bullet(self.rect.centerx, self.rect.top) #Instancia bala
        all_sprites.add(bullet) #Agregamos las balas a la lista all_sprites
        bullet_list.add(bullet) #Agregamos las balas a la lista balas
        laser_sound.play() #Reproducimos sonido al disparar

#Clase meteorito, subclase de sprite
class Meteor(pygame.sprite.Sprite):
    def __init__(self): #Iniciamos la clase
        super().__init__()
        self.image = random.choice(meteor_images) #Cargamos una imagen de meteorito aleatoria de la lista meteor_images
        self.image. set_colorkey(black) #Sacar el color negro que aparece al cargar la imagen del meteorito
        self.rect = self.image.get_rect() #Obtenemos la recta o cuadro del sprite
        self.rect.x = random.randrange(width - self.rect.width) #Poner la recta en una ubicacion aleatoria de la pantalla
        self.rect.y = random.randrange(-140, -100)  #Poner la recta en una ubicacion aleatoria de la pantalla
        self.speedy = random.randrange(1, 10) #Le damos una velocidad aleatoria a los meteoritos en y
        self.speedx = random.randrange(-5, 5) #Le damos una velocidad aleatoria a los meteoritos en x
        
    def update(self): #Funcion/metodo para mover los meteoritos
        self.rect.y += self.speedy #Aumentamos la velocidad en y
        self.rect.x += self.speedx #Aumentamos la velocidad en x
        
        #Cuando los meteoritos salen de la pantalla, vuelven a aparecer en la parte de arriba
        if self.rect.top > height + 10 or self.rect.left < -40 or self.rect.right > width + 40:
            self.rect.x = random.randrange(width - self.rect.width) 
            self.rect.y = random.randrange(-100, -40)  
            self.speedy = random.randrange(1, 10)

#Clase bala, subclase de sprite
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y): #Iniciamos la clase
        super().__init__()
        self.image = pygame.image.load("assets/laser1.png") #Cargamos la imagen del laser/bala
        self.image.set_colorkey(black) #Sacar el color negro que aparece al cargar la imagen del laser
        self.rect = self.image.get_rect() #Obtenemos la recta o cuadro del sprite
        self.rect.y = y
        self.rect.centerx = x
        self.speedy = -10 #Le damos velocidad en y a la bala
    
    def update(self): #Funcion/metodo para mover las balas
        self.rect.y += self.speedy
        
        if self.rect.bottom < 0:
            self.kill() #Metodo para eliminar todas las instancias de un objeto de cualquier lista

#Clase explosion , subclase de sprite
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center): #Iniciamos la clase
        super().__init__()
        self.image = explosion_animation[0] #Cargamos la primera imagen de explosion, y luego iteramos con un for
        self.rect = self.image.get_rect() #Obtenemos la recta
        self.rect.center = center #Centramos la imagen
        self.frame = 0 #Variable para ir cambiando el valor de [0] de self.image
        self.last_update = pygame.time.get_ticks() #Variable que sirve para saber cuanto tiempo ha transcurrido, cuando estoy iniciando, para saber cuando hacer la animacion
        self.frame_rate = 50 #Velocidad de la explosion
        
    def update(self):
        now = pygame.time.get_ticks() #Variable que sirve para saber cuanto tiempo ha transcurrido, cuando quiero crear la explosion
        
        if now - self.last_update > self.frame_rate: #Si ha transcurrido mas de 50ms vamos a hacer la explosion    
            self.last_update = now
            self.frame += 1
            
            if self.frame == len(explosion_animation): #Si ya llegue al final de la lista, elimino los sprites que hay
                self.kill()
            else:
                #Cargamos la explosion
                center = self.rect.center
                self.image = explosion_animation[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center  
                
#-----Meteoritos imagenes------
meteor_images = [] #Lista de imagenes de distintos tamaños de meteoritos 
meteor_rutes = ["assets/meteorGrey_big1.png", "assets/meteorGrey_big2.png", "assets/meteorGrey_big3.png", "assets/meteorGrey_big4.png",
                "assets/meteorGrey_med1.png", "assets/meteorGrey_med2.png", "assets/meteorGrey_small1.png", "assets/meteorGrey_small2.png",
                "assets/meteorGrey_tiny1.png", "assets/meteorGrey_tiny2.png"] #Lista de rutas de las imagenes
for img in meteor_rutes: #Iteramos para cargar cada una de las imagenes
    meteor_images.append(pygame.image.load(img).convert())

#-----Explosion imagenes-----
explosion_animation = []

for  i in range(9):
    file = "assets/regularExplosion0{}.png".format(i) #Iteramos por cada una de las imagenes de explosion que van cambiando su ultimo numero 
    img = pygame.image.load(file).convert() #Cargamos la imagen de cada una
    img.set_colorkey("black") #Quitamos el color negro de fondo
    img_scale = pygame.transform.scale(img, (30,30)) #Le damos una escala mas pequeña a la imagen
    explosion_animation.append(img) #Agregamos las imagenes a la lista explosion_animation
    
#Cargar imagen de fondo
background = pygame.image.load("assets/background.png")

all_sprites = pygame.sprite.Group() #Lista donde almacenamos todos los sprites
meteor_list = pygame.sprite.Group() #Lista donde almacenamos los meteoritos
bullet_list = pygame.sprite.Group() #Lista donde almacenamos las balas

#Cargar sonidos
laser_sound = pygame.mixer.Sound("assets/laser5.ogg")
explosion_sound = pygame.mixer.Sound("assets/explosion.wav")

#Configuramos musica
pygame.mixer.music.load("assets/music.ogg") #Cargamos la musica
pygame.mixer.music.set_volume(0.2) #Volumen para la musica, mientras mas grande el numero mas fuerte sale la musica

game_over = True #Variable para fin del juego

pygame.mixer.music.play(loops = -1) #Ponemos la musica con un valor de lopps -1 para que se repita infinitamente

#------------------------------Bucle principal del juego------------------------------------------------------------------------------
running = True
while running:
    if game_over: #Si es true
        
        show_go_screen()
        game_over = False
        
        all_sprites = pygame.sprite.Group() #Lista donde almacenamos todos los sprites
        meteor_list = pygame.sprite.Group() #Lista donde almacenamos los meteoritos
        bullet_list = pygame.sprite.Group() #Lista donde almacenamos las balas
                
        score = 0 #Variable para el marcador
        
        player = Player() #Instancia del jugador
        all_sprites.add(player) #Agregamos jugador a la lista

        #Creamos tantos meteoritos para que aparezcan en la pantalla
        for i in range(8):
            create_meteor() #Creamos los meteoritos con la funcion
    #FIN IF
             
    clock.tick(60) #60 fps
    
    for event in pygame.event.get(): #Evento para salir de la ventana al apretar X
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN: #Evento para controlar que tecla se aprieta
            if event.key == pygame.K_SPACE: #Si aprieto la barra espaciadora, el jugador dispara
                player.shoot()      
                    
    all_sprites.update() #Actualizamos la lista
    
    #Detectar colisiones meteorito con laser
    hits = pygame.sprite.groupcollide(meteor_list, bullet_list, True, True) #El doble true es para que al colisionar, desaparezcan los meteoritos y las balas
    
    for hit in hits: #Cada vez que elimino un meteorito, que aparezca arriba otra vez
        create_meteor() #Creamos los meteoritos con la funcion
        score += 10 #Aumento el marcador cuando hay colision
        explosion_sound.play() #Cuando una bala colisione con el meteorito, se escuchara la explosion
        explosion = Explosion(hit.rect.center) #Realizamos la explosion
        all_sprites.add(explosion) #Agregamos las explosiones a la lista all_sprites
        
    #Detectar colisiones jugador con meteorito
    hits = pygame.sprite.spritecollide(player, meteor_list, True) #El true es para que al chocar, el meteorito desaparezca
    
    for hit in hits: #Por cada golpe registrado en hits
        player.shield -= 20 #Cuando un meteorito me pega voy disminuyendo la salud en 25
        create_meteor() #Creamos los meteoritos con la funcion
        
        if player.shield <= 0:
            game_over = True #Si mi vida se hace 0, termina el juego

    screen.blit(background, [0,0]) #Ponemos la imagen de fondo en la posicion 0,0
    
    all_sprites.draw(screen) #Dibujar los sprites en la pantalla
    
    #Marcador
    draw_text(screen, str(score), 25, width // 2, 10)
    
    #Funcion de la barra de salud
    draw_shield_bar(screen, 5, 5, player.shield)
    
    pygame.display.flip() #Actualizamos la pantalla
pygame.quit()