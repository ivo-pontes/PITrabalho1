#!/usr/bin/env python3
# -*- coding: utf-8 -*

from PIL import Image
import numpy as np


class ProcessamentoImagem():

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
		print(self.matriz)
		#Dimensão M
		self.m = np.size(self.matriz, 1)
		#Dimensão N
		self.n = np.size(self.matriz, 0)
		print("Linhas: {}\nColunas: {}\n".format(self.m, self.n))

	'''
	Vizinho Mais Próximo por redução
	'''
	def vizinhoMaisProximoPorReducao(self):
		saida = np.zeros([self.m/2,self.n/2])
		m1 = np.size(saida, 1)
		n1 = np.size(saida, 0)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))

		#Ternário em Python
		tamM = self.m-1 if self.m/2 != 0 else self.m
		tamN = self.n-1 if self.n/2 != 0 else self.n

		#Tratando 
		for i in range(tamM):
			for j in range(tamN):
				if i%2 == 0 and j%2 == 0:
					saida[i/2][j/2] = self.matriz[i][j]
					
		print(saida)
		imagem = Image.fromarray(saida)		
		imagem.show()

	'''
	Vizinho Mais Próximo por Ampliação
	'''
	def vizinhoMaisProximoPorAmpliacao(self):
		#Criando nova matriz com dimensões M*2xN*2
		saida = np.zeros([self.m*2,self.n*2])
		m1 = np.size(saida, 1)
		n1 = np.size(saida, 0)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))