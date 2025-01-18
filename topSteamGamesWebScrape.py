from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table

console = Console()

req = Request('https://www.steamcharts.com', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

table = soup.find("table", id="top-games")
rows = table.find_all("tr")
print("Top Games on Steam")

output_table = Table(
    show_header=True,
    header_style="medium_orchid",
    row_styles=["", "medium_purple3"],
    border_style="blue"
)
output_table.add_column("Game", style="purple4", width=20)
output_table.add_column("Peak Players", style="purple4", width=20)
output_table.add_column("Current Players", style="purple4", width=20)

for row in rows:
    game = row.find("td", class_="game-name left")
    player_count_concurrent = row.find("td", class_="num period-col peak-concurrent")
    current_players = row.find("td", class_="num")

    if game and player_count_concurrent and current_players:
        game_link = game.find('a').get_text(strip=True)
        concurrent_count = player_count_concurrent.get_text(strip=True)
        active_players = current_players.get_text(strip=True)

        # Add a row to the output_table
        output_table.add_row(game_link, concurrent_count, active_players)

        console.print(output_table)
