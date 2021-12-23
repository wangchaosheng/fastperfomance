研发历程：
1.swarm->start接口修改，stop接口，init接口修改（12月1日完成）
衍生任务：搞明白locust的运行原理，自己改写一套适合的master逻辑
12月2，3日
①runner逻辑整理 ②enviorment逻辑整理 ③stats逻辑整理
计划把stats逻辑加到client上去runner只负责发送指令不再控制web状态
12月4日
①requeststats的汇总逻辑梳理 ②目的是每次stop的时候就把本分支的数据存到数据库里面去
12月5日-12月8日
复习计算机基础，python基础+python高阶（有些代码逻辑看不懂）
12月9日
①在envethook.worker_report()中添加对clients[client_id]stat = Reqeuststats()
并根据client去统计数据
②写一个extend_report方法去统计所有请求的数据并且与前端数据对比