import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val N = nextInt()
    val M = nextInt()
    var basket = IntArray(N)
    
    for (chance in 0 until M) {
        val i = nextInt()
        val j = nextInt()
        val k = nextInt()

        for (number in i-1 until j) {
            basket[number] = k
        }
    }
    
    for (i in 0 until N) {
        print(basket[i])
        print(" ")
    }
}