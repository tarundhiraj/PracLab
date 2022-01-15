/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class RadixSort
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
	
	private static void countSort(int[] arr, int exp){
		if(arr.length == 0){
			return;
		}

		int place[] = new int[10];
		int output[] = new int[arr.length];
		Arrays.fill(place, 0);

		//Fill the places

		for(int i = 0; i < arr.length ; ++i){
			++place[(arr[i]/exp)%10];
		}

		//Summation of places
		for(int i = 1 ; i < place.length; ++i){
			place[i] =+ place[i-1];
		}

		for(int i = arr.length - 1; i >= 0; --i){
			output[place[(arr[i]/exp)%10]-1] = arr[i];
			--place[(arr[i]/exp)%10];
		}

		for(int i = 0 ; i < output.length; ++i){
			arr[i] = output[i];
		}
	}

	public static int[] radixSort(int[] arr){
		int maxNum = findMax(arr);


		for(int exp = 1; (maxNum/exp) > 0; exp = exp * 10){
			countSort(arr, exp);
		}

		return arr;
	}
	
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		int arr[] = {170, 45, 75, 90, 802, 24, 2, 66};
		int narr[] = radixSort(arr);
		for(int i : narr)
			System.out.println(i);
	}
}