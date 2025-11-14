class Solution {
    public List<Integer> majorityElement(int[] nums) {
        HashMap<Integer,Integer> hs=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            hs.put(nums[i],hs.getOrDefault(nums[i],0)+1);
        }
        ArrayList<Integer> li=new ArrayList<>();
        for(Integer key:hs.keySet()){
           int d= hs.get(key);
           if(d>(nums.length)/3){
            li.add(key);
           }
        }
        return li;

    }
}