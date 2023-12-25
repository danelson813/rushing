import duckdb


def get_headers(soup):
    headers = soup.select_one('thead').select('th')
    header_ = [th.text.strip() for th in headers]
    return header_

def clean_df(df, headers):
    for header in headers[1:]:
        print(header)
        if header !=  'Rush 1st%':
            df[header] = df[header].astype(int)
        else:
            df[header] = df[header].astype(float)

    return df

def send_to_csv(df):
    df.to_csv('data/results.csv', index=False)
    return None


def send_to_duckdb(df):
    with duckdb.connect('data/football.db') as conn:
        conn.sql("CREATE OR REPLACE TABLE rushing AS SELECT * FROM df")
        # conn.sql('INSERT INTO rushing SELECT * FROM df')
        conn.table('rushing').show()
        data_= conn.sql("SELECT * FROM rushing").fetchall()
        return data_