import ply.lex as lex
import re
import codecs
import os
import sys

keywords = ['SI','SI_NO','PARA','MUESTRA','ENTRADA','ENTERO','DECIMAL','FALSO','VERDADERO','RANGO','CADENA','CARACTER']
tokens = keywords + ['IDENTIFICADOR','NUMERO','FLOTANTE','SUMA','RESTA','MULTIPLICACION','DIVISION','MAYOR','MENOR','MAYOR_IGUAL','MENOR_IGUAL','DIFERENTE','IGUAL','PARENTESIS_A','PARENTESIS_C','LLAVE_A','LLAVE_C','COMA','FIN_LINEA','IGUAL_IGUAL']

#ER's

t_ignore = r' |\t|\n'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IGUAL = r'='
t_IGUAL_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MENOR = r'<'
t_MAYOR = r'>'
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_PARENTESIS_A = r'\('
t_PARENTESIS_C = r'\)'
t_LLAVE_A = r'\{'
t_LLAVE_C = r'\}'
t_COMA = r','
t_CARACTER = r'\'.{1}\''
t_CADENA = r'\".*\"'
t_FIN_LINEA = r';'

hash_table = {}
aux = []
symbol_table = []

def escribir_archivo(symbol_table):
	with open('tabla_de_simbolos.txt', 'w') as f:
		f.write(str(symbol_table))

def t_IDENTIFICADOR(t):
	r'[a-zA-Z]_?([a-zA-Z0-9]_?)*'
	if t.value.upper() in keywords:
		t.value = t.value.upper()
		t.type = t.value
		aux.append(t.value)
	else:
		if(t.value in hash_table):
			symbol_table[hash_table[t.value][0]][-1].append(t.lineno)
		else:
			index = len(symbol_table)
			symbol_table.append([t.value, aux[-1], "IDENTIFICADOR", [t.lineno]])
			hash_table[t.value] = [index, aux[-1]]
	
	return t

def t_newLine(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMENTARIOS(t):
	r'\#.*'
	pass

def t_FLOTANTE(t):
	r'\d+\.\d'
	symbol_table.append([t.value, aux[-1], "FLOTANTE", t.lineno])
	#hash_table[t.value] = aux[-1], "FLOTANTE", t.lineno
	return t

def t_NUMERO(t):
	r'\d+(\.\d)?'
	symbol_table.append([t.value, aux[-1], "NUMERO", t.lineno])
	#hash_table[t.value] = aux[-1], "NUMERO",  t.lineno
	return t

def t_error(t):
	print(" Caracter ilegal: '%s'" %t.value[0])
	t.lexer.skip(1)

analizador = lex.lex() #IMPORTANTE