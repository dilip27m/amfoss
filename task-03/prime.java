
import java.util.*;

public class prime {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int n;

        System.out.println("Enter a number : ");
        n = input.nextInt();

        
        System.out.println("The Prime numbers up to " + n + ": ");
        for (int i = 2; i <= n; i++) {
            int count = 0;
            for (int j = 1; j <= i; j++) {
                if (i % j == 0) {
                    count++;
                }

            }
            if (count == 2) {
                System.out.println(i);
            }
        }
        System.out.println(" These are the prime numbers upto "+ n);
        input.close();
    }
}