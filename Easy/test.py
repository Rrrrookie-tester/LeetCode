"""
@Project: pythonProject   
@Description: TODO          
@Time:2021/6/4 14:31       
@Author:zexin                
 
"""
# from collections import Counter
#
# # str = "ashjkdhajklshdjk"
# # list_str = list(str)
# # list_str.sort()
# # print(list_str)
# if isinstance(4/2, int):
#     print("111")
# else:
#     print("00")
# print(4/2)

list1 = [7864, 284, 347, 7732, 8498]
list2 = []
res = ''
for i in list1:
    list2.append(str(i))
list2.sort(reverse=True)
for i in list2:
    res = res + i
print(res)