import java.util.*

fun main() = with(Scanner(System.`in`)) {
    var (H,M) = readln().split(' ').map { it.toInt() }

    if(M>44){
        M = M -45
    }else{
        if(H>=1){
            H--
            M = M+ 15
        }else{
            H = 23
            M = M+ 15
        }
    }
    println("${H} ${M}")
}