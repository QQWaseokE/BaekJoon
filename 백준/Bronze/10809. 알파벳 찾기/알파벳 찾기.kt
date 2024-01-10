import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val str = next()
    val a = "abcdefghijklmnopqrstuvwxyz"
    val array = str.toList()

    for (i in a) {
        if (i in array) {
            print(array.indexOf(i))
            print(" ")
        }
        else {
            print("-1 ")
        }
    }
}