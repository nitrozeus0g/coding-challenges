# 0	1	1	2	3	5 8 13 21	34 55 89 144 233 377 610 987 1597 2584 4181

def main(num):
	if num < 2:
		return 0
	first = 0
	second = 2
	ret = first+second
	while second < num:
		tmp = 4 * second + first
		if tmp > num:
			break
		else:
			first = second
			second = tmp
			ret += second

	return ret

if __name__ == "__main__":
	cases = int(input().strip())
	for num in range(cases):
		num = int(input().strip())
		result = main(num)
		print(result)
