


def main(num: int) -> int:
	sqr_sums = 0
	sums_sqr = 0

	for idx in range(num+1):
		sqr_sums += idx*idx
		sums_sqr += idx
	return sums_sqr**2 - sqr_sums

if __name__ == "__main__":
	cases = int(input().strip())
	for itr in range(cases):
		num = int(input().strip())
		result = main(num)
		print(result)
