public class Main{
	public static void main(String args[]){
		Pokemon caterpie = new Caterpie("Caterpie", 1000, new CantFly());
		Pokemon butterfree = new Butterfree("Butterfree", 2000, new Fly());
		System.out.println(caterpie.getName() + " " + caterpie.getCapability());
		System.out.println(butterfree.getName() + " " + butterfree.getCapability());
	}
}