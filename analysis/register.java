import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class register1 extends JFrame
 // implements ActionListener
{
	JLabel Name_l , Roll_no_l , Address_l;
	JTextField Name, Roll_no , Address;
	register1()
	{
		setSize(400,400);
		setLayout(null);
		Name_l  = new JLabel("Name");
		Name_l.setBounds(50,50,100,20);
		Name = new JTextField();
		Name.setBounds(150,50,100,20);
		Name.setToolTipText("Enter name");

		Roll_no_l  = new JLabel("Roll NO");
		Roll_no_l.setBounds(200,50,100,20);
		Roll_no = new JTextField();
		Roll_no.setBounds(250,50,100,20);
		Roll_no.setToolTipText("Enter roll no");

		Address_l  = new JLabel("Address");
		Address_l.setBounds(200,50,100,20);
		Address = new JTextField();
		Address.setBounds(250,50,100,20);
		Address.setToolTipText("Enter Address");

		add(Name_l);
		add(Name);
		add(Roll_no_l);
		add(Roll_no);
		add(Address);
		add(Address_l);

	}
}
public class register
{

	public static void main(String args[])
	{
		register1 re= new register1();
	}
}