/*
* 반복문 #8
* 11021번
* A+B - 7
*/

import java.util.*;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int arr[] = new int[n];
		
		
		for(int i = 0; i < n; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();       
			arr[i] = a + b;
		}
		sc.close();
		
		for(int k = 0; k < n; k++) {
			System.out.println("Case #" + (k+1) + ": "+ arr[k]);
		}
       
		
	}
}
