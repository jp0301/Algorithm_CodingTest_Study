/*
* 반복문
* 10871번
* X보다 작은 수
*/


import java.util.*;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int x = sc.nextInt();		
		int arr[] = new int[n];
		
		for(int i = 0; i < n; i++) {
			int num = sc.nextInt();
			arr[i] = num;
		}
		sc.close();
		
		for(int j = 0; j < n; j++) {
			if(arr[j] < x) {
				System.out.print(arr[j] + " ");
			}
		}
		

		
		
		
		
	}
}
