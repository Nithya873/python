class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dici={}
        for i in range(len(nums)):
            val=nums[i]
            if val not in dici:
                dici[val]=1
            else:
                dici[val]+=1  
        temp=[] 
        keys=list(dici.keys())
        for l in range(len(keys)):
            for j in range(len(keys)-1):
                if dici[keys[j]]>dici[keys[j+1]]:
                    keys[j],keys[j+1]=keys[j+1],keys[j]
                elif dici[keys[j]]==dici[keys[j+1]] and keys[j]<keys[j+1]:
                    keys[j],keys[j+1]=keys[j+1],keys[j]
        for k in keys:
            for m in range(dici[k]):
                temp.append(k)
        return temp         
            

                  
        