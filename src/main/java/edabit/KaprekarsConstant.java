package edabit;

import org.apache.commons.lang3.StringUtils;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

/**
 * https://edabit.com/challenge/eBkknBKXvMm8bDo8M
 */
public class KaprekarsConstant {

    private static final int KAPREKARS_CONSTANT = 6174;

    public static void main(String[] args) {
        System.out.println("kaprekar(6621) -> " + kaprekar(6621));
        System.out.println("kaprekar(6554) -> " + kaprekar(6554));
        System.out.println("kaprekar(1234) -> " + kaprekar(1234));
        System.out.println("kaprekar(1) -> " + kaprekar(1));
        System.out.println("kaprekar(12) -> " + kaprekar(12));
        System.out.println("kaprekar(101) -> " + kaprekar(101));
        System.out.println("kaprekar(110) -> " + kaprekar(110));
    }

    private static int kaprekar(Integer n) {
        if (KAPREKARS_CONSTANT == n) {
            return 0;
        }
        List<String> digits = Arrays.stream(Integer.toString(n).split("")).sorted(Collections.reverseOrder()).collect(Collectors.toList());
        for (int i = digits.size(); i < 4; i++) {
            digits.add("0");
        }
//        System.out.println(digits);
        Integer a = Integer.parseInt(StringUtils.join(digits, ""));
        Collections.reverse(digits);
//        System.out.println(digits);
        Integer b = Integer.parseInt(StringUtils.join(digits, ""));
//        System.out.println("a = " + a + " b = " + b);
        if (a > b) {
            return  1 + kaprekar(a - b);
        }
        return 1 + kaprekar(b - a);
    }
}
