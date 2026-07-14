class Solution {
    public boolean hasDuplicate(int[] nums) {
    
    boolean twice_check = false;

    int counter = 0;

    for(int i = 0; i < nums.length; i++) {

        int m = nums[i];

        for(int z = 0; z < nums.length; z++) {

            if (m == nums[z]){
                counter++;
            }

            if(counter >= 2){
                twice_check = true;
            }
        }
        counter = 0;
    }


    return twice_check;

    }
}