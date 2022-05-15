/*
* 1차원 배열
* 2577번
* 숫자의 개수
*/

import java.io.*;
//import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		 
		int[] arr = new int[10];
		
		//val에다가 br.readLine으로 읽은 값을 곱해서 저장한다.
		int val = Integer.parseInt(br.readLine()) * Integer.parseInt(br.readLine()) * Integer.parseInt(br.readLine());
		
		// val의 int형을 string형으로 변환해준 뒤
		String str = String.valueOf(val);
		
		//for문을 통해 해당 문자열의 문자 값 - 48(또는 -'0')을 추출해 내 int 배열의 index값을 1증가 시킨다.
		for (int i = 0; i < str.length(); i++) {
			arr[(str.charAt(i) - 48)]++;
		}
		
		for (int v : arr) {
			System.out.println(v);
		}

	}
}
