#!/usr/bin/env python2.4
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:31:57 2018

@author: Paulo Andrade
"""

class Factorial():
	def init(self):
		'''
		Metodo para testear el programa
		'''

		# Obtenemos el numero
		n = self.enterData()
		# Obtenemos el factorial del numero dado
		print "Factorial de "+str(n)+": "+str(self.factorial(n))


	def factorial(self, n):
		'''
		Obtenemos el factorial del numero dad0
		'''

		res = 1 # almacenamos el resultado

		for i in range(1, n + 1):
			res = res * i

		return res


	def enterData(self):
		'''
		Obtiene un dato ingresado por el usuario
		'''

		val = raw_input("Ingrese el numero a verificar: ")

		# verificamos que sea un numero entero
		try :
			val = int(val)
			return val
		except :
			return self.enterData()


# Acceso al programa
if __name__ == "__main__":
	# Instanciamos un objeto
	f = Factorial()
	# Corremos el programa
	f.init()