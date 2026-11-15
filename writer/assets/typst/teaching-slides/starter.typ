#import "vendor/calmly-touying/lib.typ": *
#import "style.typ": *

// Replace these illustrative lesson pages with the selected exercises.
#show: calmly.with(
  variant: "light",
  colortheme: "paper",
  header-style: "minimal",
  progressbar: "none",
  title-layout: "moloch",
  config-info(
    title: [编程习题讲解],
    subtitle: [思路、状态变化与代码],
    institution: [课堂练习],
    date: [#datetime.today().display("[year]年[month]月[day]日")],
  ),
)
#set text(lang: "zh", region: "CN")
#set par(leading: 0.75em, spacing: 14pt)
#set list(spacing: 16pt)
#title-slide()

== 栈：在列表右端加入和取出

从 `stack = [10, 20]` 开始，连续执行：

#lesson-table(columns: 3,
  [*操作*], [*返回值*], [*操作后的 stack*],
  [`stack.append(30)`], [`None`], [`[10, 20, 30]`],
  [`stack[-1]`], [`30`], [`[10, 20, 30]`],
  [`stack.pop()`], [`30`], [`[10, 20]`],
)

#hint[右端是栈顶；查看和弹出前先确认列表非空。]

== reverse：区分列表变化与返回值

```python
a = [1, 2, 3]
result = a.reverse()
print(a)       # [3, 2, 1]
print(result)  # None
```

#hint[reverse 原地修改 a；不要把它的返回值重新赋给 a。]

== 用两次操作跟踪同一个栈

#lesson-table(columns: 3, widths: (0.7fr, 1.6fr, 1.3fr),
  [*步骤*], [*执行*], [*栈：底部到顶部*],
  [初始], [`stack = [10]`], [`[10]`],
  [第1步], [`stack.append(20)`], [`[10, 20]`],
  [第2步], [`value = stack.pop()`], [`[10]`，value 为20],
)

#hint[先加入的10仍在底部；后加入的20先被弹出。]
