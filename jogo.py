#encoding=utf-8
from graphics import *
from random import *

altura = 720
largura = 480
janela = GraphWin("Smasher", largura, altura, autoflush = False)
fundo = Image(Point(largura/2,altura/2),"sprite/bg.png")
fundo.draw(janela)
chao = Image(Point(largura/2,altura-60),"sprite/floor.png")
chao.draw(janela)
jogImg = Image(Point(80,500),"sprite/boneco/esq/0.png")
jogImg.draw(janela)
jogSprInd = 0
jogLadBool = 0
jogAtk = False
jogAtkTime = 2
while True:
	arvore = [0,0,0,0,0,0]
	arvoreSpr = [0,0,0,0,0,0]
	arvoreImg = []
	cont = 0
	while(cont <= len(arvore)):
		img = Image(Point(largura/2,60),"sprite/tronco/"+str(randint(0,6))+".png")
		arvoreImg.append(img)
		cont += 1
	if(jogSprInd < 5):
		jogSprInd += 1
	else:
		jogSprInd = 0
	tempo = 95
	tempoJog = 0
	timer = Text(Point(48,170),tempo)
	jogPos = 0
	jogPont = 0
	pontos = Text(Point(48,30),jogPont)
	pontos.setFill('black')
	pontos.setSize(20)
	pontos.draw(janela)
	jogocomecou = False
	imgInicio = Image(Point(largura/2,altura/2),"sprite/ini.png")
	imgInicio.draw(janela)
	while tempo > 0:
		timer.undraw()
		jogImg.undraw()
		time.sleep(0.1)
		if(jogSprInd < 5):
			jogSprInd += 1
		else:
			jogSprInd = 0
		tecla = janela.checkKey()
		if(tecla == 'Left' or tecla == 'Right'):
			imgInicio.undraw()
			if(jogocomecou == False):
				tempo = 95
				jogocomecou = True
			if(tempo + 3 < 95):
				tempo += 3
			else:
				tempo = 95
			jogPont += 5
			if(tecla == "A" or tecla == "a" or tecla == 'Left'):
				jogAtk = True
				jogLadBool = 0
			elif(tecla == "D" or tecla == "d" or tecla == 'Right'):
				jogAtk = True
				jogLadBool = 1
			cont = 0
			while(cont < len(arvore)):
				arvoreImg[cont].undraw()
				cont += 1
			pontos.undraw()
			timer.undraw()	
			arvore[5] = arvore[4]
			arvore[4] = arvore[3]
			arvore[3] = arvore[2]
			arvore[2] = arvore[1]
			arvore[1] = arvore[0]
			arvore[0] = 0
			arvoreSpr[5] = arvoreSpr[4]
			arvoreSpr[4] = arvoreSpr[3]
			arvoreSpr[3] = arvoreSpr[2]
			arvoreSpr[2] = arvoreSpr[1]
			arvoreSpr[1] = arvoreSpr[0]
			arvoreSpr[0] = 0
			tronco = randint(0,3)
			arvore[0] = tronco
			arvoreSpr[0] = randint(0,3)
			cont = 0
			x = largura/2
			y = -60
			while(cont < len(arvore)):
				num = 0
				if(arvore[cont] == 0):
					num = arvoreSpr[cont] + 0
				elif(arvore[cont] == 1):
					num = arvoreSpr[cont] + 4
				elif(arvore[cont] == 2):
					num = arvoreSpr[cont] + 8
				arvoreImg[cont] = Image(Point(x,y),"sprite/tronco/"+str(num)+".png")
				arvoreImg[cont].draw(janela)
				cont += 1
				y += 120
			x = 0
			if(jogPos == 1):
				x = 40
			else:
				x = 80
			if((jogLadBool == 0 and arvore[5] == 1) or (jogLadBool == 1 and arvore[5] == 2)):
				'''print("Morreu")'''
				break
			pontos = Text(Point(48,30),jogPont)
			pontos.setFill('black')
			pontos.setSize(20)
			pontos.draw(janela)
		if(jogocomecou == True):
			if(jogAtkTime <= 0):
				jogAtk = False
				jogAtkTime = 2
			if(jogAtk == True):
				jogAtkTime -= 1
			tempoJog += 1
			tempo -= 2
			'''print(tempo)'''
			timer = Rectangle(Point(1,altura-50),Point(tempo*4.8,altura-60))
			timer.setFill("white")
			timer.draw(janela)
			if(jogAtk == True):
				if(jogLadBool == 0):
					jogImg = Image(Point(180,534),"sprite/boneco/esq/6.png")
				elif(jogLadBool == 1):
					jogImg = Image(Point(300,534),"sprite/boneco/dir/6.png")
			else:
				if(jogLadBool == 0):
					jogImg = Image(Point(80,500),"sprite/boneco/esq/"+str(jogSprInd)+".png")
				elif(jogLadBool == 1):
					jogImg = Image(Point(400,500),"sprite/boneco/dir/"+str(jogSprInd)+".png")
			jogImg.draw(janela)
			janela.flush()
	timer.undraw()
	cont = 0
	while(cont < len(arvore)):
		arvoreImg[cont].undraw()
		cont += 1
	timer.undraw()	
	fim = Image(Point(largura/2,altura/2),"sprite/pont.png")
	fim.draw(janela)
	texto = Text(Point(largura/2,altura/3),jogPont)
	texto.setSize(28)
	texto.setStyle('bold')
	texto.setFill('black')
	texto.draw(janela)
	textoPont = Text(Point(largura/2,altura/4),"Sua Pontuação:")
	textoPont.setSize(28)
	textoPont.setStyle('bold')
	textoPont.setFill('black')
	textoPont.draw(janela)
	textoTecla = Text(Point(largura/2,altura/2),"Aperte 'espaço' para continuar...")
	textoTecla.setSize(15)
	textoTecla.setFill('black')
	textoTecla.draw(janela)
	while(tecla != "space"):
		tecla = janela.getKey()
	fim.undraw()
	texto.undraw()
	textoPont.undraw()
	textoTecla.undraw()