def decimal_a_binario(decimal):
	if (decimal == 0) or (decimal == 1):
		return str(decimal)
	else:
		return decimal_a_binario(decimal//2) + str(decimal%2)

print(decimal_a_binario(200))