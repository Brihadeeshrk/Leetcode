/*
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
*/

class Solution {
    public void moveZeroes(int[] a) {
       
        int i=0,j=0;
        
        // t stores the index of the last element, which will be (number of elements - 1) as array index starts from 0.
        int t=a.length-1;
        while(i<=t)
        {
            if(a[i]!=0)
            {
                //copying only the non-zero elements in the original array itself as need to keep it in-place
                a[j++]=a[i]; 
            }
            i++;
        }
        
        // counting the number of zeroes, which will be equal to the total numbers - the non zero numbers.
        j=t-j+1;
        

        //filling the remaining array with the zeros starting from end.
        while(j!=0)
        {
            a[t--]=0;
            j--;
        }
    }     
}
