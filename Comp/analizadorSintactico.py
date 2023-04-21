import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens,analizador,hash_table,escribir_archivo,symbol_table
from sys import stdin
from analizadorSemantico import *

precedence = (
	('right','IGUAL'),
	('right','IDENTIFICADOR','SI','SI_NO','MUESTRA','ENTRADA'),
	('right','ENTERO','DECIMAL','CADENA','CARACTER'),
	('left','MENOR','MENOR_IGUAL','MAYOR','MAYOR_IGUAL','DIFERENTE','IGUAL_IGUAL'),
	('left','SUMA','RESTA'),
	('left','MULTIPLICACION','DIVISION'),
	('left','PARENTESIS_A','PARENTESIS_C'),
	('left','LLAVE_A','LLAVE_C')
	)
	
def buscar_letra(letra):
    for fila in symbol_table:
        if fila[0] == letra:
            tipo = fila[1]
            return tipo

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def p_inicio(p):
	'''inicio : sentencia'''					#inicio -> sentencia
	#print("Iniciando programa")
	p[0] = inicio(p[1],"iniciando")

def p_sentencia1(p):							#sentencia -> sentencia sentencia
	'''sentencia : sentencia sentencia'''
	#print("Sentencia lista_sentencia")
	p[0] = sentencia1(p[1],p[2],"sentencia de sentencias")

def p_sentencia2(p):
	'''sentencia : comparacion'''
	p[0] = sentencia2(p[1],"comparación")

def p_sentencia3(p):							#sentencia -> op_print;
	'''sentencia : op_print'''
	#print("Sentencia Impresión")
	p[0] = sentencia3(p[1],"Imprimir")

def p_sentencia4(p):							#sentencia -> ciclo
	'''sentencia : ciclo'''
	#print("Sentencia Ciclo")
	p[0] = sentencia4(p[1],"ciclo")

def p_sentencia5(p):							#sentencia -> declarar
	'''sentencia : declarar'''
	#print("Sentencia declaración")
	p[0] = sentencia5(p[1],"declarar")

def p_sentencia6(p):							#sentencia -> asignaEntero
	'''sentencia : asignaEntero'''
	#print("Sentencia asignaEntero")
	p[0] = sentencia6(p[1],"asigna entero")

def p_sentencia7(p):							#sentencia -> asignaFlotante
	'''sentencia : asignaFlotante'''
	#print("Sentencia asignaFlotante")
	p[0] = sentencia7(p[1],"asigna flotante")

def p_sentencia8(p):							#sentencia -> asignaCaracter
	'''sentencia : asignaCaracter'''
	#print("Sentencia asignaCaracter")
	p[0] = sentencia8(p[1],"asigna caracter")

def p_sentencia9(p):							#sentencia -> asignaCadena
	'''sentencia : asignaCadena'''
	#print("Sentencia asignaCadena")
	p[0] = sentencia9(p[1],"asigna cadena")

def p_sentencia10(p):
	'''sentencia : condicional'''				#sentencia -> condicional
	p[0] = sentencia10(p[1],"condional")

def p_declarar1(p):								#declarar -> entero identificador;
	'''declarar : ENTERO IDENTIFICADOR FIN_LINEA'''
	#print("Declaración")
	"""symbol_table.append((p[2], p[1], 1, p.lineno(2)))
	add_value_to_symbol_table(symbol_table, p[2])
	write_to_file(symbol_table)"""
	tipo_letra = buscar_letra(p[2])
	if tipo_letra != "ENTERO":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error en la declaración de la variable '" + p[2] + "', ya has declarado antes esta variable!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	p[0] = declarar1(p[1],p[2],p[3],"declaración")

def p_declarar2(p):								#declarar -> entero identificador = expresion;
	'''declarar : ENTERO IDENTIFICADOR IGUAL expresionEntero FIN_LINEA'''
	#print("Declaración")
	"""symbol_table.append((p[2], p[1], 1, p.lineno(2)))
	add_value_to_symbol_table(symbol_table, p[2])
	write_to_file(symbol_table)"""
	tipo_letra = buscar_letra(p[2])
	if tipo_letra != "ENTERO":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error en la declaración de la variable '" + p[2] + "', ya has declarado antes esta variable!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	p[0] = declarar2(p[1],p[2],p[3],p[4],p[5],"declaración y asignación")

