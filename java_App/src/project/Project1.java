package project;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.*;
import java.io.*;
import java.io.File;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Random;
import java.util.regex.*;

public class Project1 {

	private JFrame frame;
	ArrayList<String> input = new ArrayList<String>();
	ArrayList<String> login = new ArrayList<String>();
	public static ArrayList<String> Rfile = new ArrayList<String>();
	ArrayList<Integer> numbers = new ArrayList<Integer>();
	ArrayList<Integer> Score = new ArrayList<Integer>();
	ArrayList<String> Sscore = new ArrayList<String>();
	Random rand = new Random();
	String[] questions = { "which class is the Super class of any class in java?",
			"What is a correct syntax to output \"Hello World\" in Java?",
			"Which data type is used to create a variable that should store text?",
			"Which method can be used to find the length of a string?",
			"To declare an array in Java, define the variable type with:", "How do you call a method in Java?",
			"What is instance variable?",
			"Which variables can an inner class access from the class which encapsulates it?",
			"Which type of data makes java not a pure OOP language", "which methods cant be override?",
			"how many of these can a static method  call?" };
	String[] ans = { "Object,Thread,String,Java",
			"Print(\"Hello World\");,System.out.println(\"Hello World\");,Console.WriteLine(\"Hello World\");,echo(\"Hello World\");",
			"Char,Mystring,String,txt", "Len(),.lenght(),Size(),getLength()", "{},[],(),\"\"",
			"(methodname);,methodname[];,methodname;,methodname();",
			"Instance variables are static variables within a class but outside any method,Instance variables are variables defined inside methods or constructors or blocks,Instance variables are variables within a class but outside any method,None of the above",
			"All static variables,All final variables,All instance variables,only final static variables",
			"Long,Float,Boolean,Final", "static methods,Constructor,final methods,default methods",
			"static variable,non stratic variable,static method,non static method" };
	String[] Rans = { "Object", "System.out.println(\"Hello World\");", "String", ".lenght()", "[]", "methodname();",
			"Instance variables are variables within a class but outside any method", "All static variables" };
	int flag = 0;
	int flagR = 0;
	int j = 0, s, R = 0, W = 0;
	int l = 0;

	public void Qpattern() {
		while (numbers.size() < 11) {
			int x = rand.nextInt(8);
			int y = rand.nextInt(8, 11);
			if (numbers.size() > 7) {
				if (!numbers.contains(y)) {
					numbers.add(y);
				}
			} else {
				if (!numbers.contains(x)) {
					numbers.add(x);
				}
			}
		}

	}

	public static void CreateFile(String f) {
		try {
			File file = new File(f);
			if (file.createNewFile()) {
				System.out.println("File created: " + file.getName());
			} else {
				System.out.println("File already exists.");
			}
		} catch (IOException e) {
			System.out.println("An error has occurred.");
			e.printStackTrace();
		}
	}

	public static void ReadFile(String f) {
		try {
			File file = new File(f);
			Scanner Reader = new Scanner(file);
			while (Reader.hasNextLine()) {
				String data = Reader.nextLine();
				String[] items = data.split(" ");
				Rfile.add(items[0]);
				Rfile.add(items[1]);
			}
			Reader.close();
		} catch (FileNotFoundException e) {
			System.out.println("An error has occurred.");
			e.printStackTrace();
		}
	}

	public static void ReadFile(String f, ArrayList<String> Sscore) {
		try {
			File file = new File(f);
			Scanner Reader = new Scanner(file);
			Sscore.remove(0);
			while (Reader.hasNextLine()) {
				String data = Reader.nextLine();
				String[] items = data.split(" ");
				for (int i = 0; i < items.length; i++) {
					Sscore.add(items[i]);
				}
			}
			Reader.close();
		} catch (FileNotFoundException e) {
			System.out.println("An error has occurred.");
			e.printStackTrace();
		}
	}

