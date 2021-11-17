import random


# LO QUE HACE EL JUGADOR

def casillero_cascara_de_banana(posicion_jugador: int) -> int:  # le resta 20 a la posicion del jugador
	posicion_jugador = posicion_jugador - 20
	return posicion_jugador

def casillero_magico() -> int:  # cae en un lugar random entre el 2 y el 99
	return random.randrange(2, 99)

def casillero_rushero(posicion_jugador: int) -> int:
	posicion_jugador = posicion_jugador + 10 - (posicion_jugador % 10)
	return posicion_jugador

def casillero_hongos_locos(posicion_jugador: int) -> int:
	if posicion_jugador % 10 != 0:
		posicion_jugador = posicion_jugador - (posicion_jugador % 10) + 1
	else:
		posicion_jugador = posicion_jugador - 9
	return posicion_jugador

# ASIGNAR CADA CASILLERO EN EL TABLERO
def asignar_casillero_cascara_de_banana(serpientes_escaleras: dict) -> list:
	casilleros_asignados_cascara_de_banana = []
	for i in range(0, 5):
		casillero: int = random.randrange(21, 99)
		while casillero in serpientes_escaleras or casillero in serpientes_escaleras.values() or casillero in casilleros_asignados_cascara_de_banana:
			casillero = random.randrange(21, 99)
		# agrego restriccion de que no este en el diccionario, si esta, que vuelva a pedir el random
		casilleros_asignados_cascara_de_banana.append(casillero)
	# creo lista vacia, despues el for lo va a tirar 5 veces y .append agrega los numeros donde cayo a la lista
	return casilleros_asignados_cascara_de_banana

def asignar_casillero_magico(serpientes_escaleras: dict, casillero_cascara_de_banana: list) -> list:
	casilleros_asignados_magico = []
	for i in range(0, 3):
		casillero: int = random.randrange(2, 99)
		while casillero in serpientes_escaleras or casillero in serpientes_escaleras.values() or casillero in casillero_cascara_de_banana or casillero in casilleros_asignados_magico:
			casillero = random.randrange(2, 99)
		casilleros_asignados_magico.append(casillero)
	return casilleros_asignados_magico

def asignar_casillero_rushero(serpientes_escaleras: dict, casillero_cascara_de_banana: list, casillero_magico: list) -> int:
	casillero: int = random.randrange(2, 99)
	while casillero in serpientes_escaleras or casillero in serpientes_escaleras.values() or casillero in casillero_cascara_de_banana or casillero in casillero_magico or casillero % 10 == 0:
		casillero = random.randrange(2, 99)
	return casillero

def asignar_casillero_hongos_locos(serpientes_escaleras: dict, casillero_cascara_de_banana: list, casillero_magico: list,
                                   casillero_rushero: int) -> int:
	casillero: int = random.randrange(2, 99)
	while casillero in serpientes_escaleras or casillero in serpientes_escaleras.values() or casillero in casillero_cascara_de_banana or casillero in casillero_magico or casillero == casillero_rushero or (
			casillero - 1) % 10 == 0:
		casillero = random.randrange(2, 99)
	return casillero

def actualizar_casillero(serpientes_escaleras: dict, posicion_jugador: int, contadores_casilleros_especiales: list) -> (
int, list):
	if posicion_jugador in serpientes_escaleras:
		numero = serpientes_escaleras[
			posicion_jugador]  # busca la key=posicion_jugador y me devuelve el valor, ejemplo posicion_jugador = 6, valor=67
		if posicion_jugador < numero:
			contadores_casilleros_especiales[5] = contadores_casilleros_especiales[5] + 1
			print(f"SUBIS POR UNA ESCALERA Y QUEDASTE EN LA POSICION: {numero}")
		else:
			contadores_casilleros_especiales[4] = contadores_casilleros_especiales[4] + 1
			print(f"BAJAS POR UNA SERPIENTE Y QUEDASTE EN LA POSICION: {numero}")
	else:
		numero = posicion_jugador
	return (numero, contadores_casilleros_especiales)

def dado() -> int:
	numero_dado = random.randrange(1, 6)
	print(f"SACASTE UN: {numero_dado}")
	return numero_dado

