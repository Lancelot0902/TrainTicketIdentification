### 火车票识别

#### 识别方法和工具

首先将火车票按信息分割成几个区域，然后对每块信息单独识别。

使用基于Python的OpenCV将原图像读入并分割处理，再保存分割后的图像，最后远程调用百度OCR的API分别识别图像并输出到info.txt中。操作系统为Ubuntu18.04。

#### 文件结构

train_ticket_identification
* ticket_identify.py：读入并分割图像并识别。
* OCR.py：实现API的调用。
* info.txt：保存输出的车票信息
* pictures：存放分割后的图像