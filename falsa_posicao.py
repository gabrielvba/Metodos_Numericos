import math
def f(x):
	return (float)(10* math.sin(x) + math.cos(x) - 10*x)
def fl(x):
	return (float)(10*math.cos(x)- math.sin(x)-10)

def falsa_posicao(a,b,erro,i):
	auxA = a
	auxB = b
	x0 = auxA
	
	passos = ""
	fim = True
	contador = 1
	result = 0
	
	while fim :
		
		x1 = auxA - (((auxB-auxA)*f(auxA))/(f(auxB)-f(auxA)))

		if abs(x1-x0) < erro or contador > i:
			print "Diferenca = " + (str) (abs(x1 - x0))
			print "Erro = " + (str)(erro)
			print "Iteracoes = " + (str)(contador)
			result = x1
			fim = False
		else:
			if f(auxA)*f(x1) <= 0:
				auxB = x1
			else:
				auxA = x1
				
		x0 = x1
		contador += 1
		passos += (str)(contador) + ".xF = " + (str)(x1) +"\n"
		
	print "RESULTADO: " + (str)(result) + "\n"
	print passos
	return


falsa_posicao(0.5,1.0,0.0001,100)
