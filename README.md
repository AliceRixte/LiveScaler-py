# livescaler-py
A python library implementing the affine transformations of LiveScaler

## How to install

```
python setup.py install
``` 

## How to use 

```
transfo1 = Affine(4,5)
transfo1.eval(np.array([1,2,3,4])) # the array is a vector of notes to be transformed
transfo2 = Affine(5,6)
composition = transfo1 >> transfo2
composition.eval(6) # computes  transfo1(transfo1(6))
```
