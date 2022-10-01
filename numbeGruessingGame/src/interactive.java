import java.util.Random;
import java.util.Scanner;

public class interactive {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome");
        System.out.println("please enter your name: ");
        String name = scanner.next();
        System.out.println("Hello  " + name);
        System.out.println("do you want to start the game?");
        System.out.println("\t 1,Yes ");
        System.out.println("\t 2,No ");
        int a = scanner.nextInt();
        while (a != 1) {
            System.out.println("do you want to start the game?");
            System.out.println("\t 1,Yes ");
            System.out.println("\t 2,No ");
             a = scanner.nextInt();
        }
        if ( a==1 )
        {
            Random random = new Random();
            int number = random.nextInt(20);
            System.out.println(" you have 5 guesses ");
            for (int i = 1 ; i<=5 ; i ++)
            {
                System.out.println("guess the number (0-20) ");
                System.out.println("please enter your guess: ");
                int answer = scanner.nextInt();
                 if (number == answer)
                 {
                    System.out.println("congrats! you have found the number in " + i +" tries");
                    break;
                 }
                  else if (answer > number)
                  {
                    System.out.println("Lower ");
                  }
                  else if (answer < number)
                  {
                    System.out.println("Higher ");
                  }
                 if (i == 5)
                 {
                    System.out.println("the answer was = " + answer);
                    System.out.println("Game Over");
                 }
            }
        }
        else
        {
            System.out.println("Good bye");
        }
    }
}
