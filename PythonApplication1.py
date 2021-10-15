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

