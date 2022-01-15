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

class Ideone
{
	Node root;
	
	private static void morrisTraversal(Node node){
		Node current, pre;
		current = node;
		
		if(node == null){
			return;
		}
		
		while(current != null){
			if(current.left == null){
				System.out.print(current.data + " ");
				current = current.right;
			}else{
				pre = current.left;
				//Traverse to the right most node in the tree
				while(pre.right!=null && pre.right!=current){
					pre = pre.right;
				}
				
				if(pre.right==null){
					pre.right = current;
					current = current.left;
				}else{
					//correct the links
					pre.right = null;
					System.out.println(current.data + " ");
					current = current.right;
				}
			}
		}
		
	}
	private static int height(Node node){
		if(node == null){
			return 0;
		}else{
			return Math.max(height(node.left), height(node.right)) + 1;
		}
	}
	
	private static void levelOrderTraversalSpiral(Node node){
		int h = height(node);
		boolean order = false;
		for(int i = 1; i<=h; ++i){
			printTree(node, i, order);
			order = !order;
		}
	}
	
	private static void printTree(Node node, int level, boolean order){
		if(node == null){
			return;
		}else if(level == 1){
			System.out.print(node.data + " ");
		}else{
			if(!order){
				printTree(node.left, level-1, order);
				printTree(node.right, level-1, order);
			}else{
				printTree(node.right, level-1, order);
				printTree(node.left, level-1, order);
			}
		}
	}
	private static int diameter(Node node){
		//We got to calculate diameter that is the maximum of these three
		//1. diameter of left tree
		//2. diameter of right tree
		//3. height of left + height or right + 1
		if(node == null){
			return 0;
		}
		
		int ldiameter = diameter(node.left);
		int rdiameter = diameter(node.right);
		int lheight = height(node.left);
		int rheight = height(node.right);
		
		return Math.max(lheight + rheight + 1, Math.max(ldiameter, rdiameter));
	}
	
	private static void printAtDistance(Node node, int k){
		if(node == null){
			return;
		}else{
			_printAtDistance(node,k-1);
		}
	}
	
	private static void _printAtDistance(Node node, int k){
		if(node == null){
			return;
		}
		
		if(k == 1){
			System.out.println(node.data + " ");
		}else{
			_printAtDistance(node.left, k -1);
			_printAtDistance(node.right, k -1);
		}
	}
	
	
	
	
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Node root = new Node(1);
		root.left = new Node(2);
		root.right = new Node(3);
		root.left.left = new Node(4);
		root.left.right = new Node(5);
		
		//morrisTraversal(root);
		
		//levelOrderTraversalSpiral(root);
		
		printAtDistance(root, 2);
	}
}