import pandas as pd
import sqlite3


if __name__ == "__main__":
    df = pd.read_excel('./database/denis_db.xlsx')

    conn = sqlite3.connect('database/dataset.db')
    df.to_sql('dataset', conn, if_exists='replace', index=False)
    conn.close()


