import java.util.*

fun main() = with(Scanner(System.`in`)) {
    var n = nextInt()

    for(i : Int in 1..n)
        println(nextInt() + nextInt())
}