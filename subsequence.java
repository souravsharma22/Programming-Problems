import java.util.*;

public class subsequence {

    public static void main(String[] args) {
        int []arr = new int[]{3,1,2};
        List<Integer> ls = new ArrayList<>();
        int n= arr.length;
        subsequence1(0, ls, arr, n);
    }
    public static void subsequence1(int i,List<Integer> ls,int []arr,int n)
    {
        if(i==n)
        {
            System.out.println(ls);
            return;
        }
        ls.add(arr[i]);
        subsequence1(i+1, ls, arr, n);
        ls.remove(ls.size()-1);
        subsequence1(i+1, ls, arr, n);

    }
}