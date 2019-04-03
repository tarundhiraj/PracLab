public abstract class Pokemon{
	private String name;
	private int powerLevel;
	private Capability cap;
	public Pokemon(String name, int powerLevel, Capability cap){
		this.name = name;
		this.powerLevel = powerLevel;
		this.cap = cap;
	}

	public abstract String showCapability();
}