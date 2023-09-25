import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val a = nextInt()
    val b = next()

    println(a*b[2].digitToInt())
    println(a*b[1].digitToInt())
    println(a*b[0].digitToInt())
    println(a*b.toInt())
}