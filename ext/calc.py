def simpcalc(num1,num2,op):
	
	res = 0
	
	if op == "+":
		res = num1 + num2
	elif op == "-":
		res = num1 - num2
	elif op == "*":
		res = float(num1) * num2
	elif op == "/":
		if num2 == 0:
			pass
		else:
			res = num1 / num2
	else:
		print "Invalid operator"
	
	if not(isinstance(res,str)):
		print "Invalid."
		return 0
	
	return res