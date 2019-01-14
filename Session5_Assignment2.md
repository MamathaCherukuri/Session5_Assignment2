
1.Write a function to compute 5/0 and use try/except to catch the exceptions. 


```python
def div(a, b):
    try:
        a/b
    except ZeroDivisionError:
        print("Zero Division Error detected")
    else:
        print("No Zero Division Error")
    finally:
        print("Finally the division of %d/%d is done" % (a, b))
```


```python
div(1,1)
```

    No Zero Division Error
    Finally the division of 1/1 is done
    


```python
div(1,0)
```

    Zero Division Error detected
    Finally the division of 1/0 is done
    


```python
div(5,0)
```

    Zero Division Error detected
    Finally the division of 5/0 is done
    

2.Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"]. 
Hint: Subject,Verb and Object should be declared in the program as shown below. 
subjects=["Americans ","Indians"] verbs=["play","watch"] objects=["Baseball","Cricket"] 



```python
subject=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

# Using nested looping to produce the expected result/output
for i in subject:
    for j in verbs:
        for k in objects:
            print(i+" "+j+" "+k+".")
```

    Americans play Baseball.
    Americans play Cricket.
    Americans watch Baseball.
    Americans watch Cricket.
    Indians play Baseball.
    Indians play Cricket.
    Indians watch Baseball.
    Indians watch Cricket.
    


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
