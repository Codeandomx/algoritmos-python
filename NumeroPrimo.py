#!/usr/bin/env python2.4
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 22:31:57 2018

@author: Paulo Andrade
"""

class NumeroPrimo():
	def init(self):
		'''
		Metodo para testear el programa
		'''

		# Obtenemos el numero
		n = self.enterData()
		# Verificamos si es primo
		if self.isPrime(n) :
			print "Es primo"
		else : 
			print "No es primo"


	def isPrime(self, n):
		'''
		Verificamos si el numero es primo o no
		'''

		# Verificamos si es divisible entre dos
		if n % 2 == 0 : return False

		# Verificamos los numero impares
		for i in range(3, n + 1, 2):
			if (i * i) < n :
				if n % i == 0 :
					return False

		return True


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
	np = NumeroPrimo()
	# Corremos el programa
	np.init()