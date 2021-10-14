def Funccheckdown(l):
	n=len(l)
	for i in range (n-1):
		if l[i]>l[i+1]:
			return False
	return True

def Funccheckup(l):
	n=len(l)
	for i in range (n-1):
		if l[i]<l[i+1]:
			return False
	return True 
			
def Funcmodifarr(l):
	l1=[]	
	for i in range(len(l)):
		if i%4!=0:
			l1.append(l[i])
	return l1

def inputarr(n):
	i=0
	zt=[]
	while i<n:
		try:
			a=float(input("Enter elements of array"))
			zt.append(a)
			i+=1
		except ValueError:
			print("Error 404")
	return zt

try:
	n=int (input("Enter n(lenght of array)"))
	if n<1:
		raise ValueError 
	l = inputarr(n)
	if Funccheckdown(l) or Funccheckup(l):
		pass
	else:
		l=Funcmodifarr(l)

	print(l)
except ValueError:
	print("Incorrect size")

#import random

#def creatematrix(n,m):
#	zt=[]
#	for i in range(n):
#		l=[]
#		for j in range(m):
#			l.append(random.randint(-10,10))
#		zt.append(l)
#	return zt

#def printmatrix(zt):
#	for i in range(len(zt)):
#		print(zt[i])

#def matrixBcreate(zt):
#	n=len(zt)
#	m=len(zt[0])
#	B=[[0 for j in range (m)]for i in range (n)]
#	for i in range (n):
#		for j in range (m):
#			s=0
#			for k in range(i+1):
#				if a[k][j]>0:
#					s+=a[k][j]
#			B[i][j]=s
#	return B
	
#try:
#	n=int (input("Enter value of rows"))
#	m=int (input("Enter value of colums"))
#	if n<=1 or m<=1:
#		raise ValueError
#	print("Generated matrix:")
#	a=creatematrix(n,m)
#	printmatrix(a)
#	b = matrixBcreate(a)
#	print("Created matrix:")
#	printmatrix (b)
#except ValueError:
#	print("Error matrix incorrect size")