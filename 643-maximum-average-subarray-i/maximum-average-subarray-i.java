class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int MaxWindowSum = 0;
        int wsum = 0;
        
        for(int i = 0; i<k;i++){
            wsum = wsum + nums[i];
        }

        MaxWindowSum = wsum;

        for(int i = k ; i < nums.length;i++){
            wsum = wsum - nums[i-k] + nums[i];
            if (wsum > MaxWindowSum) {
                MaxWindowSum = wsum;
            }   
        }
    
        return (double) MaxWindowSum / k;       
    }
}