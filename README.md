# Finance Calculator

## Overview
This is finance calculator is integrated with an investment calculator and a home loan repayment calculator to help you calculate the home loan repayment and investment.  

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [How to Use](#how-to-use)

## Introduction
A **finance calculator** is a utility device that performs investment and home loan repayment operations on your financial details inculding deposit, number of years that money is being invested and interest rate. 

* Investment calculator- to calculate the amount of interest you'll earn on your investment.
* Home loan repayment (bond) - to calculate the amount you'll have to pay on a home loan.

## Installation
* Install the Python 3.10.7.
* Install the visual studio, but any python editor can do the job. 
* Install the math library.
```python 
pip install math
```

## How to Use
* This program can run on both Windows and linuzx operating system by using any python editors.
* This program is developed by Python 3.10.7. 
* For investment calculator: provide the details
    * Deposit Money (P)
    * Interest rate (r)
    * Number of years palnning to invest (t)
    * select **simple** or **compound** interest
* For **simple** interest case, the formula $A = P(1+r\times t)$ used to calculate the amount of interest you'll earn on your on your investment. 
```python 
A=round(P*(1+r*t),1)
```
Example of calculating investment return with simple interest.
![Example of calculating investment return with simple interest.](Investment_Simple.png)
* For **compound** interest case, the formula $A = P(1+r)^t$ used to calculate the amount of interest you'll earn on your on your investment.
```python 
A=round(P*math.pow((1+r),t),1)
```
Example of calculating investment return with compound interest.
![Example of calculating investment return with compound interest.](Investment_Compound.png)
* For Home loan repayment: proviode the details
    * House value (P)
    * Interest rate (i)
    * Number of months remaining to repay (n). 
* The formula $\frac{i\times P}{1-(1+i)^(-n)}$ will calculate the amount you'll have to pay on a home loan.
```python
repayment=(i*P)/(1-(1+i)**(-n))
```
Example of calculating remaing payment of the home loan.
![Example of calculating home loan.](Bond.png)

## Acknowledge
I would like to thank HyperionDev team who are so supportive and method of teaching. 

