import java.util.Random;

public class test {

	public static void main(String[] args) {
		 Random random = new Random();
		 Equations [] arr = new Equations[10];
         int y,z,t,s;
		 for(int i=1 ; i < 10 ; i++ )
		 {
			  s = random.nextInt(3);
			  y =  random.nextInt(10);
			  z =  random.nextInt(10);
			  t =  random.nextInt(10);
			  if (s==0) {arr[i] = new LinearEquation(y,z); arr[i].solveEquation();}
			  if (s==1) {arr[i] = new QuadraticEquation(y,z,t); arr[i].solveEquation();}
			  if (s==2) {arr[i] = new ExponentialEquation(y,z);arr[i].solveEquation();}	
		 }
	}
}
