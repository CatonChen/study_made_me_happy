### Hbase 作业实践
#### Hbase Java 代码
```java
package hBaseDemo;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.io.encoding.DataBlockEncoding;
import org.apache.hadoop.hbase.regionserver.BloomType;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * @author: chenhao
 * Date:2021-08-01
 * Des:HBase api
 */
public class HBaseDemo {
    public static final String ZK_CONNECT_KEY = "hbase.zookeeper.quorum";
    public static final String ZK_CONNECT_VALUE = "47.101.204.23:2181,47.101.216.12:2181,47.101.206.249:2181";

    public static HBaseAdmin admin = null;
    public static Connection connection = null;

    static {
        Configuration conf = HBaseConfiguration.create();
        conf.set(ZK_CONNECT_KEY, ZK_CONNECT_VALUE);
        // 获取 connection 对象
        try {
            connection = ConnectionFactory.createConnection(conf);
            admin = (HBaseAdmin) connection.getAdmin();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    public static void main(String[] args) throws Exception {

        //基本信息
        String tableName = "chenhao:student";
        String[] cfs = {"info", "score"};

        //创建表
        creatTable(tableName, cfs);

        //放一条自己的信息
        Table table = connection.getTable(TableName.valueOf(tableName));
        Put put = new Put(Bytes.toBytes("chenhao"));
        put.addColumn(Bytes.toBytes("info"), Bytes.toBytes("student_id"), Bytes.toBytes("G20200343200086"));
        put.addColumn(Bytes.toBytes("info"), Bytes.toBytes("class"), Bytes.toBytes("1"));
        put.addColumn(Bytes.toBytes("score"), Bytes.toBytes("understanding"), Bytes.toBytes("75"));
        put.addColumn(Bytes.toBytes("score"), Bytes.toBytes("programming"), Bytes.toBytes("82"));
        table.put(put);

        //全表打印
        printTable(tableName);
        // deleteTable(tableName);

        //关闭
        admin.close();
        connection.close();

    }

    /**
     * @param tableName 表名
     * @param familys   列族
     * @throws Exception
     */
    public static void creatTable(String tableName, String[] familys) throws Exception {
        //表名
        TableName studentTable = TableName.valueOf(tableName);
        if (admin.tableExists(studentTable)) {
            System.out.println("table is existed!");

            //显示所有的表名
            TableName[] tableNames = admin.listTableNames();
            for (TableName t : tableNames) {
                System.out.println(t);
            }

        } else {
            //设置列族
            List<ColumnFamilyDescriptor> descriptorList = new ArrayList<>();
            for (String cf : familys) {
                ColumnFamilyDescriptor descriptor = ColumnFamilyDescriptorBuilder.newBuilder(Bytes.toBytes(cf))
                        .setDataBlockEncoding(DataBlockEncoding.PREFIX)
                        .setBloomFilterType(BloomType.ROW)
                        .build();
                descriptorList.add(descriptor);
            }

            //设置表信息
            TableDescriptor tableDescriptor = TableDescriptorBuilder.newBuilder(studentTable)
                    .setColumnFamilies(descriptorList)
                    .build();

            admin.createTable(tableDescriptor);
            if (admin.tableExists(studentTable)) {
                System.out.println("table is created!");
            } else {
                System.out.println("table is uncreated!");
            }

            initData(tableName);
        }
    }


    /**
     * 删除表
     *
     * @param tableName 表名
     * @throws IOException
     */
    private static void deleteTable(String tableName) throws IOException {
        admin.disableTable(TableName.valueOf(tableName));
        admin.deleteTable(TableName.valueOf(tableName));
    }


    /**
     * 打印全表
     *
     * @param tableName 表名
     * @throws IOException
     */
    private static void printTable(String tableName) throws IOException {
        Table table = connection.getTable(TableName.valueOf(tableName));
        Scan scan = new Scan();
        ResultScanner scanner = table.getScanner(scan);
        printResultScanner(scanner);
    }


    /**
     * 打印结果
     *
     * @param rs hbase 的结果集
     */
    public static void printResultScanner(ResultScanner rs) {
        for (Result r : rs) {
            printResult(r);
        }

    }

    public static void printResult(Result result) {
        System.out.println(result);
    }


    /**
     * 初始化原始数据
     *
     * @param tableName 表名
     * @throws IOException
     */
    private static void initData(String tableName) throws IOException {

        Table table = connection.getTable(TableName.valueOf(tableName));
        List<Put> puts = new ArrayList<>();

        Put put = new Put(Bytes.toBytes("Tom"));
        put.addColumn(Bytes.toBytes("info"), Bytes.toBytes("student_id"), Bytes.toBytes("20210000000001"));
        put.addColumn(Bytes.toBytes("info"), Bytes.toBytes("class"), Bytes.toBytes("1"));
        put.addColumn(Bytes.toBytes("score"), Bytes.toBytes("understanding"), Bytes.toBytes("75"));
        put.addColumn(Bytes.toBytes("score"), Bytes.toBytes("programming"), Bytes.toBytes("82"));
        puts.add(put);

        put = new Put(Bytes.toBytes("Jerry"));
        put.addColumn(Bytes.toBytes("info"), Bytes.toBytes("student_id"), Bytes.toBytes("20210000000002"));
        put.addColumn(Bytes.toBytes("info"), Bytes.toBytes("class"), Bytes.toBytes("1"));
        put.addColumn(Bytes.toBytes("score"), Bytes.toBytes("understanding"), Bytes.toBytes("85"));
        put.addColumn(Bytes.toBytes("score"), Bytes.toBytes("programming"), Bytes.toBytes("67"));
        puts.add(put);

        put = new Put(Bytes.toBytes("Jack"));
        put.addColumn(Bytes.toBytes("info"), Bytes.toBytes("student_id"), Bytes.toBytes("20210000000003"));
        put.addColumn(Bytes.toBytes("info"), Bytes.toBytes("class"), Bytes.toBytes("2"));
        put.addColumn(Bytes.toBytes("score"), Bytes.toBytes("understanding"), Bytes.toBytes("80"));
        put.addColumn(Bytes.toBytes("score"), Bytes.toBytes("programming"), Bytes.toBytes("80"));
        puts.add(put);

        put = new Put(Bytes.toBytes("Rose"));
        put.addColumn(Bytes.toBytes("info"), Bytes.toBytes("student_id"), Bytes.toBytes("20210000000004"));
        put.addColumn(Bytes.toBytes("info"), Bytes.toBytes("class"), Bytes.toBytes("2"));
        put.addColumn(Bytes.toBytes("score"), Bytes.toBytes("understanding"), Bytes.toBytes("60"));
        put.addColumn(Bytes.toBytes("score"), Bytes.toBytes("programming"), Bytes.toBytes("61"));
        puts.add(put);

        table.put(puts);
        System.out.println("insert table Succeeded!");
    }

}
```

