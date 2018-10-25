import math
def f(x):
	return (float)(10* math.sin(x) + math.cos(x) - 10*x)
def fl(x):
	return (float)(10*math.cos(x)- math.sin(x)-10)
	
def newton_raphson(a,b,erro,i):
	auxA = a
	auxB = b
	
	passos = ""
	fim = True
	contador = 1
	result = 0
	
	while fim :
		x0 = auxB
		Fx0 = f(x0)	
		Flx0 = fl(x0)
		
		if Flx0 == 0:
			print "erro nr divisao por ZERO"
		
		x1 = (float)(x0 - (Fx0)/Flx0)

		if abs(x1-x0) < erro or contador > i:
			print "Diferenca = " + (str) (abs(x1 - x0))
			print "Erro = " + (str)(erro)
			print "Iteracoes = " + (str)(contador)
			result = x1
			fim = False
	
		auxB = x1
		contador += 1
		passos += (str)(contador) + ".xN = " + (str)(x1) +"\n"
		
	print "RESULTADO: " + (str)(result) + "\n"
	print passos
	return
	

newton_raphson(0.5,1.0,0.0001,100)
