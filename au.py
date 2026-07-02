import subprocess
import time
from datetime import datetime

#acá el programa se inicia y le pide al sistema la fecha para cargarse en el txt

fecha_inicio =datetime.now()

#fecha límite para poder estudiar calculo( A partir de acá se tiene que hacer todo lo posible por calmar nuestro ritmo y disfrutar de los últimos momentos antes del examén)

segLim = 12
minLim = 12
horLim = 12
DayLim = 28
mesLim = 7

dias =[
	"Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"
]

print("Hoy es {dias[fecha_inicio.weekday()]} y este es el itinerario de hoy:")

if (fecha_inicio.weekday()==6):
	print("Hay que hir a misa de 9 a 10:30 de la mañana")

if(fecha_inicio.hour == 10 and fecha_inicio.minute == 30 and fecha_inicio.second == 12):
	print("Es hora de tomar agua")
	#subprocess.Popen(["mpv"/"pay-audio","/storage/emulated/0/Music/alarma.mp3"])
if(fecha_inicio.hour == 10 and fecha_inicio.minute == 45 and fecha_inicio.secon>
        print("Hora de ver una clase del conamat")
        #subprocess.Popen(["mpv"/"pay-audio","/storage/emulated/0/Music/alarma.>
except KeyboardInterrupt:
	print("\n\nPrograma finalizado por el usuario.")
finally:
	horaFinal = fin.strftime("%H:%M:%S")
#creando el txt

with open("fecha.txt", "w", encoding="utf-8") as archivo:
	archivo.write(f"{horaFinal}/{fecha_inicio.day}/{fecha_inicio.month}/{fecha_inicio.year}")
print("\nArchivo 'fecha.txt' creado correctamente.")
print(f"Contenido: {hora_final}/{dia:02d}/{mes:02d}/{anio}")
#A=0
#B=0
#print("\t\t Hoja de prioridades \t Kata \n Que dia es?:")
#A=input()
#match A:
#	case "Lunes"|"lunes":
#		print("\n20 paginas spivak, 2 ejercicios de optimizacion\nDibujo Osita")
#	case "Martes"|"martes":
#		print("\n24 paginas spivak, 1 ejercicio de optimizacion\nRenpy\n23 de junio Moredev 11:00 am")
#	case "Miercoles"|"miercoles":
#		print("\n28 paginas spivak, 8 ejercicios de optimizacion\nBash\n 24 de junio Moredev 11:00 am")
#	case "Jueves"|"jueves":
#		print("\n33 paginas spivak,5 ejercicios de optimizacion\n 25 de junio Moredev 11:00 am")
#	case "Viernes"|"viernes":
#		print("\n38 paginas spivak, 2 ejercicios de optimizacion\nDibujo Osita")
#	case "Sabado"|"sabado":
#		print("\n44 paginas spivak, 6 ejercicios optimizacion\n Renpy")
#	case "Domingo"|"domingo":
#		print("\nMisa a las 10 am\n 50 paginas spivak, 6 ejercicios optimizacion\n Escribir ensayo para FNAFHS Zero Again ")
#if A in ["Lunes","lunes","Miercoles","miercoles","Viernes","viernes"]:
#	print("\nESCALERAS")
#else:
#	print("\nPeso Muerto 30 min, lagartijas inclinadas 30 repeticiones 3vueltas \t 3 minutos de descanzo\n")

"""
from pathlib import Path

nombre = "fecha"
extension = ".txt"

contador = 0

while True:

    if contador == 0:
        archivo = Path(f"{nombre}{extension}")
    else:
        archivo = Path(f"{nombre}{contador}{extension}")

    if not archivo.exists():
        break

    contador += 1

with open(archivo, "w", encoding="utf-8") as f:
    f.write("Contenido del archivo")

print(f"Archivo creado: {archivo}")
"""
