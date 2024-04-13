#一維串列宣告
#串列名稱=[元素1,元素2,元素3,.....]
score=[1,2,3,4,5]
print(score)

#多維串列宣告
list1=[["joe","1234"],["mary","abcd"],["David","5678"]]
print(list1[1])
print(list1[1][1])

#讀取串列元素
#串列名稱[索引值]
list2=[1,2,3,4,5]
print(list2[0])

#讀取串列元素範圍
#串列名稱[起始索引:終止索引:間隔值]
print(list2[1:4])      #不包含索引值4

#改變串列元素
#串列名稱[索引值]=元素內容
list2[0]=9
print(list2)

#使用for...迴圈讀取串列
list3=["香蕉","蘋果","橘子"]
for s in list3:
  print(s,end=",")
  print()

#範例實作:利用迴圈配合索引讀取串列元素
list4=["國文","數學","英文"]
scores=[85,79,93]
for r in range(len(scores)):
  print("%s成績:%d分"%(list4[r],scores[r]))