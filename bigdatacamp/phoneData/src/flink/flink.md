### Flink作业
#### 实现SpendReport.java中report功能的代码
```java
public static Table report(Table transactions) {
        return transactions
            .window(Tumble.over(lit(1).hour()).on($("transaction_time")).as("log_ts"))
            .groupBy($("account_id"), $("log_ts"))
            .select(
                    $("account_id"),
                    $("log_ts").start().as("log_ts"),
                    $("amount").sum().as("amount"));
    }
```

#### 在flink-playgrounds/table-walkthrough下进行编译和启动。
![](%E6%88%AA%E5%9B%BE20211023214946.png)

#### 通过访问localhost:8082打开Flink WebUI界面，观察作业运行情况。
![](%E6%88%AA%E5%9B%BE20211023221018.png)
![](%E6%88%AA%E5%9B%BE20211023221216.png)
![](%E6%88%AA%E5%9B%BE20211023221344.png)![](%E6%88%AA%E5%9B%BE20211023221438.png)

#### 通过命令进入mysql查询spend\_report表的数据
```bash
docker-compose exec mysql mysql -Dsql-demo -usql-demo -pdemo-sql
```
**在mysql命令行中查询表spend\_report的结果**
![](%E6%88%AA%E5%9B%BE20211023222108.png)
**通过SQL命令查询account\_id的amount汇总**
```sql
mysql> select account_id, sum(amount) as amount  from spend_report group by account_id order by account_id asc;

+------------+---------+
| account_id | amount  |
+------------+---------+
|          1 | 9753596 |
|          2 | 9814922 |
|          3 | 9752390 |
|          4 | 9775318 |
|          5 | 9712801 |
+------------+---------+
```

#### 在grafana中查询walkthrough的dashboard，两者一致。
![](%E6%88%AA%E5%9B%BE20211023222742.png)
