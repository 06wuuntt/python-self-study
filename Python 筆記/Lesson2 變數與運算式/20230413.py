# 宣告變數
score=90        # 設定score的值為90
fruit='香蕉'    # fruit的資料型態為字串
age,name=18,'林大山'  # 宣告多個變數


# 資料型態
# int:整數  float:小數
string='哈囉世界'   # 字串
# 布林值也有數值，True=1 False=0
num=8+True     # num的值為9


# type判斷資料型態
# type(項目)
print(type(fruit))    # 輸出結果為 <class 'str'>
print(type(score))      # 輸出結果為 <class 'int'>


# 資料型態轉換
print("小明的成績"+str(score))


# 輸出print

# 多個資料以逗號分開
# sep=分隔字元 end=結束字元
print(100,"多吃水果",60,sep=",",end=".")

