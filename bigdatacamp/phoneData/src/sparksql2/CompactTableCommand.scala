/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.spark.sql.execution.command

import java.net.URI
import java.util.Date

import org.apache.hadoop.fs.{FileSystem, Path}
import org.apache.log4j.Logger

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.{Row, SaveMode, SparkSession, SQLContext}
import org.apache.spark.sql.catalyst.TableIdentifier
import org.apache.spark.sql.catalyst.catalog.{CatalogTable, CatalogTableType, InMemoryCatalog, SessionCatalog}
import org.apache.spark.sql.catalyst.parser.ParserInterface
import org.apache.spark.sql.internal.{SessionState, SharedState}



case class CompactTableCommand(
    targetTable: TableIdentifier,
    partSpecs: partitionSpec,
    fileNum: Int) extends LeafRunnableCommand {

    val sparkConf = new SparkConf().setMaster("local[*]").setAppName("mergeFile")
    val sc = new SparkContext(sparkConf)
    val sqlContext = new HiveContext(sc)
    val fileSystem = FileSystem.get(sc.hadoopConfiguration)
    val logger = Logger.getLogger("org")

  override def run(sparkSession: SparkSession): Seq[Row] = {
    /*
    * * 合并步骤：
    * 1. 将小文件目录(srcDataPath)下的文件移动到临时目录/mergePath/${mergeTime}/src
    * 2. 使用coalesce或者repartition， 传入分区数(默认500)。 将数据写入临时的数据目录(/mergePath/${mergeTime}/data)
    * 3. 将临时数据目录文件move到文件目录(srcDataPath)
    * 4. 删除临时目录(mergePath)
    * */
    val srcDataPath = getTableLocation(targetTable.toString, sparkSession)
    val mergePath = "/Users/chenhao/github_code/spark/data/mergeTmp"
    val mergeTime = new Date().getTime.toString
    val partitionSize = fileNum
    val result = mergeFiles(sqlContext, fileSystem,
        mergeTime, srcDataPath, mergePath, partitionSize)
    Seq(Row(logger.info("result: " + result)))
  }

  def mergeFiles(sqlContext: SQLContext, fileSystem: FileSystem, mergeTime: String,
                 srcDataPath: String, mergePath: String, partitionSize: Int): String = {
    val mergeSrcPath = mergePath + "/" + mergeTime + "/src"
    val mergeDataPath = mergePath + "/" + mergeTime + "/data"
    var mergeInfo = "merge success"

    try {
      /*
      * 1.将需要合并的文件mv到临时目录
      * 2.将合并目录的src子目录下的文件合并后保存到合并目录mergeDataPath的data子目录下
      * 3.利用coalesce函数对数据文件重新分区（repartition函数应该也可以做到），即合并，并将文件保存至mergeDataPath目录下。
      * 3.将mergeDataPath的data目录下的文件移动到原目录
      * 4.删除合并目录src的子目录
      * */
      moveFiles(fileSystem, mergeTime, srcDataPath, mergeSrcPath, true)
      val srcDF = sqlContext.read.format("parquet").load(mergeSrcPath + "/")
      srcDF.coalesce(partitionSize).write.format("parquet")
        .mode(SaveMode.Overwrite).save(mergeDataPath)
      moveFiles(fileSystem, mergeTime, mergeDataPath, srcDataPath, false)
      fileSystem.delete(new Path(mergePath + "/" + mergeTime), true)

    } catch {
      case e: Exception => e.printStackTrace()
        mergeInfo = "merge failed"
    }
    mergeInfo
  }

  def moveFiles(fileSystem: FileSystem, mergeTime: String, fromDir: String,
                destDir: String, ifTruncDestDir: Boolean): Unit = {
    /*
    * 1.判断目标目录是否存在，不存在即建立
    * 2.是否清空目标目录下面的所有文件
    * 3.将srcDataPath目录下的除"_SUCCESS"外的文件逐个移动到mergeSrcPath目录下
    * */

    val fromDirPath = new Path(fromDir)
    val destDirPath = new Path(destDir)

    if (!fileSystem.exists(new Path(destDir))) {
      fileSystem.mkdirs(destDirPath.getParent)
    }

    if (ifTruncDestDir) {
      fileSystem.globStatus(new Path(destDir + "/*") )
        .foreach(x => fileSystem.delete(x.getPath(), true))
    }

    var num = 0
    fileSystem.globStatus(new Path(fromDir + "/*")).foreach(x => {
      val fromLocation = x.getPath().toString
      val fileName = fromLocation.substring(fromLocation.lastIndexOf("/") + 1)
      val fromPath = new Path(fromLocation)

      if (fileName != "_SUCCESS") {
        var destLocation = fromLocation.replace(fromDir, destDir)
        val fileSuffix = if (fileName.contains("."))
          {fileName.substring(fileName.lastIndexOf("."))}
          else {""}
        val newFileName = mergeTime + "_" + num + fileSuffix
        destLocation = destLocation.substring(0, destLocation.lastIndexOf("/") + 1) + newFileName
        num = num + 1

        val destPath = new Path(destLocation)

        if (!fileSystem.exists(destPath.getParent)) {
          fileSystem.mkdirs(destPath.getParent)
        }
        fileSystem.rename(fromPath, destPath) // hdfs dfs -mv
      }
    })
  }

  def getTableLocation(table: String, sparkSession: SparkSession): String = {
      val sessionState: SessionState = sparkSession.sessionState
      val sharedState: SharedState = sparkSession.sharedState
      val catalog: SessionCatalog = sessionState.catalog
      val sqlParser: ParserInterface = sessionState.sqlParser
      val client = sharedState.externalCatalog match {
        case catalog: HiveExternalCatalog => catalog.client
        case _: InMemoryCatalog => throw new IllegalArgumentException("In Memory catalog doesn't " +
          "support hive client API")
      }
      val idtfr = sqlParser.parseTableIdentifier(table)
      require(catalog.tableExists(idtfr), new IllegalArgumentException(idtfr + " done not exists"))
      val rawTable = client.getTable(idtfr.database.getOrElse("default"), idtfr.table)
      rawTable.location.toString
  }
}
