import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()

    for(i in 0 until n) {
        val str = next()
        println("${str[0]}${str[str.lastIndex]}")
    }
}