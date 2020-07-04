package edabit.expert;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * https://edabit.com/challenge/BWm34MorRuaJXiaz6
 */
public class VignereCipher {

    private static final int CIPHER_LENGTH = 26;
    private static final String SPOILER = "spoiler";
    private static final String PYTHON = "python";
    private static final Map<Character, Integer> vignere = new LinkedHashMap<>(CIPHER_LENGTH);
    private static final Map<Integer, Character> vignereInverse = new LinkedHashMap<>(CIPHER_LENGTH);

    static {
        buildCiphers();
    }

    public static void main(String[] args) {
        System.out.println("Soylent green is people. -> " + vignereEncipher("Soylent green is people.", SPOILER));
        System.out.println("Darth Vader is Luke's father. -> " + vignereEncipher("Darth Vader is Luke's father.", SPOILER));
        System.out.println("VPFBSZRVTFQDPLCTGNLXYWG -> " + vignereDecipher("VPFBSZRVTFQDPLCTGNLXYWG", SPOILER));
        System.out.println("HMRSSAIEKLSAXQILCCAC -> " + vignereDecipher("HMRSSAIEKLSAXQILCCAC", PYTHON));
        System.out.println("SOYLENTGREENISPEOPLE -> " + vignereEncipher("SOYLENTGREENISPEOPLE", PYTHON));
    }

    private static String vignereDecipher(final String message, String key) {
//        System.out.println(message);
//        System.out.println(key);
        key = getKey(message, key);
//        System.out.println(key);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < message.length(); i++) {
            Integer m = vignere.get(message.charAt(i));
            Integer k = vignere.get(key.charAt(i));
            Character decipheredChar = vignereInverse.get(((m - k) + CIPHER_LENGTH) % CIPHER_LENGTH);
            sb.append(decipheredChar);
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
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < message.length(); i++) {
            Integer m = vignere.get(message.charAt(i));
            Integer k = vignere.get(key.charAt(i));
            Character encipheredChar = vignereInverse.get((m + k) % CIPHER_LENGTH);
            sb.append(encipheredChar);
        }
        return sb.toString();
    }

    private static void buildCiphers() {
        int i = 0;
        for (char c = 'A'; c <= 'Z'; c++) {
            vignere.put(c, i);
            vignereInverse.put(i++, c);
        }
    }

    private static String getKey(final String message, String key) {
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
