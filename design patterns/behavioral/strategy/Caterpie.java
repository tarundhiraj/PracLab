public class Caterpie extends Pokemon{
	public Caterpie(String name, int powerLevel, Capability cap){
		super(name, powerLevel, cap);
	}

	public String showCapability(){
		cap.getCapability();
	}

	public String getName(){
		return name;
	}
}