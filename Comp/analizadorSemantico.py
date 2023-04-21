txt = " "
cont = 0

def incrementarContador():
	global cont
	cont +=1
	return("%d" %cont)

class Nodo():
	pass

class inicio(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" " + ident)
		print(ident + "Nodo: " + self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name + "]" + "\n\t"
		txt += id + "->" + son1 + "\n\t"

		return("digraph G {\n\t" + txt + "}")
	
class sentencia1(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()
		
		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id

class sentencia2(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)
		
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id
	
class sentencia3(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)
		
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class sentencia4(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)
		
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class sentencia5(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)
		
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class sentencia6(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)
		
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id
		
class sentencia7(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)
		
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id
	
class sentencia8(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)
		
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class sentencia9(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)
		
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class sentencia10(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)
		
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class declarar1(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class declarar2(Nodo):
	def __init__(self,son1,son2,son3,son4,son5,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4
		self.son5 = son5

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

		if (type(self.son4) == type(tuple())):
			self.son4[0].imprimir(" " + ident)
		else:
			self.son4.imprimir(" "+ ident)

		if (type(self.son5) == type(tuple())):
			self.son5[0].imprimir(" " + ident)
		else:
			self.son5.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		if(type(self.son4) == type(tuple())):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()
		
		if(type(self.son5) == type(tuple())):
			son5 = self.son5[0].traducir()
		else:
			son5 = self.son5.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"
		txt += id + " -> " + son5 + "\n\t"

		return id

class declarar3(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class declarar4(Nodo):
	def __init__(self,son1,son2,son3,son4,son5,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4
		self.son5 = son5

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

		if (type(self.son4) == type(tuple())):
			self.son4[0].imprimir(" " + ident)
		else:
			self.son4.imprimir(" "+ ident)

		if (type(self.son5) == type(tuple())):
			self.son5[0].imprimir(" " + ident)
		else:
			self.son5.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		if(type(self.son4) == type(tuple())):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()
		
		if(type(self.son5) == type(tuple())):
			son5 = self.son5[0].traducir()
		else:
			son5 = self.son5.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"
		txt += id + " -> " + son5 + "\n\t"

		return id

class declarar5(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class declarar6(Nodo):
	def __init__(self,son1,son2,son3,son4,son5,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4
		self.son5 = son5

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

		if (type(self.son4) == type(tuple())):
			self.son4[0].imprimir(" " + ident)
		else:
			self.son4.imprimir(" "+ ident)

		if (type(self.son5) == type(tuple())):
			self.son5[0].imprimir(" " + ident)
		else:
			self.son5.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		if(type(self.son4) == type(tuple())):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()
		
		if(type(self.son5) == type(tuple())):
			son5 = self.son5[0].traducir()
		else:
			son5 = self.son5.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"
		txt += id + " -> " + son5 + "\n\t"

		return id

class declarar7(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class declarar8(Nodo):
	def __init__(self,son1,son2,son3,son4,son5,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4
		self.son5 = son5

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

		if (type(self.son4) == type(tuple())):
			self.son4[0].imprimir(" " + ident)
		else:
			self.son4.imprimir(" "+ ident)

		if (type(self.son5) == type(tuple())):
			self.son5[0].imprimir(" " + ident)
		else:
			self.son5.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		if(type(self.son4) == type(tuple())):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()
		
		if(type(self.son5) == type(tuple())):
			son5 = self.son5[0].traducir()
		else:
			son5 = self.son5.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"
		txt += id + " -> " + son5 + "\n\t"

		return id

class asignaEntero(Nodo):
	def __init__(self,son1,son2,son3,son4,name):
		self.name = name
		self.son1 = son1 
		self.son2 = son2 
		self.son3 = son3
		self.son4 = son4

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)
		
		if (type(self.son4) == type(tuple())):
			self.son4[0].imprimir(" " + ident)
		else:
			self.son4.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		if(type(self.son4) == type(tuple())):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"

		return id

class asignaFlotante(Nodo):
	def __init__(self,son1,son2,son3,son4,name):
		self.name = name
		self.son1 = son1 
		self.son2 = son2 
		self.son3 = son3
		self.son4 = son4

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)
		
		if (type(self.son4) == type(tuple())):
			self.son4[0].imprimir(" " + ident)
		else:
			self.son4.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		if(type(self.son4) == type(tuple())):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"

		return id

class asignaCaracter(Nodo):
	def __init__(self,son1,son2,son3,son4,name):
		self.name = name
		self.son1 = son1 
		self.son2 = son2 
		self.son3 = son3
		self.son4 = son4

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)
		
		if (type(self.son4) == type(tuple())):
			self.son4[0].imprimir(" " + ident)
		else:
			self.son4.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		if(type(self.son4) == type(tuple())):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"

		return id

class asignaCadena(Nodo):
	def __init__(self,son1,son2,son3,son4,name):
		self.name = name
		self.son1 = son1 
		self.son2 = son2 
		self.son3 = son3
		self.son4 = son4

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)
		
		if (type(self.son4) == type(tuple())):
			self.son4[0].imprimir(" " + ident)
		else:
			self.son4.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		if(type(self.son4) == type(tuple())):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"

		return id

class expresionEntero1(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
		
		if(type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" " + ident)
		
		if(type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" " + ident)
	
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()
		
		if(type(self,son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self,son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id
	
class expresionEntero2(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
		
		if(type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" " + ident)
		
		if(type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" " + ident)
	
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()
		
		if(type(self,son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self,son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class expresionEntero3(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
	
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class expresionFlotante1(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
		
		if(type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" " + ident)
		
		if(type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" " + ident)
	
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()
		
		if(type(self,son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self,son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class expresionFlotante2(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
		
		if(type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" " + ident)
		
		if(type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" " + ident)
	
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()
		
		if(type(self,son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self,son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class expresionFlotante3(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
	
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class terminoEntero1(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
		
		if(type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" " + ident)
		
		if(type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" " + ident)
	
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()
		
		if(type(self,son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self,son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class terminoEntero2(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
		
		if(type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" " + ident)
		
		if(type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" " + ident)
	
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()
		
		if(type(self,son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self,son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class terminoEntero3(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
		
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class terminoFlotante1(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
		
		if(type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" " + ident)
		
		if(type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" " + ident)
	
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()
		
		if(type(self,son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self,son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class terminoFlotante2(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
		
		if(type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" " + ident)
		
		if(type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" " + ident)
	
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()
		
		if(type(self,son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self,son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class terminoFlotante3(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
		
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class factorEntero1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class factorEntero2(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class factorEntero3(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)
		
		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)

		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class factorFlotante1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class factorFlotante2(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
		
		if(type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" " + ident)
		
		if(type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" " + ident)
	
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()
		
		if(type(self,son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self,son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class factorFlotante3(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class op_print1(Nodo):
	def __init__(self,son1,son2,son3,son4,son5,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4
		self.son5 = son5

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

		if (type(self.son4) == type(tuple())):
			self.son4[0].imprimir(" " + ident)
		else:
			self.son4.imprimir(" "+ ident)

		if (type(self.son5) == type(tuple())):
			self.son5[0].imprimir(" " + ident)
		else:
			self.son5.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		if(type(self.son4) == type(tuple())):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()
		
		if(type(self.son5) == type(tuple())):
			son5 = self.son5[0].traducir()
		else:
			son5 = self.son5.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"
		txt += id + " -> " + son5 + "\n\t"

		return id

class op_print2(Nodo):
	def __init__(self,son1,son2,son3,son4,son5,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4
		self.son5 = son5

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

		if (type(self.son4) == type(tuple())):
			self.son4[0].imprimir(" " + ident)
		else:
			self.son4.imprimir(" "+ ident)

		if (type(self.son5) == type(tuple())):
			self.son5[0].imprimir(" " + ident)
		else:
			self.son5.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		if(type(self.son4) == type(tuple())):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()
		
		if(type(self.son5) == type(tuple())):
			son5 = self.son5[0].traducir()
		else:
			son5 = self.son5.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"
		txt += id + " -> " + son5 + "\n\t"

		return id

class ciclo(Nodo):
	def __init__(self,son1,son2,son3,son4,son5,son6,son7,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4
		self.son5 = son5
		self.son6 = son6
		self.son7 = son7

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

		if (type(self.son4) == type(tuple())):
			self.son4[0].imprimir(" " + ident)
		else:
			self.son4.imprimir(" "+ ident)

		if (type(self.son5) == type(tuple())):
			self.son5[0].imprimir(" " + ident)
		else:
			self.son5.imprimir(" "+ ident)

		if (type(self.son6) == type(tuple())):
			self.son6[0].imprimir(" " + ident)
		else:
			self.son6.imprimir(" "+ ident)

		if (type(self.son7) == type(tuple())):
			self.son7[0].imprimir(" " + ident)
		else:
			self.son7.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		if(type(self.son4) == type(tuple())):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()
		
		if(type(self.son5) == type(tuple())):
			son5 = self.son5[0].traducir()
		else:
			son5 = self.son5.traducir()

		if(type(self.son6) == type(tuple())):
			son6 = self.son6[0].traducir()
		else:
			son6 = self.son6.traducir()

		if(type(self.son7) == type(tuple())):
			son7 = self.son7[0].traducir()
		else:
			son7 = self.son7.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"
		txt += id + " -> " + son5 + "\n\t"
		txt += id + " -> " + son6 + "\n\t"
		txt += id + " -> " + son7 + "\n\t"

		return id

class bloque(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
	
	def imprimir(self,ident):
		if(type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" " + ident)
		
		if(type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" " + ident)
		
		if(type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" " + ident)
	
	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()
		
		if(type(self,son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()
		
		if(type(self,son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class condicional1(Nodo):
	def __init__(self,son1,son2,son3,son4,son5,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4
		self.son5 = son5

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

		if (type(self.son4) == type(tuple())):
			self.son4[0].imprimir(" " + ident)
		else:
			self.son4.imprimir(" "+ ident)

		if (type(self.son5) == type(tuple())):
			self.son5[0].imprimir(" " + ident)
		else:
			self.son5.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		if(type(self.son4) == type(tuple())):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()
		
		if(type(self.son5) == type(tuple())):
			son5 = self.son5[0].traducir()
		else:
			son5 = self.son5.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"
		txt += id + " -> " + son5 + "\n\t"

		return id

class condicional2(Nodo):
	def __init__(self,son1,son2,son3,son4,son5,son6,son7,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4
		self.son5 = son5
		self.son6 = son6
		self.son7 = son7

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

		if (type(self.son4) == type(tuple())):
			self.son4[0].imprimir(" " + ident)
		else:
			self.son4.imprimir(" "+ ident)

		if (type(self.son5) == type(tuple())):
			self.son5[0].imprimir(" " + ident)
		else:
			self.son5.imprimir(" "+ ident)

		if (type(self.son6) == type(tuple())):
			self.son6[0].imprimir(" " + ident)
		else:
			self.son6.imprimir(" "+ ident)

		if (type(self.son7) == type(tuple())):
			self.son7[0].imprimir(" " + ident)
		else:
			self.son7.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		if(type(self.son4) == type(tuple())):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()
		
		if(type(self.son5) == type(tuple())):
			son5 = self.son5[0].traducir()
		else:
			son5 = self.son5.traducir()

		if(type(self.son6) == type(tuple())):
			son6 = self.son6[0].traducir()
		else:
			son6 = self.son6.traducir()
		
		if(type(self.son7) == type(tuple())):
			son7 = self.son7[0].traducir()
		else:
			son7 = self.son7.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"
		txt += id + " -> " + son5 + "\n\t"
		txt += id + " -> " + son6 + "\n\t"
		txt += id + " -> " + son7 + "\n\t"

		return id

class comparacion1(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion2(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion3(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion4(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion5(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion6(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion7(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion8(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion9(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion10(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion11(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion12(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

""" class comparacion13(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion14(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion15(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion16(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion17(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class comparacion18(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		if (type(self.son1) == type(tuple())):
			self.son1[0].imprimir(" " + ident)
		else:
			self.son1.imprimir(" "+ ident)

		if (type(self.son2) == type(tuple())):
			self.son2[0].imprimir(" " + ident)
		else:
			self.son2.imprimir(" "+ ident)
		
		if (type(self.son3) == type(tuple())):
			self.son3[0].imprimir(" " + ident)
		else:
			self.son3.imprimir(" "+ ident)

	def traducir(self):
		global txt
		id = incrementarContador()

		if(type(self.son1) == type(tuple())):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if(type(self.son2) == type(tuple())):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if(type(self.son3) == type(tuple())):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()
		
		txt += id + "[label= " + self.name + "]\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id """