def p_declarar3(p):								#declarar -> decimal identificador;
	'''declarar : DECIMAL IDENTIFICADOR FIN_LINEA'''
	#print("Declaración")
	tipo_letra = buscar_letra(p[2])
	if tipo_letra != "DECIMAL":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error en la declaración de la variable '" + p[2] + "', ya has declarado antes esta variable!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	p[0] = declarar3(p[1],p[2],p[3],"declaración")

def p_declarar4(p):								#declarar -> decimal identificador = expresion;
	'''declarar : DECIMAL IDENTIFICADOR IGUAL expresionFlotante FIN_LINEA'''
	#print("Declaración")
	tipo_letra = buscar_letra(p[2])
	if tipo_letra != "DEECIMAL":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error en la declaración de la variable '" + p[2] + "', ya has declarado antes esta variable!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	p[0] = declarar4(p[1],p[2],p[3],p[4],p[5],"declaración y asignación")

def p_declarar5(p):								#declarar -> caracter identificador;
	'''declarar : CARACTER IDENTIFICADOR FIN_LINEA'''
	#print("Declaración")
	tipo_letra = buscar_letra(p[2])
	if tipo_letra != "CARACTER":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error en la declaración de la variable '" + p[2] + "', ya has declarado antes esta variable!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	p[0] = declarar5(p[1],p[2],p[3],"declaración")

def p_declarar6(p):								#declarar -> caracter identificador = expresion;
	'''declarar : CARACTER IDENTIFICADOR IGUAL CARACTER FIN_LINEA'''
	#print("Declaración")
	tipo_letra = buscar_letra(p[2])
	if tipo_letra != "CARACTER":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error en la declaración de la variable '" + p[2] + "', ya has declarado antes esta variable!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	p[0] = declarar6(p[1],p[2],p[3],p[4],p[5],"declaración y asignación")

def p_declarar7(p):								#declarar -> cadena identificador;
	'''declarar : CADENA IDENTIFICADOR FIN_LINEA'''
	#print("Declaración")
	tipo_letra = buscar_letra(p[2])
	if tipo_letra != "CADENA":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error en la declaración de la variable '" + p[2] + "', ya has declarado antes esta variable!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	p[0] = declarar7(p[1],p[2],p[3],"declaración")

def p_declarar8(p):								#declarar -> cadena identificador = expresion;
	'''declarar : CADENA IDENTIFICADOR IGUAL CADENA FIN_LINEA'''
	#print("Declaración")
	tipo_letra = buscar_letra(p[2])
	if tipo_letra != "CADENA":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error en la declaración de la variable '" + p[2] + "', ya has declarado antes esta variable!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	p[0] = declarar8(p[1],p[2],p[3],p[4],p[5],"declaración y asignación")

def p_asignaEntero(p):							#asignaEntero -> identificador = numero;
	'''asignaEntero : IDENTIFICADOR IGUAL NUMERO FIN_LINEA'''
	#print("Asignación")
	# 
	tipo_letra = buscar_letra(p[1])
	if tipo_letra != "ENTERO":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error en la asignacion, no estás asignando un número entero!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)	
	if(p[1] in hash_table):
		p[0] = asignaEntero(p[1],p[2],p[3],p[4],"Asignación valor entero")

def p_asignaFlotante(p):							#asignaFlotante -> identificador = flotante;
	'''asignaFlotante : IDENTIFICADOR IGUAL FLOTANTE FIN_LINEA'''
	#print("Asignación")
	tipo_letra = buscar_letra(p[1])
	if tipo_letra != "DECIMAL":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error en la declaración, no estás asignando un número decimal!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	if(p[1] in hash_table):
		p[0] = asignaFlotante(p[1],p[2],p[3],p[4],"Asignación valor decimal")

def p_asignaCaracter(p):							#asignaCadena -> identificador = caracter;
	'''asignaCaracter : IDENTIFICADOR IGUAL CARACTER FIN_LINEA'''
	#print("Asignación")
	tipo_letra = buscar_letra(p[1])
	if tipo_letra != "CARACTER":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error en la declaración, no estás asignando un caracter!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	if(p[1] in hash_table):
		p[0] = asignaCaracter(p[1],p[2],p[3],p[4],"Asignación caracter")

def p_asignaCadena(p):							#asignaCadena -> identificador = cadena;
	'''asignaCadena : IDENTIFICADOR IGUAL CADENA FIN_LINEA'''
	#print("Asignación")
	tipo_letra = buscar_letra(p[1])
	if tipo_letra != "CADENA":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error en la declaración, no estás asignando una cadena!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	if(p[1] in hash_table):
		p[0] = asignaCadena(p[1],p[2],p[3],p[4],"Asignación cadena")

