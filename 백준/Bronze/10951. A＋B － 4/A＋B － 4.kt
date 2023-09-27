import java.util.*
import java.io.*;

fun main() = with(Scanner(System.`in`)) {

    while(hasNextInt()){
        val a = nextInt()
        val b = nextInt()

        println("${a + b}")
    }
}