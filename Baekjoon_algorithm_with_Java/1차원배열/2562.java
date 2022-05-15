/*
* 1차원 배열
* 2562번
* 최댓값
*/

import java.util.*;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);	
		int arr[] = new int[9];
		
		for(int i=0; i < 9; i++) {
			arr[i] = sc.nextInt();
		}
		sc.close();
		
		int cnt = 0;
		int max = 0;
		int index = 0;
		
		for(int j: arr) { //for-each구문으로 arr배열의 원소를 하나씩 j에 저장한 뒤
			cnt++;
			
			if(j > max) { //마지막 j와 j값을 비교하여 j가 마지막 j값보다 크면 count값과 j값을 저장한다.
				max = j;
				index = cnt;
			}
		}
		System.out.print(max + "\n" + index);
		

	}
}
