def is_prime(number):
	for i in range(2, number):
		if number % i == 0:
			print "False"
			return 
	print "True"
	return 

def find_prime_factors(number):
	for i in xrange(2, number):
		if number % i == 0:
			quotient = number/i
			quotient_factors = find_prime_factors(quotient)
			quotient_factors.append(i)
			return quotient_factors
	return [number]


def main():
	print sorted(find_prime_factors(600851475143))[-1]

if __name__ == '__main__':
	main()