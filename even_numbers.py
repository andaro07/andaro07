l = int(input('Enter lower limit of the range: '))
u = int(input('Enter upper limit of the range: '))

a = []
for i in range(l, u+1):
	if i % 2 == 0:
		a.append(i)
print('The even numbers are {}'.format(a))