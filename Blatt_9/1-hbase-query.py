#!/bin/user/python3

import happybase

def connect_to_hbase(host, table_name):
    """Connects to HBase
    :param host:
    :param table_name:
    :return:
    """
    connection = happybase.Connection(host=host)
    connection.open()

    table = connection.table(table_name)

    return connection, table


def check_for_word(word, table):
    """Check table content for specific word and returns article ids, if word is in the article
    :param word: specific word
    :param table: table of HBase
    :return: article ids
    """
    article_id = []
    for key, data in table.scan(columns="data:text"):
        if word.lower() in data.lower():
            article_id.append(key)
    return article_id


if __name__ == "__main__":
    table_name = "machnitzki_burgemeister"
    conn, table = connect_to_hbase("abu2", table_name)
    articles_affected = check_for_word("test", table)