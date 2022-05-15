/*
* 1차원 배열
* 10818번
* 최소,최대
* 
*/

import java.util.*;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);	
		int N = sc.nextInt();
		int arr[] = new int[N];
		
		for(int i=0; i < N; i++) {
			arr[i] = sc.nextInt();
		}
		
		//최솟값
		int min = arr[0];
		for (int k=1; k < N; k++) {
			if(min > arr[k]) {
				min = arr[k];
			}
		}
	
		// 최댓값
		int max = arr[0];
		for (int j=1; j < N; j++) {
			if(max < arr[j]) {
				max = arr[j];
			}
		}
		System.out.print(min + " " + max);

	}
}


// 다른 풀이 방법
import java.util.*;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);	
		int N = sc.nextInt();
		int arr[] = new int[N];
		
		for(int i=0; i< N; i++) {
			arr[i] = sc.nextInt();
		}
		
		sc.close();
		Arrays.sort(arr);
		System.out.print(arr[0] + " " + arr[N-1]);

	}
}
