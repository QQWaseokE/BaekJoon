import java.util.*

fun main() = with(Scanner(System.`in`)) {
    var a = nextInt()

    val grade = when(a){
        in 90 .. 100 -> "A"
        in 80 .. 89 -> "B"
        in 70 .. 79 -> "C"
        in 60 .. 69 -> "D"
        else -> "F"
    }
    print(grade)
    }