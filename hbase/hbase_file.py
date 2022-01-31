import csv
import happybase
import time

batch_size = 1000
host = "0.0.0.0"
file_path = "Request_for_Information_Cases.csv"
namespace = "sample_data"
row_count = 0
start_time = time.time()
table_name = "rfic"
def connect_to_hbase():
    """ Connect to HBase server.
    This will use the host, namespace, table name, and batch size as defined in
    the global variables above.
    """
    conn = happybase.Connection(host = host,
        table_prefix = namespace,
        table_prefix_separator = ":")
    conn.open()
    table = conn.table(table_name)
    batch = table.batch(batch_size = batch_size)
    return conn, batch
def insert_row(batch,row):
    """ Insert a row into HBase.
    Write the row to the batch. When the batch size is reached, rows will be
    sent to the database.
    Rows have the following schema:
     
["Country","Alpha-2 code","Alpha-3 code","Numeric code","Latitude (average)","Longitude (average)"]
    """
    print(row)
    batch.put({"data:countri":row[0], "data:Alpha-2 code": row[1], "data:Alpha-3 code": row[2], "data:Numeric code": row[3],
        "data:Latitude": row[4], "data:Longitude": row[5] })

def read_csv():
    csvfile = open("code.csv", "r")
    csvreader = csv.reader(csvfile)
    return csvreader, csvfile

conn, batch = connect_to_hbase()
print ("Connect to HBase. table name: %s, batch size: %i" % (table_name, batch_size))
csvreader, csvfile = read_csv()
print ("Connected to file. name: %s" % (file_path))

try:
    # Loop through the rows. The first row contains column headers, so skip that
    # row. Insert all remaining rows into the database.
    for row in csvreader:
        row_count += 1
        if row_count == 1:
            pass
        else:
            insert_row(batch, row)

    # If there are any leftover rows in the batch, send them now.
    batch.send()
finally:
    # No matter what happens, close the file handle.
    csvfile.close()
    conn.close()

duration = time.time() - start_time
print("Done. row count: %i, duration: %.3f s" % (row_count, duration))



