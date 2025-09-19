# 📋 MY_SQL_1_1_GRID_dataSet Procedure  

The **`GRID`** in `Sub MY_SQL_1_1_GRID_dataSet()` likely refers to a **data grid** or **grid view**—a common UI element for displaying tabular data in rows and columns, similar to a spreadsheet.<br>

---

## 📑 Code  

```vbnet
Sub MY_SQL_1_1_GRID_dataSet()

    Dim strConn As String
    Dim a As String
    Dim conn As Object
    Dim rs As Object
    Dim rs1 As Object

    '-------------------------------------------------------------
    ' ### 1. Initialize SCADA tags (clear previous grid data)
    '-------------------------------------------------------------
    For i = 0 To 9
        SetTagVal "MY_SQL.SCADA_주문자명" + Format(i, "_000"), ""
        SetTagVal "MY_SQL.SCADA_수량" + Format(i, "_000"), 0
    Next i

    '-------------------------------------------------------------
    ' ### 2. Create database connection (MySQL via ODBC)
    '-------------------------------------------------------------
    strConn = "Driver=MySQL ODBC 5.3 ANSI Driver;" & _
              "Server=127.0.0.1;" & _
              "Database=cimon;" & _
              "User ID=cimonedu;" & _
              "Password=cimonedu1234;"

    Set conn = CreateObject("ADODB.Connection")
    Set rs = CreateObject("ADODB.Recordset")
    conn.Open strConn

    '-------------------------------------------------------------
    ' ### 3. Execute SQL query
    '-------------------------------------------------------------
    a = "SELECT * FROM cimon.order"
    Set rs1 = conn.Execute(a)

    '-------------------------------------------------------------
    ' ### 4. Populate SCADA tags with retrieved data
    '-------------------------------------------------------------
    SetTagVal "MY_SQL.SCADA_주문자명_000", CStr(rs1.Fields(0))
    SetTagVal "MY_SQL.SCADA_수량_000", rs1.Fields(1)

    rc = GetTagVal("MY_SQL.RS_COUNT")

    For i = 1 To rc - 1
        rs1.MoveNext
        SetTagVal "MY_SQL.SCADA_주문자명" + Format(i, "_000"), CStr(rs1.Fields(0))
        SetTagVal "MY_SQL.SCADA_수량" + Format(i, "_000"), rs1.Fields(1)
    Next i

    '-------------------------------------------------------------
    ' ### 5. Close connection and clean up
    '-------------------------------------------------------------
    conn.Close
    Set rs = Nothing
    Set conn = Nothing

End Sub
