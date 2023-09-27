import java.util.*
import java.util.Collections

fun main() = with(Scanner(System.`in`)) {
    var (a,b,c) = readln().split(' ').map { it.toInt() }
    val list = listOf(a,b,c)
    var n : Int

    if(a==b && b==c){
        n = 10000 + a*1000
    }else if(a==b){
        n=1000+a*100
    }else if(b==c){
        n = 1000 + b*100
    }else if(c==a){
        n = 1000 + c*100
    }else{
        n=Collections.max(list)*100
    }

    print(n)
}