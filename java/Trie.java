//Program to implement the Trie Data Structure

import java.util.HashMap;


public class Trie{
	
	class TrieNode{
		HashMap<Character, TrieNode> characters;
		boolean wordPresent;

		public TrieNode(){
			characters = new HashMap<>();
			wordPresent = false;
		}

	}


	public final TrieNode root;

	public Trie(){
		root  = new TrieNode();
	}


	public void insertWord(String word){
		TrieNode current = root;
		for(int i = 0 ; i < word.length(); ++i){
			char ch = word.charAt(i);

			TrieNode node = current.characters.get(ch);

			//See if character is not present in the map
			if(node == null){
				//We insert the new character
				node = new TrieNode();
				current.characters.put(ch, node);
				current = node;
			}

			current = node;
		}

		current.wordPresent = true;

	}

	public boolean searchWord(String word){
		TrieNode current = root;

		for(int i = 0 ; i < word.length(); ++i){
			char ch = word.charAt(i);
			TrieNode node = current.characters.get(ch);

			//See if the character is not present in the map
			if(node == null){
				return false; //Word is absent from the trie
			}

			current = node;
		}

		return current.wordPresent;
	}

	public boolean deleteWord(TrieNode node, String word, int index){
		
		if(index == word.length()){
			if(!node.wordPresent){
				return false;
			}

			node.wordPresent = false;

			return node.characters.size() == 0;

		}
		char ch = word.charAt(index);
		TrieNode n = node.characters.get(ch);

		if(n == null){
			return false;
		}

		boolean canDeleteCurrentNode = deleteWord(n, word, index+1);

		if(canDeleteCurrentNode){
			node.characters.remove(ch);

			return node.characters.size() == 0;
		}

		return false;
	}



	public static void main( String args[]){
		Trie trie = new Trie();
		trie.insertWord("abcd");
		trie.insertWord("abg");
		trie.insertWord("ghrce");
		trie.insertWord("bits");

		if(trie.searchWord("abcde")){
			System.out.println("Word is present in the trie");
		}else{
			System.out.println("Word is not present in the trie");
		}

		if(trie.deleteWord(trie.root, "bits", 0)){
			System.out.println("Word deleted!!");
		}else{
			System.out.println("Word can't be deleted");
		}
	}

}