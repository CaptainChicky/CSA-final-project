import java.math.BigInteger;

public class PrivateKey extends keygen{

    public PrivateKey(long num1, long num2) {
        super(num1, num2);
    }

    public BigInteger giveD() {
        return (super.giveE()).modInverse(BigInteger.valueOf(super.totient()));
    }

    @Override
    public void getKey() {
        System.out.println("n = " + super.giveN());
        System.out.println("d = " + this.giveD());
    }
}
