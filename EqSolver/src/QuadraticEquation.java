
public class QuadraticEquation implements  Equations{
	private double a,b,c;
	@Override
	public void solveEquation() {
		double d = ((a*a) - (4*b*c));
		double x1 , x2;
		if(d>0)
		{
			x1 = (-b + Math.sqrt(d))/(2*a);
			x2 = (-b - Math.sqrt(d))/(2*a);
			System.out.printf("QuadraticEquation: %.0fx^2+%.0fx+%.0f=0 x1=%f \n",a,b,c,x1);
			System.out.printf("QuadraticEquation: %.0fx^2+%.0fx+%.0f=0 x2=%f \n",a,b,c,x2);
		}
		if(d==0.0)
		{
			x1 = (-b + Math.sqrt(d))/(2*a);
			System.out.printf("QuadraticEquation %.0fx*x+%.0fx+%f=0 x=%f \n",x1);
		}
		else
		{
			System.out.println("this Equation dosen\'t have a real answer");
		}
		
	}
	public QuadraticEquation(double a, double b, double c) {
		super();
		this.a = a;
		this.b = b;
		this.c = c;
	}

}
