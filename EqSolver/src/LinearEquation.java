
public class LinearEquation implements Equations {
	private double a, b;

	@Override
	public void solveEquation() {
		if (a > 0) {
			double x = -b / a;
			System.out.printf("LinearEquation: %.0fx+%.0f=0 x=%f \n",a,b,x);
		} else {
			System.out.println("a needs to be greater than 0");
		}

	}

	public LinearEquation(double a, double b) {
		super();
		this.a = a;
		this.b = b;
	}


}
