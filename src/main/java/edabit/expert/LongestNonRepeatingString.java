package edabit.expert;

import java.util.Comparator;
import java.util.Set;
import java.util.TreeSet;
import java.util.function.Function;

/**
 * @author https://github.com/KyleWilliford
 */
public class LongestNonRepeatingString {

    public static void main(String[] args) {
        System.out.println("abcabcbb -> " + find("abcabcbb"));
        System.out.println("aaaaaa -> " + find("aaaaaa"));
        System.out.println("abcde -> " + find("abcde"));
        System.out.println("abcda -> " + find("abcda"));
    }

    private static String find(String s) {
//        System.out.println(s);
        Set<String> substrings = new TreeSet<>(
                Comparator.comparingInt(String::length)
                        .thenComparing(Function.identity()).reversed());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            String ss = s.substring(i, i + 1);
//            System.out.println(sb.toString());
            if (sb.indexOf(ss) == 0) {
                substrings.add(sb.toString());
                i += sb.length() - 1;
                sb = new StringBuilder();
            } else {
                sb.append(s, i, i + 1);
            }
        }
        if (sb.length() > 0) {
            substrings.add(sb.toString());
        }
//        System.out.println(substrings);
        return substrings.iterator().next();
    }
}
