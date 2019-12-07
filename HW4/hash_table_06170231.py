from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def Hash(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        return int(h.hexdigest(), 16)
    
    def add(self, key):
        password = MyHashSet.Hash(self, key)
        a = password % self.capacity
        node = self.data[a]
        if node == None:
            node = ListNode(password)
            self.data[a] = node
        else:
            while node.val != password:
                if node.next == None:
                    node.next = ListNode(password)         
                else:     
                    node = node.next
            pass
     
    def remove(self, key):
        password = MyHashSet.Hash(self,key)
        a = password % self.capacity
        node = self.data[a]
        if node == None:
            return 
        else:
            if node.val == password:           
                node = node.next
                self.data[a] = node
        if node:          
            while node.next != None:    
                if node.next.val == password: 
                    node.next = node.next.next
                else:     
                    node = node.next         
            return             
           
    def contains(self, key):
        password = MyHashSet.Hash(self, key)
        a = password % self.capacity
        node = self.data[a]
        if node == None:
            return False
        else:
            while node.val != password:
                node = node.next 
                if node == None:
                    return False
                
            return True

