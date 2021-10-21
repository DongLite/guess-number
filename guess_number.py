#import random

#r = random.randint(1, 3)
#num = 0

#while r != num:
#	num = input('請輸入數字：')
#	num = int(num)
#print('恭喜你猜中了')

import random
r = random.randint(1, 100)
count = 0

while True:
	count += 1
	num = input('請猜1~100其中的數字：')
	num = int(num)
	if num == r:
		print('恭喜猜中了！')
		print('共花了', count, '次')
		break
	elif num > r:
		print('---比目標數字還要大---')
	elif num < r:
		print('---比目標數字還要小---')
	print('這是你猜的第', count, '次')
	print('')