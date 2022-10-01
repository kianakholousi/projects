
public class ExponentialEquation implements  Equations{
	private double a,b;
	@Override
	public void solveEquation() {
		if(a>0)
		{
			double x;
			x = Math.log((b/a));
			System.out.printf("ExponentialEquation %.0fe^x=%.0f  x=%f \n",a,b,x);
		}
		else
		{
			System.out.println("a needs to be greater than 0");
		}
		
	}
	public ExponentialEquation(double a, double b) {
		super();
		this.a = a;
		this.b = b;
	}
	

}
