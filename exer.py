import os
import json

des= "/home/hansi/Desktop"
os.chdir(des)

if not os.path.isdir("Config"):
	os.makedirs("Config")

if not os.path.isfile("Config/dados.json"):
	with open("Config/dados.json", "w+") as arquivo:
		arquivo.write(str([]))

print(os.listdir())

while True:
	print('''
	[1]Listar os jogadores cadastrados
	[2]Cadastrar Jogador
	[3]Apagar dados de jogador
	[4]Editar clube de um jogador''')

	
	jogador = dict()

	escolha = int(input("faca a tua escolha: "))

	if escolha == 1:
		with open("/home/hansi/Desktop/Config/dados.json") as f:
			data= json.load(f)
			print(data)

	elif escolha == 2:

		jogador["Nome"] = str(input("digite o nome do jogador")).upper()
		jogador["Clube"] = str(input("digite o clube que actua")).upper()
		jogador["Nacionalidade"] = str(input("digite a nacionalidade do jogador")).upper()
		 

		with open("/home/hansi/Desktop/Config/dados.json") as f:
			data= json.load(f)
			data.append(jogador.copy()) 
		with open("/home/hansi/Desktop/Config/dados.json", "w") as f:
			data= json.dump(data, f, indent=2)
			print(data)


	elif escolha == 3:
		with open("/home/hansi/Desktop/Config/dados.json") as f:
			dados = json.load(f)
			jogador = str(input("digite o nome do jogador que deseja eliminar: ")).upper()
			for pessoa in dados:
				if pessoa["Nome"] == jogador:
					dados.remove(pessoa)
		
		with open("/home/hansi/Desktop/Config/dados.json", "w") as f:
			json.dump(dados, f)
		print(dados)


	elif escolha == 4:
		with open("/home/hansi/Desktop/Config/dados.json") as f:
			dados = json.load(f)
			jogador = str(input("digite o nome do jogador que deseja editar: ")).upper()
			clube = str(input("digite o novo clube: ")).upper()
			for pessoa in dados:
				if pessoa["Nome"] == jogador:
					pessoa["Clube"] = clube

		with open("/home/hansi/Desktop/Config/dados.json", "w") as f:
			json.dump(dados, f)
		print(dados)


	a = str(input("voce deseja continuar? [S/N]")).upper()[0]
	if a == "N":
		break









	

