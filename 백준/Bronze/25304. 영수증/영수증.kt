import java.util.*

fun main() = with(Scanner(System.`in`)) {
    var total = nextInt()
    var n = nextInt()
    var result : Int = 0

    for(i : Int in 1..n){
        var a = nextInt()
        var b = nextInt()

        result += a*b
    }

    if(total == result){
        print("Yes")
    }else {
        print("No")
    }
}