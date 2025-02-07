# python 110048224_賴奕叡_hw3.py

#class Record:獲取紀錄(init/get_cat/get_item/get_amount)
class Record:
    """Represent a record."""
    def __init__(self,cat,item,amount):
        self._category=cat
        self._item=item
        self._amount=amount

    @property
    def get_cat(self):
        return self._category
    category=property(lambda self:self.get_cat) #用property把getter包裝起來，有助於外部直接檢視這筆資料
   
    @property
    def get_item(self):
        return self._item
    item=property(lambda self:self.get_item)
    
    @property  
    def get_amount(self):
        return self._amount
    amount=property(lambda self:self.get_amount)

#------------------------------------------------------------------------------
#class Records:管理紀錄(init/add/view/delete/find/save)
#記得檢核每個method前面的註解
class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    file="records.txt"
    import sys
    def __init__(self):
    # 1. Read from 'records.txt' or prompt for initial amount of money.
    # 2. Initialize the attributes (self._records and self._initial_money)
    # from the file or user input.
        try:
            with open(Records.file,mode="r",encoding="utf-8") as fh:
                
                if fh.readline()!="": #第一行有東西代表有記錄
                    fh.seek(0) #測試完要回歸最前面   
                    self._savings=int(fh.readline()) #讀取第一行(最初的存款金額)，第一行非int會跳到例外處理

                    rawdata=fh.readlines() #得到列表、含有"\n"
                    fh.seek(0) #讓位置回歸最前面
                    self._savings=int(fh.readline()) #再讓位置停在第二行開始
                    if rawdata!=[]: #第二行開始有東西的話
                        for data in rawdata:
                            finaldata=data.strip("\n")
                            check=finaldata.split() #分離類別、品項、金額
                            int(check[2]) #試著得到金額並轉為int
                            
                    print("welcome back!")
                else:
                    try:
                        self._savings=int(input("How much money do you have?")) #檔案存在但是空的，輸入新存款
                    except ValueError:
                        print("Invalid value for money. Set to 0 by default.")
                        self._savings=0
                        self._records=[] #輸入非金額時，預設為0
                
                self._records=[] #將檔案資料讀取並寫進records列表中
                for line in fh.readlines():
                    line=line.strip("\n")
                    all_data=line.split(" ")
                    data=Record(all_data[0],all_data[1],all_data[2]) #將category、item、amount分開
                    self._records.append(data)

        except FileNotFoundError: #檔案找不到
            try:
                self._savings=int(input("How much money do you have?")) #檔案找不到就重新輸入存款
                self._records=[] 
            except ValueError:
                print("Invalid value for money. Set to 0 by default.")
                self._savings=0
                self._records=[] #輸入非金額時，預設為0

        except:
            try:
                print("Invalid format in records.txt. Deleting the contents.")
                self._savings=int(input("How much money do you have?"))
                self._records=[]  #第一行有誤、消費紀錄有誤或有非預期的錯誤，檔案重置並重新輸入
            except:
                print("Invalid value for money. Set to 0 by default.")
                self._savings=0
                self._records=[] #輸入非金額時，預設為0
        
    
    def add(self,record,categories):
    # 1. Define the formal parameter so that a string input by the user
    # representing a record can be passed in.
    # 2. Convert the string into a Record instance.
    # 3. Check if the category is valid. For this step, the predefined
    # categories have to be passed in through the parameter.
    # 4. Add the Record into self._records if the category is valid.
        """To test whether there is any wrong format which was typed from the user,if it is correct,the information
        would be saved in the records"""
        self._record=record
        itemANDmoney=self._record.split(',')
        self._categories=categories

        for item_amount in itemANDmoney:    
            if len(item_amount.split())!=3: #若輸入的格式錯誤，給提示語並重來
                print(f"The format of a record should be like this:meal breakfast -50.\nFail to add a record.")
            else:
                try:
                    item_stru=item_amount.split() #分割出項目、品項、金額
                    data=Record(item_stru[0],item_stru[1],item_stru[2])
                    if self._categories.is_category_valid(data.category)==True:
                        int(item_stru[2]) #測試item_money[2]是否可轉換為int
                        self._records.append(data)
                    else:
                        print(f'The specified category is not in the category list.You can check the category list by command "view categories".\nFail to add a record.')
                    
                except ValueError:  #若第二個值輸入不能轉換為int的內容，給提示語並重來
                    print(f"Invalid value for money.\nFail to add a record.")

    def view(self):
    # 1. Print all the records and report the balance.
        """Print all the records and report the balance."""
            
        print(f"Here's your expense and income records:\n\
Categories      Description          Amount\n============== ==================== ======")
        NB=0
        for b in self._records: 
              
            print(f"{b.category:<14} {b.item:<20} {b.amount:<6}")
            NB+=int(b.amount)
                
        print(f"==========================================\n\
Now you have {NB+self._savings} dollars.")

    def delete(self,delete_record):
    # 1. Define the formal parameter.
    # 2. Delete the specified record from self._records.
        """Delete the item that you don't want:the format should be: 'category item price'"""

        self._delete_record=delete_record
        if len(self._delete_record.split())!=3:
            return print(f"Invalid format. Fail to delete a record.\n\
The format of a record should be like this:meal breakfast -50.") 
        
        try: #找的到就刪除，找不到就顯示「查無資料」
            
            for index,rec_item in enumerate(self._records):
                if [rec_item.category,rec_item.item,rec_item.amount]==self._delete_record.split():
                    self._records.pop(index)
                    return
            raise ValueError
        except ValueError:
            print(f"There's no record with {self._delete_record}. Fail to delete a record.")
        
    def find(self,target_categories):
    # 1. Define the formal parameter to accept a non-nested list
    # (returned from find_subcategories)
    # 2. Print the records whose category is in the list passed in
    # and report the total amount of money of the listed records.
        """To print the item and price that you find from the category """
        
        self._target_categories=target_categories
        
        if self._target_categories==[]: #若沒這個類別，就印提示語
            print(f"There isn't a category called {category}")
            
        print(f"Here's your expense and income records under category '{category}':\n\
Categories      Description          Amount\n============== ==================== ======")
        NB=0
        for index,item in enumerate(self._records):  
            if item.category in self._target_categories:
                print(f'{item.category:<14} {item.item:<20} {item.amount:<6}')
                NB+=int(item.amount)
            
        print(f"===========================================\n\
The total amount above is {NB} .")

    def save(self):
    # 1. Write the initial money and all the records to 'records.txt'.
        """Save the record that you insert in this turn to the file"""
        with open(Records.file,mode="w",encoding="utf-8") as fh:
            fh.write(str(self._savings)) #寫入最終存款金額
            for data in self._records:
                fh.write("\n"+str(f"{data.category} {data.item} {data.amount}")) #寫入每個品項的紀錄

