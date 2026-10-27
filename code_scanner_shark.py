import csv
import re
import subprocess

from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

STATUS = {
    "1xx": "bold cyan",
    "2xx": "bold green",
    "3xx": "bold magenta",
    "4xx": "bold orange3",
    "5xx": "bold red",
}


def table_generation(
    stats: dict[int, int],
    last_status: str,
    name: dict[int, str],
    category: dict[int, str],
) -> Panel:

    table = Table(title="Real-Time Telemetry", border_style="cyan")
    table.add_column("HTTP Code", justify="center", style="bold")
    table.add_column("Definition", style="dim")
    table.add_column("Count", justify="right")

    legend_text = Text()
    seen_categories = set()

    for code, count in stats.items():
        new_category = category[code]
        category_prefix = new_category[:3]  # i.e "2xx"
        category_name = new_category[4:]  # i.e "Success"
        style = STATUS[category_prefix]

        if not new_category in seen_categories:
            seen_categories.add(new_category)
            legend_text.append("• ", style=style)
            legend_text.append(f"{category_name}\n", style="white")

        if count > 0:
            table.add_row(str(code), name[code], str(count), style=style)

    legend_panel = Panel(legend_text, title="Categories", border_style="dim")

    grid = Table.grid(padding=2)
    grid.add_row(legend_panel, table)

    panel_content = f"Latest Event: {last_status}"

    return Panel(
        grid, subtitle=panel_content, title="[u]DevOps Monitor[/u]", expand=False
    )


if __name__ == "__main__":
    print("Starting HTTP code scanner...")
    last_status = "Initializing..."

    stats: dict[int, int] = {}
    categories: dict[int, str] = {}
    name: dict[int, str] = {}

    with open("http_codes.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            code = int(row["Code"])
            stats[code] = 0
            categories[code] = row["Category"]
            name[code] = row["Name"]

    process = subprocess.Popen(
        [
            "docker", "exec", "-i", "mock-traffic", "stdbuf", "-oL",
            "tshark", "-i", "any", "-f", "tcp port 8080", "-Y", "http", "-T", "fields", "-e", "http.response.code"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
<<<<<<< HEAD
        text=False
=======
        text=True
>>>>>>> 9e0615d (initial commit)
    )
    pattern = r"\b([1-5]\d\d)"  # i.e "HTTP Code: 429" -> 429

    with Live(
        table_generation(stats, last_status, name, categories), refresh_per_second=2
    ) as live:
        try:
            if process.stdout:
                for line in process.stdout:
                    clean_line = line.strip()
                    if clean_line:
                        match = re.search(pattern, clean_line)
                        if match:
                            code = int(match.group(1))
                            if code in stats:
                                stats[code] += 1

                            # Checks the first digit of the HTTP error code to correspond with its category
                            status = STATUS[f"{str(code)[:1]}xx"]
                            last_status = (
                                f"[{status}]{code} - {categories[code][4:]}[/{status}]"
                            )
                            live.update(
                                table_generation(stats, last_status, name, categories)
                            )

        except KeyboardInterrupt:
            process.terminate()
            process.wait()
            print("\n Telemetry Stopped!")
