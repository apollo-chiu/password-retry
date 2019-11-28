key = 'a123456'
x = 3
while x > 0:
	psw = input('請輸入密碼: ')
	if psw == key:
		print('登入成功!')
		break
	else:
		x = x - 1
		if x > 0:
			print('密碼錯誤! 還有', x, '次機會')