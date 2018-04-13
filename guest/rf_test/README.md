##### [使用pycharm编写和运行RF脚本](https://blog.csdn.net/CCGGAAG/article/details/77529724)

- 安装 intelliBot 插件
- 配置运行方式 Settings - Tools - External Tools
  ```
  $pybot.bat -d results test_if.robot
  $pybot.bat -d results -t testpost ./

  - 配置suite
    ```
    Robot Run TestSuite
    -d results $FileName$
    $FileDir$
    ```
    [](http://ot7pupwhi.bkt.clouddn.com/18-4-13/53722325.jpg)

  - 设置case
    ```
    Robot Run SingleTestCase
    -d results -t "$SelectedText$" ./
    $FileDir$
    ```
    [](http://ot7pupwhi.bkt.clouddn.com/18-4-13/31427253.jpg)
