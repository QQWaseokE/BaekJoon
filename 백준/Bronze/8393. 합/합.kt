import java.util.*

fun main() = with(Scanner(System.`in`)) {
    var n = nextInt()
    var total : Int = 0

    for(i : Int in 1..n)
        total = total + i
        
    print(total)
}