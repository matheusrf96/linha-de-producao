#coding: utf-8

def linhaProducao(linha, troca, inicio, fim, nmaq, cam):
	c = [[0 for i in xrange(nmaq)]for i in range(2)]
	c[0][0] = inicio[0] + linha[0][0]
	c[1][0] = inicio[1] + linha[1][0]

	if c[0][0] <= c[1][0]:
		aux = "[1][1]"
		cam.append(aux)
	else:
		aux = "[2][1]"
		cam.append(aux)

	for i in range(1, nmaq):
		if c[0][i - 1] + linha[0][1] <= c[1][i - 1] + troca[1][i - 1] + linha[0][i]:
			c[0][i] = c[0][i - 1] + linha[0][1]
		else:
			c[0][i] = c[1][i - 1] + troca[1][i - 1] + linha[0][i]

		if c[1][i - 1] + linha[1][i] <= c[0][i - 1] + troca[0][i - 1] + linha[1][i]:
			c[1][i] = c[1][i - 1] + linha[1][i]
		else:
			c[1][i] = c[0][i - 1] + troca[0][i - 1] + linha[1][i]

		if c[0][i] <= c[1][i]:
			aux = "[1][" + str(i+1) + "]"
			cam.append(aux)
		else:
			aux = "[2][" + str(i+1) + "]"
			cam.append(aux)

	if c[0][nmaq - 1] + fim[0] <= c[1][nmaq - 1] + fim[1]:
		result = c[0][nmaq - 1] + fim[0]
	else:
		result = c[1][nmaq - 1] + fi[1]

	return result

def criarLinhas(linha, troca, inicio, final, nmaq):
	for i in range(2):
		print
		print "Insira o valor inicial da linha ", i+1, ": ",
		aux = input()
		inicio.append(aux)

		print
		for j in range(nmaq):
			print "Insira o tempo gasto pela máquina [", i+1, "][", j+1, "]: ", 
			linha[i][j] = input()

		print
		for j in range(nmaq - 1):
			if i == 0:
				print "Tempo de transição da máquina[", i+1, "][", j+1, "] para a maquina[", i+2, "][", j+2, "]: ",
			else:
				print "Tempo de transição da máquina[", i+1, "][", j+1, "] para a maquina[", i, "][", j+2, "]: ",		
			troca[i][j] = input()

		print
		print "Insira o valor final da linha ", i+1, ": ",
		aux = input()
		final.append(aux)
	print

maquinas = input("Insira o número de máquinas nas linhas: ")
linha = [[0 for i in xrange(maquinas)]for j in range(2)]
troca = [[0 for i in xrange(maquinas)] for j in range(2)]
inicio = []
final = []
caminho = []

criarLinhas(linha,troca, inicio, final, maquinas)

#linha =  [[7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]]
#troca =  [[2, 3, 1, 3, 4], [2, 1, 2, 2, 1]]
#inicio = [2, 4]
#final =  [3, 2]

#print "Linhas: ", linha
#print "Trocas: ", troca
#print "Inicio: ", inicio
#print "Final: ", final

melhorCaso = linhaProducao(linha, troca, inicio, final, maquinas, caminho)
print "Melhor caminho: ", caminho
print "Melhor caso: ", melhorCaso

       
