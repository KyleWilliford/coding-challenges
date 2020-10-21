package c1;

import lombok.extern.slf4j.Slf4j;

import java.util.Arrays;
import java.util.List;

@Slf4j
public class CustomSortedArray {

    public static void main(String[] args) {
//        List<Integer> arr = Arrays.asList(8, 5, 11, 4, 6);
        List<Integer> arr = Arrays.asList(4, 13, 10, 21, 20);
        int moves = moves(arr);
        logger.info("{}", moves);
        logger.info("{}", arr);
    }

    public static int moves(List<Integer> arr) {
        int moves = 0;
        int lastCheckedEven = arr.size();
        for (int i = 0; i < arr.size(); i++) {
            if (i > lastCheckedEven) {
                return moves;
            }
            if (arr.get(i) % 2 == 1) {
                for (int j = arr.size() - 1; j > i; j--) {
                    if (arr.get(j) % 2 == 0) {
                        arr.set(i, arr.get(i) + arr.get(j));
                        arr.set(j, arr.get(i) - arr.get(j));
                        arr.set(i, arr.get(i) - arr.get(j));
                        moves++;
                        lastCheckedEven = j;
                        break;
                    }
                }
            }
        }
        return moves;
    }
}