def p_terminoEntero1(p):								#termino -> terminoEntero * factorEntero
	'''terminoEntero : terminoEntero MULTIPLICACION factorEntero'''
	#print("Término multiplicación")
	p[0] = terminoEntero1(p[1],p[2],p[3],"Multiplicación de enteros")

def p_terminoEntero2(p):								#termino -> terminoEntero / factorEntero
	'''terminoEntero : terminoEntero DIVISION factorEntero'''
	#print("Término división")
	p[0] = terminoEntero2(p[1],p[2],p[3],"División de enteros")

def p_terminoEntero3(p):								#termino -> factorEntero
	'''terminoEntero : factorEntero'''
	#print("Término factor")
	p[0] = terminoEntero3(p[1],"Factor")

def p_terminoFlotante1(p):								#terminoFlotante -> terminoFlotante * factorFlotante
	'''terminoFlotante : terminoFlotante MULTIPLICACION factorFlotante'''
	#print("Término multiplicación")
	p[0] = terminoFlotante1(p[1],p[2],p[3],"Multiplicación de decimales")

def p_terminoFlotante2(p):								#terminoFlotante -> terminoFlotante / factorFlotante
	'''terminoFlotante : terminoFlotante DIVISION factorFlotante'''
	#print("Término división")
	p[0] = terminoFlotante2(p[1],p[2],p[3],"División de decimales")

def p_terminoFlotante3(p):								#terminoFlotante -> factorFlotante
	'''terminoFlotante : factorFlotante'''
	#print("terminoFlotante factor")
	p[0] = terminoFlotante3(p[1],"Factor")

def p_factorEntero1(p):								#factorEntero1 -> identificador
	'''factorEntero : IDENTIFICADOR'''
	#print("factorEntero1 valor")
	tipo_letra = buscar_letra(p[1])
	if tipo_letra != "ENTERO":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error con el identificador, no es un entero!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	elif tipo_letra == "DECIMAL":
		'''factorFlotante : IDENTIFICADOR'''
		
	p[0] = factorEntero1(p[1],"Identificador")

def p_factorFlotante1(p):								#factorFlotante1 -> identificador
	'''factorFlotante : IDENTIFICADOR'''
	#print("factorFlotante1 valor")
	tipo_letra = buscar_letra(p[1])
	if tipo_letra != "DECIMAL":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error con el identificador, no es un decimal!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	
	p[0] = factorFlotante1(p[1],"Identificador")

def p_factorEntero2(p):								#factorEntero2 -> numero
	'''factorEntero : NUMERO'''
	#print("factorEntero número")
	p[0] = factorEntero2(p[1],"Número")

def p_factorEntero3(p):								#factorEntero3 -> (expresion)
	'''factorEntero : PARENTESIS_A expresionEntero PARENTESIS_C'''
	#print("factorEntero expresión")
	p[0] = factorEntero3(p[1],p[2],p[3],"Expresión")

def p_factorFlotante2(p):								#factorFlotante2 -> (expresion)
	'''factorFlotante : PARENTESIS_A expresionFlotante PARENTESIS_C'''
	#print("factorFlotante expresión")
	p[0] = factorFlotante2(p[1],p[2],p[3],"Expresión")

def p_factorFlotante3(p):								#factorFlotante3 -> flotante
	'''factorFlotante : FLOTANTE'''
	#print("factorFlotante número")
	p[0] = factorFlotante3(p[1],"Flotante")

def p_expresionEntero1(p):							#expresionEntero -> expresionEntero + terminoEntero
	'''expresionEntero : expresionEntero SUMA terminoEntero'''
	#print("expresionEntero suma")
	p[0] = expresionEntero1(p[1],p[2],p[3],"Suma")

def p_expresionEntero2(p):							#expresionEntero -> expresionEntero - terminoEntero
	'''expresionEntero : expresionEntero RESTA terminoEntero'''
	#print("Expresión resta")
	p[0] = expresionEntero2(p[1],p[2],p[3],"Resta")

def p_expresionEntero3(p):							#expresionEntero -> terminoEntero
	'''expresionEntero : terminoEntero'''
	#print("expresionEntero terminoEntero")
	p[0] = expresionEntero3(p[1],"Término")

