package demo.hangman;


import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.mockito.Mockito;

import java.util.HashSet;
import java.util.Random;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public class HangmanTest {
    Hangman hangman;
    Random random;
    int requestedLength;

    @BeforeAll
    public void setup() {
        hangman = new Hangman();
        random = new Random();
        hangman.loadWords();
    }

    @AfterAll
    public void destroy() {
        hangman = null;
        random = null;
    }

    @BeforeEach
    public void beforeEach() {
        requestedLength = random.nextInt(6) + 5;
        hangman.setScore(0);
    }

    @Test
    void test_alphabetCountInWord() {
        String word = "pizza";
        char alphabet = 'a';

        int count = hangman.countAlphabet(word, alphabet);
        assertEquals(1, count);
    }

    @Test
    void test_lengthOfFetchedWordRandom() {
        hangman.loadWords();
        String word = hangman.fetchWord(requestedLength);
        assertTrue(requestedLength == word.length());
    }

    @Test
    void test_uniquenessOfFetchedWord() {
        Set<String> usedWordSet = new HashSet<>();
        int round = 0;
        String word = null;
        hangman.loadWords();

        while (round < 100) {
            word = hangman.fetchWord(requestedLength);
            round++;
            assertTrue(usedWordSet.add(word));
        }
    }

    @Test
    void test_fetchClueBeforeAnyGuess() {
        String clue = hangman.fetchClue("pizza");
        assertEquals("-----", clue);
    }

    @Test
    void test_fetchClueAfterCorrectGuess() {
        String clue = hangman.fetchClue("pizza");
        String newClue = hangman.fetchClue("pizza", clue, 'a');
        assertEquals("----a", newClue);
    }

    @Test
    void test_fetchClueAfterIncorrectGuess() {
        String clue = hangman.fetchClue("pizza");
        String newClue = hangman.fetchClue("pizza", clue, 'x');
        assertEquals("-----", newClue);
    }

    @Test
    void test_whenInvalidGuessThenFetchClueThrowsException() {
        assertThrows(IllegalArgumentException.class, () -> {
            hangman.fetchClue("pizza", "-----", '1');
        });
    }

    @Test
    void test_whenInvalidGuessThenFetchClueThrowsExceptionWithMessage() {
        Exception e = assertThrows(IllegalArgumentException.class, () -> {
            hangman.fetchClue("pizza", "-----", '1');
        });
        assertEquals("Invalid character", e.getMessage());
    }

    @Test
    void test_remainingAttemptsBeforeAnyGuess() {
        hangman.fetchWord(requestedLength);
        assertEquals(Hangman.MAX_ATTEMPTS, hangman.getRemainingAttempts());
    }

    @Test
    void test_remainingAttemptsAfterOneGuess() {
        hangman.fetchWord(requestedLength);
        String newClue = hangman.fetchClue("pizza", "-----", 'a');
        assertEquals(Hangman.MAX_ATTEMPTS - 1, hangman.getRemainingAttempts());
    }

    @Test
    void test_scoreBeforeAnyGuess() {
        hangman.fetchWord(requestedLength);
        assertEquals(0, hangman.getScore());
    }

    @Test
    void test_scoreAfterCorrectGuess() {
        String word = "pizza";
        String clue = "-----";
        char guess = 'a';
        hangman.fetchClue(word, clue, guess);
        assertEquals((double) Hangman.MAX_ATTEMPTS / word.length(), hangman.getScore());
    }

    @Test
    void test_saveScoreUsingMockDB() {
        MockScoreDB mockScoreDB = Mockito.mock(MockScoreDB.class);
        Hangman hangman = new Hangman(mockScoreDB);
        Mockito.when(mockScoreDB.writeScoreDB("apple", 10)).thenReturn(true);
        assertTrue(hangman.saveWordScore("apple", 10));
    }

}
