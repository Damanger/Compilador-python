
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightIGUALrightIDENTIFICADORSISI_NOMUESTRAENTRADArightENTERODECIMALCADENACARACTERleftMENORMENOR_IGUALMAYORMAYOR_IGUALDIFERENTEIGUAL_IGUALleftSUMARESTAleftMULTIPLICACIONDIVISIONleftPARENTESIS_APARENTESIS_CleftLLAVE_ALLAVE_CCADENA CARACTER COMA DECIMAL DIFERENTE DIVISION ENTERO ENTRADA FALSO FIN_LINEA FLOTANTE IDENTIFICADOR IGUAL IGUAL_IGUAL LLAVE_A LLAVE_C MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MUESTRA MULTIPLICACION NUMERO PARA PARENTESIS_A PARENTESIS_C RANGO RESTA SI SI_NO SUMA VERDADEROinicio : sentenciasentencia : sentencia sentenciasentencia : comparacionsentencia : op_printsentencia : ciclosentencia : declararsentencia : asignaEnterosentencia : asignaFlotantesentencia : asignaCaractersentencia : asignaCadenasentencia : condicionaldeclarar : ENTERO IDENTIFICADOR FIN_LINEAdeclarar : ENTERO IDENTIFICADOR IGUAL expresionEntero FIN_LINEAdeclarar : DECIMAL IDENTIFICADOR FIN_LINEAdeclarar : DECIMAL IDENTIFICADOR IGUAL expresionFlotante FIN_LINEAdeclarar : CARACTER IDENTIFICADOR FIN_LINEAdeclarar : CARACTER IDENTIFICADOR IGUAL CARACTER FIN_LINEAdeclarar : CADENA IDENTIFICADOR FIN_LINEAdeclarar : CADENA IDENTIFICADOR IGUAL CADENA FIN_LINEAasignaEntero : IDENTIFICADOR IGUAL NUMERO FIN_LINEAasignaFlotante : IDENTIFICADOR IGUAL FLOTANTE FIN_LINEAasignaCaracter : IDENTIFICADOR IGUAL CARACTER FIN_LINEAasignaCadena : IDENTIFICADOR IGUAL CADENA FIN_LINEAterminoEntero : terminoEntero MULTIPLICACION factorEnteroterminoEntero : terminoEntero DIVISION factorEnteroterminoEntero : factorEnteroterminoFlotante : terminoFlotante MULTIPLICACION factorFlotanteterminoFlotante : terminoFlotante DIVISION factorFlotanteterminoFlotante : factorFlotantefactorEntero : IDENTIFICADORfactorFlotante : IDENTIFICADORfactorEntero : NUMEROfactorEntero : PARENTESIS_A expresionEntero PARENTESIS_CfactorFlotante : PARENTESIS_A expresionFlotante PARENTESIS_CfactorFlotante : FLOTANTEexpresionEntero : expresionEntero SUMA terminoEnteroexpresionEntero : expresionEntero RESTA terminoEnteroexpresionEntero : terminoEnteroexpresionFlotante : expresionFlotante SUMA terminoFlotanteexpresionFlotante : expresionFlotante RESTA terminoFlotanteexpresionFlotante : terminoFlotanteop_print : MUESTRA PARENTESIS_A IDENTIFICADOR PARENTESIS_C FIN_LINEAop_print : MUESTRA PARENTESIS_A CADENA PARENTESIS_C FIN_LINEAciclo : PARA IDENTIFICADOR RANGO PARENTESIS_A NUMERO PARENTESIS_C bloquebloque : LLAVE_A sentencia LLAVE_Ccondicional : SI PARENTESIS_A comparacion PARENTESIS_C bloquecondicional : SI PARENTESIS_A comparacion PARENTESIS_C bloque SI_NO bloquecomparacion : factorEntero IGUAL_IGUAL factorEnterocomparacion : factorEntero DIFERENTE factorEnterocomparacion : factorEntero MAYOR factorEnterocomparacion : factorEntero MENOR factorEnterocomparacion : factorEntero MAYOR_IGUAL factorEnterocomparacion : factorEntero MENOR_IGUAL factorEnterocomparacion : factorFlotante IGUAL_IGUAL factorFlotantecomparacion : factorFlotante DIFERENTE factorFlotantecomparacion : factorFlotante MAYOR factorFlotantecomparacion : factorFlotante MENOR factorFlotantecomparacion : factorFlotante MAYOR_IGUAL factorFlotantecomparacion : factorFlotante MENOR_IGUAL factorFlotante'
    
