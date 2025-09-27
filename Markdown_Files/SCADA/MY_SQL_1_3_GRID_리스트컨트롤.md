# 📋 MY_SQL_1_3_GRID_리스트컨트롤 Procedure  

This procedure refreshes and populates the **MYSQL_리스트컨트롤** on the SCADA screen with data retrieved from the database.<br>

---

## 📑 Code  

```vbnet
Sub MY_SQL_1_3_GRID_리스트컨트롤()

    RunScript "MY_SQL_1_1_GRID_dataSet" 
    rc = GetTagVal("MY_SQL.RS_COUNT") 

    Sleep(300)

    wcGridCommand "MYSQL_리스트컨트롤", 100, 0, 0

    For i = 0 To rc-1

        주문자명_변수 = GetTagVal("MY_SQL.SCADA_주문자명" + Format(i, "_000")) 
        wcGridSetData "MYSQL_리스트컨트롤", 0, i, 주문자명_변수

        수량_변수 = GetTagVal("MY_SQL.SCADA_수량" + Format(i, "_000")) 
        wcGridSetData "MYSQL_리스트컨트롤", 1, i, 수량_변수

        '✅ "MYSQL_리스트컨트롤"
        'This is the name of the grid or list control on your SCADA screen.
        'It’s likely used to display a list of items—such as orders, alarms, or device statuses.

        '✅ 100
        'This is the command code.
        'In many SCADA environments (like CIMON SCADA), command 100 typically means: 🧹 Clear all data from the grid or list control.

        '✅ 0, 0
        'These are additional parameters, often unused for command 100.
        'They may act as placeholders or default values.

    Next i

End Sub

🗒️ Key Notes
• RunScript "MY_SQL_1_1_GRID_dataSet"

Runs the dataset script to ensure the SCADA tags are populated before updating the list control.<br>

• wcGridCommand "MYSQL_리스트컨트롤", 100, 0, 0

MYSQL_리스트컨트롤: Name of the SCADA list control.<br>

100: Command code (commonly clears or resets the grid/list).<br>

0, 0: Unused/default parameters for this command.<br>

• wcGridSetData

Populates rows and columns of the list control with tag values dynamically fetched from the database.<br>

• Sleep(300)

Pauses execution briefly (300 ms) to allow previous commands or data retrieval to complete before updating the grid.<br>