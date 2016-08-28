# -*- coding: utf-8 -*-

'''
x为vec
'''

import xalglib

def function1_grad(x, grad, param):
    #
    # this callback calculates f(x0,x1) = 100*(x0+3)^4 + (x1-3)^4
    # and its derivatives df/d0 and df/dx1
    #
    func = 100*(x[0]+3)**4 + (x[1]-3)**4
    #计算一阶导
    grad[0] = 400*(x[0]+3)**3
    grad[1] = 4*(x[1]-3)**3
    return func


if __name__ == '__main__':
	#从（0,0）出发
	x = [0,0]
	epsg = 0.0000000001
	epsf = 0
	epsx = 0
	maxits = 0

	#initializes algorithm state
	#1表示修正个数，M-BFGS算法中要求的海塞矩阵更新数，3<=M<=7  M<=N
	#state-存储算法状态
	state = xalglib.minlbfgscreate(1, x)
	'''
	tunes solver parameters 调整参数
	通过MinLBFGSSetCond()函数调整停止条件
	如果目标函数包括exp()或者其他快增长的功能函数，优化算法可能导致溢出，
	使用MinLBFGSSetStpMax()函数限制算法的步长，然而，L-BFGS算法很少需要这样的调整
	MaxIts-最大迭代次数，如果为0，则不限制迭代次数
	如果EpsG=0, EpsF=0, EpsX=0 且 MaxIts=0 则使用默认设置
	'''
	xalglib.minlbfgssetcond(state, epsg, epsf, epsx, maxits)
	#calculates F/G.
	#调用计算函数function1_grad计算在点x的函数和梯度值
	xalglib.minlbfgsoptimize_g(state, function1_grad)
	#get solution
	#rep为optimization report，可以检测错误原因
	'''
	rep-优化反馈--- 结束类型:
       * -8    internal integrity control  detected  infinite
	           or NAN values in  function/gradient.  Abnormal
	           termination signalled.
	   * -7    gradient verification failed.
	           See MinLBFGSSetGradientCheck() for more information.
	   * -2    rounding errors prevent further improvement.
	           X contains best point found.
	   * -1    incorrect parameters were specified
	   		   制定了不正确的参数 
	   *  1    relative function improvement is no more than
	           EpsF.相关函数的改进只是epsF
	   *  2    relative step is no more than EpsX.
	   		   相关步长只是EpsX 
	   *  4    gradient norm is no more than EpsG
	   		   梯度规范化只是EpsG 
	   *  5    MaxIts steps was taken
	   *  7    stopping conditions are too stringent,
	           further improvement is impossible
	           停止约束太过严格，还有提升的空间
	   *  8    terminated by user who called minlbfgsrequesttermination().
	           X contains point which was "current accepted" when
	           termination request was submitted.
	'''
	x, rep = xalglib.minlbfgsresults(state)

	print(rep.terminationtype) # expected 4
	print(x) # expected [-3,3]