#### HBse shell 练习
```apache
# 创建表空间
create_namespace 'chenhao'
describe_namespace 'chenhao'

# 创建表
create 'chenhao:student','info','score'

# 插入数据
put 'chenhao:student','Tom','info:student_id' ,'20210000000001'
put 'chenhao:student','Jerry','info:student_id' ,'20210000000002'
put 'chenhao:student','Jack','info:student_id' ,'20210000000003'
put 'chenhao:student','Rose','info:student_id' ,'20210000000004'
put 'chenhao:student','chenhao','info:student_id' ,'G20200343200086'
put 'chenhao:student','Tom','info:class' ,'1'
put 'chenhao:student','Jerry','info:class' ,'1'
put 'chenhao:student','Jack','info:class' ,'2'
put 'chenhao:student','Rose','info:class' ,'2'
put 'chenhao:student','chenhao','info:class','1'
put 'chenhao:student','Tom','score:understanding' ,'75'
put 'chenhao:student','Jerry','score:understanding' ,'85'
put 'chenhao:student','Jack','score:understanding' ,'80'
put 'chenhao:student','Rose','score:understanding' ,'60'
put 'chenhao:student','chenhao','score:understanding' ,'70'
put 'chenhao:student','Tom','score:programming' ,'82'
put 'chenhao:student','Jerry','score:programming' ,'67'
put 'chenhao:student','Jack','score:programming' ,'80'
put 'chenhao:student','Rose','score:programming' ,'61'
put 'chenhao:student','chenhao','score:programming' ,'70'

# 获取数据
get 'chenhao:student','chenhao'
# 扫描表
scan 'chenhao:student'
# 统计总数
count 'chenhao:student'
# 删除数据
delete 'chenhao:student','chenhao','info:student_id'
# 删除表：先 disable 再 drop
disable 'chenhao:student'
drop 'chenhao:student'
```

#### 运行结果
![][image-1]
![][image-2]

[image-1]:	hbase01.png
[image-2]:	hbase02.png