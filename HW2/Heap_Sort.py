def heapify(arr,n,i):#將list轉成heap
    
    largest = i      #設i的數值為最大
    left = 2*i+1     #左邊node的位置
    right = 2*i+2    #右邊node的位置
    
    if n <= 1:       #如果array長度<=1,則回傳
        
        return arr
    
    if left < n and arr[i] < arr[left]:   #root的數值要比child大,如果child比較大,則設child為最大
        largest = left
        
    if right < n and arr[i] < arr[right]: #和上述相同
        largest = right
        
    if largest != i : 
        arr[i], arr[largest] = arr[largest], arr[i]
        
        heapify(arr,n,i)
        
def heapsort(arr):  

    n = len(arr)   #長度為array的長度
    
    for i in range(n,-1,-1):             #for迴圈從n開始到-1進行heapify
        heapify(arr,n,i)
        
    for i in range(n-1,0,-1):            #將最後一個index和index0進行交換,固定交換完的數值,從array最後面開始遞減到0進行交換
        arr[i], arr[0] = arr[0], arr[i]
        
        heapify(arr,i,0)
        
        
    return arr

arr = [8,11,9,2,10,16]  #測試執行結果
heapsort(arr) 
