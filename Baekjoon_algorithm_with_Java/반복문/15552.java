
/*
* 반복문 #5
* 15552번
* 빠른 A+B
*/

import java.io.*;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
       
       StringTokenizer st;
       int n = Integer.parseInt(br.readLine());
       
       
       for(int i = 0; i < n; i++) {
    	   st = new StringTokenizer(br.readLine());
    	   
    	   int a = Integer.parseInt(st.nextToken());
    	   int b = Integer.parseInt(st.nextToken());
    	   int sum = a + b;
    	   
    	   bw.write(sum + "\n");
       }
       bw.flush();
       bw.close();
       
		
	}
}
