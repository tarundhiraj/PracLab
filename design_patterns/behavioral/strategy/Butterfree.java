public class Butterfree extends Pokemon{
	public Butterfree(String name, int powerLevel, Capability cap){
		super(name, powerLevel, cap);
	}

	public String showCapability(){
		super.cap.getCapability();
	}

	public String getName(){
		return super.name;
	}
}