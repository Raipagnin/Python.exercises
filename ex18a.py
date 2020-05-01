# dado um angulo, descubra o seno, coseno e tangente dessa merda
import math
ang = float(input('Digite o angulo: '))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O angulo de {} tem o SENO de {:.2f}\nO COSSENO de {:.2f}\nE a tangente de {:.2f}'.format(ang, sin, cos, tan))
