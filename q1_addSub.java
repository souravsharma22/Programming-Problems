public class q1_addSub {

    public static String addSub(String str)
    {
        System.out.println(str);
        String[] numbers = str.split("\\+|\\-");
        for (String string : numbers) {
            System.out.println(string);
        }
        return "";
    }
    public static void main(String[] args) {
        String ans=addSub("-1/2+2/2");
        System.out.println(ans);
    }

}
