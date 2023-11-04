def main(num):
	num = num-1
	threes = (3 * ((num // 3) * ((num // 3) + 1))) // 2
	fives = (5 * ((num // 5) * ((num // 5) + 1))) // 2
	lcm = (15 * ((num // 15) * ((num // 15) + 1))) // 2
	return threes + fives - lcm

if __name__ == "__main__":
	cases = int(input().strip())
	for num in range(cases):
		num = int(input().strip())
		result = main(num)
		print(result)
