
import time


hora = time.strftime('%H') 
minuto = time.strftime('%M') 


if int(hora) >= 19:
	print ("Tiempo de regresar") 
else:
	print ("Quedan {} horas y {} minutos para irnos a casa".format(18- int(hora), 59-int(minuto)))