def jugar(posicion_jugador: int, serpientes_escaleras: dict, casilleros_cascara_de_banana: list, casilleros_magico: list,
          casillero_rushero_asignado: int, casillero_hongos_locos_asignado: int,
          contadores_casilleros_especiales: list) -> tuple[int, list]:
	posicion_jugador = dado() + posicion_jugador
	print(f"AHORA TU POSICION ES: {posicion_jugador}")
	tupla_jugador: [int, list] = actualizar_casillero(serpientes_escaleras, posicion_jugador, contadores_casilleros_especiales)
	posicion_jugador = tupla_jugador[0]
	contadores_casilleros_especiales = tupla_jugador[1]

	if posicion_jugador in casilleros_cascara_de_banana:
		posicion_jugador = casillero_cascara_de_banana(posicion_jugador)
		print(f"CAISTE EN UN CASILLERO CASCARA DE BANANA Y QUEDASTE EN LA POSICION: {posicion_jugador}")
		contadores_casilleros_especiales[0] = contadores_casilleros_especiales[0] + 1
	elif posicion_jugador in casilleros_magico:
		posicion_jugador = casillero_magico()
		print(f"CAISTE EN UN CASILLERO MAGICO Y QUEDASTE EN LA POSICION: {posicion_jugador}")
		contadores_casilleros_especiales[1] = contadores_casilleros_especiales[1] + 1
	elif posicion_jugador == casillero_rushero_asignado:
		posicion_jugador = casillero_rushero(posicion_jugador)
		print(f"CAISTE EN UN CASILLERO RUSHERO Y QUEDASTE EN LA POSICION: {posicion_jugador}")
		contadores_casilleros_especiales[2] = contadores_casilleros_especiales[2] + 1
	elif posicion_jugador == casillero_hongos_locos_asignado:
		posicion_jugador = casillero_hongos_locos(posicion_jugador)
		print(f"CAISTE EN UN CASILLERO HONGOS LOCOS Y QUEDASTE EN LA POSICION: {posicion_jugador}")
		contadores_casilleros_especiales[3] = contadores_casilleros_especiales[3] + 1

	return posicion_jugador, contadores_casilleros_especiales

def asignar_letra_en_tablero(tablero, casillero: int, letra: str):
	if casillero >= 100:
		tablero[9][9] = letra
	else:
		if casillero % 10 == 0:
			tablero[int((casillero / 10) - 1)][9] = letra
		else:
			tablero[int(casillero / 10)][(casillero % 10) - 1] = letra
	return tablero

def resetear_casillero_en_tablero(tablero, casillero: int):
	if casillero >= 100:
		tablero[9][9] = casillero
	else:
		if casillero % 10 == 0:
			tablero[int((casillero / 10) - 1)][9] = casillero
		else:
			tablero[int(casillero / 10)][(casillero % 10) - 1] = casillero
	return tablero

def asignar_casilleros_al_tablero(tablero, casilleros_cascara_de_banana: list, casilleros_magico: list,
                                  casillero_rushero: int, casillero_hongos_locos: int):
	escaleras: dict = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96}
	serpientes: dict = {86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}
	contador: int = 1
	for casillero_m in casilleros_magico:
		tablero = asignar_letra_en_tablero(tablero, casillero_m, 'M')
	for casillero_c in casilleros_cascara_de_banana:  # casillero_c toma valores del casillero_cascara_de_banana y despues reemplaza un valor C al tablero
		tablero = asignar_letra_en_tablero(tablero, casillero_c, 'C')
	for casillero_e in escaleras:
		tablero = asignar_letra_en_tablero(tablero, casillero_e, 'E' + str(contador))
		tablero = asignar_letra_en_tablero(tablero, escaleras[casillero_e], 'E' + str(contador))
		contador = contador + 1
	contador = 1
	for casillero_s in serpientes:
		tablero = asignar_letra_en_tablero(tablero, casillero_s, 'S' + str(contador))
		tablero = asignar_letra_en_tablero(tablero, serpientes[casillero_s], 'S' + str(contador))
		contador = contador + 1
	tablero = asignar_letra_en_tablero(tablero, casillero_rushero, 'R')
	tablero = asignar_letra_en_tablero(tablero, casillero_hongos_locos, 'H')
	return tablero

