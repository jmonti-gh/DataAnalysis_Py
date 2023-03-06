## Permutation Generator

# bp = input('Elements to permut?  ')
# n = len(bp)
# #lsti = [bp]
# lst = [bp]                  # where to storage permutations
# print(lst)

# np = bp                     # is a copy (like deepcopy)
# for i in range(n - 1):
#     for j in range(n - 2):
#         #print(i, j, j+i+1)   
#         np = np.replace(bp[j+i+1], bp[i])
#         # lsti.append(np)
#         # print(bp[i], bp[j+i+1], np[j+i+1])
#         np = np.replace(bp[i], bp[j+i+1], 1)    # to make only one replacement
#         lst.append(np)

# #print(lsti)
# print(lst)

print()
ln = [5, 6, 3, 4, 1]
print(ln)

cnt = 1
while cnt < len(ln):
    for i in range(len(ln) - 1):
        for j in range(len(ln) - 1):
            if ln[i] > ln[i+1]: ln[i], ln[i+1] = ln[i+1], ln[i]
    cnt += 1
print(ln)
    
print()
tri = 'xyz'
lt1 = []
n = len(tri)

t2 = tri
for i in range(n -1):
    mv_char = t2[i]
    print(mv_char)
    for j in range(n - i - 1):
        nx_char = t2[i+j+1]
        t1 = t2.replace(t2[j+i+1], mv_char, 1)
        t2 = t1.replace(t2[j+i], nx_char, 1)
        print(j, t2)
        lt1.append(t2)
print(lt1)
                  


#cnt = 1
#while cnt < len(tri):
# for i in range(len(tri) - 1):
#     mv_char = tri[i]
#     for j in range(len(tri) - 1):
#         nx_char = tri[j+i+1]
#         tri = tri.replace(tri[j+i+1], mv_char, 1)
#         tri = tri.replace(tri[j+i], nx_char, 1)
#         lt1.append(tri)
#             #if ln[i] > ln[i+1]: ln[i], ln[i+1] = ln[i+1], ln[i]
#             # try:
#             #     char = tri[i+1]
#             #     tri = tri.replace(tri[i+1], tri[i], 1)
#             #     tri = tri.replace(tri[i], char, 1)
#             #     lt1.append(tri)
#             # except:
#             #     pass
#     #cnt += 1
# print(lt1)
    