def p_expresionFlotante1(p):							#expresionFlotante -> expresionFlotante + terminoFlotante
	'''expresionFlotante : expresionFlotante SUMA terminoFlotante'''
	#print("expresionFlotante suma")
	p[0] = expresionFlotante1(p[1],p[2],p[3],"Suma")

def p_expresionFlotante2(p):							#expresionFlotante -> expresionFlotante - terminoFlotante
	'''expresionFlotante : expresionFlotante RESTA terminoFlotante'''
	#print("expresionFlotante resta")
	p[0] = expresionFlotante2(p[1],p[2],p[3],"Resta")

def p_expresionFlotante3(p):							#expresionFlotante -> terminoFlotante
	'''expresionFlotante : terminoFlotante'''
	#print("expresionFlotante terminoFlotante")
	p[0] = expresionFlotante3(p[1],"Término")

def p_op_print1(p):								#op_print -> muestra(identificador);
	'''op_print : MUESTRA PARENTESIS_A IDENTIFICADOR PARENTESIS_C FIN_LINEA'''
	#print("Operación imprimir")
	p[0] = op_print1(p[1],p[2],p[3],p[4],p[5],"Imprimir dato")

def p_op_print2(p):								#op_print -> muestra("cadena");
	'''op_print : MUESTRA PARENTESIS_A CADENA PARENTESIS_C FIN_LINEA'''
	#print("Operación imprimir cadena")
	p[0] = op_print2(p[1],p[2],p[3],p[4],p[5],"Imprimir cadena")

def p_ciclo(p):									#ciclo -> para identificador rango(numero) bloque
	'''ciclo : PARA IDENTIFICADOR RANGO PARENTESIS_A NUMERO PARENTESIS_C bloque'''
	tipo_letra = buscar_letra(p[2])
	if tipo_letra != "ENTERO":
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
		print("Error con el identificador, no es un entero!")
		print(bcolors.FAIL + "###############################################################################################" + bcolors.RESET)
	
	#print("Ciclo para")
	p[0] = ciclo(p[1],p[2],p[3],p[4],p[5],p[6],p[7],"Imprimir cadena")

def p_bloque(p):								#bloque -> {sentencia}
	'''bloque : LLAVE_A sentencia LLAVE_C'''
	#print("Bloque sentencia")
	p[0] = bloque(p[1],p[2],p[3],"Bloque")

def p_condicional1(p):							#condicional -> si(comparacion) bloque
	'''condicional : SI PARENTESIS_A comparacion PARENTESIS_C bloque'''
	#print("Condicional si")
	p[0] = condicional1(p[1],p[2],p[3],p[4],p[5],"condicional si")

def p_condicional2(p):							#condiconal -> si(comparacion) bloque si_no bloque 
	'''condicional : SI PARENTESIS_A comparacion PARENTESIS_C bloque SI_NO bloque'''
	#print("Condicional si_no")
	p[0] = condicional2(p[1],p[2],p[3],p[4],p[5],p[6],p[7],"condicional si_no")

def p_comparacion1(p):							#comparacion -> factorEntero == factorEntero
	'''comparacion : factorEntero IGUAL_IGUAL factorEntero'''
	#print("Comparación igual_igual")
	p[0] = comparacion1(p[1],p[2],p[3],"comparación entero igual_igual")

def p_comparacion2(p):							#comparacion -> factorntero != factorEntero
	'''comparacion : factorEntero DIFERENTE factorEntero'''
	#print("Comparación diferente")
	p[0] = comparacion2(p[1],p[2],p[3],"comparación entero diferente")

def p_comparacion3(p):							#comparacion -> factorEntero > factorEntero
	'''comparacion : factorEntero MAYOR factorEntero'''
	#print("Comparación mayor")
	p[0] = comparacion3(p[1],p[2],p[3],"comparación entero mayor")

def p_comparacion4(p):							#comparacion -> factorEntero < factorEntero
	'''comparacion : factorEntero MENOR factorEntero'''
	#print("Comparación menor")
	p[0] = comparacion4(p[1],p[2],p[3],"comparación entero menor")

def p_comparacion5(p):							#comparacion -> factorEntero >= factorEntero
	'''comparacion : factorEntero MAYOR_IGUAL factorEntero'''
	#print("Comparación mayor_igual")
	p[0] = comparacion5(p[1],p[2],p[3],"comparación entero mayor_igual")

