<font face="微软雅黑" size=5  > What is Merge Sort?  
<font face="微软雅黑" size=3  >Merge Sort屬於比較進階的演算法，排序方法也比較複雜一點，基本的步驟可以分為「拆分」與「合併」：
拆分
把大陣列切一半成為兩個小陣列
把切好的兩個小陣列再各自切一半
重複步驟二直到每個小陣列都只剩一個元素
合併
排序兩個只剩一個元素的小陣列並合併
把兩邊排序好的小陣列合併並排序成一個陣列
重複步驟二直到所有小陣列都合併成一個大陣列    
<font face="微软雅黑" size=3  >我一開始的想法是,把array一分為二,先把兩個分割到只剩一個並且先排列.
然後再把兩個排列好的array從index=0相互比較,將比較小的加入第三個array,
也就是最後mergesort出來的array
def mergesort(array):  #定義一個函數
    
    if len(array) <= 1: #array長度<=1則回傳
        
        return array
    
    if len(array) > 1:
        
        middle = len(array) // 2 #將array一分為二
        
        left = array[:middle]    #array從0到middle
        
        right = array[middle:]   #array從miiddle+1到尾巴

        mergesort(left)   #先mergesort兩個array
        mergesort(right)  

        i = 0; # left的index
        j = 0; # 第三個array的index
        k = 0; # right的index
        
        while k < len(right) and i < len(left):
            
            if right[k] < left[i]:   #比較兩個array中的index,比較小的放入第三個array,然後移動到下一個index
                array[j] = right[k]  
                k += 1 
                
            else:
                array[j] = left[i]   #反之
                i += 1

            j += 1                   #放入第三個array之後移動到下一個

        while k < len(right):        #檢查有無遺漏直
            
            array[j] = right[k]
            k += 1
            j += 1

        while i < len(left):
            
            array[j] = left[i]
            i += 1
            j += 1
            
array = [24, 31, 32, 1, 15, 5, 26]
mergesort(array)
print(array)  

參考資料

https://stackoverflow.com/questions/18761766/mergesort-with-python
https://docs.google.com/presentation/d/e/2PACX-1vToxkEzc1H1RT5MI9G941KQFBC7GO_Efn95wTqXLEdr3LDBSNcQb-M46IOC-_RzZih6IBEwwy3rWQuE/pub?start=false&loop=false&delayms=3000&slide=id.g6f5f9558de_0_31
https://pjchender.blogspot.com/2017/09/merge-sort.html
https://emn178.pixnet.net/blog/post/87965707
