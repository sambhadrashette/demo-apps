package demo.hangman;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Hangman {
    private Set<String> usedWords = new HashSet<>();
    private List<String> wordsList = new ArrayList<>();
    public static final int MAX_ATTEMPTS = 10;
    private int remainingAttempts = 0;
    private int score = 0;
    MockScoreDB scoreDB = null;

    public Hangman() {

    }

    public Hangman(MockScoreDB scoreDB) {
        this.scoreDB = scoreDB;
    }

    public int countAlphabet(String word, char alphabet) {
        int result = 0;
        for (char c : word.toCharArray()) {
            if (c == alphabet) {
                result++;
            }
        }
        return result;
    }

    public String fetchWord(int requestedLength) {
        remainingAttempts = MAX_ATTEMPTS;
        for (String result : wordsList) {
            if (result.length() != requestedLength) continue;
            else if (usedWords.add(result)) return result;
        }
        return null;
    }

    public void loadWords() {
        String word = null;
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader("WordSource.txt"))) {
            while ((word = bufferedReader.readLine()) != null) {
                wordsList.add(word);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String fetchClue(String word) {
        StringBuilder result = new StringBuilder();
        for (int count = 0; count < word.length(); count++) {
            result.append("-");
        }
        return result.toString();
    }

    public String fetchClue(String word, String clue, char guess) {
        if (guess >= 'A' && guess <= 'Z') guess+= 32;
        if (guess < 'a' || guess > 'z' ) throw new IllegalArgumentException("Invalid character");
        StringBuilder newClue = new StringBuilder();
        for (int counter = 0; counter < word.length(); counter++) {
            if (guess == word.charAt(counter) && guess != clue.charAt(counter)) {
                newClue.append(guess);
                score += (double)MAX_ATTEMPTS/word.length();
            } else newClue.append(clue.charAt(counter));
        }
        remainingAttempts--;
        return newClue.toString();
    }

    public int getScore() {
        return score;
    }

    public int getRemainingAttempts() {
        return remainingAttempts;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public boolean saveWordScore(String word, int score) {
        return this.scoreDB.writeScoreDB(word, score);
    }
}
