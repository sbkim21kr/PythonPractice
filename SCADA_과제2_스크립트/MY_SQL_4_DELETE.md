# 📋 MY_SQL_4_DELETE Procedure  

This procedure deletes a record from the **`cimon.order`** table in the MySQL database using a value retrieved from a SCADA tag.<br>

---

## 📑 Code  

```vbnet
Sub MY_SQL_4_DELETE()

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
    ' 3. Construct and execute SQL DELETE query
    '-------------------------------------------------------------
    a = "DELETE FROM cimon.order WHERE name = '" & GetTagVal("MY_SQL.SCADA_주문자명") & "'"
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

End Sub

🗒️ Key Notes
• Connection String

Uses MySQL ODBC 5.3 ANSI Driver to connect to the local MySQL database cimon with credentials.<br>

• ADO Objects

ADODB.Connection: Manages the database connection.<br>

ADODB.Recordset: Can hold results from queries (not strictly needed for DELETE).<br>

• SQL Query

DELETE FROM cimon.order WHERE name = ... removes the record matching the given name.<br>

SCADA tag value (SCADA_주문자명) is used dynamically.<br>

• Clean-Up

Always close the connection to free resources.<br>