import re

def find(x):
	f = re.findall(r"[^aeiouAEIOU+,-]*([aeiouAEIOU]{2,})*[^aeiouAEIOU+,-]", x)
	ret = '\n'.join(x for x in f if len(x) >= 2)
	if len(ret) == 0:
		return -1
	else:
		return ret

if __name__ == "__main__":
	s = input()
	result = find(s)
	print(result)

