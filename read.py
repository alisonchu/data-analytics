data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 100000 == 0:
			print(len(data))
print('檔案讀取完畢, 總共有', len(data), '筆資料')

# 算留言的平均長度
sum_len = 0
for d in data:
	sum_len += len(d)
	
print('留言平均長度為', sum_len / len(data), '個字元')


# 篩選長度在100字元內的留言
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('字元小於100的留言共有', len(new), '筆')
print(new[21740])
