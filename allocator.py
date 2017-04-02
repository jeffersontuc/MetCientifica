#coding: utf-8

import sys

orders = [
['best-fit', 0.20, 0.02], 
['best-fit', 0.55, 0.02], 
['best-fit', 1, 0.02], 
['best-fit', 0.20, 0.1], 
['best-fit', 0.55, 0.1], 
['best-fit', 1, 0.1], 
['best-fit', 0.20, 0.4], 
['best-fit', 0.55, 0.4], 
['best-fit', 1, 0.4],
['worst-fit', 0.20, 0.02], 
['worst-fit', 0.55, 0.02], 
['worst-fit', 1, 0.02], 
['worst-fit', 0.20, 0.1], 
['worst-fit', 0.55, 0.1], 
['worst-fit', 1, 0.1], 
['worst-fit', 0.20, 0.4], 
['worst-fit', 0.55, 0.4], 
['worst-fit', 1, 0.4] ]

def worstFit(blocs, process):
	
	qtdAlocadas = 0
	
	for i in range(len(process)):

		crrIdx = -1
		for j in range(len(blocs)):
			if(blocs[j][0] >= process[i][0] and blocs[j][1] >= process[i][1]):
				if(crrIdx == -1):
					crrIdx = j
				elif(blocs[crrIdx][0] > blocs[j][0]):
					crrIdx = j

		if(crrIdx != -1):
			qtdAlocadas += 1
			blocs[crrIdx][0] -= process[i][0]
			blocs[crrIdx][1] -= process[i][1]

	return (qtdAlocadas, blocs)


def bestFit(blocs, process):
	
	qtdAlocadas = 0
	
	for i in range(len(process)):

		crrIdx = -1
		for j in range(len(blocs)):
			if(blocs[j][0] >= process[i][0] and blocs[j][1] >= process[i][1]):
				if(crrIdx == -1):
					crrIdx = j
				elif(blocs[crrIdx][0] > blocs[j][0]):
					crrIdx = j

		if(crrIdx != -1):
			qtdAlocadas += 1
			blocs[crrIdx][0] -= process[i][0]
			blocs[crrIdx][1] -= process[i][1]

	return (qtdAlocadas, blocs)


def main():
	toFile = ""
	order = sys.argv
	order = [order[1], float(order[2]), float(order[3])]
	if(len(order)):
		orders = [order]

	print orders
	for order in range(len(orders)):
		process = []
		blocs = []
		for i in range(10):
			blocs.append([orders[order][1], orders[order][1]])
		if(orders[order][0] == 'best-fit'):
			if(orders[order][2] == 0.02):
				file = open("task_02.csv")
				linhas = file.readlines()
			elif(orders[order][2] == 0.1):
				file = open("task_01.csv")
				linhas = file.readlines()
			else:
				file = open("task_04.csv")
				linhas = file.readlines()
			for i in range(len(linhas)):
			    linha = linhas[i].strip().split(';')
			    cpu = float(linha[8])
			    memoria = float(linha[9])
			    process.append([cpu, memoria])
			 
			result = bestFit(blocs, process)

			fragmentacaoMemoria = 0
			fragmentacaoCpu = 0

			for fragMen in range(len(result[1])):
				fragmentacaoMemoria += result[1][fragMen][1]

			for fragCpu in range(len(result[1])):
				fragmentacaoCpu += result[1][fragCpu][0]

			toFile += "Recurso requisitado por VM: 0.02" + "\n"
			toFile += "Quantidade de máquinas físicas: 10" + "\n"
			toFile += "Capacidade de CPU: " + str(orders[order][1]) + "\n"
			toFile += "Capacidade de Memória: " + str(orders[order][1]) + "\n"
			toFile += "Algoritmo executado: Best Fit" + "\n"
			toFile += "Fragmentação de CPU: " + str(fragmentacaoCpu) + "\n"
			toFile += "Fragmentação de memória: " + str(fragmentacaoMemoria) + "\n"
			toFile += "Quantidade de requisições " + str(len(process)) + "\n"
			toFile += "Quantidade de VMs alocadas: " + str(result[0]) + "\n"
			toFile += "Quantidade de VMs rejeitadas: " + str(len(process) - result[0]) + "\n"
			toFile += "=================================================================================" + "\n"
			toFile += "\n"

		elif(orders[order][0] == 'worst-fit'):
			if(orders[order][2] == 0.02):
				file = open("task_02.csv")
				linhas = file.readlines()
			elif(orders[order][2] == 0.1):
				file = open("task_01.csv")
				linhas = file.readlines()
			else:
				file = open("task_04.csv")
				linhas = file.readlines()
			for i in range(len(linhas)):
			    linha = linhas[i].strip().split(';')
			    cpu = float(linha[8])
			    memoria = float(linha[9])
			    process.append([cpu, memoria])
			 
			result = bestFit(blocs, process)

			fragmentacaoMemoria = 0
			fragmentacaoCpu = 0

			for fragMen in range(len(result[1])):
				fragmentacaoMemoria += result[1][fragMen][1]

			for fragCpu in range(len(result[1])):
				fragmentacaoCpu += result[1][fragCpu][0]

			toFile += "Recurso requisitado por VM: 0.02" + "\n"
			toFile += "Quantidade de máquinas físicas: 10" + "\n"
			toFile += "Capacidade de CPU: " + str(orders[order][1]) + "\n"
			toFile += "Capacidade de Memória: " + str(orders[order][1]) + "\n"
			toFile += "Algoritmo executado: Worst Fit" + "\n"
			toFile += "Fragmentação de CPU: " + str(fragmentacaoCpu) + "\n"
			toFile += "Fragmentação de memória: " + str(fragmentacaoMemoria) + "\n"
			toFile += "Quantidade de requisições " + str(len(process)) + "\n"
			toFile += "Quantidade de VMs alocadas: " + str(result[0]) + "\n"
			toFile += "Quantidade de VMs rejeitadas: " + str(len(process) - result[0]) + "\n"
			toFile += "=================================================================================" + "\n"
			toFile += "\n"

	arquivo = open("log_result.txt", "a")
	arquivo.writelines(toFile.strip())
	arquivo.close()


main()

