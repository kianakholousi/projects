# All possible path in a Maze 

The `maze2` package provides a `SquareMatrix` class that allows you to find all possible paths from the top left to the bottom right corner in a square matrix. This file provides an overview and instructions on how to use it.

## Installation

To use the `maze2` package, follow these steps:
1. Clone the repository from GitHub:
2. Import the `maze2` package into your project.

## Usage

The `SquareMatrix` class in the `maze2` package contains a `paths` method that finds all possible paths in a square matrix. Here's how you can use it:
customize by changing mat= 2D array as a square 
```java
import maze2.SquareMatrix;

public class Main {
    public static void main(String[] args) {
        int mat[][] = { 
            { 11, 12, 13, 14, 15 },  
            { 21, 22, 23, 24, 25 },
            { 31, 32, 33, 34, 35 },
            { 41, 42, 43, 44, 45 },
            { 51, 52, 53, 54, 55 }};
        int m = mat.length;
        int n = mat[0].length;
        System.out.printf("Number of rows: %d, Number of columns: %d\n", m, n);
        int maxPathLength = m + n - 1;
        SquareMatrix.paths(mat, m, n, 0, 0, new int[maxPathLength], 0);
    }
}
```

In the above example, we create a `SquareMatrix` object and call the `paths` method, passing in the square matrix `mat`, the number of rows `m`, the number of columns `n`, the starting position `(0, 0)`, an array to store the path, and the current index.

The `paths` method recursively finds all possible paths in the matrix and prints them to the console.
