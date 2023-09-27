import java.util.*

fun main() = with(Scanner(System.`in`)) {
    var (H,M) = readln().split(' ').map { it.toInt() }
    var N = nextInt()
    var T : Int = M+N

    while (T>=60){
        if (T>=60){
            H += 1
            T -= 60
            if (H==24){
                H = 0
            }
        }
    }

    println("${H} ${T}")
}