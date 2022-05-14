/*
* 반복문 #8
* 11022번
* A+B - 8
*/


import java.util.*;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int arr[] = new int[n];
		
		int arr1[] = new int[n];
		int arr2[] = new int[n];
		
		
		for(int i = 0; i < n; i++) {
			int a = sc.nextInt();
			arr1[i] = a;
			int b = sc.nextInt();
			arr2[i] = b;
			
			arr[i] = arr1[i] + arr2[i];
		}
		sc.close();
		
		for(int k = 0; k < n; k++) {
			System.out.println("Case #" + (k+1) + ": " + arr1[k] + " + " + arr2[k] + " = " + arr[k]);
		}
       
	
	}
}
