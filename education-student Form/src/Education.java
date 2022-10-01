import java.io.*;
import java.util.ArrayList;
 class Education extends methods {
	ArrayList<String> name = new ArrayList<>();
	ArrayList<String> code = new ArrayList<>();
	ArrayList<Integer> phone_number = new ArrayList<>();


	void ADD(String Name, String Code, int Phone_number) {
		this.name.add(Name);
		this.code.add(Code);
		this.phone_number.add(Phone_number);
	}
	
	void Remove(int n) {
		this.name.remove(n);
		this.code.remove(n);
		this.phone_number.remove(n);
	}
	
	void Change(int n, String Name, String Code, int Phone_number) {
		this.name.set(n, Name);
		this.code.set(n, Code);
		this.phone_number.set(n, Phone_number);
	}
	
	void Show() {
		System.out.println("name\tCode\tphone number");
        for(int i =0 ; i<name.size(); i++)
        {
          System.out.printf((i+1)+"."+name.get(i)+"\t"+code.get(i)+"\t"+phone_number.get(i)+"\n");
        }
	}

	
	void Save(BufferedWriter Edu) throws IOException {
		for(int i=0; i<name.size();i++)
		{ 
			Edu.write(name.get(i)+"\t"+code.get(i)+"\t"+phone_number.get(i)+"\n");
		}
		Edu.close();
	}

	@Override
	void Read(BufferedReader Redu) throws IOException {
		String str;
		int i =0;
		while((str=Redu.readLine())!=null)
        {    
			String[] input =  str.split("\t");
			this.name.add(input[i]);
			i++;
			this.code.add(input[i]);
			i++;
			this.phone_number.add(Integer.valueOf(input[i]));
			i++;
        }
		i=0;
		Redu.close();
	}
}