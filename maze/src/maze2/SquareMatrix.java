package maze2;

public class SquareMatrix {
	private static void paths(int mat[][], int m, int n, int i, int j, int path[], int idx) {
		path[idx] = mat[i][j];

//left bottom of the matrix can only move to right
		if (i == m - 1) {
			for (int k = j + 1; k < n; k++) {
				path[idx + k - j] = mat[i][k];
			}
			for (int l = 0; l < idx + n - j; l++) {
//				System.out.print(i+" - "+j+" = "+path[l] + "\t");
				System.out.print(path[l] + " ");
			}
			System.out.println();
			return;
		}

// top right corner of the matrix can only move down 
		if (j == n - 1) {
			for (int k = i + 1; k < m; k++) {
				path[idx + k - i] = mat[k][j];
			}
			for (int l = 0; l < idx + m - i; l++) {
//				System.out.print(i+" "+j+" "+path[l] + "\t");
				System.out.print(path[l] + " ");
			}
			System.out.println();
			return;
		}
// Print all the paths that are possible after moving down 
		paths(mat, m, n, i + 1, j, path, idx + 1);

// Print all the paths that are possible after moving right 
		paths(mat, m, n, i, j + 1, path, idx + 1);
	}

 
	public static void main(String[] args) {
		
		int mat[][] = { 
				{ 11, 12, 13, 14 , 15 },  
				{ 21, 22, 23, 24 , 25 },
				{ 31, 32, 33, 34 , 35 },
				{ 41, 42, 43, 44 , 45 },
				{ 51, 52, 53, 54 , 55 }};
		int m = mat.length;
		int n = mat[0].length;
		System.out.printf("number of rows:%d number of columns:%d \n",m,n);
		int maxPathLenght = m + n - 1;
		paths(mat, m, n, 0, 0, new int[maxPathLenght], 0);
	}

}
