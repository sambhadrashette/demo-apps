import org.junit.jupiter.api.*;

class FizzBuzzTest {

    FizzBuzz fizzBuzz;

    @BeforeEach
    public void beforeEach() {
        fizzBuzz =  new FizzBuzz();
    }

    @DisplayName("Play FizzBuzz with number = 1")
    @Test
    public void testNumber() {
        String actualResponse = fizzBuzz.play(1);
        Assertions.assertEquals("1", actualResponse);
    }

    @DisplayName("Play FizzBuzz with number = 3")
    @Test
    public void testFizz() {
        String actualResponse = fizzBuzz.play(3);
        Assertions.assertEquals("Fizz", actualResponse);
    }

    @DisplayName("Play FizzBuzz with number = 5")
    @Test
    public void testBuzz() {
        String actualResponse = fizzBuzz.play(5);
        Assertions.assertEquals("Buzz", actualResponse);
    }


    @DisplayName("Play FizzBuzz with number = 0 to throw exception")
    @Test
    public void testException() {
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
                fizzBuzz.play(0);
        });
    }

    //for ignoring test
    @Disabled
    @DisplayName("Play FizzBuzz with number = 2")
    @Test
    public void testIgnoredTest() {
        String actualResponse = fizzBuzz.play(2);
        Assertions.assertEquals("2", actualResponse);
    }

}