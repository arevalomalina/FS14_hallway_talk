def euler_one(number): #finds the sum all multiples of three or five for any given set length.
	running_total = 0
	for i in range(number):
		if i % 3 == 0 or i % 5 == 0:
			running_total = i + running_total
	print running_total

def main():
   euler_one(10)

if __name__ == '__main__':
    main()