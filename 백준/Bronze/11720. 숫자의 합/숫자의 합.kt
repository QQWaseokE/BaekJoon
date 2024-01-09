import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    val str = next()
    val array = str.toList()
    var sum = 0

    for (i in 0 until n) {
        val num = array[i]
        sum += num - '0'
    }

    println(sum)

}