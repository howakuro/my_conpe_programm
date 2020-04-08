import java.util.*;
public class Main{
    public static void main(String Args[]){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        String answer = ((a*b)%2==0)? "Even" : "Odd";
        System.out.println(answer);
    }
}