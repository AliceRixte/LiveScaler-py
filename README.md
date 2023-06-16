# livescaler-py
A python library implementing the affine transformations of LiveScaler

## How to install

```
python setup.py install
``` 

## How to use 

```python

from livescaler import Affine, StdAffine

transfo1 = Affine(4,5)
transfo1.eval(np.array([1,2,3,4])) # the array is a vector of notes to be transformed
transfo2 = Affine(5,6)
composition = transfo1 >> transfo2
composition.eval(6) # computes  transfo2(transfo1(6))
composition2 = StdAffine.I >> transfo1 >> StdAffine.vi
```

## How to test

```
pytest
```
