/*
* 반복문 #3
* 8393번
* 합
*/

import java.util.*;

public class Main {
	public static void main(String[] args) {
		
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = 0;
        
        for(int i = 1; i <= n; i++) {
        	a += i;
        }
        System.out.println(a);
	}
}
