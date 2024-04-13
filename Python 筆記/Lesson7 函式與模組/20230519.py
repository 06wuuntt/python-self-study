#import模組
import sys as s
print(s.platform)
print(s.maxsize)

import geometry 
result=geometry.distance(1,1,5,5)
print(result)
result=geometry.slope(1,2,5,6)
print(result)

#模組的搜尋路徑
import sys 
print(sys.path)
#調整模組搜尋路徑
sys.path.append("modules")
import geometry
print(geometry.distance(1,1,5,5))

#亂數模組random
import random
#randint函式:由指定範圍內隨機產生一個亂數
#random.randint(起始值,終止值)
for i in range(5):
  print(random.randint(1,10),end=",")
print("\n")
#randrange函式:與randint雷同，只是多了一個遞增值
#random.randrange(起始值,終止值[,遞增值])
for i in range(5):
  print(random.randrange(0,12,2),end=",")
print("\n")
#random函式:隨機產生一個0到1之間的浮點數
#random.random()
print(random.random(),"\n")
#uniform函式:隨機產生一個指定範圍內的浮點數
#random.uniform(起始值,終止值)
print(random.uniform(3,10),"\n")

#隨機練習:骰子遊戲
sum=0
print("你三次擲骰子的點數為",end=" ")
for i in range(3):
  num=random.randint(1,6)
  print(num,end=" ")
  sum=sum+num
print("總點數為:{}".format(sum))


#choice函式:隨機取得一個字元或串列元素
#random.choice(字串或串列)
for i in range(5):
  print(random.choice("abcdefg"), end=",")
print(" ")
for i in range(5):
  print(random.choice([1,2,3,4,5,6,7]),end=",")
print(" ")
#sample函式:和choice雷同，只是sample函式可以取得多個字元
#random.sample(字串或串列,數量)
print(random.sample("abcdefg",3))

#延伸練習:樂透
list1=random.sample(range(0,9),4)
list1.sort()
print("本期大樂透中獎號碼:",end=" ")
for i in range(4):
  if i==3:
    print(str(list1[i]))
  else:
    print(str(list1[i]),end=" ,")

    #時間模組time
import time
#time函式:取得從1970/1/1到現在的秒數(微秒)\
#time.time()
print(time.time())
#localtime函式:取得使用者時區的日期及時間資訊
#time.localtime([時間數值])
print(time.localtime())
time1=time.localtime(time.time())
print(time1.tm_year)
print(time1[2])
#ctime函式:回傳字串格式的現在時間
#time.ctime([時間數值])
print(time.ctime())
print(time.ctime(time.time()))

#範例實作:列印時間函式所有資訊
import time as t
week=["一","二","三","四","五","六","日"]
dst=["無日光節約時間","有日光節約時間"]
time1=t.localtime()
show="現在時刻:中華民國 "+str(int(time1.tm_year)-1911)+"年"
show+=str(time1.tm_mon)+"月"+str(time1.tm_mday)+"日"
show+=str(time1.tm_hour)+"點"+str(time1.tm_min)+"分"
show+=str(time1.tm_sec)+"秒 星期"+week[time1.tm_wday]+"\n"
show+="今天是今年的第 "+str(time1.tm_yday)+"天，此地"+dst[time1.tm_isdst]
print(show)