package edabit;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * https://edabit.com/challenge/Mgrj26S3LwM8CLAdL
 */
public class Sherlock {

    public static void main(String[] args) {
        System.out.println(sherlock("abba"));
        System.out.println(sherlock("aabbcd"));
        System.out.println(sherlock("aabbccddeefghi"));
        System.out.println(sherlock("abcdefghhgfedecba"));
    }

    private static String sherlock(String s) {
        System.out.println(s);
        Map<String, Integer> charToFreq = new LinkedHashMap<>(s.length());
        for (int i = 0; i < s.length(); i++) {
            String sub = s.substring(i, i + 1);
            Integer freq = charToFreq.getOrDefault(sub, 0);
            charToFreq.put(sub, ++freq);
        }
        System.out.println(charToFreq);
        Map<Integer, Integer> freqToCount = new LinkedHashMap<>(charToFreq.size());
        for (Map.Entry<String, Integer> entry : charToFreq.entrySet()) {
            Integer v = freqToCount.getOrDefault(entry.getValue(), 0);
            freqToCount.put(entry.getValue(), ++v);
        }
        System.out.println(freqToCount);
        if (freqToCount.size() == 0 || freqToCount.size() == 1) {
            return "YES";
        } else if (freqToCount.size() > 2) {
            return "NO";
        }
        for (Map.Entry<Integer, Integer> entry : freqToCount.entrySet()) {
            if (entry.getValue() == 1) {
                return "YES";
            }
        }
        return "NO";
    }
}
