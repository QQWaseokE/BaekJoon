import java.util.*
import java.io.*;

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var writer = BufferedWriter(OutputStreamWriter(System.out))

    for(i in 1..readLine().toInt()){
        StringTokenizer(readLine()).run{
            val a = nextToken().toInt()
            val b = nextToken().toInt()

            writer.write("Case #$i: $a + $b = ${a+b}\n")
        }
    }

    writer.flush()
    writer.close()
    close()
}