def generate_fibonacci():
	fib_seq = [1, 2]
	sum_of_even_values = 0

	i = 0
	while fib_seq[-1] <= 4000000:
		fib_seq.append(fib_seq[i] + fib_seq[i+1])
		i += 1
	
	for i in fib_seq:
		if i % 2 == 0:
			sum_of_even_values += i

	print sum_of_even_values



def main():
	generate_fibonacci()
if __name__ == '__main__':
	main()
