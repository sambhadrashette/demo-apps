package demo.hangman;

public interface MockScoreDB {
    boolean writeScoreDB(String word, double score);
}
