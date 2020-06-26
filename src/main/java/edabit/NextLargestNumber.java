package edabit;

/**
 * https://edabit.com/challenge/EtW6o2eH88C89NYzw
 */
public class NextLargestNumber {

    public static void main(String[] args) {
        System.out.println(nextNumber(3542));
    }

    private static Integer nextNumber(Integer n) {
        Integer next = n;
        String s = Integer.toString(n);
        System.out.println("[" + s + "]");
        int j;
        for (int i = s.length() - 1; i >= 0; i--) {
            for (j = i - 1; j >= 0; j--) {
                if (s.substring(i, i + 1).compareTo(s.substring(j, j + 1)) < 0) {
                    s = swap(s, i, j);
                    System.out.println("swap " + s.substring(i, i + 1) + " and " + s.substring(j, j + 1));
                    break;
                }
            }
        }


        return next;
    }

    private static String swap(String s, int i, int j) {
        StringBuilder sb = new StringBuilder();
        String i1 = s.substring(i , i + 1);
        String j1 = s.substring(j , j + 1);
        return sb.toString();
    }
}
