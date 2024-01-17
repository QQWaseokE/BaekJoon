import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val str = readLine()!!.trim().split(" ").toMutableList()
    str.removeAll(listOf(""))
    println(str.count())
}