import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    var (n,m) = readln().split(' ').map { it.toInt() }
    var basket = IntArray(n) {it + 1}

    for (l in 0 until m) {
        var (i,j) = readln().split(' ').map { it.toInt() }

        while (i<j) {
        val temp = basket[i-1]
        basket[i-1] = basket[j-1]
        basket[j-1] = temp
        i++
        j--
        }
    }

    basket.forEach {print("${it} ")}

}