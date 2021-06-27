## 6.10 Range
```{python}
for v in range(10):
    print(v)
```


```{python}
for v in range(5, 8):
    print(v)
```

```{python}
for t in range(3, 33, 3):
    print(t, end=" ")
```
o *end=" "* é um parâmetro opcional do print que impede que se pule a linha depois de cada impressão.
## 6.11 Enumerate
```{python}
L = [5, 9 ,13]
x = 0
for e in L:
    print(f"[{x}] {e}")
    x += 1
```
o mesmo mas usando *enumerate*
```{python}
L = [5, 9, 13]
for x, e in enumerate(L):
    print(f"[{x}] {e}")
```
teste comparativo
```{python}
L = [5, 9, 13]
for z in enumerate(L):
    x, e = z
    print(f"[{x}] {e}")
    print(z)
```
