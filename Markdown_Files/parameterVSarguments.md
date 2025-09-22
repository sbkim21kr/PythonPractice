### 1. Parameter

A parameter is a variable in the function/method definition.

Think of it as a placeholder that will receive a value when the function is called.

Example in VBA:
```
Sub PrintName(name As String)
    MsgBox "Hello, " & name
End Sub
```

### 2. Argument

An argument is the actual value you pass to the function when calling it.

Example:
```
PrintName "Alice"

```