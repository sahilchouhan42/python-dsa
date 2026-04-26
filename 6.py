#FREQUECY MAP/DICTIONARY

#METHOD 1

num = [1, 2, 2, 3, 4, 3]
freq_map={}
x=3

for i in range (0, len(num)):
    if num[i] in freq_map:
        freq_map[num[i]]+=1
    else:
        freq_map[num[i]]=1

#print(freq_map) 
#print(freq_map[num[x]])

#method 2
hash_map={}
n = len(num)

for i in range(0, n):
    hash_map[num[i]] = hash_map.get(num[i], 0)+1

print(hash_map)