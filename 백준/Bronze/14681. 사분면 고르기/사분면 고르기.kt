import java.util.*

fun main() = with(Scanner(System.`in`)) {
    var a = nextInt()
    var b = nextInt()

    if(a>0){
        if(b>0){
            print("1")
        }else{
            print("4")
        }
    }else{
        if(b>0){
            print("2")
        }else{
            print("3")
        }
    }
}