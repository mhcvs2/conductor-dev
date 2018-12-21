operation
-------------
<pre><code>
conductor-cli start -n put_metadata -i '{"metadata_script":"/root/gitSwarm/metadata/gen_consul_data_for_mysql_ms.py"}'

conductor-cli start -n scale_cluster -i 
'{"metadata_script":"/root/gitSwarm/metadata/gen_consul_data_for_mysql_ms.py","image":"registry.bst-1.cns.bstjpc.com:5000/dbelt/mysql-ms-mysql-v5.6.36-v0.2.0:20171207","compose_file":"/root/gitSwarm/dbcm-base-managers/compose/mysql.yml","service_name":"mysql","number":"2"}'

conductor-cli start -n delete_cluster -i '{"cluster_id":"mysqlms723","compose_file":"/root/gitSwarm/dbcm-base-managers/compose/mysql.yml"}'

conductor-cli start -n delete_cluster_maz -i '{"cluster_id":"mysqlms848","compose_file":"/root/gitSwarm/dbcm-base-managers/compose/mysql.yml"}'

conductor-cli start -n scale_cluster_mysql_ms -i '{"image":"registry.bst-1.cns.bstjpc.com:5000/dbelt/mysql-ms-mysql-v5.6.36-v0.5.0:20180118","number":"2"}'

conductor-cli start -n scale_cluster_mysql_ms_maz -i '{"image":"registry.bst-1.cns.bstjpc.com:5000/dbelt/mysql-ms-mysql-v5.6.36-v0.2.0:20171226","number":"1"}'

conductor-cli start -n scale_cluster_mysql_pxc -i '{"image":"registry.bst-1.cns.bstjpc.com:5000/dbelt/mysql-pxc-mysql-v5.6-v0.5.0:20180111","number":"2"}'

conductor-cli start -n scale_cluster_redis_ms -i '{"image":"registry.bst-1.cns.bstjpc.com:5000/dbelt/redis-ms-redis-v3.2-v0.5.0:20180111","number":"3"}'






conductor-cli start -n scale_nodes_mysql_ms -i '{"cluster_id":"mysqlms140","number":"3"}'
conductor-cli start -n scale_nodes_mysql_pxc -i '{"cluster_id":"mysqlms197","number":"3"}'















conductor-cli start -n consul_clear_service

</code></pre>
