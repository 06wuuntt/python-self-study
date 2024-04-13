#input輸入命令
#變數=input([提示字串])
score=input("請輸入數學成績:")
print("得分:{}\n\n".format(score))

#輸入資料型態為字串
#print(score+10)→錯誤
print(int(score)+10)

#範例實作:計算成績總分
chinese=input("請輸入國文成績:")
math=input("請輸入數學成績:")
english=input("請輸入英文成績:")
total=int(chinese)+int(math)+int(english)
print("你的成績總分:{}\n\n".format(total))

#延伸練習
salary=int(input("請輸入薪資金額:"))
prize=int(input("請輸入工作獎金:"))
fee=int(input("請輸入加班費:"))
total1=salary+prize+fee
print("本月時領金額為:%d\n\n"%(total1))

#範例實作:計算梯形面積
up=float(input("請輸入梯形上底長度:"))
down=float(input("請輸入梯形下底長度:"))
height=float(input("請輸入梯形高度:"))
area=(up+down)*height/2
print("梯形的面積為"+str(area))

#範例實作:計算複利本金
money=float(input("請輸入本金存款金額:"))
total=1.02**6*money
print("6年後的存款為:"+str(total) +"\n\n")

#綜合演練:英吋轉換
height=float(input("請問你的身高是幾公分?"))
a=height/2.54
b=int(a)/12
c=a-int(b)*12
print("身高{}公分等於{}呎{}吋".format(int(height),int(b),int(c)))