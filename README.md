# Magic: The Gathering Price Data Analysis
This project explores current prices for Magic: The Gathering by gathering average card prices per card ID from retail providers like TCGPlayer, CardKingdom, and CardSphere. Hasbro does not publicly report on sales per released set, but we can use current pricing trends to show general interest and current value in sets and by years of release.

## Quick Notes
- MTG is the first modern, global trading card game (TCG) created, only now rivaled by Pokemon TCG.  
- There are ~30k unique MTG cards and over 1M individual cards when considering reprints, alt arts, languages, promos, foils, etc.  
- There is an estimated 50 billion MTG cards printed since the games launch in 1993.  
- Hasbro just announced its highest set sales in 2025 with Final Fantasy.

## How to Use
1. Clone this repository.
2. Install the required Python packages:  
   pip install -r requirements.txt
3. Open `mtgAnalysis.ipynb` in Jupyter Notebook or JupyterLab.

## Example Output
As of August 26, 20205 - cards on average from MTG's release year, 1993, still hold the most value by over 6 times the next popular year, 2022, mostly due to the 30th anniversary set.

## Data Sources
- cards CSV file
    * main data source
    * provided by mtgjson.com

- cardPrices CSV file
    * secondary data pricing source
    * provided by mtgjson.com
- setDetails CSV file
    * showing set names, set codes, and release dates
    * provided by mtgdecks.net/prices

## Author
Curtis Schneider – CodeYou Capstone Project