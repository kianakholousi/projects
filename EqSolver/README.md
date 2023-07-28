
# Equation Solver

This project provides a simple equation solver to solve linear, exponential, and quadratic equations. It includes the following classes:

- `Equations`: An interface that defines the `solveEquation()` method.
- `ExponentialEquation`: A class that implements the `Equations` interface and solves exponential equations.
- `LinearEquation`: A class that implements the `Equations` interface and solves linear equations.
- `QuadraticEquation`: A class that implements the `Equations` interface and solves quadratic equations.
- `test`: A test class that generates and solves random equations using the equation solver.

## Usage

To use the equation solver, follow these steps:

1. Create an instance of the `Equations` interface.
2. Call the `solveEquation()` method on the instance to solve the equation.

Here's an example of how to use the equation solver:

```java
public static void main(String[] args) {
    Random random = new Random();
    Equations[] arr = new Equations[10];
    int y, z, t, s;
    for (int i = 1; i < 10; i++) {
        s = random.nextInt(3);
        y = random.nextInt(10);
        z = random.nextInt(10);
        t = random.nextInt(10);
        if (s == 0) {
            arr[i] = new LinearEquation(y, z);
            arr[i].solveEquation();
        }
        if (s == 1) {
            arr[i] = new QuadraticEquation(y, z, t);
            arr[i].solveEquation();
        }
        if (s == 2) {
            arr[i] = new ExponentialEquation(y, z);
            arr[i].solveEquation();
        }
    }
}
```

