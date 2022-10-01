import java.util.Scanner;
import java.io.*;
public class KH3 {

	public static void main(String[] args) throws IOException {
		int ch1 = 0, ch2 = 0, n3=0, n4 = 0;
		String n, n1, n2;
		Education e = new Education();
		Student s = new Student();
		Scanner input = new Scanner(System.in);
		BufferedWriter Edu = new BufferedWriter(new FileWriter("Edu.txt"));
		BufferedWriter Stu = new BufferedWriter(new FileWriter("Stu.txt"));
		BufferedReader Redu = new BufferedReader(new FileReader("Edu.txt"));
		BufferedReader Rstu = new BufferedReader(new FileReader("Stu.txt"));
		
		System.out.println("Choices:\n 1.Education\n 2.Student\n 3.Exit");
		ch1 = input.nextInt();
		while (ch1 != 3) {
			System.out.println("1.Add\n2.Remove\n3.Change\n4.Show\n5.Save\n6.Read\n7.Exit");
			ch2 = input.nextInt();
			while (ch2 != 7) {
				if (ch1 == 1) {
					switch (ch2) {
					case 1:
						System.out.println("Name\tCode\tPhone Number\t");
						n = input.next();
						n1 = input.next();
						n3 = input.nextInt();
						e.ADD(n, n1, n3);
						break;
					case 2:
						System.out.println("Idex you want removed:");
						n4 = input.nextInt();
						e.Remove(n4 - 1);
						break;
					case 3:
						System.out.println("index(from 0)\tName\tCode\tPhone Number\t");
						n4 = input.nextInt();
						n = input.next();
						n1 = input.next();
						n3 = input.nextInt();
						e.Change(n4, n, n1, n3);
						break;
					case 4:
						e.Show();
						break;
					case 5:
				        e.Save(Edu);
				        break;
					case 6:
				        e.Read(Redu);
				        break;
					}
				}
				if (ch1 == 2) {

					switch (ch2) {
					case 1:
						System.out.println("Name\tStudent ID\tScore");
						n = input.next();
						n1 = input.next();
						n3 = input.nextInt();
						s.ADD(n, n1, n3);
						break;
					case 2:
						System.out.println("Idex you want removed:");
						n4 = input.nextInt();
						s.Remove(n4 - 1);
						break;
					case 3:
						System.out.println("index(from 0)\tName\tStudent ID\tScores\t");
						n4 = input.nextInt();
						n = input.next();
						n1 = input.next();
						n3 = input.nextInt();
						s.Change(n4, n, n1, n3);
						break;
					case 4:
						s.Show();
						break;
					case 5:
				        s.Save(Stu);
				        break;
					case 6:
				        s.Read(Rstu);
				        break;
					}
				}
				System.out.println("1.Add\n2.Remove\n3.Change\n4.Show\n5.Save\n6.Read\n7.Exit");
				ch2 = input.nextInt();
			}
			System.out.println("Choices:\n 1.Education\n 2.Student\n 3.Exit");
			ch1 = input.nextInt();
		}

	}
}