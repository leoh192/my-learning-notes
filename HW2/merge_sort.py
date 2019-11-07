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
            
array = [24, 31, 32, 1, 15, 5, 26]  #測試執行結果
mergesort(array)
print(array)  
