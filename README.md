# L-BFGS_tool

##简介
>L-BFGS_tool调用了alglib库中的L-BFGSpython版本的方法。

## 方法
  [L-BFGS](https://hehuihui1994.github.io/hehuihui1994.github.io/2016/08/28/L-BFGS/#more)
## 文件说明
* xalglib.py<br>
  含有L-BFGS方法的库文件。<br>
* manual.cpython.html<br>
  库文件xalglib.py的使用说明。<br>
* L-BFGS_test.py<br>
  输入的x为向量vec，求解使得函数最小时x的解。如func = 100*(x[0]+3)^4 + (x[1]-3)^4
* L-BFGS_test_matrix.py<br>
  输入的x为矩阵matrix，求解使得函数最小时x的解。如func = 100*(x_m[0][0] -1)^4 + (x_m[0][1]-2)^4 + 100*(x_m[1][0] -3)^4 + (x_m[1][1]-4)^4
