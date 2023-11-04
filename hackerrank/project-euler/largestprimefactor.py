def main(num):
	i = 2
	while i*i <= num:
		if num%i:
			i += 1
		else:
			num //= i
	return num

if __name__ == "__main__":
	cases = int(input().strip())
	for num in range(cases):
		num = int(input().strip())
		result = main(num)
		print(result)
