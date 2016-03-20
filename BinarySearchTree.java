import java.util.Scanner;
class Node
{
	Node left,right;
	double sri;
	String name;
	public Node(String n,double d)
	{
		left=right=null;
		sri=d;
		name=new String();
		name=n;
	}
}

public class BinarySearchTree 
{
	
	Node root,temp;
	Scanner sc = new Scanner(System.in);
	
	public void create()
	{
		double d=0;
		String name=new String();
		int ch=0;
		
		System.out.println("Enter base employee name and sum risk index");
		name=sc.next();
		d = sc.nextDouble();
		root=new Node(name,d);
		while(ch!=2)
		{
			System.out.println("Enter 1 for inputting data for employee and 2 to exit");
			ch=sc.nextInt();
			if(ch==1)
			{
				System.out.println("Enter employee name and sum risk index to input");
				name=sc.next();
				d=sc.nextDouble();
			}
			else break;
			temp=root;
			while(true)
			{
			   if(d<temp.sri)
			   {
				   if(temp.left==null)
				   {
					   temp.left=new Node(name,d);
					   break;
				   }
				   else temp=temp.left;
			   }	
			   else if(d>=temp.sri)
			   {
				   if(temp.right==null)
				   {
					   temp.right=new Node(name,d);
					   break;
				   }
				   else temp=temp.right;
			   }
			}
			
		}
		
	}
	public void search(double d)
	{
		search(root,d);
	}
	public void search(Node start,double d)
		{
			if(d<start.sri)
			search(start.left,d);
			
			else if(d>start.sri)
			search(start.right,d);
			
			else if(d==start.sri) 
			{
				System.out.println();
				System.out.println("Employee :"+start.name);
				System.out.println("Sum Risk Index:"+start.sri);
			} 
			
		}
		
	public void best()
	{
		best(root);
	}
	public void best(Node start)
		{
			if(start.sri>4.0&&start.sri<=5.50)
			{
				System.out.println();
				System.out.println("Employee :"+start.name);
				System.out.println("Sum Risk Index:"+start.sri);
			} 
			
			if(start.left!=null) best(start.left);
			if(start.right!=null) best(start.right);
			
			
			
		}
		
		
	
	public void search(String s)
	{
		search(root,s);
	}
	public void search(Node start,String s)
		{
			if(start.name.equals(s))
			{
				System.out.println();
				System.out.println("Employee :"+start.name);
				System.out.println("Sum Risk Index:"+start.sri);
			}
			
		    if(start.left!=null) search(start.left,s);
		    if(start.right!=null) search(start.right,s);
			
		}	
		
	public void print()
	{
		print(root);
	}
	public void print(Node start)
		{
			
				System.out.println();
				System.out.println("Employee :"+start.name);
				System.out.println("Sum Risk Index:"+start.sri);
			
			
		  if(start.left!=null)  print(start.left);
		  if(start.right!=null) print(start.right);
			
		}
		
	
	public static void main (String args[]) {
		Scanner sc = new Scanner(System.in);
		
		BinarySearchTree bst = new BinarySearchTree();
		bst.create();
		int ch=0;
		while(ch!=4)
		{
		   System.out.println("Enter 1 to retrieve performance by name,2 to retrieve performance by Sum Risk Index , 3 to display all employee data , 4 for best performers and 5 to exit");
		   ch=sc.nextInt();
		   switch(ch)
		   {
		   case 1:
		          System.out.println("enter name of employee to search");
		          String s=sc.next();
		          bst.search(s);
		          break;
		   
		   case 2:
		          System.out.println("enter data to search");
		          double d=sc.nextDouble();
		          bst.search(d);
		          break;
		   
		   case 3:
		          bst.print();
		          break;
		          
		   case 4: bst.best();
		           break;
		   
		   case 5: break;
	    }
		
	    }
	}
}

