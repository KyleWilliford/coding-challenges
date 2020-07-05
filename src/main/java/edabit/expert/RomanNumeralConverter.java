package edabit.expert;

import org.apache.commons.lang3.tuple.Triple;

/**
 * https://edabit.com/challenge/KnpqDdkibon22Eexa
 */
public class RomanNumeralConverter {

    private static final int MAX_SUPPORTED = 3999999;

    private static final Triple<String, String, String> ONES = Triple.of("I", "V", "X");
    private static final Triple<String, String, String> TENS = Triple.of("X", "L", "C");
    private static final Triple<String, String, String> HUNDREDS = Triple.of("C", "D", "M");
    private static final Triple<String, String, String> THOUSANDS = Triple.of("M", "V", "X");
    private static final Triple<String, String, String> TEN_THOUSANDS = Triple.of("X", "L", "C");
    private static final Triple<String, String, String> HUNDRED_THOUSANDS = Triple.of("C", "D", "M");
    private static final Triple<String, String, String> MILLIONS = Triple.of("M", "", "");

    public static void main(String[] args) {
        for (int i = 1; i <= 3999; i++) {
            System.out.println(i + " -> " + convert(i));
        }
    }

    private static String convert(int n) {
        if (n > MAX_SUPPORTED) {
            return "Numbers larger than 3999 not supported.";
        }
        StringBuilder sb = new StringBuilder();
        sb.append(convertPart(n % 10, ONES));
        n /= 10;
        sb.append(convertPart(n % 10, TENS));
        n /= 10;
        sb.append(convertPart(n % 10, HUNDREDS));
        n /= 10;
        sb.append(convertPart(n % 10, THOUSANDS));
        n /= 10;
        sb.append(convertPart(n % 10, TEN_THOUSANDS));
        n /= 10;
        sb.append(convertPart(n % 10, HUNDRED_THOUSANDS));
        n /= 10;
        sb.append(convertPart(n % 10, MILLIONS));
        sb.reverse();
//        System.out.println(sb.toString());
        return sb.toString();
    }

    private static String convertPart(int r, Triple<String, String, String> symbols) {
        if (r == 0) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        if (r == 4) {
            sb.append(symbols.getMiddle()).append(symbols.getLeft());
        } else if (r == 5) {
            sb.append(symbols.getMiddle());
        } else if (r == 9) {
            sb.append(symbols.getRight()).append(symbols.getLeft());
        } else if (r > 5) {
            sb.append(symbols.getLeft().repeat(r % 5)).append(symbols.getMiddle());
        } else {
            sb.append(symbols.getLeft().repeat(r));
        }
//        System.out.println(sb.toString());
        return sb.toString();
    }
}
