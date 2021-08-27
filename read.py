data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count +1 
		if count % 1000 == 0:
			print(len(data))
print('file has been read','it contains', len(data), 'data(s)')

sum_len = 0 
for d in data:
	sum_len = sum_len + len(d) # sum_len += len(d)

print('average comment len is', sum_len / len(data))
