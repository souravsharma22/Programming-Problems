
import java.util.*;



class cc_problem
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0)
		{
		    int n = sc.nextInt();
		    String str = sc.next();
			List<Integer> ls = new ArrayList<>();
		    for(int i=1;i<n;i++)
		    {
		        if(str.charAt(i-1)==str.charAt(i))
		           ls.add(i);
		    }
		    if(ls.size()>2)
				System.out.println("NO");
			else if(ls.size()==2)
				if(str.charAt(ls.get(0))== str.charAt(ls.get(1)))
					System.out.println("NO");
				else
					System.out.println("Yes");
			else if(ls.size()==1)
				if(str.charAt(ls.get(0))!=str.charAt(0) || str.charAt(ls.get(0))!=str.charAt(n-1))
					System.out.println("yes");
				else
					System.out.println("No");
			else{
				System.out.println("YES");
			}
		}

	}
}