#------------------------------------------------------------------------------
#class Categories:管理類別(view/is_category_valid/find_subcategories)
class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self):
        # 1. Initialize self._categories as a nested list.
        """Initialized the categories which restrict the user to insert"""
        all_cat=["expense", ["food", ["meal", "snack", "drink"], "transportation", ["bus", "railway"]], "income", ["salary", "bonus"]]
        self._categories=all_cat

    def view(self):
        # 1. Define the formal parameters so that this method
        #    can be called recursively.
        # 2. Recursively print the categories with indentation.
        # 3. Alternatively, define an inner function to do the recursion.
        "To view the present categories"
        def view_categories(categories,n=0):  #使用遞迴加上縮排與標頭"- "
            for item in categories:
                if type(item)!=list:
                    print(" "*n*2 + "- " +f"{item}")
                else:
                    view_categories(item,n+1)
                
        view_categories(self._categories)

    def is_category_valid(self, category):
        # 1. Define the formal parameters so that a category name can be
        #    passed in and the method can be called recursively.
        # 2. Recursively check if the category name is in self._categories.
        # 3. Alternatively, define an inner function to do the recursion.
        self._category=category
        def check_category_valid(category, categories):
            """To test whether the category the user type is valid in categories which you initialiized,and
            would be called in the add function"""
            if type(categories) in {list,tuple}:
                for a in categories:
                    c=check_category_valid(category,a)
                    if c:
                        return True
            return category==categories
        return check_category_valid(self._category,self._categories)

    def find_subcategories(self,category):
        # 1. Define the formal parameters so that a category name can be
        #    passed in and the method can be called recursively.
        # 2. Recursively find the target category and call the
        #    self._flatten method to get the subcategories into a flat list.
        # 3. Alternatively, define an inner function to do the recursion.
        """Will list the subcategory of the category that you want"""
        self._category=category #str
        
        def find_subcategories_gen(category, categories, found=False): #使用遞迴與生成器來尋找子類別
            if type(categories) == list:  #如果是列表，代表還不是最底層的類別
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories)and type(categories[index + 1]) == list:
                        yield from find_subcategories_gen(category,categories[index+1],True)
                    
            else:
                if categories == category or found==True: #不是列表代表已經是最底層，停止遞迴與生成器的迭代
                    yield categories
        return [i for i in find_subcategories_gen(self._category,self._categories)]
    
    
#------------------------------------------------------------------------------
#執行函式
import sys        

categories = Categories()
records = Records()

while True:
    command = input('\nWhat do you want to do (add / view / delete /view categories /find /exit)? ')
    if command == 'add':
        record = input('Add some expense or income records with category, description, and amount (separate by spaces):\ncat1 desc1 amt1, cat2 desc2 amt2, cat3 desc3 amt3, ...\n')
        records.add(record, categories)
    elif command == 'view':
        records.view()
    elif command == 'delete':
        delete_record = input("Which record do you want to delete? ")
        records.delete(delete_record)
    elif command == 'view categories':
        categories.view()
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        records.find(target_categories)
    elif command == 'exit':
        records.save()
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')
