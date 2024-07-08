driving = input('你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit
age = input('請輸入年齡')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你符合規定')
	else:
		print('你未滿18歲，怎麼可以開車？')
else:
	if age >= 18:
		print('那你可以去考駕照了!')
	else:
		print('你再過幾年就可以去考駕照了')