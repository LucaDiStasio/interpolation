# -*- coding: utf-8 -*-

'''
=====================================================================================

Copyright (c) 2017 Université de Lorraine & Luleå tekniska universitet
Author: Luca Di Stasio <luca.distasio@gmail.com>
                       <luca.distasio@ingpec.eu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

=====================================================================================

DESCRIPTION



Tested with Python 2.7 Anaconda 2.4.1 (64-bit) distribution
       in Windows 7.


'''

import sys

def zeros(m,n):
    res = []
    if m>1 and n>1:
        for i in range(0,m):
            row = []
            for j in range(0,n):
                row.append(0.0)
            res.append(row)
    elif m>1:
        for i in range(0,m):
            res.append(0.0)
    else:
        for i in range(0,n):
            res.append(0.0)
    return res

def ones(m,n):
    res = []
    if m>1 and n>1:
        for i in range(0,m):
            row = []
            for j in range(0,n):
                row.append(1.0)
            res.append(row)
    elif m>1:
        for i in range(0,m):
            res.append(1.0)
    else:
        for i in range(0,n):
            res.append(1.0)
    return res

def dividedDiffNewton(x,y):
    #  Input: N x 1 vector x of interpolation nodes
    #         N x 1 vector y of values at interpolation nodes
    #  Output: N x N lower-triangular matrix d of divided differences
    my = len(y)
    d = zeros(my,my);
    for i in range(0,my):
        d[i][0] = y[i]
    for j in range(1,my):
        for i in range(j,my):
            d[i][j] = (d[i][j-1]-d[i-1][j-1])/(x[i]-x[i-j+1])
    return d

def interpolantLagrange(x,xval,index):
    #  Input: N x 1 vector x of interpolation nodes
    #         M x 1 vector xval of nodes for function evaluation
    #         index "index" of current node
    #  Output: M x 1 vector l of interpolant evaluations
    N = len(x);
    M = len(xval);
    l = ones(M,1);
    for i in range(0,N):
        if i!=index:
            for j in range(0,M):
                l[j] = l[j]*(xval[j]-x[i])./(x[index]-x[i])
    return l

def interpLagrange1D(x,y,z):
    # Input: N x 1 vector x of interpolation nodes
    #        N x 1 vector y of values at interpolation nodes
    #        M x 1 vector z of nodes for function evaluation
    #  Output: M x 1 vector f of function evaluations
    d = dividedDiffNewton(x,y)
    N = len(x)
    M = len(z)
    f = zeros(M,1)

    for k=1:size(x,1)
        omega = ones(size(z,1),1)
        for j=1:k-1
            omega = omega.*(z-x(j,1))
        f = f + omega*d(k,k);
    return f

def interpLagrange2D():

def interpLagrange3D():

def interpHermite1D():

def interpHermite2D():

def interpHermite3D():


def main(argv):


if __name__ == "__main__":
    main(sys.argv[1:])
