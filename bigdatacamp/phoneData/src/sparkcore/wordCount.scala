package sparkcore

import org.apache.spark.{SparkConf, SparkContext}

/**
 * localMode
 */
object WordCount {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setMaster("local").setAppName("My App")
    val sc = new SparkContext(conf)

    //使用sc创建RDD并执行相应的transformation和action
    sc.textFile("/Users/chenhao/github_code/study_made_me_happy/bigdatacamp/phoneData/src/sparkcore/data/1.txt")
      .flatMap(_.split(" "))
      .map((_, 1))
      .reduceByKey(_ + _, 1)
      .sortBy(_._2, false)
      .saveAsTextFile("/Users/chenhao/github_code/study_made_me_happy/bigdatacamp/phoneData/src/sparkcore/1out")
  }
}