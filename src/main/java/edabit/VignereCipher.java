package edabit;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * https://edabit.com/challenge/BWm34MorRuaJXiaz6
 */
public class VignereCipher {

    public static void main(String[] args) {
        System.out.println("Soylent green is people. -> " + vignereEncipher("Soylent green is people.", "spoiler"));
        System.out.println("Darth Vader is Luke's father. ->" + vignereEncipher("Darth Vader is Luke's father.", "spoiler"));
        System.out.println("HMRSSAIEKLSAXQILCCAC -> " + vignereDecipher("HMRSSAIEKLSAXQILCCAC", "python"));
        System.out.println("SOYLENTGREENISPEOPLE -> " + vignereEncipher("SOYLENTGREENISPEOPLE", "python"));
    }

    private static String vignereDecipher(String message, String key) {
//        System.out.println(message);
//        System.out.println(key);
        key = getKey(message, key);
//        System.out.println(key);
        Map<Character, Integer> vignere = new LinkedHashMap<>();
        Map<Integer, Character> vignereInverse = new LinkedHashMap<>();
        int i = 0;
        for (char c = 'A'; c <= 'Z'; c++) {
            vignere.put(c, i);
            vignereInverse.put(i++, c);
        }
        StringBuilder sb = new StringBuilder();
        for (int j = 0; j < message.length(); j++) {
            Integer m = vignere.get(message.charAt(j));
            Integer k = vignere.get(key.charAt(j));
            Character encipher = vignereInverse.get(((m - k) + vignere.size()) % vignere.size());
            sb.append(encipher);
        }
        return sb.toString();
    }

    private static String vignereEncipher(String message, String key) {
//        System.out.println(message);
//        System.out.println(key);
        message = message.replaceAll("[^a-zA-Z0-9]", "").toUpperCase();
//        System.out.println(message);
        key = getKey(message, key);
//        System.out.println(key);
        Map<Character, Integer> vignere = new LinkedHashMap<>();
        Map<Integer, Character> vignereInverse = new LinkedHashMap<>();
        int i = 0;
        for (char c = 'A'; c <= 'Z'; c++) {
            vignere.put(c, i);
            vignereInverse.put(i++, c);
        }
        StringBuilder sb = new StringBuilder();
        for (int j = 0; j < message.length(); j++) {
            Integer m = vignere.get(message.charAt(j));
            Integer k = vignere.get(key.charAt(j));
            Character encipher = vignereInverse.get((m + k) % vignere.size());
            sb.append(encipher);
        }
        return sb.toString();
    }

    private static String getKey(String message, String key) {
        StringBuilder sb = new StringBuilder();
        int j = 0;
        for (int i = 0; i < message.length(); i++) {
            sb.append(key.substring(j, j + 1).toUpperCase());
            ++j;
            if (j >= key.length()) {
                j = 0;
            }
        }
        key = sb.toString();
        return key;
    }
}
