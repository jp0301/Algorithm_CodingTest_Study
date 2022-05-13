/*
* 반복문 #2
* 10950번
* A + B -3 문제
*/

import java.util.*;

public class Test {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int c = sc.nextInt();
		int arr[] = new int[c];
		
		for(int i = 0; i < c; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			arr[i] = a + b;
		}
		sc.close();
		
		for(int k : arr) {
			System.out.println(k);
		}
	}
}

// BufferedReader 을 쓰는 방식
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Test {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			sb.append(Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken()));
			sb.append('\n');
		}
		
		
		System.out.println(sb);

		
		
		
	}
}


