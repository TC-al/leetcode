class Solution {
    public int searchInsert(int[] nums, int target) {
        
        List<Integer> l = new ArrayList<>();
        for (var x : nums) {
            l.add(x);
        }

        l.add(target);
        Collections.sort(l);
        
        for (int i = 0; i < l.size(); i++) {
            if (l.get(i) == target) {
                return i;
            }
        }
        return 0;
    }
}