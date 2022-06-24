<h1 align="center">Spending Rounding Script</h1>

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue)
![Coverage 100%](https://img.shields.io/badge/Coverage-100%25-brightgreen)

## Description

This script calculates the total amount of money needs to be
transferred to piggy bank according to user spending.


## Rounding explained

Script uses so-called smart rounding scale. It means, 
the higher money amount is spent, the more rounding amount 
will be.

Example:<br>
You have defined following rounding boundaries:
 - If you spent from 0 to 500 rubbles, 
you round up to closest 100;
 - If you spent from 500 to 2000 rubbles, 
you round up to closest 500;

So for your 114 rubbles spent the rounding result will 
be 86 rubbles.
On the other hand, for your 1690 spending the result will 
be 310 rubbles.  

## Rounding boundaries

The default boundaries is defined like this:
 - from 0 to 50 round to closest 10
 - from 50 to 300 round to closest 50
 - from 300 to 2000 round to closest 100
 - from 2000 to 10000 round to closest 500
 - from 10000 to 1000000 round to closest 1000

If you want to use your own rounding boundaries, 
you can edit the `BOUNDARIES` list in `calculator.py`. You can add as
many rounding steps as you want. The start value will be inclusive,
the end value will be not inclusive.

Example: from 100 to 1000 round to closest 200:
```python
BOUNDARIES = [
    # Some boundaries
    RoundingBoundary(start=100, end=1000, ceiling=200),
    # Some boundaries
]
```

## Setup

There is no required packages needed to be installed, however the 
`requirements.txt` is in the project. It's because `isort` and 
`coverage` packages were used during development.

 - Clone the project:
```shell
$ git clone https://github.com/BreachAndHole/spending-roundings.git
$ cd spending-roundings/
```

 - Run the script:
```shell
$ python3 spending.py
```
