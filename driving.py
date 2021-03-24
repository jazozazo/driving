age = input("請輸入年齡:")
age = int(age)
country = input("請輸入國家:")
if country == '美國':
    if age >= 16:
    	print("可以考照")
    else:
    	print("不可考照")
elif country == '台灣':
 	if age >= 18:
 	    print("可以考照")
 	else:
 		print("不可考照")
else:
	print("國籍請輸入美國或台灣")