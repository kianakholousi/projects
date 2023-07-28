import java.awt.event.*;
import java.util.ArrayList;
import javax.swing.*;
import java.awt.*;

public class ADD {

	private JFrame frame;
	private JTextField textField;
	 ArrayList<String> Ename = new ArrayList<>();
	 ArrayList<String> code = new ArrayList<>();
	 ArrayList<Integer> phone_number = new ArrayList<>();
	 ArrayList<String> Sname = new ArrayList<>();
	 ArrayList<String> student_ID = new ArrayList<>();
	 ArrayList<Integer> score = new ArrayList<>();
	 ArrayList<String> input = new ArrayList<String>();	
	 int flag=0;
	 private JButton Save;
	 private JButton Education;
	 private JButton Student;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args)  {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					ADD window = new ADD();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public ADD() {
		initialize();

	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JPanel panel = new JPanel();
		frame.getContentPane().add(panel, BorderLayout.CENTER);

		textField = new JTextField();
		textField.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String txt = textField.getText();
				input.add((txt));
				textField.setText("");
				System.out.println(txt);
	
				
			}
			
			
		});
		
		Education = new JButton("Education");
		Education.setBackground(Color.white);
		Education.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				flag = 1;
				Student.setForeground(Color.black);
				Education.setForeground(Color.black);
				Save.setBackground(Color.white);
				Student.setBackground(Color.white);
				Education.setBackground(Color.cyan);
			}
		});
		panel.add(Education);
		
		Student = new JButton("Student");
		Student.setBackground(Color.white);
		Student.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				flag = 2;
				Student.setForeground(Color.black);
				Education.setForeground(Color.black);
				Save.setBackground(Color.white);
				Education.setBackground(Color.white);
				Student.setBackground(Color.cyan);

			}
		});
		panel.add(Student);
		panel.add(textField);
		textField.setColumns(10);
		
		Save = new JButton("Save");
		Save.setBackground(Color.white);
		Save.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Save.setBackground(Color.blue);
				System.out.println("data:");
				if(flag==1)
				{
				Education.setForeground(Color.blue);
				for(int i =0 ; i<3 ; i++)
				{
					if(i==0) {Ename.add(input.get(i));}
					if(i==1) {code.add(input.get(i));}
					if(i==2) {phone_number.add(Integer.valueOf(input.get(i)));}
				}
				System.out.printf("name = %s code= %s phone number=%s\n",Ename,code,phone_number);
				System.out.println(input);
				}
				if(flag==2)
				{
				Student.setForeground(Color.blue);
				for(int i =0 ; i<3 ; i++)
				{
					if(i==0) {Sname.add(input.get(i));}
					if(i==1) {student_ID.add(input.get(i));}
					if(i==2) {score.add(Integer.valueOf(input.get(i)));}
				}
				System.out.printf("name = %s student ID= %s Score=%s\n",Ename,code,phone_number);
				System.out.println(input);
				}
			}
		});
		panel.add(Save);

	}

}
