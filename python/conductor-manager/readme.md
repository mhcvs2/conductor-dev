<pre><code>
1. 安装
pip install -r requirements.txt
python setup.py install

2. 配置
默认配置位置: /etc/cm.conf， 也可运行时用--config-file指定

[DEFAULT]
register_check_path=
存放定义文件的根目录， 定义内容是json格式

[conductor]
server_url=http://ip:port/api

conductor server的访问地址
也可用环境变量CONDUCTOR_SERVER_URL覆盖


3. help
conductor-manager.exe -h
usage: conductor-manager [register|cw|ct]

optional arguments:
  -h, --help          show this help message and exit
  --config-dir DIR    Path to a config directory to pull `*.conf` files from.
                      This file set is sorted, so as to provide a predictable
                      parse order if individual options are over-ridden. The
                      set is parsed after the file(s) specified via previous
                      --config-file, arguments hence over-ridden options in
                      the directory take precedence.
  --config-file PATH  Path to a config file to use. Multiple config files can
                      be specified, with values in later files taking
                      precedence. Defaults to None.
  --version           show program's version number and exit

Commands:
  {register,cw,ct}    Available commands
    register          Register workflow/task definition to conductor server
    cw                Create workflow definition file form template
    ct                Create task definition file form template

4. 示例

创建定义文件
conductor-manager cw mhc1 --sub_path test1
conductor-manager ct mhc1 --sub_path test1
conductor-manager ct mhc2 --sub_path test1

修改下

注册定义:
conductor-manager register --path test1
</code></pre>