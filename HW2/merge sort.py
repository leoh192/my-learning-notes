{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<font face=\"微软雅黑\" size=5  > What is Merge Sort?  \n",
    "<font face=\"微软雅黑\" size=3  >Merge Sort屬於比較進階的演算法，排序方法也比較複雜一點，基本的步驟可以分為「拆分」與「合併」：\n",
    "拆分\n",
    "把大陣列切一半成為兩個小陣列\n",
    "把切好的兩個小陣列再各自切一半\n",
    "重複步驟二直到每個小陣列都只剩一個元素\n",
    "合併\n",
    "排序兩個只剩一個元素的小陣列並合併\n",
    "把兩邊排序好的小陣列合併並排序成一個陣列\n",
    "重複步驟二直到所有小陣列都合併成一個大陣列    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<font face=\"微软雅黑\" size=3  >我一開始的想法是,把array一分為二,先把兩個分割到只剩一個並且先排列.\n",
    "然後再把兩個排列好的array從index=0相互比較,將比較小的加入第三個array,\n",
    "也就是最後mergesort出來的array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 5, 15, 24, 26, 31, 32]\n"
     ]
    }
   ],
   "source": [
    "def mergesort(array):  #定義一個函數\n",
    "    \n",
    "    if len(array) <= 1: #array長度<=1則回傳\n",
    "        \n",
    "        return array\n",
    "    \n",
    "    if len(array) > 1:\n",
    "        \n",
    "        middle = len(array) // 2 #將array一分為二\n",
    "        \n",
    "        left = array[:middle]    #array從0到middle\n",
    "        \n",
    "        right = array[middle:]   #array從miiddle+1到尾巴\n",
    "\n",
    "        mergesort(left)   #先mergesort兩個array\n",
    "        mergesort(right)  \n",
    "\n",
    "        i = 0; # left的index\n",
    "        j = 0; # 第三個array的index\n",
    "        k = 0; # right的index\n",
    "        \n",
    "        while k < len(right) and i < len(left):\n",
    "            \n",
    "            if right[k] < left[i]:   #比較兩個array中的index,比較小的放入第三個array,然後移動到下一個index\n",
    "                array[j] = right[k]  \n",
    "                k += 1 \n",
    "                \n",
    "            else:\n",
    "                array[j] = left[i]   #反之\n",
    "                i += 1\n",
    "\n",
    "            j += 1                   #放入第三個array之後移動到下一個\n",
    "\n",
    "        while k < len(right):        #檢查有無遺漏直\n",
    "            \n",
    "            array[j] = right[k]\n",
    "            k += 1\n",
    "            j += 1\n",
    "\n",
    "        while i < len(left):\n",
    "            \n",
    "            array[j] = left[i]\n",
    "            i += 1\n",
    "            j += 1\n",
    "            \n",
    "array = [24, 31, 32, 1, 15, 5, 26]\n",
    "mergesort(array)\n",
    "print(array)  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "參考資料\n",
    "\n",
    "https://stackoverflow.com/questions/18761766/mergesort-with-python\n",
    "https://docs.google.com/presentation/d/e/2PACX-1vToxkEzc1H1RT5MI9G941KQFBC7GO_Efn95wTqXLEdr3LDBSNcQb-M46IOC-_RzZih6IBEwwy3rWQuE/pub?start=false&loop=false&delayms=3000&slide=id.g6f5f9558de_0_31\n",
    "https://pjchender.blogspot.com/2017/09/merge-sort.html\n",
    "https://emn178.pixnet.net/blog/post/87965707"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
