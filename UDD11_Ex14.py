#Crear el joc d’arkanoid utilitzant la llibreria pygame.
import pygame
from random import randint

# Inicialitzem la llibreria, dibuixem la finestra i li posem nom
pygame.init()                      	 
w = pygame.display.set_mode((640,480))  
pygame.display.set_caption("Joc")   
    
 # Carreguem una imatge, agafem l'àrea, li assignem una velocitat i ho posem a dalt a l'esquerra
pilota = pygame.image.load("bola.png")  
pilotarect = pilota.get_rect()    	 
speed = [randint(2,6),randint(2,6)]	 
pilotarect.move_ip(0,0)
    
# Carreguem una imatge, agafem l'àrea i el movem quasi a la part inferior i enmig
barra = pygame.image.load("barra.png")
barrarect = barra.get_rect()
barrarect.move_ip(240,450)

# Tamany de la font que sortirà per pantalla
fuente = pygame.font.Font(None, 36)

# Bucle principal
j = True
while j:
	# Controlem tots els esdeveniments i si el jugador tanca, acabem
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				j = False
	# Controlem la barra amb el teclat: fletxa esquerra i dreta, movem en la direcció adient.
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
				barrarect = barrarect.move(-3,0)
		if keys[pygame.K_RIGHT]:
				barrarect = barrarect.move(3,0)
		if barrarect.colliderect(pilotarect):
				speed[1] = -speed[1]
	# Controlem la pilota: col·lisions canviem el sentit en un eix, depenent d'on sigui.
		pilotarect = pilotarect.move(speed)
		if pilotarect.left < 0 or pilotarect.right > w.get_width():
			speed[0] = -speed[0]
		if pilotarect.top < 0:
			speed[1] = -speed[1]
	# Si la pelota toca el terra, hem perdut! si no ens ha salvat la barra!
		if pilotarect.bottom > w.get_height():
			texto = fuente.render("Has perdut!", True, (125,125,125))
			txto_rect = texto.get_rect()
			texto_x = w.get_width() / 2 - texto_rect.width / 2
			texto_y = w.get_height() / 2 - texto_rect.height / 2
			w.blit(texto, [texto_x, texto_y])
		else:
   	 # Esborrem tot, tornem a dibuixar la bolla i la barra
			w.fill((252, 243, 207))
			w.blit(pilota, pilotarect)
			w.blit(barra, barrarect)
		pygame.display.flip()
		pygame.time.Clock().tick(60)

pygame.quit()
