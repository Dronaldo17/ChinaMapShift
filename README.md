ChinaMapShift
=============
Algorithm for the map offset problem in China.
解决中国地图偏移问题的算法。

Include a KML file processor (Python) to transform coordinates between WGS-84 and GCJ-02 (China).／
提供在通用的 WGS-84 坐标系和中国的 GCJ-02 坐标系间，转换 KML 文件中的地理坐标的 Python 脚本。

-------
Enviornment／
环境要求

Ensure you have china_shift.dll stored in the same folder with china_shift.py.／
首先确定库文件 china_shift.dll 与脚本 china_shift.py 在同一文件夹下。

And you have python 2.7 installed on your system, together with the following libraries.／
并确定你的系统安装了 Python 及其以下库（一般的 Python 安装都自带这些库）：
    ctypes, 
    argparse, 
    xml, 
    csv

-------
Usage／
使用方法

In terminal／
在命令行下运行

    python china_shift.py -g input.kml

to transform all coordinates in input.kml from WGS-84 to GCJ-02.／
将文件 input.kml 中的坐标由 WGS-84 坐标系转换到 GCJ-02 坐标系。

and／
而

    python china_shift.py -w input.kml

to transform all coordinates in input.kml from GCJ-02 to WGS-84.／
将文件 input.kml 中的坐标由 GCJ-02 坐标系转换到 WGS-84 坐标系。

-------
More／
其他

The source code of the china_shift.dll library is in /algorithm. It contains the algorithm for transformation.／
动态链接库文件 china_shift.dll 的源代码位于 /algorithm 文件夹下，该代码包含转换算法。

    china_shift.c   --> source file / 源文件
    china_shift.h   --> header file / 头文件

Most of this source code comes from someone anonymous on the Internet. transformFromGCJToWGS() is added by me (fengzee@fengzee.me).／
该算法的大多数部分来自网络。GCJ-02 转换到 WGS-84 的算法 transformFromGCJToWGS() 由我（fengzee@fengzee.me）使用迭代法在其逆变换的基础上实现。

Please be aware that it might be illegal or politically risky in China to use or transmit this algorithm.／
请注意，使用和传播此算法可能违反中国有关国家秘密的相关法律。

Evil is evil. I take the risk. ／
我认为中国政府相关部门使用此算法进行的地图偏移政策是不正确的。我自愿承担这一风险传播此算法。
