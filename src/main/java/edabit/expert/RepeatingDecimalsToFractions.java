package edabit.expert;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * https://edabit.com/challenge/YLdgd8dav2joTpXbn
 */
public class RepeatingDecimalsToFractions {

    private static final Pattern p = Pattern.compile("(\\d*)\\.(\\d*)\\((\\d*)\\)");
    public static final String NUMERATOR = "numerator: ";
    public static final String DENOMINATOR = "denominator: ";

    public static void main(String[] args) {
        System.out.println("0.(6) -> " + fractions("0.(6)"));
        System.out.println("1.(1) -> " + fractions("1.(1)"));
        System.out.println("3.(142857) -> " + fractions("3.(142857)"));
        System.out.println("0.19(2367) -> " + fractions("0.19(2367)"));
        System.out.println("0.1097(3) -> " + fractions("0.1097(3)"));
        System.out.println("0.606(6) -> " + fractions("0.606(6)"));
        System.out.println("10.0 -> " + fractions("10.0"));
        System.out.println("10.0(0) -> " + fractions("10.0(0)"));
        System.out.println("10.0(1) -> " + fractions("10.0(1)"));
        System.out.println("0.101(1) -> " + fractions("0.101(1)"));
    }

    private static String fractions(final String s) {
        Matcher m = p.matcher(s);
        if (!m.matches()) {
            return "invalid input";
        }
        String wholeNumber = m.group(1);
        String nonRepeating = m.group(2);
        String repeating = m.group(3);
//        System.out.println(wholeNumber);
//        System.out.println(nonRepeating);
//        System.out.println(repeating);
        double tenPowerLength = Math.pow(10, (double) nonRepeating.length() + repeating.length());
        double numerator = Double.parseDouble(nonRepeating + repeating) / tenPowerLength;
        if (numerator == 0) {
            return wholeNumber + "/" + 1;
        }
        int denominator = (int) Math.pow(10, repeating.length());
//        System.out.println(NUMERATOR + numerator);
//        System.out.println(DENOMINATOR + denominator);
        double scale = Math.pow(10, Double.toString(numerator).length());
        numerator = Math.round((((numerator * denominator) + (Double.parseDouble(repeating) / tenPowerLength)) - numerator) * scale) / scale;
        denominator--;
//        System.out.println(NUMERATOR + numerator);
//        System.out.println(DENOMINATOR + denominator);
        if (numerator % 1 != 0) {
            String placesAfterDecimal = Double.toString(numerator).split("\\.")[1];
//            System.out.println("placesAfterDecimal: " + placesAfterDecimal.length());
            if (placesAfterDecimal.length() != 0 && !"0".equals(placesAfterDecimal)) {
                numerator *= Math.pow(10, placesAfterDecimal.length());
                denominator *= Math.pow(10, placesAfterDecimal.length());
            }
        }
//        System.out.println(NUMERATOR + numerator);
//        System.out.println(DENOMINATOR + denominator);
        long longNumerator = (long) numerator;
        int gcf = findGCF(longNumerator, denominator);
//        System.out.println("gcf = " + gcf);
        longNumerator /= gcf;
        denominator /= gcf;
        longNumerator += (denominator * Long.parseLong(wholeNumber));
        return longNumerator + "/" + denominator;
    }

    private static int findGCF(long numerator, long denominator) {
//        System.out.println("Find GCF of numerator: " + numerator);
//        System.out.println("Find GCF of denominator: " + denominator);
        int gcf = 1;
        for (int i = 2; i <= numerator; i++) {
            if (numerator % i == 0 && denominator % i == 0) {
                gcf = i;
//                System.out.println("gcf = " + gcf);
            }
        }
        return gcf;
    }
}