def p_comparacion6(p):							#comparacion -> factorEntero <= factorEntero
	'''comparacion : factorEntero MENOR_IGUAL factorEntero'''
	#print("Comparación menor_igual")
	p[0] = comparacion6(p[1],p[2],p[3],"comparación entero menor_igual")
	
def p_comparacion7(p):							#comparacion -> factorEntero == factorEntero
	'''comparacion : factorFlotante IGUAL_IGUAL factorFlotante'''
	#print("Comparación igual_igual")
	p[0] = comparacion7(p[1],p[2],p[3],"comparación flotante igual_igual")

def p_comparacion8(p):							#comparacion -> factorFlotante != factorFlotante
	'''comparacion : factorFlotante DIFERENTE factorFlotante'''
	#print("Comparación diferente")
	p[0] = comparacion8(p[1],p[2],p[3],"comparación flotante diferente")

def p_comparacion9(p):							#comparacion -> factorFlotante > factorFlotante
	'''comparacion : factorFlotante MAYOR factorFlotante'''
	#print("Comparación mayor")
	p[0] = comparacion9(p[1],p[2],p[3],"comparación flotante mayor")
	
def p_comparacion10(p):							#comparacion -> factorFlotante < factorFlotante
	'''comparacion : factorFlotante MENOR factorFlotante'''
	#print("Comparación menor")
	p[0] = comparacion10(p[1],p[2],p[3],"comparación flotante menor")

def p_comparacion11(p):							#comparacion -> factorFlotante >= factorFlotante
	'''comparacion : factorFlotante MAYOR_IGUAL factorFlotante'''
	#print("Comparación mayor_igual")
	p[0] = comparacion11(p[1],p[2],p[3],"comparación flotante mayor_igual")

def p_comparacion12(p):							#comparacion -> factorFlotante <= factorFlotante
	'''comparacion : factorFlotante MENOR_IGUAL factorFlotante'''
	#print("Comparación menor_igual")
	p[0] = comparacion12(p[1],p[2],p[3],"comparación flotante menor_igual")
	
"""def p_comparacion13(p):							#comparacion -> factorCaracter == factorCaracter
	'''comparacion : factorCaracter IGUAL_IGUAL factorCaracter'''
	#print("Comparación igual_igual")
	p[0] = comparacion13(p[1],p[2],p[3],"comparación caracter igual_igual")

def p_comparacion14(p):							#comparacion -> factorCaracter != factorCaracter
	'''comparacion : factorCaracter DIFERENTE factorCaracter'''
	#print("Comparación diferente")
	p[0] = comparacion14(p[1],p[2],p[3],"comparación caracter diferente")

def p_comparacion15(p):							#comparacion -> factorCaracter > factorCaracter
	'''comparacion : factorCaracter MAYOR factorCaracter'''
	p[0] = comparacion15(p[1],p[2],p[3],"comparación caracter diferente")

def p_comparacion16(p):							#comparacion -> factorCaracter < factorCaracter
	'''comparacion : factorCaracter MENOR factorCaracter'''
	#print("Comparación menor")
	p[0] = comparacion16(p[1],p[2],p[3],"comparación caracter diferente")

def p_comparacion17(p):							#comparacion -> factorCaracter >= factorCaracter
	'''comparacion : factorCaracter MAYOR_IGUAL factorCaracter'''
	#print("Comparación mayor_igual")
	p[0] = comparacion17(p[1],p[2],p[3],"comparación caracter diferente")

def p_comparacion18(p):							#comparacion -> factor <= factorCaracter
	'''comparacion : factorCaracter MENOR_IGUAL factorCaracter'''
	#print("Comparación menor_igual")
	p[0] = comparacion18(p[1],p[2],p[3],"comparación caracter menor_igual")"""

def p_error(p):									#errores
	print("Error de Sintaxis ",p)
	print("Error en la línea "+str(p.lineno))

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print(str(cont) + "." + file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nIngrese el número del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print("Elegiste \"%s\" \n" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

directorio = '/home/damanger/Documents/502/C/Comp/test/'
archivo = buscarFicheros(directorio)
test = directorio + archivo
#codecs permite leer acentos y ñ's
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena,debug=1)

while True:
	tokens=analizador.token() #IMPORTANTE
	escribir_archivo(symbol_table) #IMPORTANTE
	if not tokens: break #IMPORTANTE

#print()
#print(hash_table)