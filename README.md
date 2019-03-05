# Gchart *description* 

version 0.0.0

## 一. 功能

辅助分析 ctf 中有关于堆利用的 pwn 题，本工具旨在构建一套简单易用的堆利用框架，目前设想其主要功能为作为 EXP 的父模板，结合程序逻辑创建出一张直观的**堆图像**，达到堆可视化的目的。

## 二. 技术细节

开发语言 python

### 1. 数据结构


**heap**

为了构建方便将其抽象为一个栈(python 中可以使用 list 表示)，如图

```
                     malloc a chunk
           +-----------------------------+
           |        equal to push        |
           |                             |
           |                             |
           |                             v
           |
+----------+-----------+     +------------------------+
|                      |     |                        |
|                      |     |                        |
|      chunk c         |     |                        |
|                      |     |       TOP CHUNK        |    <-------+  virtual, not real
|                      |     |                        |
+----------------------+     |                        |
                             |                        |
                             +------------------------+
                             |                        |
                             |                        |
                             |       chunk b          |   <------------+ free a chunk
                             |                        |
                             |                        |                  equal to pop
                             +------------------------+
                             |                        |
                             |                        |
                             |       chunk  a         |
                             |                        |
                             |                        |
                             +------------------------+

```



**bins**

缓冲区的存在使得整个 malloc 变得很复杂，参照 heap 的数据结构， bins 将以链表形式存在



### 2. 项目文件组织方式

模块化是核心设计思想，目前将整个项目划分为以下几个模块

```
Gchart
     |
     +---+ config.py
     |
     +---+ Gchart.py       main file
     |
     |
     +---+ models.py       chunk and bins model
     |
     |
     +---+ views.py        show images
     |
     |
     |
     +---+ rules.py        define malloc and free rules
     |
     |
     +---+ utils.py        store some useful func
     +
     
```



### 3. 视图构建

利用 ASCII FLOW 样式构建，根据每个堆块的 size 进行高度换算(要将所有数据打印在屏幕上，还是设置阈值？)，并根据内容范围进行色彩填充，以达到直观、用户友好的目的。





## 三. Further scenarios

1. 由于每一个程序的行为都是不确定的，为了使模型达到最大化兼容效果，能否摆脱脚本的束缚，而直接对 malloc 、free 进行 hook，以达到精确跟踪每一个堆块的目的。
2. 模型稳定之后，接入堆溢出的辅助功能(payload生成、甚至半自动化测试)。
