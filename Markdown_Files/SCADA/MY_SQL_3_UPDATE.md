# 📋 MY_SQL_3_UPDATE Procedure  

This procedure updates existing records in the **`cimon.order`** table in the MySQL database using values retrieved from SCADA tags.<br>

---

## 📑 Code  

```vbnet
Sub MY_SQL_3_UPDATE()

    Dim strConn As String
    Dim a As String

    '-------------------------------------------------------------
    ' 1. Database connection string
    '-------------------------------------------------------------
    strConn = "Driver=MySQL ODBC 5.3 ANSI Driver; Server=127.0.0.1;" & _
              "Database=cimon; User ID=cimonedu; Password=cimonedu1234;"

    '-------------------------------------------------------------
    ' 2. Create ADO connection and recordset objects
    '-------------------------------------------------------------
    Set conn = CreateObject("ADODB.Connection")
    Set rs = CreateObject("ADODB.Recordset")

    ' Open the database connection
    conn.Open strConn
    ' A schema is essentially a database
    ' Collation defines how text is sorted and compared

    '-------------------------------------------------------------
    ' 3. Construct and execute SQL UPDATE query
    '-------------------------------------------------------------
    a = "UPDATE cimon.order SET count = " & GetTagVal("MY_SQL.SCADA_수량") & _
        " WHERE name = '" & GetTagVal("MY_SQL.SCADA_주문자명") & "'"
    ' cimon.order: table 'order' inside schema 'cimon'

    Set rs1 = conn.Execute(a)
    ' Executes the SQL query and stores the result in rs1
    ' rs1 contains any returned rows (if applicable)

    ' In the context of databases and SCADA systems:
    ' A query is a request for information or action (INSERT, SELECT, UPDATE, DELETE)

    '-------------------------------------------------------------
    ' 4. Close connection and clean up
    '-------------------------------------------------------------
    conn.Close
    Set rs = Nothing
    Set conn = Nothing

End Sub

🗒️ Key Notes
• Connection String

Uses MySQL ODBC 5.3 ANSI Driver to connect to the local MySQL database cimon with credentials.<br>

• ADO Objects

ADODB.Connection: Manages the database connection.<br>

ADODB.Recordset: Can hold results from queries.<br>

• SQL Query

UPDATE cimon.order SET count = ... WHERE name = ... updates the count field for the record matching the given name.<br>

SCADA tag values (SCADA_주문자명 and SCADA_수량) are used dynamically.<br>

• Clean-Up

Always close the connection and release objects to free resources.<br>