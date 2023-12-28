import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val N = nextInt()
    val M = nextInt()
    var basket = IntArray(N)

    for (i in 0 until N) {
        basket[i] = i+1
    }
    
    for (num in 0 until M) {
        val i = nextInt()
        val j = nextInt()

        var k = basket[i-1]
        basket[i-1] = basket[j-1]
        basket[j-1] = k
    }
    
    for (i in 0 until N) {
        print(basket[i])
        print(" ")
    }
}