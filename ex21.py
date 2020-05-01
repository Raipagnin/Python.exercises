#from pygame import mixer
#mixer.init()
#mixer.music.load('ex21.mp3.mp3')
#mixer.music.play()
#input('agora vc escuta?')
#so funciona por conta do input, porem desse jeito forca o programa a esperar que vc coloque algum valor manualmente, nao encerrando o programa apos

import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('ex21.mp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()
#a musica para facilmente... acessando browser ou outra coisa