_lr_action_items = {'MUESTRA':([0,2,3,4,5,6,7,8,9,10,11,19,23,25,53,54,56,57,58,59,60,61,62,64,65,66,67,68,71,74,85,88,90,92,105,106,107,108,115,116,117,119,120,121,122,123,126,127,128,129,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-11,-32,-35,14,-48,-30,-49,-50,-51,-52,-53,-54,-31,-55,-56,-57,-58,-59,-33,-34,-18,-12,-14,-16,-20,-21,-22,-23,-42,-43,-19,-13,-15,-17,-46,14,14,-44,-47,-45,]),'PARA':([0,2,3,4,5,6,7,8,9,10,11,19,23,25,53,54,56,57,58,59,60,61,62,64,65,66,67,68,71,74,85,88,90,92,105,106,107,108,115,116,117,119,120,121,122,123,126,127,128,129,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-32,-35,18,-48,-30,-49,-50,-51,-52,-53,-54,-31,-55,-56,-57,-58,-59,-33,-34,-18,-12,-14,-16,-20,-21,-22,-23,-42,-43,-19,-13,-15,-17,-46,18,18,-44,-47,-45,]),'ENTERO':([0,2,3,4,5,6,7,8,9,10,11,19,23,25,53,54,56,57,58,59,60,61,62,64,65,66,67,68,71,74,85,88,90,92,105,106,107,108,115,116,117,119,120,121,122,123,126,127,128,129,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-32,-35,20,-48,-30,-49,-50,-51,-52,-53,-54,-31,-55,-56,-57,-58,-59,-33,-34,-18,-12,-14,-16,-20,-21,-22,-23,-42,-43,-19,-13,-15,-17,-46,20,20,-44,-47,-45,]),'DECIMAL':([0,2,3,4,5,6,7,8,9,10,11,19,23,25,53,54,56,57,58,59,60,61,62,64,65,66,67,68,71,74,85,88,90,92,105,106,107,108,115,116,117,119,120,121,122,123,126,127,128,129,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-32,-35,21,-48,-30,-49,-50,-51,-52,-53,-54,-31,-55,-56,-57,-58,-59,-33,-34,-18,-12,-14,-16,-20,-21,-22,-23,-42,-43,-19,-13,-15,-17,-46,21,21,-44,-47,-45,]),'CARACTER':([0,2,3,4,5,6,7,8,9,10,11,19,23,25,46,53,54,56,57,58,59,60,61,62,64,65,66,67,68,71,74,85,88,90,92,93,105,106,107,108,115,116,117,119,120,121,122,123,126,127,128,129,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-32,-35,22,83,-48,-30,-49,-50,-51,-52,-53,-54,-31,-55,-56,-57,-58,-59,-33,-34,-18,-12,-14,-16,113,-20,-21,-22,-23,-42,-43,-19,-13,-15,-17,-46,22,22,-44,-47,-45,]),'CADENA':([0,2,3,4,5,6,7,8,9,10,11,19,23,25,38,46,53,54,56,57,58,59,60,61,62,64,65,66,67,68,71,74,85,86,88,90,92,105,106,107,108,115,116,117,119,120,121,122,123,126,127,128,129,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-32,-35,17,70,84,-48,-30,-49,-50,-51,-52,-53,-54,-31,-55,-56,-57,-58,-59,-33,-34,-18,109,-12,-14,-16,-20,-21,-22,-23,-42,-43,-19,-13,-15,-17,-46,17,17,-44,-47,-45,]),'IDENTIFICADOR':([0,2,3,4,5,6,7,8,9,10,11,15,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,71,72,73,74,75,76,77,78,79,80,85,88,89,90,91,92,105,106,107,108,115,116,117,119,120,121,122,123,126,127,128,129,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-11,45,47,48,-32,49,50,51,-35,16,54,54,54,54,54,54,62,62,62,62,62,62,69,45,-48,-30,54,-49,-50,-51,-52,-53,-54,-31,62,-55,-56,-57,-58,-59,-33,54,54,-34,62,62,54,54,62,62,-18,-12,54,-14,62,-16,-20,-21,-22,-23,-42,-43,-19,-13,-15,-17,-46,16,16,-44,-47,-45,]),'SI':([0,2,3,4,5,6,7,8,9,10,11,19,23,25,53,54,56,57,58,59,60,61,62,64,65,66,67,68,71,74,85,88,90,92,105,106,107,108,115,116,117,119,120,121,122,123,126,127,128,129,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-32,-35,24,-48,-30,-49,-50,-51,-52,-53,-54,-31,-55,-56,-57,-58,-59,-33,-34,-18,-12,-14,-16,-20,-21,-22,-23,-42,-43,-19,-13,-15,-17,-46,24,24,-44,-47,-45,]),'NUMERO':([0,2,3,4,5,6,7,8,9,10,11,15,19,23,25,26,27,28,29,30,31,46,52,53,54,55,56,57,58,59,60,61,62,64,65,66,67,68,71,72,73,74,77,78,85,88,89,90,92,105,106,107,108,110,115,116,117,119,120,121,122,123,126,127,128,129,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,19,-32,-35,19,19,19,19,19,19,19,81,19,-48,-30,19,-49,-50,-51,-52,-53,-54,-31,-55,-56,-57,-58,-59,-33,19,19,-34,19,19,-18,-12,19,-14,-16,-20,-21,-22,-23,118,-42,-43,-19,-13,-15,-17,-46,19,19,-44,-47,-45,]),'PARENTESIS_A':([0,2,3,4,5,6,7,8,9,10,11,14,15,19,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,71,72,73,74,75,76,77,78,79,80,85,87,88,89,90,91,92,105,106,107,108,115,116,117,119,120,121,122,123,126,127,128,129,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-11,38,15,-32,-35,52,15,55,55,55,55,55,55,63,63,63,63,63,63,15,-48,-30,55,-49,-50,-51,-52,-53,-54,-31,63,-55,-56,-57,-58,-59,-33,55,55,-34,63,63,55,55,63,63,-18,110,-12,55,-14,63,-16,-20,-21,-22,-23,-42,-43,-19,-13,-15,-17,-46,15,15,-44,-47,-45,]),'FLOTANTE':([0,2,3,4,5,6,7,8,9,10,11,15,19,23,25,32,33,34,35,36,37,46,52,53,54,56,57,58,59,60,61,62,63,64,65,66,67,68,71,74,75,76,79,80,85,88,90,91,92,105,106,107,108,115,116,117,119,120,121,122,123,126,127,128,129,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,23,-32,-35,23,23,23,23,23,23,23,82,23,-48,-30,-49,-50,-51,-52,-53,-54,-31,23,-55,-56,-57,-58,-59,-33,-34,23,23,23,23,-18,-12,-14,23,-16,-20,-21,-22,-23,-42,-43,-19,-13,-15,-17,-46,23,23,-44,-47,-45,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,19,23,25,53,54,56,57,58,59,60,61,62,64,65,66,67,68,71,74,85,88,90,92,105,106,107,108,115,116,117,119,120,121,122,127,128,129,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-32,-35,-2,-48,-30,-49,-50,-51,-52,-53,-54,-31,-55,-56,-57,-58,-59,-33,-34,-18,-12,-14,-16,-20,-21,-22,-23,-42,-43,-19,-13,-15,-17,-46,-44,-47,-45,]),'LLAVE_C':([3,4,5,6,7,8,9,10,11,19,23,25,53,54,56,57,58,59,60,61,62,64,65,66,67,68,71,74,85,88,90,92,105,106,107,108,115,116,117,119,120,121,122,126,127,128,129,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-32,-35,-2,-48,-30,-49,-50,-51,-52,-53,-54,-31,-55,-56,-57,-58,-59,-33,-34,-18,-12,-14,-16,-20,-21,-22,-23,-42,-43,-19,-13,-15,-17,-46,129,-44,-47,-45,]),'IGUAL_IGUAL':([12,13,16,19,23,45,71,74,],[26,32,-30,-32,-35,-30,-33,-34,]),'DIFERENTE':([12,13,16,19,23,45,71,74,],[27,33,-30,-32,-35,-30,-33,-34,]),'MAYOR':([12,13,16,19,23,45,71,74,],[28,34,-30,-32,-35,-30,-33,-34,]),'MENOR':([12,13,16,19,23,45,71,74,],[29,35,-30,-32,-35,-30,-33,-34,]),'MAYOR_IGUAL':([12,13,16,19,23,45,71,74,],[30,36,-30,-32,-35,-30,-33,-34,]),'MENOR_IGUAL':([12,13,16,19,23,45,71,74,],[31,37,-30,-32,-35,-30,-33,-34,]),'IGUAL':([16,47,49,50,51,],[46,86,89,91,93,]),'MULTIPLICACION':([19,23,41,42,43,44,45,54,62,71,74,97,98,99,100,101,102,103,104,],[-32,-35,77,79,-26,-29,-30,-30,-31,-33,-34,77,77,79,79,-24,-25,-27,-28,]),'DIVISION':([19,23,41,42,43,44,45,54,62,71,74,97,98,99,100,101,102,103,104,],[-32,-35,78,80,-26,-29,-30,-30,-31,-33,-34,78,78,80,80,-24,-25,-27,-28,]),'PARENTESIS_C':([19,23,39,40,41,42,43,44,45,53,54,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,74,94,97,98,99,100,101,102,103,104,118,],[-32,-35,71,74,-38,-41,-26,-29,-30,-48,-30,-49,-50,-51,-52,-53,-54,-31,-55,-56,-57,-58,-59,95,96,-33,-34,114,-36,-37,-39,-40,-24,-25,-27,-28,124,]),'SUMA':([19,23,39,40,41,42,43,44,45,54,62,71,74,97,98,99,100,101,102,103,104,111,112,],[-32,-35,72,75,-38,-41,-26,-29,-30,-30,-31,-33,-34,-36,-37,-39,-40,-24,-25,-27,-28,72,75,]),'RESTA':([19,23,39,40,41,42,43,44,45,54,62,71,74,97,98,99,100,101,102,103,104,111,112,],[-32,-35,73,76,-38,-41,-26,-29,-30,-30,-31,-33,-34,-36,-37,-39,-40,-24,-25,-27,-28,73,76,]),'FIN_LINEA':([19,23,41,42,43,44,47,49,50,51,54,62,71,74,81,82,83,84,95,96,97,98,99,100,101,102,103,104,109,111,112,113,],[-32,-35,-38,-41,-26,-29,85,88,90,92,-30,-31,-33,-34,105,106,107,108,115,116,-36,-37,-39,-40,-24,-25,-27,-28,117,119,120,121,]),'RANGO':([48,],[87,]),'LLAVE_A':([114,124,125,],[123,123,123,]),'SI_NO':([122,129,],[125,-45,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'sentencia':([0,2,25,123,126,],[2,25,25,126,25,]),'comparacion':([0,2,25,52,123,126,],[3,3,3,94,3,3,]),'op_print':([0,2,25,123,126,],[4,4,4,4,4,]),'ciclo':([0,2,25,123,126,],[5,5,5,5,5,]),'declarar':([0,2,25,123,126,],[6,6,6,6,6,]),'asignaEntero':([0,2,25,123,126,],[7,7,7,7,7,]),'asignaFlotante':([0,2,25,123,126,],[8,8,8,8,8,]),'asignaCaracter':([0,2,25,123,126,],[9,9,9,9,9,]),'asignaCadena':([0,2,25,123,126,],[10,10,10,10,10,]),'condicional':([0,2,25,123,126,],[11,11,11,11,11,]),'factorEntero':([0,2,15,25,26,27,28,29,30,31,52,55,72,73,77,78,89,123,126,],[12,12,43,12,53,56,57,58,59,60,12,43,43,43,101,102,43,12,12,]),'factorFlotante':([0,2,15,25,32,33,34,35,36,37,52,63,75,76,79,80,91,123,126,],[13,13,44,13,61,64,65,66,67,68,13,44,44,44,103,104,44,13,13,]),'expresionEntero':([15,55,89,],[39,39,111,]),'expresionFlotante':([15,63,91,],[40,40,112,]),'terminoEntero':([15,55,72,73,89,],[41,41,97,98,41,]),'terminoFlotante':([15,63,75,76,91,],[42,42,99,100,42,]),'bloque':([114,124,125,],[122,127,128,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> sentencia','inicio',1,'p_inicio','analizadorSintactico.py',33),
  ('sentencia -> sentencia sentencia','sentencia',2,'p_sentencia1','analizadorSintactico.py',38),
  ('sentencia -> comparacion','sentencia',1,'p_sentencia2','analizadorSintactico.py',43),
  ('sentencia -> op_print','sentencia',1,'p_sentencia3','analizadorSintactico.py',47),
  ('sentencia -> ciclo','sentencia',1,'p_sentencia4','analizadorSintactico.py',52),
  ('sentencia -> declarar','sentencia',1,'p_sentencia5','analizadorSintactico.py',57),
  ('sentencia -> asignaEntero','sentencia',1,'p_sentencia6','analizadorSintactico.py',62),
  ('sentencia -> asignaFlotante','sentencia',1,'p_sentencia7','analizadorSintactico.py',67),
  ('sentencia -> asignaCaracter','sentencia',1,'p_sentencia8','analizadorSintactico.py',72),
  ('sentencia -> asignaCadena','sentencia',1,'p_sentencia9','analizadorSintactico.py',77),
  ('sentencia -> condicional','sentencia',1,'p_sentencia10','analizadorSintactico.py',82),
  ('declarar -> ENTERO IDENTIFICADOR FIN_LINEA','declarar',3,'p_declarar1','analizadorSintactico.py',86),
  ('declarar -> ENTERO IDENTIFICADOR IGUAL expresionEntero FIN_LINEA','declarar',5,'p_declarar2','analizadorSintactico.py',99),
  ('declarar -> DECIMAL IDENTIFICADOR FIN_LINEA','declarar',3,'p_declarar3','analizadorSintactico.py',112),
  ('declarar -> DECIMAL IDENTIFICADOR IGUAL expresionFlotante FIN_LINEA','declarar',5,'p_declarar4','analizadorSintactico.py',122),
  ('declarar -> CARACTER IDENTIFICADOR FIN_LINEA','declarar',3,'p_declarar5','analizadorSintactico.py',132),
  ('declarar -> CARACTER IDENTIFICADOR IGUAL CARACTER FIN_LINEA','declarar',5,'p_declarar6','analizadorSintactico.py',142),
  ('declarar -> CADENA IDENTIFICADOR FIN_LINEA','declarar',3,'p_declarar7','analizadorSintactico.py',152),
  ('declarar -> CADENA IDENTIFICADOR IGUAL CADENA FIN_LINEA','declarar',5,'p_declarar8','analizadorSintactico.py',162),
  ('asignaEntero -> IDENTIFICADOR IGUAL NUMERO FIN_LINEA','asignaEntero',4,'p_asignaEntero','analizadorSintactico.py',172),
  ('asignaFlotante -> IDENTIFICADOR IGUAL FLOTANTE FIN_LINEA','asignaFlotante',4,'p_asignaFlotante','analizadorSintactico.py',184),
  ('asignaCaracter -> IDENTIFICADOR IGUAL CARACTER FIN_LINEA','asignaCaracter',4,'p_asignaCaracter','analizadorSintactico.py',195),
  ('asignaCadena -> IDENTIFICADOR IGUAL CADENA FIN_LINEA','asignaCadena',4,'p_asignaCadena','analizadorSintactico.py',206),
  ('terminoEntero -> terminoEntero MULTIPLICACION factorEntero','terminoEntero',3,'p_terminoEntero1','analizadorSintactico.py',217),
  ('terminoEntero -> terminoEntero DIVISION factorEntero','terminoEntero',3,'p_terminoEntero2','analizadorSintactico.py',222),
  ('terminoEntero -> factorEntero','terminoEntero',1,'p_terminoEntero3','analizadorSintactico.py',227),
  ('terminoFlotante -> terminoFlotante MULTIPLICACION factorFlotante','terminoFlotante',3,'p_terminoFlotante1','analizadorSintactico.py',232),
  ('terminoFlotante -> terminoFlotante DIVISION factorFlotante','terminoFlotante',3,'p_terminoFlotante2','analizadorSintactico.py',237),
  ('terminoFlotante -> factorFlotante','terminoFlotante',1,'p_terminoFlotante3','analizadorSintactico.py',242),
  ('factorEntero -> IDENTIFICADOR','factorEntero',1,'p_factorEntero1','analizadorSintactico.py',247),
  ('factorFlotante -> IDENTIFICADOR','factorFlotante',1,'p_factorFlotante1','analizadorSintactico.py',258),
  ('factorEntero -> NUMERO','factorEntero',1,'p_factorEntero2','analizadorSintactico.py',269),
  ('factorEntero -> PARENTESIS_A expresionEntero PARENTESIS_C','factorEntero',3,'p_factorEntero3','analizadorSintactico.py',274),
  ('factorFlotante -> PARENTESIS_A expresionFlotante PARENTESIS_C','factorFlotante',3,'p_factorFlotante2','analizadorSintactico.py',279),
  ('factorFlotante -> FLOTANTE','factorFlotante',1,'p_factorFlotante3','analizadorSintactico.py',284),
  ('expresionEntero -> expresionEntero SUMA terminoEntero','expresionEntero',3,'p_expresionEntero1','analizadorSintactico.py',289),
  ('expresionEntero -> expresionEntero RESTA terminoEntero','expresionEntero',3,'p_expresionEntero2','analizadorSintactico.py',294),
  ('expresionEntero -> terminoEntero','expresionEntero',1,'p_expresionEntero3','analizadorSintactico.py',299),
  ('expresionFlotante -> expresionFlotante SUMA terminoFlotante','expresionFlotante',3,'p_expresionFlotante1','analizadorSintactico.py',304),
  ('expresionFlotante -> expresionFlotante RESTA terminoFlotante','expresionFlotante',3,'p_expresionFlotante2','analizadorSintactico.py',309),
  ('expresionFlotante -> terminoFlotante','expresionFlotante',1,'p_expresionFlotante3','analizadorSintactico.py',314),
  ('op_print -> MUESTRA PARENTESIS_A IDENTIFICADOR PARENTESIS_C FIN_LINEA','op_print',5,'p_op_print1','analizadorSintactico.py',319),
  ('op_print -> MUESTRA PARENTESIS_A CADENA PARENTESIS_C FIN_LINEA','op_print',5,'p_op_print2','analizadorSintactico.py',324),
  ('ciclo -> PARA IDENTIFICADOR RANGO PARENTESIS_A NUMERO PARENTESIS_C bloque','ciclo',7,'p_ciclo','analizadorSintactico.py',329),
  ('bloque -> LLAVE_A sentencia LLAVE_C','bloque',3,'p_bloque','analizadorSintactico.py',340),
  ('condicional -> SI PARENTESIS_A comparacion PARENTESIS_C bloque','condicional',5,'p_condicional1','analizadorSintactico.py',345),
  ('condicional -> SI PARENTESIS_A comparacion PARENTESIS_C bloque SI_NO bloque','condicional',7,'p_condicional2','analizadorSintactico.py',350),
  ('comparacion -> factorEntero IGUAL_IGUAL factorEntero','comparacion',3,'p_comparacion1','analizadorSintactico.py',355),
  ('comparacion -> factorEntero DIFERENTE factorEntero','comparacion',3,'p_comparacion2','analizadorSintactico.py',360),
  ('comparacion -> factorEntero MAYOR factorEntero','comparacion',3,'p_comparacion3','analizadorSintactico.py',365),
  ('comparacion -> factorEntero MENOR factorEntero','comparacion',3,'p_comparacion4','analizadorSintactico.py',370),
  ('comparacion -> factorEntero MAYOR_IGUAL factorEntero','comparacion',3,'p_comparacion5','analizadorSintactico.py',375),
  ('comparacion -> factorEntero MENOR_IGUAL factorEntero','comparacion',3,'p_comparacion6','analizadorSintactico.py',380),
  ('comparacion -> factorFlotante IGUAL_IGUAL factorFlotante','comparacion',3,'p_comparacion7','analizadorSintactico.py',385),
  ('comparacion -> factorFlotante DIFERENTE factorFlotante','comparacion',3,'p_comparacion8','analizadorSintactico.py',390),
  ('comparacion -> factorFlotante MAYOR factorFlotante','comparacion',3,'p_comparacion9','analizadorSintactico.py',395),
  ('comparacion -> factorFlotante MENOR factorFlotante','comparacion',3,'p_comparacion10','analizadorSintactico.py',400),
  ('comparacion -> factorFlotante MAYOR_IGUAL factorFlotante','comparacion',3,'p_comparacion11','analizadorSintactico.py',405),
  ('comparacion -> factorFlotante MENOR_IGUAL factorFlotante','comparacion',3,'p_comparacion12','analizadorSintactico.py',410),
]
