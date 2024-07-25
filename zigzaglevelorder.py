# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result=[]
        level=0
        qeue=collections.deque()
        qeue.append(root)

        while qeue:
            qlen=len(qeue)
            levellist=[]

            for i in range(qlen):
                if level%2==0:
                    element=qeue.popleft()
                    if element:
                        levellist.append(element.val)
                        qeue.append(element.left)
                        qeue.append(element.right)
                else:
                    element=qeue.pop()
                    if element:
                        levellist.append(element.val)
                        qeue.appendleft(element.right)
                        qeue.appendleft(element.left)
                
            level+=1
            if levellist:
                result.append(levellist)
        return result

'''
For odd level append to right and pop from left
for even level pop from right and append to left
increase level after everyiteration
'''
                    

            

        
