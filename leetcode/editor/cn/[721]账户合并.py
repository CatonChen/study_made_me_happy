# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其
# 余元素是 emails 表示该账户的邮箱地址。 
# 
#  现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为
# 人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。 
# 
#  合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按字符 ASCII 顺序排列的邮箱地址。账户本身可以以任意顺序返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnn
# ybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Ma
# ry", "mary@mail.com"]]
# 输出：
# [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  
# ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# 解释：
# 第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。 
# 第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
# 可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
# ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的
# 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  accounts的长度将在[1，1000]的范围内。 
#  accounts[i]的长度将在[1，10]的范围内。 
#  accounts[i][j]的长度将在[1，30]的范围内。 
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 252 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self):
        self.father = {}

    def add(self, x):
        if x not in self.father:
            self.father[x] = None

    def find(self, x):
        root = x
        self.add(root)
        while self.father[root] is not None:
            root = self.father[root]
        # 路径压缩
        while x != root:
            o_father = self.father[x]
            self.father[x] = root
            x = o_father
        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToIndex = {}
        emailToName = {}
        # 将email与name建立哈希字典关系。
        # 将email与分配编号建立字典关系。
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToIndex:
                    emailToIndex[email] = len(emailToIndex)
                    emailToName[email] = name
        # print(emailToIndex)
        # print(emailToName)
        # 通过并查集将具有相同email的账户进行合并，使得这些email具有相同的分配编号
        uf = UnionFind()
        for account in accounts:
            firstIndex = emailToIndex[account[1]]
            for email in account[2:]:
                uf.merge(firstIndex, emailToIndex[email])
        # print(uf)
        # 遍历email与编号的字典
        indexToEmail = collections.defaultdict(list)
        for email, index in emailToIndex.items():
            index = uf.find(index)  # 通过并查集将具有相同编号
            # 通过相同编号将email重新归集在一起
            indexToEmail[index].append(email)
        # print(indexToEmail)

        ans = list()
        for emails in indexToEmail.values():
            # 通过email找出账户名，并拼接排序的email列表
            ans.append([emailToName[emails[0]]] + sorted(emails))
        return ans

# leetcode submit region end(Prohibit modification and deletion)
