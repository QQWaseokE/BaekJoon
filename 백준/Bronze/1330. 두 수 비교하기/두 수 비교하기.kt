import java.util.*

fun main() = with(Scanner(System.`in`)) {
    var (a, b) = readln().split(' ').map { it.toInt() }

    if (a > b){
        print(">")
    } else if (a < b){
        print("<")
    } else {
        print("==")
    }
}