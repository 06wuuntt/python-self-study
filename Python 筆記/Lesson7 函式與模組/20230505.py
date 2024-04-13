#範例實作:學生均分蘋果
person=int(input("請輸入學生人數:"))
apple=int(input("請輸入蘋果總數:"))
ret=divmod(apple,person)
print("每個學生可以分得蘋果"+str(ret[0])+"個")
print("蘋果剩"+str(ret[1])+"個")

#延伸練習:生活費
ret1=divmod(10000,350)
print("可維持生活"+str(ret1[0])+"天")
print("生活費剩餘"+str(ret1[1])+"元")

#最大值、最小值、總和、排序
#(1)最大值最小值
print(max(1,3,5,7))
print(max([1,3,5,7]))
print(min(2,4,6,8))
print(min([2,4,6,8]))

#(2)計算總和:sum(串列,[額外數值])
print(sum([1,3,5,7]))
print(sum([1,3,5,7],10))

#(3)排序:sorted(串列[,reverse=True|False])
print(sorted([3,1,7,5]))
print(sorted([3,1,5,7],reverse=True))

#範例實作:總和及排序
innum=0
list=[]
while(innum!=-1):
  innum=int(input("請輸入電費(-1結束):"))
  list.append(innum)
list.pop()
print("共輸入{}個數".format(len(list)))
print("最多電費為:{}".format(max(list)))
print("最少電費為:{}".format(min(list)))
print("電費總和為:{}".format(sum(list)))
print("電費由大到小排序:{}".format(sorted(list,reverse=True)))

#連接與分割字串
#join函式:連接字串.join(串列)
list1=["This","is","a","book"]
print(" ".join(list1))
print("zzz".join(list1))

#split函式:字串.split([分隔字串])
str1="This is a book."
print(str1.split(" "))
str2="Thiszzziszzzazzzbook."
print(str2.split("zzz"))


#檢查起始或結束字串
#startswith函式:字串.startswith(起始字串)
str3="mailto:test@e-happy.com.tw"
print(str3.startswith("mailto"))
print(str3.startswith("to"))

#endswith函式:字串.endswith(結尾字串)
print(str3.endswith(".tw"))
print(str3.endswith(".cn"))


#延伸練習:判斷檔案格式
file=str(input("請輸入圖片檔案名稱:"))
if file.endswith("jpg"):
  print("圖片格式是jpg!")
else:
  print("圖片格式不是jpg!")