# pyqif
A tool for Quantitative information flow applications.
At this point the tool calculates a hyper distribution from a channel marix and a prior distribution.
## How to run:
After installation do:

```
pyqif
```
Takes ordered inputs from stdin:
1. Channel label, ex: `C`
2. Prior lenght & channel's output size, ex: `3 4`
3. Pior distribution, ex: `1/3 0.3333333 1/3`
4. Channel matrix, line by line:
```
1/4 1/4 1/4 1/4
0.25 0.25 0.25 0.25
1/4 1/4 1/4 1/4
```

## Flags

### Help
Prints command's help.
```
pyqif --help
```

### Verbose
Activates verbose execution mode.
```
pyqif --verbose
```

### Latex
Switches output type to latex. The latex code format is appropriate for markdown documents that use `$$` as math block dellimiters.
```
pyqif --latex
```

## Examples

### File input
Executing tool redirecting input from *file*.

Creating example *file*:
```
C
3 4
1/4 1/2 1/4
1/2 1/2 0 0
0 1/4 1/2 1/4
1/2 1/3 1/6 0
``` 


```
pyqif  < file
```

### Latex ooutput

Executing tool with redirected input and output. In this scenario the *test.md* file will cointains the formatted results.
```
pyqif -l < file > test.md
```
