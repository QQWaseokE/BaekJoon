import java.util.*
import java.io.*;

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var writer = BufferedWriter(OutputStreamWriter(System.out))

    for(i in 1..readLine().toInt()){
        for(j in 1..i){
            print("*")
        }
        println()
    }

}