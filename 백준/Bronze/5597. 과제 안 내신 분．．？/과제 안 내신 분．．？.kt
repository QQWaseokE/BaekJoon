import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    var basket = IntArray(30)
    var basket2 = IntArray(30)

    for (i in 0 until 28) {
        val N = nextInt()
        basket[i] = N

    }

    for (j in 0 until 30) {
        basket2[j] = j+1
    }

    for (i in 0 until 30) {
        for (j in 0 until 30) {
            if(basket2[j] == basket[i]){
                basket2[j] = 33
                break
            }
        }
    }

    for (j in 0 until 30) {
        if (basket2[j] != 33) {
            println(basket2[j])
        }
    }
}