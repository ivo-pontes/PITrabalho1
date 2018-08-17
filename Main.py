#!/usr/bin/env python3
# -*- coding: utf-8 -*

from VizinhoMaisProximo import VizinhoMaisProximo
from InterpolacaoBilinear import InterpolacaoBilinear

if __name__ == '__main__':
	print("Processamento de Imagens.")

	vizinho = VizinhoMaisProximo("img/lena-impar.png")
	vizinho.carregarImagem()
	interpolacao = InterpolacaoBilinear("img/lena-impar.png")
	interpolacao.carregarImagem()

	op = -1

	menuStr = "\n\nDigite 0 para sair.\nMenu:\n"
	menuStr += "Vizinho Mais Próximo\n1 - Por Redução\n2 - Por Ampliação\n"
	menuStr += "Interpolação Bilinear\n3 - Para Redução\n4 - Para Ampliação\n"

	while op != 0:
		op = input(menuStr)
		op = int(op)
		if op == 1:
			vizinho.porReducao()
		elif op == 2:
			vizinho.porAmpliacao()
		elif op == 3:
			interpolacao.paraReducao()
		elif op == 4:
			interpolacao.paraAmpliacao()

	print("Fim execução!!")
