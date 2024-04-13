#字典:「鍵－值」的方式儲存元素
#建立字典的方式
#(1)字典名稱={鍵1:值1,鍵2:值2,...}
dict1={"香蕉":50,"蘋果":20}
#(2)字典名稱=([[鍵1,值1],[鍵2,值2],...])
dict2=([["橘子",90],["西瓜",80]])
#(3)字典名稱=dict(鍵1=值1,鍵2=值2,...)
dict3=dict(哈密瓜=30,蓮霧=70)    #鍵不能為數字

#字典取值
#字典名稱[鍵]
print(dict3["哈密瓜"])

#get方法取值
#字典名稱.get(鍵[,預設值])
#預設值可有可無
print(dict1.get("蘋果"))    #20
print(dict1.get("鳳梨"))    #None
print(dict1.get("蘋果",80)) #20
print(dict1.get("鳳梨",80)) #80


#範例實作:血型個性查詢
dict1={"A":"內向穩重","B":"外向樂觀","O":"堅強自信","AB":"聰明自然"}
inblood=input("輸入要查詢的血型:")
blood=dict1.get(inblood)
if blood==None:
  print("沒有「{}」血型！".format(inblood))
else:
  print("{}血型的個性為:{}".format(inblood,blood))


#字典維護
#修改字典
#字典名稱[鍵]=值
print(dict1["香蕉"])
dict1["香蕉"]=80
print(dict1["香蕉"])
#若鍵不存在就是新增元素
dict1["鳳梨"]=90
print(dict1["鳳梨"])

#刪除字典
#(1)刪除特定元素
#del 字典名稱[鍵]
del dict1["鳳梨"]
#(2)刪除字典中所有元素
#字典名稱.clear()
dict1.clear()
print(dict1)   #{}
#(3)刪除字典
#del 字典名稱
del dict1

#字典進階操作
#in 功能:檢查鍵是否存在
#鍵 in 字典名稱
dict0={"香蕉":20,"蘋果":50,"橘子":30}
print("香蕉" in dict0)    #True
print("鳳梨" in dict0)    #False


#延伸練習:電器價錢
dict1={'電視':15000,'冰箱':23000,'冷氣':28000}
subject=input("輸入電器名稱:")
if (subject in dict1):
  print(subject+"的價格為"+str(dict1[subject]))
else:
  money=input("輸入電器價格:")
  dict1[subject]=money
  print("字典內容"+str(dict1))


#keys和values用法
#keys():取得字典中所有的鍵
key1=dict0.keys()
print(key1)     #dict_keys(['香蕉', '蘋果', '橘子'])
#values():取得字典中所有的值
value1=dict0.values()
print(value1)   #dict_values([20, 50, 30])


#延伸練習:星座個性1
dict2={"水瓶座":"活潑善變","雙魚座":"迷人保守","白羊座":"天生勇者","金牛座":"熱情敏感"}
listkey=list(dict2.keys())
listvalue=list(dict2.values())
for i in range(0,4):
  print(listkey[i],"的性格特徵為",listvalue[i])
  print()


#items方法
item1=dict0.items()
print(item1)   #dict_items([('香蕉', 20), ('蘋果', 50), ('橘子', 30)])


#延伸練習:星座個性2
dict3={"水瓶座":"活潑善變","雙魚座":"迷人保守","白羊座":"天生勇者","金牛座":"熱情敏感"}
item2=dict3.items()
for star,personaility in item2:
  print("{} 的性格特徵為 {}\n".format(star,personaility))


#setdefault方法
#字典名稱.setdefault(鍵[,預設值])