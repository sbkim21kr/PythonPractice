# 📋 MY_SQL_2_INSERT Procedure  

This procedure inserts new data into the **`cimon.order`** table in the MySQL database using values retrieved from SCADA tags.<br>

---

## 📑 Code  

```vbnet
Sub MY_SQL_2_INSERT()

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
    ' 3. Construct and execute SQL INSERT query
    '-------------------------------------------------------------
    a = "INSERT INTO cimon.order VALUES ('" & GetTagVal("MY_SQL.SCADA_주문자명") & "'," & GetTagVal("MY_SQL.SCADA_수량") & ")"
    ' cimon.order: table 'order' inside schema 'cimon'

    Set rs1 = conn.Execute(a)
    ' Executes the SQL query and stores the result in rs1
    ' rs1 contains any returned rows (if applicable)

    ' In the context of databases and SCADA systems:
    ' A query is a request for information or action (INSERT, SELECT, UPDATE, DELETE)

    '--------------

🗒️ Key Notes
• Connection String

Uses MySQL ODBC 5.3 ANSI Driver to connect to the local MySQL database cimon with credentials.<br>

• ADO Objects

ADODB.Connection: Manages the database connection.<br>

ADODB.Recordset: Can hold results from queries.<br>

• SQL Query

INSERT INTO cimon.order VALUES (...) adds a new record to the table.<br>

SCADA tag values (SCADA_주문자명 and SCADA_수량) are inserted dynamically.<br>

• Clean-Up

Always close the connection and release objects to free resources.<br>