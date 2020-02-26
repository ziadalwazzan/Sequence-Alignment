import random
import numpy as np

def alignStrings(x, y):
	nx = len(x)
	ny = len(y)
	costIndel = 1
	costSub = 2
	S = [ [0 for i in range(nx+1)] for j in range(ny+1)]
	S[0][0] = 0
	for i in range(1,nx+1):
		S[0][i] = i
	for j in range(1,ny+1):
		S[j][0] = j



	for i in range(1,ny+1):
		for j in range(1,nx+1):
			S[i][j] = cost(i, j, S, x, y)
	return S

def cost(i, j, S, x, y):
	costSub = S[i-1][j-1] +2
	costIn= S[i-1 ][j]+1
	costDel= S[i][j-1] +1
	if x[j-1] == y[i-1]:
		costSub-=2
		costIn-= 1
		costDel-= 1
	return min([costSub, costIn, costDel])


def extractAlignment(S,x,y):
	a = []
	i = len(x)
	j = len(y)
	while i>0 or j>0:
		(r, i, j) = optimalOp(i, j, S, x, y)
		a.append(r)
	a.reverse()
	return a
		


def optimalOp(i, j, S, x, y):
	Del= S[j][i-1]
	In = S[j-1 ][i]
	Sub = S[j-1][i-1]
	# change ar based on position.... if im on the edge I cant check for j any more because it will be negative if I check for the del\in because it will check for j-1 which is -1
	if j == 0: #for deletion
		return (1, i-1, j)
	if i == 0:
		return (1, i, j-1)
	if i == 0 and j == 0:
		return (0, i, j)
	ar = [Del, In, Sub]
	minArr = [0 for g in range(3)]
	var = np.random.choice([0, 1, 2], size = 3, replace = False)
	f = 0
	for val in var:
		minArr[val] = ar[f]
		f+=1
	m = min(minArr)
 # arcmin to recieve the index of minimum
	if m == S[j][i-1] and S[j][i-1] != S[j][i]:
		return (1, i-1, j)
	elif m == S[j-1 ][i] and S[j-1][i] != S[j][i]:
		return (1, i, j-1)
	elif m == S[j-1][i-1] and S[j-1][i-1] != S[j][i]:
		return (2, i-1, j-1)

	elif m == S[j][i-1] and S[j][i-1] == S[j][i]:
		return (0, i-1, j)
	elif m == S[j-1 ][i] and S[j-1][i] == S[j][i]:
		return (0, i, j-1)
	else:
		return (0, i-1, j-1)



def commonSubstrings(x, L, a):
	t = False
	z =[]
	indi = 0
	indj = 0
	for i in range(len(a)):
		if a[i] == 0 and t == False:
			indi = i
			t = True
		elif a[i]!=0 and t == True:
			indj = i-1
			if indj-indi >= L:
				z.append((indi, indj-1))
			t = False
		elif a[i] == 0 and i ==len(a)-1 and t == True:
			indj = i
			if indj-indi >= L:
				z.append((indi, indj))
	strings = []
	for point in z:
		(s, e) = point
		strings.append(x[s:e+1])
	print(strings)








def main():

	print('self test:')
	s = alignStrings('grape', 'shape')
	a = extractAlignment(s,'grape', 'shape')
	c = commonSubstrings('grape', 5, a )
	
	print(s)
	print(a)

main()






