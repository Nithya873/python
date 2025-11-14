class Solution {
    public int mostFrequentEven(int[] nums) {
        HashMap<Integer,Integer> hs=new HashMap<>();
        for(int i=0;i<nums.length;i++){
          if(nums[i]%2==0){
            hs.put(nums[i],hs.getOrDefault(nums[i],0)+1);
          }
        }
        int max1=0;
        int ans=-1;
        for(Integer key:hs.keySet()){
             int d=hs.get(key);
             if(max1<d){
               max1=d;
               ans=key;
             }
             else if(max1==d && key<ans){
                ans=key;
             }
        }
        return ans;
    }
}