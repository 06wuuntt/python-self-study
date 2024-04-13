#ljust函式:將字串擴充為指定長度，原始字串會置於新字串的左方
#字串.ljust(字串長度[,填充字元])
str1="python"
print(str1.ljust(12))
print(str1.ljust(12,"$"))   #python$$$$$$
print(str1.ljust(4,"$"))    #字串長度小於原始字串長度，無效
# print(str1.ljust(12,"$@"))  #錯誤，填充字元超過一個


#rjust及center函式
print(str1.rjust(12,"$"))   #$$$$$$python
print(str1.center(12,"$"))  #$$$python$$$


#lstrip、rstrip、strip函式
#lstrip:移除字串左方的空白字元
#rstrip:移除字串右方的空白字元
#strip:同時移除字串左右方的空白字元
str2="   I love python.   "
print(str2.rstrip())
print(str2.strip())


#範例實作:以字串排版函式列印成績單
listname=["林大明","陳阿忠","張小英"]
listchinese=[100,87,79]
listmath=[85,88,65]
listenglish=[79,100,8]
print("姓名     座號  國文  數學  英文")
for i in range(0,3):
  print(listname[i].ljust(5),str(i+1).rjust(3),str(listchinese[i]).rjust(5),str(listmath[i]).rjust(5),str(listenglish[i]).rjust(5))


#find函式:尋找搜尋字串在字串的位置
#字串.find(搜尋字串)
str1="I love python."
print(str1.find("o"))      #3
print(str1.find("python"))   #7
print(str1.find("x"))    #沒有此字串，回傳-1

#replace函式:將特定字串替換成另一個字串
#字串.replace(被取代字串, 取代字串[,最大次數])
print(str1.replace("o","&"))  #I l&ve pyth&n.
print(str1.replace("o","&",1)) #I l&ve python.
print(str1.replace("o",""))  #空字串即是刪除此字元，I lve pythn.


#延伸練習:轉換時間格式
time="10:23:41"
time=time.replace(":","點",1)
time=time.replace(":","分",1)
time=time+"秒"
print(time)