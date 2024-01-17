import java.util.Scanner
import kotlin.math.*

fun main() = with(Scanner(System.`in`)) {
    var (a, b) = readln().split(' ').map { it.toString() }

    var c = StringBuffer(a).reverse().toString()
    var d = StringBuffer(b).reverse().toString()

    println(listOf(c,d).max())
}