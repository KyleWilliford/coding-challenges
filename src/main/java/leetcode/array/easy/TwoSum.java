package leetcode.array.easy;

import lombok.extern.slf4j.Slf4j;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 */
@Slf4j
public class TwoSum {

    public static void main(String[] args) {
        TwoSum twoSum = new TwoSum();
        int[] nums = {2, 7, 11, 15};
        logger.info("{}", twoSum.twoSum(nums, 9));
        logger.info("{}", twoSum.twoSumMap(nums, 9));
        nums = new int[] {3, 2, 4};
        logger.info("{}", twoSum.twoSum(nums, 6));
        logger.info("{}", twoSum.twoSumMap(nums, 6));
        nums = new int[] {3, 3};
        logger.info("{}", twoSum.twoSum(nums, 6));
        logger.info("{}", twoSum.twoSumMap(nums, 6));
    }

    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (target == nums[i] + nums[j]) {
                    return new int[] {i, j};
                }
            }
        }
        throw new UnsupportedOperationException("No TwoSum found for target " + target);
    }

    public int[] twoSumMap(int[] nums, int target) {
        Map<Integer, List<Integer>> map = new LinkedHashMap<>();
        for (int i = 0; i < nums.length; i++) {
            List<Integer> values = map.getOrDefault(nums[i], new ArrayList<>());
            values.add(i);
            map.put(nums[i], values);
            values = map.get(target - nums[i]);
            if (values != null && !values.isEmpty()) {
                if (values.size() == 1 && nums[i] != target - nums[i]) {
                    return new int[] {values.get(0), i};
                } else if (values.size() == 2) {
                    return new int[] {values.get(0), values.get(1)};
                }
            }
        }
        throw new UnsupportedOperationException("No TwoSum found for target " + target);
    }
}
