package edabit.expert;

import java.util.HashSet;
import java.util.Set;

/**
 * @author https://github.com/KyleWilliford
 *
 * https://edabit.com/challenge/owwJbMCXJBv9n5FJD
 */
public class Josephus {
    public static void main(String[] args) {
        for (int i = 2; i <= 500; i++) {
            for (int j = 1; j <= 10; j++) {
                System.out.println("(" + i + ", " + j + ") -> " + josephus(i, j));
            }
        }
//        System.out.println("(41, 3) -> " + josephus(41, 3));
//        System.out.println("(35, 11) -> " + josephus(35, 11));
//        System.out.println("(11, 1) -> " + josephus(11, 1));
//        System.out.println("(2, 2) -> " + josephus(2, 2));
//        System.out.println("(500, 6) -> " + josephus(500, 6));
    }

    /**
     * Counting up and tracking killed places along the way
     */
    private static int josephus(int n, int d) {
        if (n <= 1 || d > n) {
            return 0;
        }
        if (d == 1) {
            return n;
        }
        Set<Integer> killed = new HashSet<>();
        int place = 0;
        for (int i = 0; i < n; i++) {
            int count = 0;
            while (count < d) {
                place = (place % n) + 1;
                if (killed.contains(place)) {
//                    System.out.println("Already killed " + place);
                    place = (place % n) + 1;
                }
                if (!killed.contains(place)) {
                    count++;
                }
            }
//            System.out.println("killed " + place);
            killed.add(place);
        }
        return place;
    }
}
