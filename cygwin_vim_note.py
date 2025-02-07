#用cygwin操作vim文字編輯器

#什麼是shell、bash、vim
"""
shell是連接使用者與電腦核心的殼，目前常用的是叫bash的shell
vim是一種文字編輯器
"""

#cygwin基礎操作
"""
pwd:print working directory.顯示路徑，告訴你正在哪個資料夾

ls:list.列出所有資料夾
    ls -l:列出資料夾與其詳細資料
    ls -lt:以時間排序列出(較長)
    ls -t:以時間排序列出(較短)
    ls -a:列出所有資料夾(連隱藏的都列出)

cd:change directory.變換資料夾
    後面打要移入的資料夾:cd xxx
    若只打cd會將檔案移回home directory

mv:move(or rename).移動或重新命名資料夾
    重新命名:mv file1 file2 (將file1改名為file2)
    移入資料夾:,mv file dir (輸入檔案名&資料夾名 可一次輸入多個檔案名)

rm:remove.刪除檔案(不是刪資料夾)
    刪除檔案:rm file1 (可一次刪除多個)
        rm -i:會在刪除前跟你確認
    刪除資料夾:rmdir dir (資料夾必須已清空)
        rm -r dir:可以一口氣連資料夾的檔案都刪除

cp:copy files.

mkdir:make directory.
    資料夾名稱直接加在後面 ex: mkdir xxx

man:manual page for a command.我還不知道這是啥
"""

#vim:是一種文字編輯器，有自己的語法跟不同的模式
"""
先在cygwin輸入vim xxx.py，開啟檔案進入編輯
要印出來就是 $ python3 xxx.py

command mode:指令模式，所有按鍵都有它的功能，並且不會詮釋成文字指令
    syntax on/off:開啟/關閉語法顏色標示
    :set nu:顯示行數
    :wq:存檔並退出
    shift-zz:存檔並退出
    :q!:不存檔退出
    u:上一步
    
    k、j、h、l:上下左右移動
    w、b:一次跳一個字(前後)
    ctrl-f、ctrl-b:前/後一頁
    ctrl-e、ctrl-y:上/下捲動
    ^、$:那一行的 第一個字/最後一個字
    ctrl-h、ctrl-l:跳到最左上角/跳到螢幕中的最後一行
    %:match，確認左右有沒有對齊(例如檢查括號)

    x:刪除一個字母
    dw:刪除一個字
    db:刪除前一個字
    dd:刪除行
    d2d:刪除幾個行(中間數字可自訂)
    d}:從游標開始刪除整段
    D:從游標開始刪除整行
    p:在下一行貼上(刪除的也會暫存，所以也能貼上)
    P:直接貼上
    y:yank，拷貝的意思，把d換成y即可

insertion mode:詮釋文字指令
    i:進入insert
    esc:回到command mode
"""

#如何進入/退出互動式環境
"""
打python3就會進入互動式環境(或打 -i檔名)
在互動式中打"ctrl+D"就會退出
"""
