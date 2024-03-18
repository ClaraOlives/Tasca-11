import sys    # para usar exit()
import time   # para usar sleep()
import pygame

ANCHO = 640 # Ancho de la pantalla.
ALTO = 480  # Alto de la pantalla.
color_azul = (0, 0, 64)  # Color azul para el fondo.
color_blanco = (255, 255, 255) # Color blanco, para textos.

pygame.init()

class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('/home/cicles/AO/Tasca11/bola.png')
        # Obtener rectangulo de la imagen
        self.rect = self.image.get_rect()
        # Posicion inicial centrada en pantalla.
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        # Establecer velocidad inicial.
        self.speed = [3, 3]

    def update(self):
        # Evitar que salga por debajo.
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        # Evitar que salga por la derecha.
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        # Mover en base a posicion actual y velocidad.
        self.rect.move_ip(self.speed)

class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('/home/cicles/AO/Tasca11/barra.png')
        # Obtener rectangulo de la imagen
        self.rect = self.image.get_rect()
        # Posicion inicial centrada en pantalla en X.
        self.rect.midbottom = (ANCHO / 2, ALTO - 20)
        # Establecer velocidad inicial.
        self.speed = [0, 0]

    def update(self, evento):
        # Buscar si se presiono flecha izquierda.
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5, 0]
        # Si se presiono flecha derecha.
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [5, 0]
        else:
            self.speed = [0, 0]
        # Mover en base a posicion actual y velocidad.
        self.rect.move_ip(self.speed)

class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('/home/cicles/AO/Tasca11/ladrillo.png')
        # Obtener rectangulo de la imagen
        self.rect = self.image.get_rect()
        # Posicion inicial, provista externamente.
        self.rect.topleft = posicion

class Muro(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos):
        pygame.sprite.Group.__init__(self)

        pos_x = 0
        pos_y = 20
        for i in range(cantidadLadrillos):
            ladrillo = Ladrillo((pos_x, pos_y))
            self.add(ladrillo)

            pos_x += ladrillo.rect.width
            if pos_x >= ANCHO:
                pos_x = 0
                pos_y += ladrillo.rect.height

# Funcion llamada tras dejar pasar la bola.
def juego_terminado():
    fuente = pygame.font.SysFont('Arial', 72)
    texto = fuente.render('Juego terminado :(', True, color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.center = [ANCHO / 2, ALTO / 2]
    pantalla.blit(texto, texto_rect)
    pygame.display.flip()
    # Pausar por tres segundos
    time.sleep(3)
    # Salir.
    sys.exit()

def mostrar_puntuacion():
    fuente = pygame.font.SysFont('Consolas', 20)
    texto = fuente.render(str(puntuacion).zfill(5), True, color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.topleft = [0, 0]
    pantalla.blit(texto, texto_rect)

def mostrar_vidas():
    fuente = pygame.font.SysFont('Consolas', 20)
    cadena = "Vidas: " + str(vidas).zfill(2)
    texto = fuente.render(cadena, True, color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.topright = [ANCHO, 0]
    pantalla.blit(texto, texto_rect)

def victoria():
    fuente = pygame.font.SysFont('Arial', 72)
    texto = fuente.render('Juego ganado!! :)', True, color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.center = [ANCHO / 2, ALTO / 2]
    pantalla.blit(texto, texto_rect)
    pygame.display.flip()
    # Pausar por tres segundos
    time.sleep(3)
    # Salir.
    sys.exit()


# Inicializando pantalla.
pantalla = pygame.display.set_mode((ANCHO, ALTO))
# Configurar titulo de pantalla.
pygame.display.set_caption('PyBrick')
# Crear el reloj.
reloj = pygame.time.Clock()
# Ajustar repeticion de evento de tecla presionada.
pygame.key.set_repeat(30)

cantidadLadrillos = 48
bolita = Bolita()
jugador = Paleta()
muro = Muro(cantidadLadrillos)
puntuacion = 0
vidas = 3
esperando_saque = True

while True:
    # Establecer FPS.
    reloj.tick(60)

    # Revisar todos los eventos.
    for evento in pygame.event.get():
        # Si se presiona la tachita de la barra de titulo,
        if evento.type == pygame.QUIT:
            # cerrar el videojuego.
            sys.exit()
        # Buscar eventos del teclado,
        elif evento.type == pygame.KEYDOWN:
            jugador.update(evento)
            if esperando_saque == True and evento.key == pygame.K_SPACE:
                esperando_saque = False
                if bolita.rect.centerx < ANCHO / 2:
                    bolita.speed = [3, -3]
                else:
                    bolita.speed = [-3, -3]

    # Actualizar posicion de la bolita.
    if esperando_saque == False:
        bolita.update()
    else:
        bolita.rect.midbottom = jugador.rect.midtop

    # Colision entre bolita y jugador.
    if pygame.sprite.collide_rect(bolita, jugador):
        bolita.speed[1] = -bolita.speed[1]

    # Colision de la bolita con el muro.
    lista = pygame.sprite.spritecollide(bolita, muro, False)
    if lista:
        ladrillo = lista[0]
        cx = bolita.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita.speed[0] = -bolita.speed[0]
        else:
            bolita.speed[1] = -bolita.speed[1]
        muro.remove(ladrillo)
        puntuacion += 10
        cantidadLadrillos -= 1


    # Revisar si bolita sale de la pantalla.
    if bolita.rect.top > ALTO:
        vidas -= 1
        esperando_saque = True

    # Rellenar la pantalla.
    pantalla.fill(color_azul)
    # Mostrar puntuacion
    mostrar_puntuacion()
    # Mostrar vidas.
    mostrar_vidas()
    # Dibujar bolita en pantalla.
    pantalla.blit(bolita.image, bolita.rect)
    # Dibujar jugador en pantalla.
    pantalla.blit(jugador.image, jugador.rect)
    # Dibujar los ladrillos.
    muro.draw(pantalla)
    # Actualizar los elementos en pantalla.
    pygame.display.flip()

    #Comprobamos si ya no quedan ladrillo
    if cantidadLadrillos <= 0:
        victoria()

    #Comprobamos si nos hemos quedados sin vidas
    if vidas <= 0:
        juego_terminado()