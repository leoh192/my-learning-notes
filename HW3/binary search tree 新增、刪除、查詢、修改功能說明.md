# Binary Search Tree 

### Insert
如果tree沒有東西，則insert的數字就等rrot
如果有東西，就和root做比較，比root大的往右邊排，比root小的往左邊，如果有子節點就在和子節點比較，大的往右排，小的往左，以此類推


### Delete
如果沒有delete的數值則直接回傳
1.如果刪除的node沒有子節點，則直接刪除
2.如果刪除的有一個子節點:就拿樹左邊的最大值來補，並且刪除來填補原本的node，
                       就拿樹右邊的最小值來補，並且刪除來填補原本的node
3.如果刪除的有兩個子節點:拿樹左邊的最大值，或拿樹右邊的最小值來填補，並且把填補原本的node刪除

### Search
如果樹裡沒東西或沒有找到要找的數值則回傳None
如果要找的樹比root大，則往樹的右邊找，和每一個node比對
如果要找的樹比root小，則往樹的左邊找，和每一個node比對

### Modify

把要刪除的數值刪除，在insert一個新的數值進去














參考資料

http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html



