data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 #count = count +1 
        if count % 1000 == 0:
            print(len(data))
print('file has been read','it contains', len(data), 'data(s)')

print(data[0])

# sum_len = 0 
# for d in data:
#     sum_len = sum_len + len(d) # sum_len += len(d)

# print('average comment len is', sum_len / len(data))

# new = []
# for d in data:
#     if len(d) < 100:
#         new.append(d)
# print(len(new), 'comments its length are less than 100 ')
# print(new[1])

# good = []
# for d in data:
#     if 'good' in d:
#         good.append(d)
# print('there are', len(good), 'data(s) mentioning the word good')
# print(good[0])


# good = [d for d in data if 'good' in d] # 進階快解法 list comprehension
# print(good)

# bad = ['bad' in d for d in data]



# text count
wc = {} # word_count
for d in data:
    words = d.split() 
    for word in words:
        if word in wc: 
            wc[word] += 1
        else:
            wc[word] = 1 

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))
print(wc['David'])

while True:
    word = input('Which word is your inquiry: ') 
    if word == 'q':
        break
    if word in wc:
    	print(word,'appear', wc[word], 'times')
    else:
    	print('this word does not exist in the file ' )

print('thanks for using the browser funtion ')








