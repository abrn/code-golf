# 123 chars

P=print
for x in range(1,101):
	if x%3==0 and x%5==0:P('FizzBuzz')
	elif x%3==0:P('Fizz')
	elif x%5==0:P('Buzz')
	else:P(x)