	public static void WriteFile(String f, ArrayList<String> data) {
		try {
			FileWriter Writer = new FileWriter(f, true);
			for (int i = 0; i < data.size(); i++) {
				Writer.write(data.get(i));
				Writer.write(" ");
			}
			Writer.close();
			System.out.println("Successfully written.");
		} catch (IOException e) {
			System.out.println("An error has occurred.");
			e.printStackTrace();
		}
	}

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Project1 window = new Project1();
					window.frame.setVisible(true);

				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 * 
	 * @throws IOException
	 */
	public Project1() throws IOException {
		initialize();

	}

	/**
	 * Initialize the contents of the frame.
	 * 
	 * @throws IOException
	 */
	private void initialize() throws IOException {
		// ========================================declaration
		frame = new JFrame();
		frame.setBounds(100, 100, 600, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JPanel panel1 = new JPanel();
		JPanel panelR = new JPanel();
		JPanel panelL = new JPanel();
		JPanel panelQ = new JPanel();
		JPanel panelF = new JPanel();
		frame.getContentPane().add(panel1, BorderLayout.CENTER);

		JLabel label = new JLabel("welcome! \n please sign in\\up to answer some questions");
		label.setPreferredSize(new Dimension(310, 13));
		panel1.add(label);
		JButton register = new JButton("Sign up");
		JTextField user = new JTextField("Username");
		user.setColumns(10);
		JTextField Pass = new JTextField("Password");
		Pass.setColumns(10);
		JTextField RePass = new JTextField("Confirm your Password");
		RePass.setColumns(15);
		JTextField userL = new JTextField("Username");
		userL.setColumns(10);
		JTextField PassL = new JTextField("Password");
		PassL.setColumns(10);
		JButton submit = new JButton("Submit");
		JButton Back = new JButton("Back");
		JButton Login = new JButton("Sign in");
		JButton enter = new JButton("Enter");
		JTextArea textArea = new JTextArea();
		textArea.setColumns(25);
		JRadioButton A = new JRadioButton();
		A.setBorder(BorderFactory.createLineBorder(Color.black));
		JRadioButton B = new JRadioButton();
		B.setBorder(BorderFactory.createLineBorder(Color.black));
		JRadioButton C = new JRadioButton();
		C.setBorder(BorderFactory.createLineBorder(Color.black));
		JRadioButton D = new JRadioButton();
		D.setBorder(BorderFactory.createLineBorder(Color.black));
		JButton Check = new JButton("Check");
		JButton Next = new JButton("Next");
		JCheckBox A1 = new JCheckBox();
		A1.setBorder(BorderFactory.createLineBorder(Color.black));
		JCheckBox B1 = new JCheckBox();
		B1.setBorder(BorderFactory.createLineBorder(Color.black));
		JCheckBox C1 = new JCheckBox();
		C1.setBorder(BorderFactory.createLineBorder(Color.black));
		JCheckBox D1 = new JCheckBox();
		D1.setBorder(BorderFactory.createLineBorder(Color.black));
		JButton resualt = new JButton("see Resualts");
		JLabel labelC = new JLabel(
				"Test: Right answer +3 point Wrong answer -1 point,Multiple correct: each Righ  choice +1 Righ  choice -1 ");
		labelC.setForeground(Color.blue);
		JLabel labelS = new JLabel("Right: " + R + " Wrong: " + W);
		labelS.setForeground(Color.cyan);
		JButton again = new JButton("Try Again");
		Score.add(0, 0);

		Qpattern();
		register.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				panel1.setVisible(false);
				frame.getContentPane().add(panelR, BorderLayout.CENTER);
				panelR.setVisible(true);

				user.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						user.setText("");
					}
				});
				user.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						String txt = user.getText();
						input.add((txt));
					}
				});
				panelR.add(user);

				Pass.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						Pass.setText("");
					}
				});
				Pass.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						String txt = Pass.getText();
						String regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).+$";
						Pattern p = Pattern.compile(regex);
						Matcher m = p.matcher(txt);
						if (m.matches() && txt.length() >= 8) {
							input.add((txt));
						} else {
							JOptionPane.showMessageDialog(Pass,
									"Password must be at least 8 charachter contain 1 upper case letter 1 lower case letter and a number");
						}
					}
				});
				panelR.add(Pass);

				RePass.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						RePass.setText("");
					}
				});
				RePass.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						String txt = RePass.getText();
						if ((txt.equals(input.get(input.size() - 1)))) {
							label.setVisible(true);
							label.setText("password confirmed");
							label.setForeground(Color.green);
							panelR.add(label);
						} else {
							JOptionPane.showMessageDialog(RePass, "Password Does Not Match");
						}
					}
				});
				panelR.add(RePass);

				submit.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						user.setText("");
						Pass.setText("");
						RePass.setText("");
						label.setVisible(false);
						// open file save data to file close file
						CreateFile("register.txt");
						WriteFile("register.txt", input);
						JOptionPane.showMessageDialog(submit, "Thank you for registering");
					}
				});
				panelR.add(submit);

				Back.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						panelR.setVisible(false);
						frame.getContentPane().add(panel1, BorderLayout.CENTER);
						panel1.setVisible(true);
					}
				});
				panelR.add(Back);
			}
		});
		panel1.add(register);

		Login.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				panel1.setVisible(false);
				frame.getContentPane().add(panelL, BorderLayout.CENTER);
				panelL.setVisible(true);

				userL.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						userL.setText("");
					}
				});
				userL.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						String txt = userL.getText();
						login.clear();
						login.add(txt);
					}
				});
				panelL.add(userL);

				PassL.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						PassL.setText("");
					}
				});
				PassL.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						String txt = PassL.getText();
						login.add(txt);
					}
				});
				panelL.add(PassL);
			}
		});
		panel1.add(Login);

		enter.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				int i = 0;
				// read from file and check if user pass exist and correct close file
				// open score file add the scores to score arraylist update l close score file
				ReadFile("register.txt");
				do {
					if ((login.get(0).equals(Rfile.get(i))) && (login.get(1).equals(Rfile.get(i + 1)))) {
						JOptionPane.showMessageDialog(enter, "Hello " + login.get(0));
						flag = 1;
						break;
					}
					i += 2;
				} while (i <= (input.size() - 2));
				if (flag == 0) {
					JOptionPane.showMessageDialog(enter, "There is no user registered with this id or password");
				}
				if (flag == 1) {
					panelL.setVisible(false);
					frame.getContentPane().add(panelQ, BorderLayout.CENTER);
					panelQ.setVisible(true);
					panelQ.add(labelC);
					labelC.setVisible(true);
					panelQ.add(labelS);
					labelS.setVisible(true);
					textArea.setText(questions[numbers.get(0)]);
					panelQ.add(textArea);
					String[] arrOfStr = ans[numbers.get(0)].split(",");
					A.setText(arrOfStr[0]);
					B.setText(arrOfStr[1]);
					C.setText(arrOfStr[2]);
					D.setText(arrOfStr[3]);
					panelQ.add(A);
					panelQ.add(B);
					panelQ.add(C);
					panelQ.add(D);
					panelQ.add(Check);

					Check.addActionListener(new ActionListener() {

						public void actionPerformed(ActionEvent e) {
							if (A.isSelected() && (!B.isSelected()) && (!C.isSelected()) && (!D.isSelected())) {
//									System.out.printf("A: %s Rans[%d]:%s eq =%s ", A.getText(), numbers.get(0), Rans[numbers.get(0)],A.getText().equals(Rans[numbers.get(0)]));
								if (A.getText().equals(Rans[numbers.get(0)])) {
									s = Score.get(l) + 3;
									Score.set(l, s);
									R++;
									labelS.setText("Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
									labelS.setVisible(true);
									A.setBackground(Color.green);
									label.setVisible(true);
									label.setText("Correct!");
									label.setForeground(Color.green);
									panelQ.add(label);
								}

								else {
									s = Score.get(l) - 1;
									Score.set(l, s);
									W++;
									labelS.setText("Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
									labelS.setVisible(true);
									A.setBackground(Color.red);
									label.setVisible(true);
									label.setText("Wrong!");
									label.setForeground(Color.red);
									panelQ.add(label);
								}
							}
							if (!A.isSelected() && (B.isSelected()) && (!C.isSelected()) && (!D.isSelected())) {
//									System.out.printf("B: %s Rans[%d]:%s eq =%s ", B.getText(), numbers.get(0), Rans[numbers.get(0)],B.getText().equals(Rans[numbers.get(0)]));
								if (B.getText().equals(Rans[numbers.get(0)])) {
									s = Score.get(l) + 3;
									Score.set(l, s);
									R++;
									labelS.setText("Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
									labelS.setVisible(true);
									B.setBackground(Color.green);
									label.setVisible(true);
									label.setText("Correct!");
									label.setForeground(Color.green);
									panelQ.add(label);
								}

								else {
									s = Score.get(l) - 1;
									Score.set(l, s);
									W++;
									labelS.setText("Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
									labelS.setVisible(true);
									B.setBackground(Color.red);
									label.setVisible(true);
									label.setText("Wrong!");
									label.setForeground(Color.red);
									panelQ.add(label);
								}
							}
							if (!A.isSelected() && (!B.isSelected()) && (C.isSelected()) && (!D.isSelected())) {
//									System.out.printf("C: %s Rans[%d]:%s eq =%s ", C.getText(), numbers.get(0), Rans[numbers.get(0)],C.getText().equals(Rans[numbers.get(0)]));
								if (C.getText().equals(Rans[numbers.get(0)])) {
									s = Score.get(l) + 3;
									Score.set(l, s);
									R++;
									labelS.setText("Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
									labelS.setVisible(true);
									C.setBackground(Color.green);
									label.setVisible(true);
									label.setText("Correct!");
									label.setForeground(Color.green);
									panelQ.add(label);
								}

								else {
									s = Score.get(l) - 1;
									Score.set(l, s);
									W++;
									labelS.setText("Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
									labelS.setVisible(true);
									C.setBackground(Color.red);
									label.setVisible(true);
									label.setText("Wrong!");
									label.setForeground(Color.red);
									panelQ.add(label);
								}
							}
							if (!A.isSelected() && (!B.isSelected()) && (!C.isSelected()) && (D.isSelected())) {
//									System.out.printf("D: %s Rans[%d]:%s eq =%s ", D.getText(), numbers.get(0), Rans[numbers.get(0)],D.getText().equals(Rans[numbers.get(0)]));
								if (D.getText().equals(Rans[numbers.get(0)])) {
									s = Score.get(l) + 3;
									Score.set(l, s);
									R++;
									labelS.setText("Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
									labelS.setVisible(true);
									D.setBackground(Color.green);
									label.setVisible(true);
									label.setText("Correct!");
									label.setForeground(Color.green);
									panelQ.add(label);
								}

								else {
									s = Score.get(l) - 1;
									Score.set(l, s);
									W++;
									labelS.setText("Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
									labelS.setVisible(true);
									D.setBackground(Color.red);
									label.setVisible(true);
									label.setText("Wrong!");
									label.setForeground(Color.red);
									panelQ.add(label);
								}
							}
							A.setSelected(false);
							B.setSelected(false);
							C.setSelected(false);
							D.setSelected(false);
						}
					});

					Next.addActionListener(new ActionListener() {
						public void actionPerformed(ActionEvent e) {
							A.setBackground(null);
							B.setBackground(null);
							C.setBackground(null);
							D.setBackground(null);
							flagR++;
							label.setVisible(false);
							if (flagR == 10) {
								Next.setVisible(false);
								panelQ.add(resualt);
								resualt.addActionListener(new ActionListener() {
									public void actionPerformed(ActionEvent e) {
										// open file save score to file colse file
										String fileName = login.get(0) + "score.txt";
										CreateFile(fileName);
										Sscore.add(String.valueOf(Score.get(Score.size() - 1)));
										WriteFile(fileName, Sscore);
										panelQ.setVisible(false);
										frame.getContentPane().add(panelF, BorderLayout.CENTER);
										panelF.setVisible(true);
										label.setForeground(Color.black);
										label.setText("Final Score= " + Score.get(l));
										label.setVisible(true);
										panelF.add(label);
										ReadFile(fileName, Sscore);
										// plot graph
										MainPanel daGraph = new MainPanel(Sscore);
										panelF.add(daGraph);
										daGraph.setVisible(true);
									}
								});
								A1.setSelected(false);
								A1.setForeground(Color.black);
								B1.setSelected(false);
								B1.setForeground(Color.black);
								C1.setSelected(false);
								C1.setForeground(Color.black);
								D1.setSelected(false);
								D1.setForeground(Color.black);
							}
							if (flagR > 7 && flagR < 11) {
								A.setVisible(false);
								B.setVisible(false);
								C.setVisible(false);
								D.setVisible(false);
								textArea.setText(questions[numbers.get(flagR)]);
								panelQ.add(textArea);
								String[] arrOfStr = ans[numbers.get(flagR)].split(",");
								A1.setText(arrOfStr[0]);
								B1.setText(arrOfStr[1]);
								C1.setText(arrOfStr[2]);
								D1.setText(arrOfStr[3]);
								panelQ.add(A1);
								panelQ.add(B1);
								panelQ.add(C1);
								panelQ.add(D1);
								Check.addActionListener(new ActionListener() {
									public void actionPerformed(ActionEvent e) {

										if (numbers.get(flagR) == 8) {
											if (A1.isSelected() && (B1.isSelected()) && (C1.isSelected())
													&& (!D1.isSelected())) {
												s = Score.get(l) + 3;
												Score.set(l, s);
												R++;
												labelS.setText(
														"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
												labelS.setVisible(true);
												A1.setForeground(Color.green);
												B1.setForeground(Color.green);
												C1.setForeground(Color.green);
												label.setVisible(true);
												label.setText("Correct!");
												label.setForeground(Color.green);
												panelQ.add(label);
											}

											else {
												if (((A1.isSelected() && B1.isSelected())
														&& (!C1.isSelected() && !D1.isSelected()))
														|| ((A1.isSelected() && !B1.isSelected())
																&& (C1.isSelected() && !D1.isSelected()))
														|| ((!A1.isSelected() && B1.isSelected())
																&& (C1.isSelected() && !D1.isSelected()))) {
													s = Score.get(l) + 2;
													Score.set(l, s);
													W++;
													labelS.setText(
															"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
													labelS.setVisible(true);
													A1.setForeground(Color.green);
													B1.setForeground(Color.green);
													C1.setForeground(Color.green);
													label.setVisible(true);
													label.setText("Wrong!");
													label.setForeground(Color.red);
													panelQ.add(label);
												} else if (((A1.isSelected() && !B1.isSelected())
														&& (!C1.isSelected() && !D1.isSelected()))
														|| ((!A1.isSelected() && B1.isSelected())
																&& (!C1.isSelected() && !D1.isSelected()))
														|| ((!A1.isSelected() && !B1.isSelected())
																&& (C1.isSelected() && !D1.isSelected()))) {
													s = Score.get(l) + 1;
													Score.set(l, s);
													W++;
													labelS.setText(
															"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
													labelS.setVisible(true);
													A1.setForeground(Color.green);
													B1.setForeground(Color.green);
													C1.setForeground(Color.green);
													label.setVisible(true);
													label.setText("Wrong!");
													label.setForeground(Color.red);
													panelQ.add(label);
												} else {
													s = Score.get(l) - 1;
													Score.set(l, s);
													W++;
													labelS.setText(
															"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
													labelS.setVisible(true);
													A1.setForeground(Color.green);
													B1.setForeground(Color.green);
													C1.setForeground(Color.green);
													label.setVisible(true);
													label.setText("Wrong!");
													label.setForeground(Color.red);
													panelQ.add(label);
												}
											}
										}
										if (numbers.get(flagR) == 9) {
											if (A1.isSelected() && (B1.isSelected()) && (C1.isSelected())
													&& (!D1.isSelected())) {
												s = Score.get(l) + 3;
												Score.set(l, s);
												R++;
												labelS.setText(
														"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
												labelS.setVisible(true);
												A1.setForeground(Color.green);
												B1.setForeground(Color.green);
												C1.setForeground(Color.green);
												label.setVisible(true);
												label.setText("Correct!");
												label.setForeground(Color.green);
												panelQ.add(label);
											}

											else {
												if (((A1.isSelected() && B1.isSelected())
														&& (!C1.isSelected() && !D1.isSelected()))
														|| ((A1.isSelected() && !B1.isSelected())
																&& (C1.isSelected() && !D1.isSelected()))
														|| ((!A1.isSelected() && B1.isSelected())
																&& (C1.isSelected() && !D1.isSelected()))) {
													s = Score.get(l) + 2;
													Score.set(l, s);
													W++;
													labelS.setText(
															"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
													labelS.setVisible(true);
													A1.setForeground(Color.green);
													B1.setForeground(Color.green);
													C1.setForeground(Color.green);
													label.setVisible(true);
													label.setText("Wrong!");
													label.setForeground(Color.red);
													panelQ.add(label);
												} else if (((A1.isSelected() && !B1.isSelected())
														&& (!C1.isSelected() && !D1.isSelected()))
														|| ((!A1.isSelected() && B1.isSelected())
																&& (!C1.isSelected() && !D1.isSelected()))
														|| ((!A1.isSelected() && !B1.isSelected())
																&& (C1.isSelected() && !D1.isSelected()))) {
													s = Score.get(l) + 1;
													Score.set(l, s);
													W++;
													labelS.setText(
															"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
													labelS.setVisible(true);
													A1.setForeground(Color.green);
													B1.setForeground(Color.green);
													C1.setForeground(Color.green);
													label.setVisible(true);
													label.setText("Wrong!");
													label.setForeground(Color.red);
													panelQ.add(label);
												} else {
													s = Score.get(l) - 1;
													Score.set(l, s);
													W++;
													labelS.setText(
															"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
													labelS.setVisible(true);
													A1.setForeground(Color.green);
													B1.setForeground(Color.green);
													C1.setForeground(Color.green);
													label.setVisible(true);
													label.setText("Wrong!");
													label.setForeground(Color.red);
													panelQ.add(label);
												}
											}
										}
										if (numbers.get(flagR) == 10) {
											if (A1.isSelected() && (!B1.isSelected()) && (C1.isSelected())
													&& (!D1.isSelected())) {
												s = Score.get(l) + 2;
												Score.set(l, s);
												R++;
												labelS.setText(
														"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
												labelS.setVisible(true);
												A1.setForeground(Color.green);
												C1.setForeground(Color.green);
												label.setVisible(true);
												label.setText("Correct!");
												label.setForeground(Color.green);
												panelQ.add(label);
											} else {
												if (((A1.isSelected() && !B1.isSelected())
														&& (!C1.isSelected() && !D1.isSelected()))
														|| ((!A1.isSelected() && !B1.isSelected())
																&& (C1.isSelected() && !D1.isSelected()))) {
													s = Score.get(l) + 1;
													Score.set(l, s);
													W++;
													labelS.setText(
															"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
													labelS.setVisible(true);
													A1.setForeground(Color.green);
													C1.setForeground(Color.green);
													label.setVisible(true);
													label.setText("Worng!");
													label.setForeground(Color.red);
													panelQ.add(label);
												} else {
													s = Score.get(l) - 1;
													Score.set(l, s);
													W++;
													labelS.setText(
															"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
													labelS.setVisible(true);
													A1.setForeground(Color.green);
													C1.setForeground(Color.green);
													label.setVisible(true);
													label.setText("Wrong!");
													label.setForeground(Color.red);
													panelQ.add(label);
												}
											}
										}
									}

								});

								A1.setSelected(false);
								A1.setForeground(Color.black);
								B1.setSelected(false);
								B1.setForeground(Color.black);
								C1.setSelected(false);
								C1.setForeground(Color.black);
								D1.setSelected(false);
								D1.setForeground(Color.black);
							} else {
								textArea.setText(questions[numbers.get(flagR)]);
								panelQ.add(textArea);
								String[] arrOfStr = ans[numbers.get(flagR)].split(",");
								A.setText(arrOfStr[0]);
								B.setText(arrOfStr[1]);
								C.setText(arrOfStr[2]);
								D.setText(arrOfStr[3]);
								Check.addActionListener(new ActionListener() {
									public void actionPerformed(ActionEvent e) {

										if (A.isSelected() && (!B.isSelected()) && (!C.isSelected())
												&& (!D.isSelected())) {
//										System.out.printf("A: %s Rans[%d]:%s eq =%s ", A.getText(), x, Rans[x],A.getText().equals(Rans[x]));
											if (A.getText().equals(Rans[numbers.get(flagR)])) {
												s = Score.get(l) + 3;
												Score.set(l, s);
												R++;
												labelS.setText(
														"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
												labelS.setVisible(true);
												A.setBackground(Color.green);
												label.setVisible(true);
												label.setText("Correct!");
												label.setForeground(Color.green);
												panelQ.add(label);
											}

											else {
												s = Score.get(l) - 1;
												Score.set(l, s);
												W++;
												labelS.setText(
														"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
												labelS.setVisible(true);
												A.setBackground(Color.red);
												label.setVisible(true);
												label.setText("Wrong!");
												label.setForeground(Color.red);
												panelQ.add(label);
											}
										}
										if (!A.isSelected() && (B.isSelected()) && (!C.isSelected())
												&& (!D.isSelected())) {
//										System.out.printf("B: %s Rans[%d]:%s eq =%s ", B.getText(), x, Rans[x],B.getText().equals(Rans[x]));
											if (B.getText().equals(Rans[numbers.get(flagR)])) {
												s = Score.get(l) + 3;
												Score.set(l, s);
												R++;
												labelS.setText(
														"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
												labelS.setVisible(true);
												B.setBackground(Color.green);
												label.setVisible(true);
												label.setText("Correct!");
												label.setForeground(Color.green);
												panelQ.add(label);
											}

											else {
												s = Score.get(l) - 1;
												Score.set(l, s);
												W++;
												labelS.setText(
														"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
												labelS.setVisible(true);
												B.setBackground(Color.red);
												label.setVisible(true);
												label.setText("Wrong!");
												label.setForeground(Color.red);
												panelQ.add(label);
											}
										}
										if (!A.isSelected() && (!B.isSelected()) && (C.isSelected())
												&& (!D.isSelected())) {
//										System.out.printf("C: %s Rans[%d]:%s eq =%s ", C.getText(), x, Rans[x],C.getText().equals(Rans[x]));
											if (C.getText().equals(Rans[numbers.get(flagR)])) {
												s = Score.get(l) + 3;
												Score.set(l, s);
												R++;
												labelS.setText(
														"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
												labelS.setVisible(true);
												C.setBackground(Color.green);
												label.setVisible(true);
												label.setText("Correct!");
												label.setForeground(Color.green);
												panelQ.add(label);
											}

											else {
												s = Score.get(l) - 1;
												Score.set(l, s);
												W++;
												labelS.setText(
														"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
												labelS.setVisible(true);
												C.setBackground(Color.red);
												label.setVisible(true);
												label.setText("Wrong!");
												label.setForeground(Color.red);
												panelQ.add(label);
											}
										}
										if (!A.isSelected() && (!B.isSelected()) && (!C.isSelected())
												&& (D.isSelected())) {
//										System.out.printf("D: %s Rans[%d]:%s eq =%s ", D.getText(), x, Rans[x],D.getText().equals(Rans[x]));
											if (D.getText().equals(Rans[numbers.get(flagR)])) {
												s = Score.get(l) + 3;
												Score.set(l, s);
												R++;
												labelS.setText(
														"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
												labelS.setVisible(true);
												D.setBackground(Color.green);
												label.setVisible(true);
												label.setText("Correct!");
												label.setForeground(Color.green);
												panelQ.add(label);
											}

											else {
												s = Score.get(l) - 1;
												Score.set(l, s);
												W++;
												labelS.setText(
														"Right: " + R + " Wrong: " + W + " Score= " + Score.get(l));
												labelS.setVisible(true);
												D.setBackground(Color.red);
												label.setVisible(true);
												label.setText("Wrong!");
												label.setForeground(Color.red);
												panelQ.add(label);
											}
										}
										A.setSelected(false);
										B.setSelected(false);
										C.setSelected(false);
										D.setSelected(false);
									}

								});
								A.setBackground(null);
								B.setBackground(null);
								C.setBackground(null);
								D.setBackground(null);
							}
						}
					});
					panelQ.add(Next);
				}
			}
		});
		panelL.add(enter);

	}
}
