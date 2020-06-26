package edabit;

import org.apache.commons.lang3.tuple.Pair;

/**
 * https://edabit.com/challenge/EtW6o2eH88C89NYzw
 */
public class NextLargestNumber {

    public static void main(String[] args) {
        System.out.println("19 -> " + nextNumber(19));
        System.out.println("3542 -> " + nextNumber(3542));
        System.out.println("5432 -> " + nextNumber(5432));
        System.out.println("58943 -> " + nextNumber(58943));
    }

    private static Integer nextNumber(Integer n) {
        String s = Integer.toString(n);
        Pair<String, Integer> pair = swapFirstLargestDigit(s);
        s = pair.getLeft();
        Integer m = pair.getRight();
        if (n.toString().equals(s)) {
            return Integer.parseInt(s);
        }
        s = sort(s, m);
        return Integer.parseInt(s);
    }

    private static String sort(String s, Integer m) {
        for (int i = s.length() - 1; i > m; i--) {
            for (int j = i - 1; j > m; j--) {
                if (s.substring(i, i + 1).compareTo(s.substring(j, j + 1)) < 0) {
                    s = swap(s, i, j);
                }
            }
        }
        return s;
    }

    private static Pair<String, Integer> swapFirstLargestDigit(String s) {
        for (int i = s.length() - 1; i >= 0; i--) {
            for (int j = i - 1; j >= 0; j--) {
                if (s.substring(i, i + 1).compareTo(s.substring(j, j + 1)) > 0) {
                    s = swap(s, i, j);
                    return Pair.of(s, j);
                }
            }
        }
        return Pair.of(s, 0);
    }

    private static String swap(String s, int i, int j) {
        StringBuilder sb = new StringBuilder();
        for (int k = 0; k < s.length(); k++) {
            if (k == i) {
                sb.append(s, j, j + 1);
            } else if (k == j) {
                sb.append(s, i, i + 1);
            } else {
                sb.append(s, k, k + 1);
            }
        }
        return sb.toString();
    }
}
