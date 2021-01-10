Textrank4zh2（下文称之为“当前项目”）基于textrankzh（下文称之为“原项目”）改进而来，原理及使用方式与其大体一致。当前仅在Python3环境得到验证。

------

主要变更：

- util.py --> util2.py

  更改combine方法中window的实现：原项目window对应的是窗口个数而非窗口大小，当前项目实现真正的窗口大小。

- 引入价值密度概念，以抽取的关键词为密度单位，确定摘要句子的重要程度，对摘要句子做打分调整。

  优化方案1对应test/word_density.py；优化方案2对应test/word_sen_density.py；具体原理可参考[博客](https://blog.csdn.net/phynikesi/article/details/109229117)。