import java.util.*;
public class Main{
    static boolean checkEven(int A[]){
        for(int i = 0;i < A.length; i++){
            if(A[i] % 2 != 0) return false;
        }
        return true;
    }

    static int[] getTwoDivisionArray(int A[]){
        for(int i = 0;i < A.length; i++){
            A[i] /= 2;
        }
        return A;
    }

    static void printArray(int A[]){
        for(int i = 0;i < A.length; i++){
            System.out.print(A[i]);
            if(i != A.length-1) System.out.print(",");
        }
        System.out.println("");
    }


    public static void main(String Args[]){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), count = 0;
        int A[] = new int[N];
        for(int i = 0;i < A.length; i++){
            A[i] = sc.nextInt();
        }
        while(Main.checkEven(A)){
            A = getTwoDivisionArray(A);
            count++;
        }
        System.out.println(count);
    }
}