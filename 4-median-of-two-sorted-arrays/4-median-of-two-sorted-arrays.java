class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] arr = Arrays.copyOf(nums1, nums1.length + nums2.length);
        System.arraycopy(nums2, 0, arr, nums1.length, nums2.length);
        
        Arrays.sort(arr);
        int size = arr.length;
        double median;
        if(size % 2 == 0)
            median = (arr[size/2] + arr[size/2 - 1]) / 2.0;
        else
            median = arr[size/2];
        
        return median;
    }
}