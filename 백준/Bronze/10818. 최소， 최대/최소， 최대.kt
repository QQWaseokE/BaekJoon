import java.util.*
import java.io.*;

fun main() = with(Scanner(System.`in`)) {
    var n = nextInt()
    val array = ArrayList<Int>()
    for (i in 1..n){
        array.add(nextInt())
    }

    print("${array.minOrNull()} ")
    print("${array.maxOrNull()}")
}