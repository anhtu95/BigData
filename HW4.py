from math import exp,ceil,log
import matplotlib.pyplot as plt

def solve() :
	stream = open('./HW4-q4/words_stream.txt','r')
	sigma = exp(-5)
	eps = exp(1)*(10**-4)
	c = []
	for i in range(0,int(ceil(log(1/sigma)))):
		c.append([])
		for j in range(0,int(ceil(exp(1)/eps))):
			c[i].append(0)
	
	params_a = []
	params_b = []
	params = open('./HW4-q4/hash_params.txt','r')
	for param in params:
		tmp = param.split()
		params_a.append(int(tmp[0]))
		params_b.append(int(tmp[1]))		

	#print(params_a)
	#print(params_b)
	
	for x in stream:
		for i in range(0,len(params_a)):
			j = hash_fun(params_a[i],params_b[i],123457,10000,int(x))
			c[i][j] = c[i][j] + 1
	
	count = open('./HW4-q4/counts.txt','r')
	x_axis = []
	y_axis = []	
	for line in count:
		tmp = line.split()
		min_c = 1000000000		
		for i in range(0,len(params_a)):
			hx = hash_fun(params_a[i],params_b[i],123457,10000,int(tmp[0]))
			min_c = min(min_c,hx)
		er = (min_c-int(tmp[1]))/int(tmp[1])
		y_axis.append(er)
		x_axis.append(int(tmp[1])/1407593)
	
	plt.plot(x_axis,y_axis)
	plt.show()	
	
def hash_fun(a,b,p,n_buckets,x):
	y = x % p
	hash_val = (a*y + b) % p
	return hash_val % n_buckets

solve()
