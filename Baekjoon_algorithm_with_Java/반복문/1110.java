/*
* 반복문
* 1110번
* 더하기 사이클
*/

import java.util.*;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);	
		int N = sc.nextInt();
		
		if(N < 10) {
			N *= 10;
		}
		
		int num1, num2, sum = N, cnt = 0;
		
		while(true) {
			num1 = sum / 10;
			num2 = sum % 10;
			sum = num1 + num2;
			
			sum = (num2 * 10) + sum % 10;
			
			cnt++;
			if(sum == N) {
				break;
			}
		}
		System.out.println(cnt);
	}
}
