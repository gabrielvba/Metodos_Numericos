import math
def f(x):
	return (float)(10* math.sin(x) + math.cos(x) - 10*x)
def fl(x):
	return (float)(10*math.cos(x)- math.sin(x)-10)

def misto_nr_fp(a,b,erro,i):
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
		
		xN = (float)(x0 - (Fx0)/Flx0)

	
		if f(auxA)*f(xN) < 0:
			auxB = xN
		else:
			auxA = xN
		
		xF = (float)(auxA - (((auxB-auxA)*f(auxA))/(f(auxB)-f(auxA))))
		
		passos += (str)(contador) + ".xN = " + (str)(xN) +"\n"
		passos += (str)(contador) + ".xF = " + (str)(xF) +"\n"
		
				
		if abs(xF - xN)< erro or contador > i:
			print "Diferenca = " + (str) (abs(xF - xN))
			print "Erro = " + (str)(erro)
			print "Iteracoes = " + (str)(contador)
			fim = False
			result = (xN + xF)/2	
			
		auxB = xF
		
		
		contador += 1
		
	print "RESULTADO: " + (str)(result) + "\n"
	print passos
	return

misto_nr_fp(0.5,1.0,0.0001,100)
