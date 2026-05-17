class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        li=[]
        for i in range(len(order)):
        
            if order[i] in friends:
                li.append(order[i])
        return li            
          
        