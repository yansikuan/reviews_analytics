data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		# count += 1
		# if count % 1000 == 0:
		# 	print(len(data))
print('Read finished, there is', len(data), 'in total.')

print(data[0])

#文字计数
wordcount = {}
for d in data:
	words = d.split() # d.split(' ')切不包含空字串
	for word in words:
		if word in wordcount:
			wordcount[word] += 1
		else:
			wordcount[word] = 1 #新增key

# for word in wordcount:
# 	if wordcount[word] > 100:
# 		print(word, wordcount[word])

print(len(wordcount))

while True:
	word = input('Please enter the word you are searching for: ')
	if word == 'q':
		print('Thanks for using this function.')
		break
	if word in wordcount:
		print(word, 'appeared', wordcount[word], 'times')
	else:
		print(word, 'doesnot exist.')




# sum_len = 0
# for d in data:
# 	sum_len += len(d)
# print('average length of comments is', sum_len/len(data))

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('There is',len(new),'comments, which length is smaller than 100')


# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('There is', len(good), 'in total, which mentioned the word good')

#is equivalent to
# good = [d for d in data if 'good' in d]
# print('There is', len(good), 'in total, which mentioned the word good')






