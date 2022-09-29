data = []
count = 0
with open('reviews.txt', 'r') as f:
	for review in f:
		data.append(review)
		count = count + 1
		if count % 1000 == 0:
		    print(len(data))

print('檔案讀取完畢 總共有', len(data), '筆留言')

total = 0
for d in data:
	total = total + (len(d))
avg = total/len(data)
print('檔案讀取完畢 平均留言長度為', avg)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new),'筆資料留言長度小於100')
print(new[0])
