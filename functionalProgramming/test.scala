object test {
  object sierpinskiTri {
    class Triangle(top:(Int, Int), row:Int, col:Int){
        def getRow()= row
        def getCol()= col
        def getTop()= top
        
        def tri2CanvasCor(top:(Int, Int), row:Int, col:Int):Seq[(Int, Int)]={
            row match {
            case 1 => Seq(top)
            case k => tri2CanvasCor(top, k-1, col-2) ++ {for (j <- 1 until col) yield (row, j)}
            }
        }

        def triangleTrans():Vector[Triangle]={
            Vector(new Triangle(top, row/2, (col-1)/2),
                   new Triangle((top._1+row/2, top._2-row/2), row/2, (col-1)/2),
                   new Triangle((top._1+row/2, top._2+row/2), row/2, (col-1)/2)
                   )
                }
    }

    class Canvas(seqOfOne:Seq[(Int, Int)], row:Int=32, col:Int=63){
        def seqOfOne():Seq[(Int, Int)] = seqOfOne
        def canvasCor():Seq[String]={
            for (i <- 1 until row)
                yield Seq.fill(col)("_").zipWithIndex.map(x=>if (seqOfOne.contains((i, x._2+1))) "1" else "_").mkString("")
        }
        def drawCanvas()
            println(canvasCor().mkString("\n"))
    }
    
    def allTriangleTrans(original:Vector[Triangle]):Vector[Triangle] = {
        original.flatMap(x=>x.triangleTrans())
    }
        
    def triangleAsCor(triCollection:Vector[Triangle]):Seq[(Int, Int)]={
            triCollection.flatMap(x=>x.tri2CanvasCor(x.getTop(), x.getRow(), x.getCol()))
    }


    
    def trianglesN(triangles:Vector[Triangle], n:Int):Canvas={
        n match {
            case 0 => new Canvas(triangleAsCor(triangles))
            case k => trianglesN(allTriangleTrans(triangles),k-1)
        }
    }
    println(trianglesN(Vector(new Triangle((1,32), 32, 63)), 0))
    }
}