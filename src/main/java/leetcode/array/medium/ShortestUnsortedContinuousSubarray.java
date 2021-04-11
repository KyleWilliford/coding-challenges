package leetcode.array.medium;

import lombok.extern.slf4j.Slf4j;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * Challenge 581
 */
@Slf4j
public class ShortestUnsortedContinuousSubarray {

    public static void main(String[] args) {
        int[] arr = {2, 6, 4, 8, 10, 9, 15};
        int length = findUnsortedSubarray(arr);
        logger.info("Shorted unsorted subarray {} length: {}", arr, length);
        assertEquals(5, length);
        int[] arr2 = {1, 2, 3, 4};
        length = findUnsortedSubarray(arr2);
        logger.info("Shorted unsorted subarray {} length: {}", arr2, length);
        assertEquals(0, length);
        int[] arr3 = {1};
        length = findUnsortedSubarray(arr3);
        logger.info("Shorted unsorted subarray {} length: {}", arr3, length);
        assertEquals(0, length);
        int[] arr4 = {1, 3, 2, 2, 2};
        length = findUnsortedSubarray(arr4);
        logger.info("Shorted unsorted subarray {} length: {}", arr4, length);
        assertEquals(4, length);
        int[] arr5 = {1, 2, 3, 3, 3};
        length = findUnsortedSubarray(arr5);
        logger.info("Shorted unsorted subarray {} length: {}", arr5, length);
        assertEquals(0, length);
        int[] arr6 = {1, 1};
        length = findUnsortedSubarray(arr6);
        logger.info("Shorted unsorted subarray {} length: {}", arr6, length);
        assertEquals(0, length);
        int[] arr7 = {1, 2, 4, 5, 3};
        length = findUnsortedSubarray(arr7);
        logger.info("Shorted unsorted subarray {} length: {}", arr7, length);
        assertEquals(3, length);
        int[] arr8 = {2, 1};
        length = findUnsortedSubarray(arr8);
        logger.info("Shorted unsorted subarray {} length: {}", arr8, length);
        assertEquals(2, length);
    }

    public static int findUnsortedSubarray(int[] nums) {
        int current;
        Integer start = null;
        int end = 0;
        for (int i = 0; i < nums.length; i++) {
            current = nums[i];
            boolean unordered = false;
            for (int j = i - 1; j >= 0; j--) {
                if (current < nums[j]) {
                    unordered = true;
                    break;
                }
            }
            for (int k = i + 1; k < nums.length; k++) {
                if (current > nums[k]) {
                    unordered = true;
                    break;
                }
            }
            if (unordered) {
                if (start == null) {
                    start = i;
                }
                end = i;
            }
        }
        if (start == null) {
            return 0;
        }
        return (end - start) + 1;
    }
}
