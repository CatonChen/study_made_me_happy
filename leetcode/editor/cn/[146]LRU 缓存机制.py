# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制 。 
# 
#  
#  
#  实现 LRUCache 类： 
# 
#  
#  LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存 
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 
#  void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上
# 限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。 
#  
# 
#  
#  
#  
# 
#  进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？ 
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 3000 
#  0 <= value <= 104 
#  最多调用 3 * 104 次 get 和 put 
#  
#  Related Topics 设计 
#  👍 1279 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 定义一个双向链表节点
class DLinkNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()  # 哈希字典
        # 伪头部节点和伪尾部节点
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity  # 链表容量
        self.size = 0  # 容量计数

    def addToHead(self, node):
        # 插入到头部
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        # 删除节点
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        # 移动到头部
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        # 删除尾部节点
        node = self.tail.prev
        self.removeNode(node)
        return node

    def get(self, key: int) -> int:
        # key不存在，返回-1
        if key not in self.cache:
            return -1
        # key存在，先移动到头部，再返回
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # key不存在，创建一个
        if key not in self.cache:
            node = DLinkNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加到头部
            self.addToHead(node)
            # 判断链表容量
            self.size += 1
            if self.size > self.capacity:
                # 删除尾部节点，再从哈希表中删除
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:  # key存在，先定位，再更新节点值，再移动到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
