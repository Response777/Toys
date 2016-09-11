plain = 'flag{f5s_RoDah}'
# plain = '|KkJaA?^HHNLrZ'
cipher = ''

levels = [39928,89256,452,86899,30897,90861,70991,137,21594,15314,35422,22497,74842,12865,86173]
ENCODED = [158,196,165,20,202,139,122,250,5,128,49,165,59,41,224]
print(len(levels))
print(len(plain))
print(len(ENCODED))

# print(len(plain))
for i in range(len(levels)):
    cipher+=chr(ord(plain[i])^(levels[i]&255))
#     if(i%4==0):
#         cipher+=chr(ord(plain[i])^26);
#     if(i%4==1):
#         cipher+=chr(ord(plain[i])^39)
#     if(i%4==2):
#         cipher+=chr(ord(plain[i])^10)
#     if(i%4==3):
#         cipher+=chr(ord(plain[i])^45)
print(cipher)
for i in cipher:
    print(ord(i))