# python 110048224_賴奕叡_hw2.py
import sys
#--------------------------------------------------
#檔案初始化
def initialize():

    try:
        with open("records.txt",mode="r",encoding="utf-8") as fh:
            
            if fh.readline()!="": #第一行有東西代表有記錄
                fh.seek(0) #測試完要回歸最前面   
                savings=int(fh.readline()) #讀取第一行(最初的存款金額)，第一行非int會跳到例外處理

                rawdata=fh.readlines() #得到列表、含有"\n"
                fh.seek(0) #讓位置回歸最前面
                savings=int(fh.readline()) #再讓位置停在第二行開始
                if rawdata!=[]: #第二行開始有東西的話
                    for data in rawdata:
                        finaldata=data.strip("\n")
                        check=finaldata.split() #分離品項與金額
                        int(check[1]) #試著得到金額並轉為int
                        
                print("welcome back!")
            else:
                try:
                    savings=int(input("How much money do you have?")) #檔案存在但是空的，輸入新存款
                except ValueError:
                    print("Invalid value for money. Set to 0 by default.")
                    savings=0
                    records=[] #輸入非金額時，預設為0
            
            records=[] #將檔案資料寫進records列表中
            for line in fh.readlines():
                finalline=line.strip("\n") #刪除結尾的換行才不會導致每次輸入資料都多一行
                records.append(finalline)

    except FileNotFoundError: #檔案找不到
        try:
            savings=int(input("How much money do you have?")) #檔案找不到就重新輸入存款
            records=[] 
        except ValueError:
            print("Invalid value for money. Set to 0 by default.")
            savings=0
            records=[] #輸入非金額時，預設為0

    except:
        try:
            print("Invalid format in records.txt. Deleting the contents.")
            savings=int(input("How much money do you have?"))
            records=[]  #第一行有誤、消費紀錄有誤或有非預期的錯誤，檔案重置並重新輸入
        except:
            print("Invalid value for money. Set to 0 by default.")
            savings=0
            records=[] #輸入非金額時，預設為0
    
    return savings,records
#--------------------------------------------------
#add
def add(record):
    itemANDmoney=input("Add some expense or income records with description and amount:\
desc1 amt1, desc2 amt2, desc3 amt3, ...").split(",")
    for item_amount in itemANDmoney:    
        if len(item_amount.split())!=2: #若輸入的格式錯誤，給提示語並重來
            print(f"The format of a record should be like this: breakfast -50.\nFail to add a record.")
            return record
        else:
            try:
                item_money=item_amount.split() #分割出品項與金額
                int(item_money[1]) #測試item_money[1]是否可轉換為int
                record.append(item_amount)
                
            except ValueError:  #若第二個值輸入不能轉換為int的內容，給提示語並重來
                print(f"Invalid value for money.\nFail to add a record.")
                return record
    return record
#--------------------------------------------------
#view
def view(savings,record):
    print(f"This is your account\n\
Description          Amount\n==================== ======")
    NB=0
    for b in record:
        itemANDmoney=b.split()
        print(f"{itemANDmoney[0]:<20} {itemANDmoney[1]:<6}") #對齊上面的"="
        NB+=int(itemANDmoney[1])
    print(f"==================== ======\nNow you have {savings+NB} dollars.")
#--------------------------------------------------
#delete (區分"輸入錯誤&無記錄")
def delete(record):
    del_item=input("Which record do you want to delete?")
    if len(del_item.split())!=2: #指定輸入的內容一定要是「breakfast -50」的型態
        print(f"Invalid format. Fail to delete a record.\n\
The format of a record should be like this: breakfast -50.")
        return record #終止函式執行，先回傳結果
                       
    try:
        for index,rec_item in enumerate(record):
            if rec_item==del_item:
                record.pop(index)
                return record
        raise ValueError
    except ValueError:
        print(f"There's no record with {del_item}. Fail to delete a record.")
        return record
#--------------------------------------------------
#exit:存取並退出
def save(savings,record):
    with open("records.txt",mode="w",encoding="utf-8") as fh:
        fh.write(str(savings))  #寫入最終存款金額
        for item in record:
            fh.write("\n"+str(item)) #寫入每個品項的紀錄
#--------------------------------------------------
# The 5 function definitions here

savings, records = initialize()
while True:
    command = input('\nWhat do you want to do (add / view / delete / exit)? ')
    if command == 'add':
        records = add(records)
    elif command == 'view':
        view(savings, records)
    elif command == 'delete':
        records = delete(records)
    elif command == 'exit':
        save(savings, records)
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')