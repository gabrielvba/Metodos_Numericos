import math
def f(x):
	return (float)(10* math.sin(x) + math.cos(x) - 10*x)
def fl(x):
	return (float)(10*math.cos(x)- math.sin(x)-10)

def bissecao(a,b,erro,i):
	auxA = a
	auxB = b
	
	passos = ""
	fim = True
	contador = 1
	result = 0
	
	while fim :
		
		xB = (auxA+auxB)/2
		
		if f(auxA)*f(xB) <= 0:
				auxB = xB
		else:
				auxA = xB
		
		passos += (str)(contador) + ".xB = " + (str)(xB) +"\n"
				
		if abs(f(xB)) < erro or abs(b-a)< erro or contador > i:
			print "Diferenca = " + (str) (f(xB))
			print "Erro = " + (str)(erro)
			print "Iteracoes = " + (str)(contador)
			fim = False
			result = (xB)
		contador += 1
		
	print "RESULTADO: " + (str)(result) + "\n"
	print passos
	return

bissecao(0.5,1.0,0.0001,100)
