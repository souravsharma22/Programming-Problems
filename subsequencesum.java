import java.util.ArrayList;
import java.util.List;

public class subsequencesum {
    public static void main(String[] args) {
        int []arr = new int[]{1,2,1};
        int k=2;
        int sum=0;
        List<Integer> ls = new ArrayList<>();
        int n= arr.length;
        subsequence1(0, ls, arr, n,k,sum);
    }
    public static void subsequence1(int i,List<Integer> ls,int []arr,int n,int k,int sum)
    {
        if(i==n || sum>=k)
        {
            if(sum==k)
                System.out.println(ls);
            return;
        }
        ls.add(arr[i]);
        sum+=arr[i];
        subsequence1(i+1, ls, arr, n,k,sum);
        ls.remove(ls.size()-1);
        sum-=arr[i];
        subsequence1(i+1, ls, arr, n,k,sum);

    }
}
