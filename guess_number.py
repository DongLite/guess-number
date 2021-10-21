#import random

#r = random.randint(1, 3)
#num = 0

#while r != num:
#	num = input('請輸入數字：')
#	num = int(num)
#print('恭喜你猜中了')

import random
r = random.randint(1, 100)

while True:
	num = input('請猜1~100其中的數字：')
	num = int(num)
	if num == r:
		print('恭喜猜中了！')
		break
	elif num > r:
		print('比目標數字還要大')
	elif num < r:
		print('比目標數字還要小')