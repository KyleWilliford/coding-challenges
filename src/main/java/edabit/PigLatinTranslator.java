package edabit;

import org.apache.commons.lang3.StringUtils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

/**
 * https://edabit.com/challenge/6dEDvruWbEDqXb7dk
 */
public class PigLatinTranslator {

    private static final Pattern VOWELS = Pattern.compile("[aAeEiIoOuUyY]");
    private static final Pattern LETTERS = Pattern.compile("[a-zA-Z]");

    public static void main(String[] args) {
        System.out.println("flag -> " + translate("flag"));
        System.out.println("Apple -> " + translate("Apple"));
        System.out.println("button -> " + translate("button"));
        System.out.println("\"\" -> " + translate(""));
        System.out.println("I like to eat honey waffles. -> " + translate("I like to eat honey waffles."));
        System.out.println("Do you think it is going to rain today? -> " + translate("Do you think it is going to rain today?"));
        System.out.println("How do you like them apples? -> " + translate("How do you like them apples?"));
        System.out.println("Dracula's name backwards is Alucard! -> " + translate("Dracula's name backwards is Alucard!"));
        System.out.println("Hark! Listen! -> " + translate("Hark! Listen!"));
        System.out.println("Take a seat and cram this story of a cat that used a trebuchet to launch a shrimp. -> "
                + translate("Take a seat and cram this story of a cat that used a trebuchet to launch a shrimp."));
    }

    private static String translate(final String phrase) {
        if (StringUtils.isBlank(phrase)) {
            return "";
        }
        String[] words = phrase.split("\\s+");
//        System.out.println(words);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            List<String> letters = new ArrayList<>(Arrays.asList(word.split("")));
//            System.out.println(letters);
            String letter = letters.get(0);
            if (VOWELS.matcher(letter).find()) {
                translateVowelWord(sb, letters);
            } else {
                translateConsonantWord(sb, letters);
            }
            if (i + 1 < words.length) {
                sb.append(" ");
            }
        }
        return sb.toString();
    }

    private static void translateVowelWord(StringBuilder sb, List<String> letters) {
        String letter;
        letter = letters.get(letters.size() - 1);
        boolean isPunctuated = !LETTERS.matcher(letter).find();
        if (isPunctuated) {
            letters.remove(letter);
        }
        sb.append(String.join("", letters)).append("yay");
        if (isPunctuated) {
            sb.append(letter);
        }
    }

    private static void translateConsonantWord(StringBuilder sb, List<String> letters) {
        int index = 0;
        for (int i = 1; i < letters.size(); i++) {
            final String letter = letters.get(i);
            if (LETTERS.matcher(letter).find()) {
                boolean isVowel = VOWELS.matcher(letter).find();
                if (isVowel) {
                    index = i;
                    break;
                }
            }
        }
        if (Character.isUpperCase(letters.get(0).charAt(0))) {
            letters.set(0, letters.get(0).toLowerCase());
            letters.set(index, letters.get(index).toUpperCase());
        }
        final String letter = letters.get(letters.size() - 1);
        boolean isPunctuated = !LETTERS.matcher(letter).find();
        if (isPunctuated) {
            letters.remove(letter);
        }
        sb.append(letters.stream().skip(index).limit((long) letters.size() - index).collect(Collectors.joining()))
                .append(letters.stream().limit(index).collect(Collectors.joining()))
                .append("ay");
        if (isPunctuated) {
            sb.append(letter);
        }
//        System.out.println(sb.toString());
    }
}