def turno_jugador(jugador: str, posicion_jugador: int,jugador_en_tablero: str, serpientes_escaleras: dict, casilleros_cascara_de_banana: list,
                    casilleros_magico: list, casillero_rushero_asignado: int,
                    casillero_hongos_locos_asignado: int,
                    contadores_casilleros_especiales: list, tablero: list[list]) -> tuple[int, list]:

	print(f"\n TURNO JUGADOR {jugador} \n")
	print(f"TU POSICION ACTUAL ES {posicion_jugador}")

	tupla_jugador: [int, list] = jugar(posicion_jugador, serpientes_escaleras, casilleros_cascara_de_banana,
	                                     casilleros_magico, casillero_rushero_asignado,
	                                     casillero_hongos_locos_asignado,
	                                     contadores_casilleros_especiales)

	print(mostrarTablero(asignar_letra_en_tablero(tablero, tupla_jugador[0], jugador_en_tablero)))  # muestra todos J por donde pasó
	resetear_casillero_en_tablero(tablero, tupla_jugador[0])  # resetear posicion anterior
	asignar_casilleros_al_tablero(tablero, casilleros_cascara_de_banana, casilleros_magico,
	                                        casillero_rushero_asignado, casillero_hongos_locos_asignado)

	return tupla_jugador


def jugar_partida(contadores_casilleros_especiales: list) -> list:
	jugador_1: str = str(input(f"\n Jugador 1, Ingrese su nombre: \n")).upper()
	jugador_2: str = str(input(f" \n Jugador 2, Ingrese su nombre: \n")).upper()
	posicion_jugador_1: int = 0
	posicion_jugador_2: int = 0
	serpientes_escaleras = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96, 86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}
	tablero = []


	for i in range(10):
		tablero.append(list(range(1 + 10 * i, 1 + 10 * (i + 1))))

	casilleros_cascara_de_banana = asignar_casillero_cascara_de_banana(
		serpientes_escaleras)  # creo la lista para tenerla en el main y la asigno a la funcion que cree antes
	casilleros_magico = asignar_casillero_magico(serpientes_escaleras,
	                                             casilleros_cascara_de_banana)  # restringo casilleros cascara de banana
	casillero_rushero_asignado = asignar_casillero_rushero(serpientes_escaleras, casilleros_cascara_de_banana,
	                                                       casilleros_magico)  # lo defino como un entero porque tengo un solo casillero para asinarlo
	casillero_hongos_locos_asignado = asignar_casillero_hongos_locos(serpientes_escaleras, casilleros_cascara_de_banana,
	                                                                 casilleros_magico, casillero_rushero_asignado)
	tablero = asignar_casilleros_al_tablero(tablero, casilleros_cascara_de_banana, casilleros_magico,
	                                        casillero_rushero_asignado, casillero_hongos_locos_asignado)
	print(mostrarTablero(tablero))

	sorteo: int = random.randrange(1, 3)  # SORTEO ENTRE JUGADOR 1 y 2 para empezar el juego

	while posicion_jugador_1 < 100 and posicion_jugador_2 < 100:
		if sorteo == 1 and posicion_jugador_2 < 100:
			interaccion: str = input(f"\n {jugador_1} PRESIONE ENTER PARA JUGAR: ")
			tupla_jugador = turno_jugador(jugador_1, posicion_jugador_1,'J1', serpientes_escaleras, casilleros_cascara_de_banana,
			                                  casilleros_magico, casillero_rushero_asignado,
			                                  casillero_hongos_locos_asignado,
			                                  contadores_casilleros_especiales, tablero)
			posicion_jugador_1 = tupla_jugador[0]
			contadores_casilleros_especiales = tupla_jugador[1]
			sorteo = 2

		if sorteo == 2 and posicion_jugador_1 < 100:
			interaccion: str = input(f"\n {jugador_2} PRESIONE ENTER PARA JUGAR: ")
			tupla_jugador = turno_jugador(jugador_2, posicion_jugador_2,'J2', serpientes_escaleras, casilleros_cascara_de_banana,
			                                  casilleros_magico, casillero_rushero_asignado,
			                                  casillero_hongos_locos_asignado,
			                                  contadores_casilleros_especiales, tablero)
			posicion_jugador_2 = tupla_jugador[0]
			contadores_casilleros_especiales = tupla_jugador[1]
			sorteo = 1

	if posicion_jugador_1 > posicion_jugador_2:
		print(f"\n Gano el jugador 1, FELICITACIONES {jugador_1}")
	else:
		print(f"\n Gano el jugador 2, FELICITACIONES {jugador_2}")
	return contadores_casilleros_especiales


