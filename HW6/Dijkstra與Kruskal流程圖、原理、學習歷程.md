
###Dijkstra 原理說明
Dijkstra演算法算是單源最短路徑(Single Souce Shortest Path)的一種方法，計算一個節點到其他所有節點的最短路徑，主要特點是以起始點為中心向外層層擴展，直到擴展到終點為止且沒有負權邊
時間複雜度：
若使用Binary Heap，需要O((E+V)logV)
若使用Fibonacci Heap，只需要O(E+VlogV)
dijkstra演算法的步驟：
至起始點找尋尚未拜訪的相鄰結點
更新最短路徑表
找尋目前未拜訪的最短路徑結點，將此結點設為起始點，並設為已拜訪(已得到最短路徑)
重複第一步，直到所有結點皆為已拜訪
結論:
若權值皆不為負，使用Dijkstra演算法可以找到最短路徑的最佳解，不過因走訪的節點太多，故效率不佳
###Kruskal 原理說明
Kruskal演算法是一個計算最小生成樹(Minimum Spaning Tree)的方法，按照邊的權重順序（從小到大）將邊加入生成樹中，但是若加入該邊會與生成樹形成環(cycle)則不加入該邊，直到樹中含有「頂點個數-1」條邊為止
時間複雜度：O(nlogn)
kruskal演算法的步驟：
將每個頂點放入其自身的資料集合中
按照權值的升序由小至大選擇邊
選擇每條邊時，判斷定義邊的頂點是否在不同的資料集中，若是，將此邊插入最小生成樹的集合中，同時，將集合中包含每個頂點的聯合體取出
若不是，移動到下一條邊
重複上述過程直到所有邊都探查過
結論
Kruskal演算法主要是針對邊來展開，邊數少時效率會非常高，對於稀疏圖有很大的優勢



參考資料:
https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html
http://alrightchiu.github.io/SecondRound/single-source-shortest-pathdijkstras-algorithm.html
http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html
