import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()

    for (i in 0 until n) {
        val m = nextInt()
        val str = next()
        var result = ""

        for(j in str.indices) {
            repeat(m) {
                result += str[j]
            }
        }
        println(result)
    }
}