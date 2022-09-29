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