import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    var n = nextInt()
    var score = IntArray(n)
    var sum:Double = 0.0

    for (i in 0 until n) {
        score[i] = nextInt()
    }

    val maxScore = score.max()

    for (i in 0 until n) {
        var cheat:Double = (score[i].toDouble()/maxScore.toDouble())*100
        sum = sum + cheat
    }

    print(sum/n)
}