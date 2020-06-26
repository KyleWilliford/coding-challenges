package edabit;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/**
 * https://edabit.com/challenge/RkicZ4kkcSx8K3d4e
 *
 * ulam(4) ➞ 4
 * ulam(9) ➞ 16
 * ulam(206) ➞ 1856
 */
public class Ulam {
    public static void main(String[] args) {
        System.out.println(ulam(9));
    }

    private static Integer ulam(int n) {
        List<Integer> seq = new ArrayList<>();
        seq.add(1);
        seq.add(2);
        for (int k = seq.size(); k < n; k++) {
            System.out.println("Seq " + seq);
            Map<Integer, Integer> results = new TreeMap<>();
            for (int i = 0; i < seq.size(); i++) {
                for (int j = i + 1; j < seq.size(); j++) {
                    Integer result = seq.get(i) + seq.get(j);
                    if (result > seq.get(seq.size() - 1)) {
                        Integer frequency = results.getOrDefault(result, 0);
                        results.put(result, frequency + 1);
                    }
                }
            }
            System.out.println("results " + results);
            for (Map.Entry<Integer, Integer> entry : results.entrySet()) {
                if (entry.getValue() == 1) {
                    seq.add(entry.getKey());
                    break;
                }
            }
            if (seq.size() == n) {
                return seq.get(seq.size() - 1);
            }
        }
        return -1;
    }
}
