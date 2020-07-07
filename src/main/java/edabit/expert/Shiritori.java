package edabit.expert;

import lombok.Getter;
import lombok.NoArgsConstructor;
import org.apache.commons.lang3.StringUtils;

import java.util.LinkedList;
import java.util.List;

/**
 * https://edabit.com/challenge/rqum6rzyZQrC43Ldv
 */
@Getter
@NoArgsConstructor
public class Shiritori {

    private final List<String> words = new LinkedList<>();
    private boolean gameOver = false;

    public String play(String word) {
        if (StringUtils.isBlank(word)) {
            return "invalid input";
        }
        if (words.isEmpty()) {
            words.add(word.toLowerCase());
            return words.toString();
        }
        String lastWord = words.get(words.size() - 1);
        if (words.contains(word) || lastWord.charAt(lastWord.length() - 1) != word.charAt(0)) {
            gameOver = true;
            return "game over";
        }
        words.add(word.toLowerCase());
        return words.toString();
    }

    public String restart() {
        words.clear();
        gameOver = false;
        return "game restarted";
    }

    public static void main(String[] args) {
        Shiritori shiritori = new Shiritori();
        System.out.println(shiritori.play("apple"));
        System.out.println(shiritori.play("ear"));
        System.out.println(shiritori.play("rhino"));
        System.out.println(shiritori.play("corn"));
        System.out.println(shiritori.getWords());
        System.out.println(shiritori.restart());
        System.out.println(shiritori.getWords());
        System.out.println(shiritori.play("hostess"));
        System.out.println(shiritori.play("stash"));
        System.out.println(shiritori.play("hostess"));
    }
}
