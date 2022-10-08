data = [] #每一筆留言變成一串string存在data清單中
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

good =[]
for d in data:
  if 'good' in d:
      good.append(d)
print('含有good字樣的留言共有', len(good), '筆留言')

###82課堂新增###用字典做文字計數
wc = {} #word count
for d in data: #第d筆在data清單中的留言
    words = d.strip().split(' ') #利用split(' ')將每筆留言（string）分割成清單裝著留言中單字們
    for word in words:
        if word in wc:
            wc[word] = wc[word] + 1
        else:
            wc[word] = 1

for word in wc: #word是字典當中的每一個key 
    if wc[word] > 1000000:
        print(word, wc[word])

while True:
    n = input('請輸入欲查找字： ')
    if n == 'q':
        break
    elif n in wc:
        print(n, wc[n])
    else:
        print('這個字', n,'沒有出現過，請重新輸入欲查詢字')
print('感謝使用本查詢功能')




