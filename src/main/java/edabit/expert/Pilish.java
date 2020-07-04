package edabit.expert;

import org.apache.commons.lang3.StringUtils;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * https://edabit.com/challenge/Fy2ySuj6XK5mxrsgR
 */
public class Pilish {

    private static final int PI_PLACES = 15;
    private static final List<Integer> PI;

    static {
        PI = Arrays.stream(Double.toString(Math.PI).replaceAll("\\.", "").split(""))
                .limit(PI_PLACES)
                .map(Integer::parseInt).collect(Collectors.toList());
//        System.out.println(PI);
    }

    public static void main(String[] args) {
        System.out.println("HOWINEEDADRINKALCOHOLICINNATUREAFTERTHEHEAVYLECTURESINVOLVINGQUANTUMMECHANICSANDALLTHESECRETSOFTHEUNIVERSE -> "
                + pilish("HOWINEEDADRINKALCOHOLICINNATUREAFTERTHEHEAVYLECTURESINVOLVINGQUANTUMMECHANICSANDALLTHESECRETSOFTHEUNIVERSE"));
        System.out.println("FORALOOP -> " + pilish("FORALOOP"));
        System.out.println("CANIMAKEAGUESSNOW -> " + pilish("CANIMAKEAGUESSNOW"));
        System.out.println("33314444 -> " + pilish("33314444"));
        System.out.println("TOP -> " + pilish("TOP"));
        System.out.println("X -> " + pilish("X"));
        System.out.println("\"\" -> " + pilish(""));
    }

    private static String pilish(String txt) {
        if (StringUtils.isBlank(txt)) {
            return "";
        }
        StringBuilder phrase = new StringBuilder();
        int i = 0;
        for (Integer d : PI) {
            if (i == txt.length()) {
                break;
            }
            StringBuilder word = new StringBuilder();
            for (; word.length() < d && i < txt.length(); i++) {
                word.append(txt, i, i + 1);
            }
            if (word.length() < d) {
                word.append(txt.substring(txt.length() - 1).repeat(d - word.length()));
            }
            phrase.append(word).append(" ");
        }
//        System.out.println(phrase.toString());
        return phrase.toString();
    }
}
