class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] solution = new int[2];
        for (int i = 0; i < nums.length; i++){
            for (int j = i + 1; j < nums.length; j++){
                if (nums[i] + nums[j] == target){
                    solution[1] = i;
                    solution[0] = j;
                }
            }
        }
        return solution;
    }
}