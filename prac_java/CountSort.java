/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class CountSort
{
	public static int findMax(int arr[]){
		int max = Integer.MIN_VALUE;
		
		for(int i = 0 ; i < arr.length; ++i){
			if(max < arr[i]){
				max = arr[i];
			}
		}
		
		return max;
	}
	
	public static int[] countSort(int[] arr){
		if(arr.length == 0){
			return null;
		}
		
		int output[] = new int[arr.length];
		int max = findMax(arr);
		int place[] = new int[max+1];
		
		Arrays.fill(place, 0);
		
		//count the occurance of each digit
		for(int i = 0 ; i < arr.length; ++i){
			++place[arr[i]];
		}
		
		//add the places
		for(int i = 1 ; i < place.length; ++i){
			place[i] += place[i-1];
		}
		
		for(int i = 0 ; i< arr.length; ++i){
			output[place[arr[i]]-1] = arr[i];
			--place[arr[i]];
		}
		
		return output;
	}
	
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		int arr[] = {1,4,1,2,7,5,2};
		int narr[] = countSort(arr);
		for(int i : narr)
			System.out.println(i);
	}
}