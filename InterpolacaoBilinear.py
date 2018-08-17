#!/usr/bin/env python3
# -*- coding: utf-8 -*

from PIL import Image
import numpy as np

class InterpolacaoBilinear():

	def __init__(self, nome_imagem):
		self.nome_imagem = nome_imagem
		self.m = 0
		self.n = 0
		self.matriz = []

	'''
	Abrindo o arquivo e pegando dimensões MxN
	'''
	def carregarImagem(self):
		img = Image.open(self.nome_imagem)
		img.show()
		#Converte Imagem Object para Matriz
		self.matriz = np.asarray(img.convert('L'))
		#Dimensão M
		self.m = np.size(self.matriz, 1)
		#Dimensão N
		self.n = np.size(self.matriz, 0)
		print("Linhas: {}\nColunas: {}\n".format(self.m, self.n))
		print(self.matriz)


	'''
	Interpolação Bilinear para Redução
	'''
	def paraReducao(self):
		saida = np.zeros([self.m/2,self.n/2])
		m1 = np.size(saida, 1)
		n1 = np.size(saida, 0)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))

		#Ternário em Python
		tamM = self.m-1 if self.m/2 != 0 else self.m
		tamN = self.n-1 if self.n/2 != 0 else self.n

		#Tratando 
		for i in range(0,tamM,2):
			for j in range(0,tamN,2):
				x = self.matriz
				if i < tamM and j < tamN:
					soma = int(x[i][j]) + int(x[i][j+1]) + int(x[i+1][j]) + int(x[i+1][j+1])
					saida[i/2][j/2] = int(soma/4)

											
		print(saida)
		imagem = Image.fromarray(saida)		
		imagem.show()

	'''
	Interpolação Bilinear para Ampliação
	Ainda a fazer, código abaixo é do Vizinho mais próx
	'''
	def paraAmpliacao(self):
		#Criando nova matriz com dimensões M*2xN*2
		saida = np.zeros([self.m*2,self.n*2])
		m1 = np.size(saida, 1)
		n1 = np.size(saida, 0)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))

		for i in range(m1):
			for j in range(n1):
				#Se coluna j é par, então saida[i][j] = matriz[metade][metade]
				if j%2 == 0 and i%2 == 0:
					saida[i][j] = self.matriz[i/2][j/2]
				elif j!=0 and j%2 != 0:#Se é impar, pega valor na saida[i][j-1]
					saida[i][j] = saida[i][j-1]
				#Se linha i	é impar, então recebe valor da linha par
				if i%2 != 0:
					saida[i][j] = saida[i-1][j]
				
				

		print(saida)
		imagem = Image.fromarray(saida)		
		imagem.show()