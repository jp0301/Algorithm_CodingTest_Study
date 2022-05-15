/*
* 1차원 배열
* 3052번
* 나머지
*/

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		HashSet<Integer> h = new HashSet<Integer>();
		
		for(int i = 0; i< 10; i++) {
			h.add(Integer.parseInt(br.readLine()) % 42);
		}
		
		System.out.println(h.size());

	}
}



// 배열 사용한 풀이
public class Main {
	public static void main(String[] args) throws IOException {
		
		boolean[] arr = new boolean[42];
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int i = 0; i< 10; i++) {
			arr[Integer.parseInt(br.readLine()) % 42] = true;
		}
		
		int cnt = 0;
		for(boolean value: arr) {
			if(value) {
				cnt++;
			}
		}
		System.out.println(cnt);

	}
}
