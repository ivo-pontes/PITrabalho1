#!/usr/bin/env python3
# -*- coding: utf-8 -*

from ProcessamentoImagem import ProcessamentoImagem

if __name__ == '__main__':
    print("Processamento de Imagens.")

    pi = ProcessamentoImagem("img/lena-impar.png")

    pi.carregarImagem()
    pi.vizinhoMaisProximoPorReducao()

    print("Fim execução!!")
   