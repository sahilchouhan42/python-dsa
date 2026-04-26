#hasing in python
n=[1,5,6,7,3,1,1,10]
m = [1,4,55,77,8,111, 5, 3, 3]

#bruteful method

for num in m:
    count=0
    for x in n:
        if x==num:
            count+=1
        
#print(count)

#second method 
# hash_list = [0]*11

# for num in n:
#     hash_list[num]+=1

# for num in m:
#     if num<0 or num>10:
#         print(0)
#     else:
#         print(hash_list[num])

#freqmap method
freq_map={}

for i in range (0, len(n)):
    if n[i] in freq_map:
        freq_map[n[i]]+=1
    else:
        freq_map[n[i]]=1

for num in m:
    count = 0
    if num in freq_map:
        count+=freq_map[num]

#print(count)

#character hashing

s = "azyxyyzaaa"
q = ["d", "x", "a", "y"]

hash_list = [0]*26

for ch in s:
    ascii_val=ord(ch)
    index = ascii_val -97
    hash_list[index]+=1

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val-97
    print(hash_list[index])