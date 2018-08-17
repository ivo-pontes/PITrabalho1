#!/usr/bin/env python3
# -*- coding: utf-8 -*

from VizinhoMaisProximo import VizinhoMaisProximo
from InterpolacaoBilinear import InterpolacaoBilinear

if __name__ == '__main__':
    print("Processamento de Imagens.")

    #vizinho = VizinhoMaisProximo("img/lena-impar.png")
    #vizinho.carregarImagem()
    #vizinho.porReducao()
    #vizinho.porAmpliacao()

    interpolacao = InterpolacaoBilinear("img/lena-impar.png")
    interpolacao.carregarImagem()
    #interpolacao.paraReducao()
    interpolacao.paraAmpliacao()

    print("Fim execução!!")
   