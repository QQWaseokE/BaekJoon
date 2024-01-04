import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    var basket = IntArray(10)

    for (i in 0 until 10) {
        val n = nextInt()
        val m = n%42
        basket[i] = m
    }

    print(basket.distinct().count())

}