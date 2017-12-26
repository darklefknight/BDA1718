#!/bin/user/python3

import happybase
import csv


def connect_to_hbase(host):
    connection = happybase.Connection(host=host)
    connection.open()
    return connection


def connect_to_table(connection, table_name):
    """Connect to table in HBase and creates batch
    :param connection: connection in HBase
    :param table_name: string
    :return: table_batch for writing
    """
    table = connection.table(table_name)
    batch = table.batch(batch_size=1000) # if batch_size is reached -> batch.send()
    return batch


def insert_row(batch, row):
    """ Insert a row into HBase.
    Write the row to the batch. When the batch size is reached, rows will be
    sent to the database.
    """

    batch.put(row[0], {"data:url": row[1],
                       "data:title": row[2],
                       "data:text": row[3],
                       "data:categories": row[4]})


if __name__ == "__main__":
    file_path = "/home/bigdata/9/enwiki-clean-10MiB.csv"
    table_name = "machnitzki_burgemeister"

    conn = connect_to_hbase("abu2")

    conn.create_table(table_name)

    batch = connect_to_table(conn, table_name)

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            insert_row(batch, row)

    batch.send()

    conn.close()