def mostrarTablero(matriz):
	cadena = ''
	matriz = matriz[::-1]
	for i in range(len(matriz)):
		cadena += '['
		if i % 2 == 0:
			matriz[i] = matriz[i][::-1]
		for j in range(len(matriz[i])):
			cadena += '{:>4s}'.format(str(matriz[i][j]))
		cadena += ']\n'
		if i % 2 == 0:
			matriz[i] = matriz[i][::-1]
	return cadena


def main() -> None:
	salir: str = "4"
	print("\n BIENVENIDO AL JUEGO SERPIENTES Y ESCALERAS")
	print("\n LAS REGLAS SON LAS SIGUIENTES: \n "
	      "Se tiene un tablero con números del 1 al 100,\n"
	      " en el cuál hay serpientes, escaleras y casilleros especiales.\n"
	      " Se juega por turnos, son dos jugadores.\n"
	      " Se tira un dado y se avanza cantidad de casilleros como número que haya salido en el dado,\n"
	      " Si se termina en una escalera; se sube por ella.\n"
	      " Si se termina en una serpiente, se baja por ella.\n"
	      " Casilleros especiales: \n"
	      " Cascara de banana, el jugador cae dos pisos.\n"
	      " Magico, el jugador se transporta a cualquier lugar del tablero.\n"
	      " Rushero, el jugador corre hasta la esquina de la parte del tablero ascendente.\n"
	      " Hongos locos, el jugador corre hasta la esquina de la parte del tablero descendiente.")
	contadores_casilleros_especiales: list = [0, 0, 0, 0, 0,
	                                          0]  # cascara_banana,magico,rushero,hongos,serpiente,escalera
	respuesta_usuario: str = input("\n QUE DESEA REALIZAR?:"
	                               "\n 1. INICIAR PARTIDA"
	                               "\n 2. MOSTRAR ESTADISTICAS DE LOS CASILLEROS"
	                               "\n 3. RESETEAR ESTADISTICAS DE LOS CASILLEROS"
	                               "\n 4. SALIR \n"
	                               "\n")
	while respuesta_usuario != salir:
		if respuesta_usuario == "1":
			contadores_casilleros_especiales = jugar_partida(contadores_casilleros_especiales)
		if respuesta_usuario == '2':
			print("CANTIDAD DE VECES QUE SE PASARON POR CASILLEROS ESPECIALES: \n"
			      "CASILLERO CASCARA DE BANANA:" + str(contadores_casilleros_especiales[0]) +
			      "\nCASILLERO MAGICO:" + str(contadores_casilleros_especiales[1]) +
			      "\nCASILLERO RUSHERO:" + str(contadores_casilleros_especiales[2]) +
			      "\nCASILLERO HONGOS LOCOS:" + str(contadores_casilleros_especiales[3]) +
			      "\nSERPIENTES:" + str(contadores_casilleros_especiales[4]) +
			      "\nESCALERAS:" + str(contadores_casilleros_especiales[5]))
		if respuesta_usuario == '3':
			contadores_casilleros_especiales = [0, 0, 0, 0, 0, 0]
			print("CANTIDAD DE VECES QUE SE PASARON POR CASILLEROS ESPECIALES: \n"
			      "CASILLERO CASCARA DE BANANA:" + str(contadores_casilleros_especiales[0]) +
			      "\nCASILLERO MAGICO:" + str(contadores_casilleros_especiales[1]) +
			      "\nCASILLERO RUSHERO:" + str(contadores_casilleros_especiales[2]) +
			      "\nCASILLERO HONGOS LOCOS:" + str(contadores_casilleros_especiales[3]) +
			      "\nSERPIENTES:" + str(contadores_casilleros_especiales[4]) +
			      "\nESCALERAS:" + str(contadores_casilleros_especiales[5]))
		respuesta_usuario: str = input("\n QUE DESEA REALIZAR?:"
		                               "\n 1. INICIAR PARTIDA"
		                               "\n 2. MOSTRAR ESTADISTICAS DE LOS CASILLEROS"
		                               "\n 3. RESETEAR ESTADISTICAS DE LOS CASILLEROS"
		                               "\n 4. SALIR \n"
		                               "\n")
	if respuesta_usuario == '4':
		print(f"\n GRACIAS POR JUGAR SERPIENTES Y ESCALERAS"
		      "\n HASTA LA PROXIMA")


main()
