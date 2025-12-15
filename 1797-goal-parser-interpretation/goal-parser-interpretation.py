class Solution:
    def interpret(self, command: str) -> str:
        li=list(command)
        s=[]
        for i in range(len(li)):
            if li[i]=='(' and li[i+1]==')':
                s.append('o')
            elif li[i] not in "()":
                s.append(li[i])  
        return "".join(s)        
        