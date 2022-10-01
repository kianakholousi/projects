import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Student extends methods{

	ArrayList<String> name = new ArrayList<>();
	ArrayList<String> student_ID = new ArrayList<>();
	ArrayList<Integer> score = new ArrayList<>();
	
	void ADD(String Name, String Student_ID, int Score) {
		this.name.add(Name);
		this.student_ID.add(Student_ID);
		this.score.add(Score);
	}
	
	void Remove(int n) {
		this.name.remove(n);
		this.student_ID.remove(n);
		this.score.remove(n);
	}
	
	void Change(int n, String Name, String Student_ID, int Score) {
		this.name.set(n,Name);
		this.student_ID.set(n,Student_ID);
		this.score.set(n,Score);
	}
	
	void Show() {
		System.out.println("name\tStudent ID\tScore");
        for(int i =0 ; i<name.size(); i++)
        {
          System.out.printf((i+1)+"."+name.get(i)+"\t"+student_ID.get(i)+"\t"+score.get(i)+"\n");
        }
	}

	
	void Save(BufferedWriter Stu) throws IOException {
		for(int j=0; j<name.size();j++)
		{ 
			Stu.write("Name"+name.get(j)+"\tStudent ID"+student_ID.get(j)+"\tScore"+score.get(j)+"\n");
		}
		Stu.close();
		
	}

	@Override
	void Read(BufferedReader Rstu) throws IOException {
		String str;
		int i =0;
		while((str=Rstu.readLine())!=null)
        {    
			String[] input =  str.split("\t");
			this.name.add(input[i]);
			i++;
			this.student_ID.add(input[i]);
			i++;
			this.score.add(Integer.valueOf(input[i]));
			i++;
        }
		i=0;
		Rstu.close();
	}
	
}
