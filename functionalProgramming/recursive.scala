object Solution {
    def pascalTriangle(levels:Int):Unit={
        def factorial(n:Int):Int = {
            n match {
                case 1 => 1
                case k => k * factorial(k-1)
            }
        }
        // The value at nthrow and rth column of the triangle is equal to n! / (r! * (n-r)!)
        for (row <- 1 to levels)
            for (col <- 1 to row)
                println(factorial(row)/(factorial(col)*factorial(row-col)))
            println("\n")
    }
    pascalTriangle(5)
}