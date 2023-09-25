import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val (a, b, c) = Triple(nextInt(), nextInt(), nextInt())

    println((a+b)%c)
    println(((a%c)+(b%c))%c)
    println((a*b)%c)
    println(((a%c)*(b%c))%c)
}