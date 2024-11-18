# UEFA_DataAnalysis

数据分析萌新的小课题

---

## 文档结构

- 代码文件夹
  - .ipynb文件
  - 爬虫代码
  - 数据清洗代码
  - 数据分析代码
- 数据文件夹
    - 爬取数据
    - 清洗数据
    - 分析数据
- 文档
    - 笔记文档
    - 项目简介
    - 元数据

## 数据分析发现

### 黄牌数量

#### 各裁判每场黄牌数

![alt text](image.png)

存在两场异常值：
- match_id 2036195：小组赛 捷克    vs  土耳其 黄牌数18张
- match_id 2036205：淘汰赛 西班牙 vs  德国    黄牌数15张

该指标后续分析将排除这两场比赛

排除异常值后初步描述黄牌数分布情况

比赛数量 | 平均 | 标准差 | 最小值 | 25% | 中位数 | 75% | 最大值
----|----|----|----|----|----|----|----
49 | 4.22 | 1.96 | 1 | 3 | 4 | 5 | 9

各裁判平均黄牌数

ref_name | yellow_cards | match_count
----|----|----
Jesús Gil Manzano | 7.00 | 1
Daniel Siebert | 7.00 | 2
Danny Makkelie | 7.00 | 2
Umut Meler | 6.33 | 3
István Kovács | 6.00 | 2
Felix Zwayer | 4.75 | 4
Clément Turpin | 4.67 | 3
Slavko Vinčić | 4.67 | 3
Facundo Tello | 4.50 | 2
Daniele Orsato | 4.25 | 4
Marco Guida | 4.00 | 2
Ivan Kružliak | 4.00 | 2
Glenn Nyberg | 3.67 | 3
Sandro Schärer | 3.50 | 2
François Letexier | 3.50 | 4
Artur Soares Dias | 3.00 | 3
Szymon Marciniak | 3.00 | 2
Michael Oliver | 2.00 | 4
Anthony Taylor | 1.50 | 3

#### 不同比赛阶段黄牌数

phase | yellow_cards
----|----
Group | 4.47
Knockout | 5.27

淘汰赛阶段的身体接触果然还是要更火爆一些！


### 跑动数据
#### 各球队平均跑动距离
team_name | distance_covered
----|----
Portugal | 127.15
Slovakia | 124.76
Slovenia | 122.73
Germany | 122.12
England | 120.87
Switzerland | 119.57
Spain | 118.95
Croatia | 118.90
Czechia | 117.15
Italy | 116.47
Albania | 115.83
Austria | 115.54
Ukraine | 114.50
France | 113.77
Serbia | 113.57
Hungary | 113.09
Poland | 112.94
Denmark | 112.81
Türkiye | 112.55
Georgia | 112.14
Scotland | 111.64
Romania | 111.59
Belgium | 109.97
Netherlands | 108.38

#### 跑动更多的球队赛果统计
比赛结果 | 场次
----|----
获胜 | 19
打平 | 18
失利 | 14