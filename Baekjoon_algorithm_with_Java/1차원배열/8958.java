/*
* 1차원 배열
* 8958번
* ox퀴즈
*/

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		
		Scanner sc = new Scanner(System.in);
		
		String arr[] = new String[sc.nextInt()];
		
		//String 배열 arr의 각 원소에 문자열을 저장해준다.
		for(int i=0; i < arr.length; i++) {
			arr[i] = sc.next();
		}
		sc.close();
		
		//cnt는 몇 번 연속했는지, sum은 누적 합산 값을 나타내는 변수로 선언해준다.
		for(int i = 0; i < arr.length; i++) {
			int cnt = 0; // 연속 횟수
			int sum = 0; // 누적 합산
			
			//for문으로 한 원소당 String의 길이만큼 반복하여 해당 원소의 문자열을 charAt() 메소드를 통해 하나하나 검사한다.
			for(int j=0; j < arr[i].length(); j++) {
				//만약 O라는 문자가 나타나면 cnt 1증가 X문자이면 0으로 초기화
				if(arr[i].charAt(j) == 'O') {
					cnt++;
				} else {
					cnt = 0;
				}
				//sum에 cnt 값 누적
				sum += cnt;
			}
				
			System.out.println(sum);
		}
	}
}

// bufferedReader 풀이
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
		StringBuilder sb = new StringBuilder();
		int test_case = Integer.parseInt(br.readLine());	//테스트 케이스
		
		String arr[] = new String[test_case];
 
		for (int i = 0; i < test_case; i++) {
			arr[i] = br.readLine();
		}
 
		
		for (int i = 0; i < test_case; i++) {
			
			int cnt = 0;	// 연속횟수
			int sum = 0;	// 누적 합산 
			
			for (int j = 0; j < arr[i].length(); j++) {
				
				if (arr[i].charAt(j) == 'O') {
					cnt++;
				} else {
					cnt = 0;
				}
				sum += cnt;
			}
			
			sb.append(sum).append('\n');
		}
		
		System.out.print(sb);
	}
}
