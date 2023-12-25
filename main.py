from utils.selenium_template import get_soup
from utils.util import get_headers, clean_df, send_to_csv, send_to_duckdb
import pandas as pd


url = "https://www.nfl.com/stats/player-stats/category/rushing/2023/reg/all/rushingyards/desc"
soup = get_soup(url)

headers = get_headers(soup)

players = soup.find('tbody').find_all('tr')
print(f"there are {len(players)} in the list.")

results = []
for player in players:
    row = [td.text.strip() for td in player.find_all('td')]
    result = {
        headers[0]: row[0],
        headers[1]: row[1],
        headers[2]: row[2],
        headers[3]: row[3],
        headers[4]: row[4],
        headers[5]: row[5],
        headers[6]: row[6],
        headers[7]: row[7],
        headers[8]: row[8],
        headers[9]: row[9],
    }
    results.append(result)


df = pd.DataFrame(results)
df = clean_df(df, headers)
send_to_csv(df)
df2 = send_to_duckdb(df)
print(df2)