package edabit.expert;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

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
        List<Integer> digits = Arrays.stream(Integer.toString(n).split("")).map(Integer::parseInt).collect(Collectors.toList());
        int skip = swapFirstLargestDigit(digits);
//        System.out.println(digits);
//        System.out.println(skip);
        List<Integer> finalDigits = digits.stream().limit(skip).collect(Collectors.toList());
        finalDigits.addAll(digits.stream().skip(skip).sorted().collect(Collectors.toList()));
//        System.out.println(finalDigits);
        return Integer.parseInt(finalDigits.stream().map(d -> Integer.toString(d)).collect(Collectors.joining("")));
    }

    private static int swapFirstLargestDigit(List<Integer> digits) {
        for (int i = digits.size() - 1; i >= 0; i--) {
            for (int j = i - 1; j >= 0; j--) {
                Integer digitI = digits.get(i);
                Integer digitJ = digits.get(j);
                if (digitI > digitJ) {
                    digits.set(i, digitJ);
                    digits.set(j, digitI);
                    return j + 1;
                }
            }
        }
        return digits.size();
    }
}
