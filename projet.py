def somme(T):
	s=0
	for t in T:
		S+=t
	return S
Data = [1,3,5]

Som = sum(Data)
print("La somme est:",Som)

if Data:
	print("La somme est:", sum(Data))
	print("Le min est:", min(Data))
	print("Le Max est:", max(Data))
else:
	print("liste vide")

