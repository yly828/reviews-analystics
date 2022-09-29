data = []
count = 0
with open('reviews.txt', 'r') as f:
	for review in f:
		data.append(review)
		count = count + 1
		if count % 1000 == 0:
		    print(len(data))
