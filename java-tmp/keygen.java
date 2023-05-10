import java.math.BigInteger;
public abstract class keygen {
    private final long p;
    private final long q;
    private final BigInteger E = BigInteger.valueOf(3);

    // n = p * q
    // let e be a number from >1 to <totient that GCD(totient, e)=1
    // (n, e) is public key
    // (n, d) is private key with e * d = 1 mod totient


    //Precondition: e is a number from >1 to <totient that GCD(totient, e)=1
    public keygen(long num1, long num2) {
        p = num1;
        q = num2;

        if (this.GCD(E, this.totient()) != 1) {
            throw new IllegalArgumentException();
        }
    }

    public long GCD(BigInteger a, long b) {
        if (b == 0) {
            return Integer.parseInt(String.valueOf(a));
        }
        return GCD(BigInteger.valueOf(b), Integer.parseInt(String.valueOf(a)) % b);
    }

    public long totient() {
        return (p - 1) * (q - 1);
    }

    public long giveN() {
        return p * q;
    }

    public BigInteger giveE() {
        return this.E;
    }

    public abstract void getKey();
}

