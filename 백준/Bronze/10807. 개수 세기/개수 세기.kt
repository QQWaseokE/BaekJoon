import java.util.*
import java.io.*;

fun main() = with(Scanner(System.`in`)) {
    var n = nextInt()
    val array = ArrayList<Int>()
    for (i in 1..n){
        array.add(nextInt())
    }

    var a = nextInt()
    var result = 0

    for(i in array){
        if(i==a){
            result += 1
        }
    }

    print(result)
}