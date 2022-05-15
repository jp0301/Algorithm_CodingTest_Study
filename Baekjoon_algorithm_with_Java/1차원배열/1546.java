/*
* 1차원 배열
* 1536번
* 평균
*/


import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		double arr[] = new double[Integer.parseInt(br.readLine())];
		
		//공백까지 한 줄로 한 번에 받기 때문에 반드시 문자열 분리를 해주어야 한다.
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		for(int i=0; i < arr.length; i++) {
			arr[i] = Double.parseDouble(st.nextToken());
		}
		
		double sum = 0;
		Arrays.sort(arr);
		

		for(int j=0; j < arr.length; j++) {
			sum += ((arr[j] / arr[arr.length -1]) * 100);
		}
		System.out.println(sum / arr.length);
		
		

	}
}
