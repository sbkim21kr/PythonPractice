# 📋 MY_SQL_1_2_GRID_입출력테이블 Procedure  

This procedure updates and refreshes the **MYSQL_입출력테이블** grid in the SCADA system with data retrieved from the database.<br>  

---

## 📑 Code  

```vbnet
Sub MY_SQL_1_2_GRID_입출력테이블()

    RunScript "MY_SQL_1_1_GRID_dataSet" 
    rc = GetTagVal("MY_SQL.RS_COUNT") 

    Sleep(300)

    wcGridCommand "MYSQL_입출력테이블", 7, 0, 0

    '✅ "MYSQL_입출력테이블"
    'The name of the grid control you're targeting.
    'This is likely a visual table on the SCADA screen showing input/output data from the database.

    '✅ 7
    'This is the command code.
    'In many SCADA environments (like Cimon SCADA), wcGridCommand uses numeric codes to trigger specific actions.
    'Command 7 typically means: 🔄 Refresh or reload the grid data from its data source.

    '✅ 0, 0
    'These are additional parameters that vary depending on the command.
    'For command 7, they’re often unused or default values.
    'They might represent row/column indices, flags, or placeholders depending on the grid’s configuration.

    For i = 1 To rc

        주문자명_변수 = GetTagVal("MY_SQL.SCADA_주문자명" + Format(i-1, "_000")) 
        wcGridSetData "MYSQL_입출력테이블", 1, i, 주문자명_변수

```
### wcGridSetData(GridName, Column, Row, Value)
```

        '🔍 What wcGridSetData Does
        'It allows you to:
        'Insert or update a specific cell in a grid
        'Define the row, column, and value to be placed
        'Dynamically populate grid content from scripts, database queries, or tag values

        수량_변수 = GetTagVal("MY_SQL.SCADA_수량" + Format(i-1, "_000")) 
        wcGridSetData "MYSQL_입출력테이블", 2, i, 수량_변수

    Next i

End Sub

🗒️ Key Notes
• RunScript "MY_SQL_1_1_GRID_dataSet"

Runs another script to initialize and retrieve the dataset before updating the grid.<br>

• wcGridCommand "MYSQL_입출력테이블", 7, 0, 0

MYSQL_입출력테이블: Name of the SCADA grid control.<br>

7: Command code (commonly means refresh or reload).<br>

0, 0: Additional parameters, unused or default for this command.<br>

• wcGridSetData

Populates the grid by setting values in specific rows and columns dynamically using tag values retrieved from the database.<br>

• Sleep(300)

Adds a short delay (300 ms) to ensure the dataset is ready before updating the grid.<br>