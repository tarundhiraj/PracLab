/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class BalancedBraces
{
	public static Set<String> getBalancedBraces(int n){
		HashSet<String> result = new HashSet<>();
		
		if(n == 1){
			result.add(new String("()"));
		}else{
			Set<String> perms = getBalancedBraces(n-1);
			for(String s : perms){
				for(int i = 0 ; i < s.length(); ++i){
					StringBuffer t = new StringBuffer();
					t.append(s.substring(0,i));
					t.append("()");
					t.append(s.substring(i));
					result.add(t.toString());
				}
			}
		}
		
		return result;
	}
	public static void main (String[] args) throws java.lang.Exception
	{
		for(String s : getBalancedBraces(5)){
			System.out.println(s);
		}
	}
}