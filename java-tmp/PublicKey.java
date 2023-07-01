public class PublicKey extends keygen {

    public PublicKey(long num1, long num2) {
        super(num1, num2);
    }

    @Override
    public void getKey() {
        System.out.println("n = " + super.giveN());
        System.out.println("e = " + super.giveE());
    }
}
