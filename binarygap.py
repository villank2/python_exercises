def binarygap(n):
	binary = (bin(n))
	li = binary.split('1')[1:]
	print(len(max(li,key=len)))
binarygap(15)