import java.awt.event.*;
import javax.swing.*;
import java.awt.*;

public class Calculator1 extends JFrame implements ActionListener{

	static JFrame frame;
	static JTextField textField;
	String s0, s1, s2;
	public Calculator1() {
		initialize();
		s0 = s1 = s2 = "";
	}
	
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 220, 230);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
	}

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Calculator1 window = new Calculator1();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});

		JPanel panel = new JPanel();
		frame = new JFrame("calculator");
		
		Calculator1 c = new Calculator1();
		
		textField = new JTextField(16);
		textField.setEditable(false);
		panel.add(textField);
		
		JButton ba = new JButton("+");
		panel.add(ba);
		ba.addActionListener(c);
		JButton b1 = new JButton("1");
		panel.add(b1);
		b1.addActionListener(c);
		JButton b2 = new JButton("2");
		panel.add(b2);
		b2.addActionListener(c);
		JButton b3 = new JButton("3");
		panel.add(b3);
		b3.addActionListener(c);
		JButton bs = new JButton("-");
		panel.add(bs);
		bs.addActionListener(c);
		JButton b4 = new JButton("4");
		panel.add(b4);
		b4.addActionListener(c);
		JButton b5 = new JButton("5");
		panel.add(b5);
		b5.addActionListener(c);
		JButton b6 = new JButton("6");
		panel.add(b6);
		b6.addActionListener(c);
		JButton bm = new JButton("*");
		panel.add(bm);
		bm.addActionListener(c);
		JButton b7 = new JButton("7");
		panel.add(b7);
		b7.addActionListener(c);
		JButton b8 = new JButton("8");
		panel.add(b8);
		b8.addActionListener(c);
		JButton b9 = new JButton("9");
		panel.add(b9);
		b9.addActionListener(c);
		JButton bd = new JButton("/");
		panel.add(bd);
		bd.addActionListener(c);
		JButton bc = new JButton("C");
		panel.add(bc);
		bc.addActionListener(c);
		JButton b0 = new JButton("0");
		panel.add(b0);
		b0.addActionListener(c);
		JButton be = new JButton(".");
		panel.add(be);
		be.addActionListener(c);
		JButton beq = new JButton("=");
		panel.add(beq);
		beq.addActionListener(c);
		frame.setBackground(Color.gray);
		frame.getContentPane().add(panel);
		frame.show();
	}

	 public void actionPerformed(ActionEvent e)
     {
         String s = e.getActionCommand();
       
         if ((s.charAt(0) >= '0' && s.charAt(0) <= '9') || s.charAt(0) == '.')
         {
             if (!s1.equals(""))
                 s2 = s2 + s;
             else
                 s0 = s0 + s;
             textField.setText(s0 + s1 + s2);
         }
         else if (s.charAt(0) == 'C')
         {
             s0 = s1 = s2 = "";
             textField.setText(s0 + s1 + s2);
         }
         else if (s.charAt(0) == '=') {
             double te=0.0;
  
             if (s1.equals("+"))
                 te = (Double.valueOf(s0) + Double.valueOf(s2));
             else if (s1.equals("-"))
                 te = (Double.valueOf(s0) - Double.valueOf(s2));
             else if (s1.equals("/"))
                 te = (Double.valueOf(s0) / Double.valueOf(s2));
             else if (s1.equals("*"))
                 te = (Double.valueOf(s0) * Double.valueOf(s2));
  
             textField.setText(s0 + s1 + s2 + "=" + te);
             s0 = Double.toString(te);
             s1 = s2 = "";
         }
         else {
             // if there was no operand
             if (s1.equals("") || s2.equals(""))
                 s1 = s;
             // else evaluate
             else {
                 double te=0.0;
                 if (s1.equals("+"))
                     te = (Double.valueOf(s0) + Double.valueOf(s2));
                 else if (s1.equals("-"))
                     te = (Double.valueOf(s0) - Double.valueOf(s2));
                 else if (s1.equals("/"))
                     te = (Double.valueOf(s0) / Double.valueOf(s2));
                 else if (s1.equals("*"))
                     te = (Double.valueOf(s0) * Double.valueOf(s2));
  
                 s0 = Double.toString(te);
                 s1 = s;
                 s2 = "";
             }
             textField.setText(s0 + s1 + s2);
         }
 }
	
}
