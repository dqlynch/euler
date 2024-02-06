def is_bouncy(n):
	increasing = decreasing = False
	str_n = str(n)
	for i in range(1, len(str_n)):
		if str_n[i] > str_n[i-1]:
			increasing = True
		elif str_n[i] < str_n[i-1]:
			decreasing = True
		if increasing and decreasing:
			return True
	return False

bouncy_count = 0
total_count = 0
n = 1

while True:
	if is_bouncy(n):
		bouncy_count += 1
	total_count += 1
	if bouncy_count / total_count == 0.99:
		break
	n += 1

print("The least number for which the proportion of bouncy numbers is exactly 99% is:", n)

