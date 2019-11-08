<font face="微软雅黑" size=7  >Merge Sort V.S Heap Sort
  
<font face="微软雅黑" size=7  > Heap Sort
  
<font face="微软雅黑" size=3  >特點
以陣列表示，但是以完全二元樹的方式理解。
唯一能夠同時最優地利用空間和時間的方法——最壞情況下也能保證使用 2N \log N2NlogN 次比較和恒定的額外空間。
在索引從0開始的陣列中：
父節點 i 的左子節點在位置(2*i+1)
父節點 i 的右子節點在位置(2*i+2)
子節點 i 的父節點在位置floor((i-1)/2)
  
堆的基本操作

最大堆調整（Max_Heapify）：將堆的末端子節點作調整，使得子節點永遠小於父節點
創建最大堆（Build_Max_Heap）：將堆所有數據重新排序
堆排序（HeapSort）：移除位在第一個數據的根節點，並做最大堆調整的遞迴運算 
不穩定排序：排序後，相同鍵值的元素相對位置可能改變。
原地排序：不需額外花費儲存空間來排序。
較差的 CPU 快取：heap 不連續存取位址的特性，不利於 CPU 快取。


<font face="微软雅黑" size=7  > Merge Sort
  
<font face="微软雅黑" size=3  >合併排序法(或稱歸併排序法)，是排序演算法的一種，使用Divide and Conquer的演算法來實作。排序時需要額外的空間來處理，過程依照以下步驟進行：

將陣列分割直到只有一個元素。
開始兩兩合併，每次合併同時進行排序，合併出排序過的陣列。
重複2的動作直接全部合併完成。

實作又可分為Top-down和Bottom-up，依據原始的步驟會先將陣量分割直到剩一個元素(Top-down)，然而也可以一開始就直接切割成單一元素開始合併(Bottom-up)。

分析

最佳時間複雜度：O(nlog n)

平均時間複雜度：O(nlog n)

最差時間複雜度：O(nlog n)

空間複雜度：O(n)

Stable sort：是





<font face="微软雅黑" size=5  >參考資料

https://emn178.pixnet.net/blog/post/87965707
https://rust-algo.club/sorting/heapsort/
  
