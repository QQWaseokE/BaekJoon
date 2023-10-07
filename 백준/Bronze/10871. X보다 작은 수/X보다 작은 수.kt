import java.util.*
import java.io.*;

fun main() = with(Scanner(System.`in`)) {
    var (n, a) = readln().split(' ').map { it.toInt() }
    val array = ArrayList<Int>()
    for (i in 1..n){
        array.add(nextInt())
    }

    for(i in array){
        if(i<a){
            print(i)
            print(" ")
        }
    }
}