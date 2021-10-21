#import random

#r = random.randint(1, 3)
#num = 0

#while r != num:
#	num = input('請輸入數字：')
#	num = int(num)
#print('恭喜你猜中了')

import random
start = input('請決定隨機數字範圍開始值；')
end = input('請決定隨機數字範圍結束值：')
start =int(start)
end = int(end)
r = random.randint(start, end)
count = 0

while True:
	count += 1
	num = input('請猜數字：')
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