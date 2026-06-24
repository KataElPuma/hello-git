,A=0
B=0
print("\t\t Hoja de prioridades \t Kata \n Que dia es?:")
A=input()
match A:
	case "Lunes"|"lunes":
		print("\n20 paginas spivak, 2 ejercicios de optimizacion\nDibujo Osita")
	case "Martes"|"martes":
		print("\n24 paginas spivak, 1 ejercicio de optimizacion\nRenpy\n23 de junio Moredev 11:00 am")
	case "Miercoles"|"miercoles":
		print("\n28 paginas spivak, 8 ejercicios de optimizacion\nBash\n 24 de junio Moredev 11:00 am")
	case "Jueves"|"jueves":
		print("\n33 paginas spivak,5 ejercicios de optimizacion\n 25 de junio Moredev 11:00 am")
	case "Viernes"|"viernes":
		print("\n38 paginas spivak, 2 ejercicios de optimizacion\nDibujo Osita")
	case "Sabado"|"sabado":
		print("\n44 paginas spivak, 6 ejercicios optimizacion\n Renpy")
	case "Domingo"|"domingo":
		print("\nMisa a las 10 am\n 50 paginas spivak, 6 ejercicios optimizacion\n Escribir ensayo para FNAFHS Zero Again ")
if A in ["Lunes","lunes","Miercoles","miercoles","Viernes","viernes"]:
	print("\nESCALERAS")
else:
	print("\nPeso Muerto 30 min, lagartijas inclinadas 30 repeticiones 3vueltas \t 3 minutos de descanzo\n")
