import java.util.*

fun main() = with(Scanner(System.`in`)) {
    var a = nextInt()
    //readln().split(' ').map { it.toInt() }

    if (a%400 == 0){
        print("1")
    } else{
        if (a%4 ==0){
            if(a%100 != 0){
                print("1")
            } else{
                print("0")
            }
        } else{
            print("0")
        }
    }
}