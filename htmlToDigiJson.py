from bs4 import BeautifulSoup
import json

# Provided HTML snippet
html_content = """
<tbody>
    <tr>
        <td><strong>Name</strong></td>
        <td><strong>HP</strong></td>
        <td><strong>MP</strong></td>
        <td><strong>Strength</strong></td>
        <td><strong>Stamina</strong></td>
        <td><strong>Wisdom</strong></td>
        <td><strong>Speed</strong></td>
        <td><strong>Weight</strong></td>
        <td><strong>Mistakes</strong></td>
        <td><strong>Bond</strong></td>
        <td><strong>Discipline</strong></td>
        <td><strong>Wins</strong></td>
        <td><strong>Key Digimon</strong></td>
        <td><strong>Key Points</strong></td>
    </tr>
    <tr>
        <td><a href="?page=1#Birdramon">Birdramon</a></td>
        <td>-</td>
        <td>4800</td>
        <td>400</td>
        <td>-</td>
        <td>-</td>
        <td>500</td>
        <td>≤14</td>
        <td>≤5</td>
        <td>50</td>
        <td>50</td>
        <td>-</td>
        <td>Biyomon</td>
        <td>5</td>
    </tr>
    <tr>
        <td><a href="?page=1#Piddomon">Piddomon</a></td>
        <td>-</td>
        <td>2400</td>
        <td>-</td>
        <td>-</td>
        <td>300</td>
        <td>300</td>
        <td>≤19</td>
        <td>≤3</td>
        <td>-</td>
        <td>50</td>
        <td>-</td>
        <td>-</td>
        <td>4</td>
    </tr>
    <tr>
        <td><a href="?page=2#RedVeedramon">RedVeedramon</a></td>
        <td>4800</td>
        <td>-</td>
        <td>550</td>
        <td>350</td>
        <td>-</td>
        <td>-</td>
        <td>20</td>
        <td>≤1</td>
        <td>50</td>
        <td>-</td>
        <td>20</td>
        <td>-</td>
        <td>5</td>
    </tr>
    <tr>
        <td><a href="?page=2#Youkomon">Youkomon</a></td>
        <td>-</td>
        <td>2400</td>
        <td>-</td>
        <td>-</td>
        <td>400</td>
        <td>200</td>
        <td>≤19</td>
        <td>≤5</td>
        <td>-</td>
        <td>50</td>
        <td>-</td>
        <td>-</td>
        <td>4</td>
    </tr>
</tbody>
"""

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")
rows = soup.find_all("tr")

# Extract headers
headers = [header.text.strip() for header in rows[0].find_all("strong")]

# Extract rows and convert to JSON structure
data = []
for row in rows[1:]:  # Skip header row
    cells = row.find_all("td")
    entry = {}
    for i, cell in enumerate(cells):
        header = headers[i]
        text = cell.text.strip()
        
        # Dynamically replace "≤" with "<=" in each cell's text
        text = text.replace("≤", "<=")
        
        if text == "-":
            value = None
        elif header in ["HP", "MP", "Strength", "Stamina", "Wisdom", "Speed", "Bond", "Discipline", "Wins", "Key Points"]:
            value = int(text) if text.isdigit() else text
        else:
            value = text
        entry[header] = value
    data.append(entry)

# Convert to the required JSON format
json_data = []
for item in data:
    json_entry = {
        "Name": item.get("Name"),
        "HP": item.get("HP"),
        "MP": item.get("MP"),
        "Strength": item.get("Strength"),
        "Stamina": item.get("Stamina"),
        "Wisdom": item.get("Wisdom"),
        "Speed": item.get("Speed"),
        "Weight": item.get("Weight"),
        "Mistakes": item.get("Mistakes"),
        "Bond": item.get("Bond"),
        "Discipline": item.get("Discipline"),
        "Wins": item.get("Wins"),
        "Key Digimon": item.get("Key Digimon"),
        "Key Points": item.get("Key Points"),
    }
    json_data.append(json_entry)

# Print JSON output
print(json.dumps(json_data, indent=4))
