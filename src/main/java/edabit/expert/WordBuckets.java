package edabit.expert;

import java.util.ArrayList;
import java.util.List;

/**
 * @author https://github.com/KyleWilliford
 *
 * https://edabit.com/challenge/3FAMXz4wAYGqpCtDR
 */
public class WordBuckets {

    public static void main(String[] args) {
        System.out.println("she sells sea shells by the sea -> " +
                bucketize("she sells sea shells by the sea", 10));
        System.out.println("the mouse jumped over the cheese -> " +
                bucketize("the mouse jumped over the cheese", 7));
        System.out.println("fairy dust coated the air -> " +
                bucketize("fairy dust coated the air", 20));
        System.out.println("a b c d e -> " +
                bucketize("a b c d e", 2));
    }

    private static List<String> bucketize(String s, int n) {
        String[] split = s.split(" ");
        List<String> buckets = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (String word : split) {
//            System.out.println(sb.toString());
            if (sb.length() + word.length() <= n) {
                sb.append(word).append(" ");
            } else {
                if (sb.length() > 1) {
                    buckets.add(sb.toString().trim());
                    sb = new StringBuilder();
                    sb.append(word).append(" ");
                }
            }
//            System.out.println(buckets);
        }
        if (sb.length() > 1) {
            buckets.add(sb.toString().trim());
        }
        return buckets;
    }
}
