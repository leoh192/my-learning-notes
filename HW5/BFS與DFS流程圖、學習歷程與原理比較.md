## BFS
廣度優先搜尋法（Breadth-First Search, BFS）是一種樹（Tree）或圖（Graph）資料結構的搜索演算法，從圖的某一節點(vertex, node) 開始走訪，接著走訪此一節點所有相鄰且未拜訪過的節點，才進一步走訪下一層級的節點。
時間複雜度：O(V+E)（分別遍歷所有節點和各節點的所有鄰居）
空間複雜度：O(V)（Queue中最多可能存放所有節點）
用於有效率的迭代(traversal)
迭代的方式為鄰近的先訪問(level-ordered)
劣勢在於儲存指標記憶體空間，有時用DFS替代
使用FIFO的Queue來實作，Queue為空代表完成迭代

## DFS
是一種用來遍尋一個樹(tree)或圖(graph)的演算法。由樹的根(或圖的某一點當成 根)來開始探尋，先探尋邊(edge)上未搜尋的一節點(vertex or node)，並儘可能深的搜索，直到該節點的所有邊上節點都已探尋；就回溯(backtracking)到前一個節點，重覆探尋未搜尋的節點，直到找到目 的節點或遍尋全部節點。
時間複雜度：O(V+E)
空間複雜度：O(logV)（訪問至末端節點後LIFO，Stack最多只會同時存在logV個節點，也就是樹的高度）
為了解Maze Problem而生的演算法
效能比BFS稍佳
使用LIFO的Stack來實作

## BFS與DFS的原理比較
BFS是由選定的頂點V0開始，和相鄰的點V1、V2...開始搜尋，如果還沒搜尋到則由V1開始搜尋V1的臨點...以此類推。由此可知BFS是廣度優先搜尋，由頂點開始往外。
DFS是由選定的頂點V0開始，由第一個相鄰的點開始，先把V1的臨點都先搜尋一遍，再換到V2、V3...以此類推，所以DFS是深度優先搜尋，主要先往一個臨點開始搜尋。



參考資料:
https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Graphs/breadth-first_search.html
https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
https://super9.space/archives/1562
http://simonsays-tw.com/web/DFS-BFS/DepthFirstSearch.html
https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
http://alrightchiu.github.io/SecondRound/graph-li-yong-dfshe-bfsxun-zhao-connected-component.html
