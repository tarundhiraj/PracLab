/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Node{
	int data;
	Node left, right;
	
	public Node(int data){
		this.data = data;
		this.left = null;
		this.right = null;
	}
	
}

class BinaryTree
{
	Node root;
	
	private static void serialiseTree(Node root, FileWriter fw){
		if(root == null){
			fw.write(-1);
			return;
		}

		fw.write(root.data);
		serialiseTree(root.left, fw);
		serialiseTree(root.right, fw);
	}

	private static void deserializeTree(Node root, Scanner sc){
		int s;
		if((s = sc.nextInt()) == null || s == -1){
			return;
		}

		root = new Node(s);

		deserializeTree(root.left, sc);
		deserializeTree(root.right, sc);
	}
	
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Node root = new Node(1);
		root.left = new Node(2);
		root.right = new Node(3);
		root.left.left = new Node(4);
		root.left.right = new Node(5);

		
		
		
	
	}
}