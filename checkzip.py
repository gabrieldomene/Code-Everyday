# 39820-2057
# #81r10-3142
list1 = []
zip_code = "39820-2057"
zip_code1 = "81r10-3142"
def check_zip(num):
	x = num
	if len(num) != 10:
		return False
	else:
		for a in num:
			for i in range(0,5):
				if num[i].isdigit() is False:
					return False
			if num[5] != "-":
				return False
			for b in range(6, 10):
				if num[b].isdigit() is False:
					return False
	return True
list1.append(check_zip(zip_code))
list1.append(check_zip(zip_code1))
print("{0}" .format(list1))

