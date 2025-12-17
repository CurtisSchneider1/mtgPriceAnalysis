# Card and Pricing Analysis - Magic: The Gathering 

<img src='images/magic.png'>

## Project Overview  
This project explores Magic: The Gathering (MTG) card and pricing data from secondary sales providers like CardKingdom, Cardsphere, Mana Pool, and TCGPlayer. 

The project goals are to: 
* Provide insights on how consumers value cards through pandas, visualizations, and SQL queries.
* Establish a custom market price per card using the different price providers.  
* Give additional tools to consumers not readily available elsewhere.  

>Source data last updated: December 9, 2025

## Project Background
Hasbro, parent company of Wizards of the Coast, does not sell single cards but instead sells sealed decks, boosters packs, and similar product. Hasbro also does not publicly report granular sales numbers per released set. Since there is then no official source for sets or individual card value, we must look at the secondary market.

## MTG Overview
* MTG is the first modern, global trading card game (TCG) created, only recently rivaled by Pokémon TCG.  
* There are ~30k unique MTG cards and over 1 million individual cards when considering reprints, alt arts, languages, promos, and foils.  
* There is an estimated 50 billion MTG cards printed since the games launch in 1993.  
* Hasbro announced its highest set sales with Final Fantasy in 2025.

## How to Setup This Project  
### Prerequisites  
* Python 3.10+
* [Git](https://git-scm.com/install/windows)
* [Visual Studio Code](https://code.visualstudio.com/download) (VS Code)  
> This project was developed in VS Code on Windows.  
> Jupyter Notebook or JupyterLab may work for most notebooks but are not supported for CLI autocomplete functionality (specifically for functionCardSearchAdvanced.py*).  

### Setup Instructions

1. Open a terminal (Git Bash, PowerShell, VS Code Terminal, etc.) and navigate to the directory where you want to clone the project. 

2. Create and activate a virtual environment:  

    **Windows**  
    `python -m venv venv`  
    `source venv/Scripts/activate`  
 
    **Linux/macOS**  
    `python3 -m venv venv`  
    `source venv/bin/activate`

3. Clone the repository:  
`git clone https://github.com/CurtisSchneider1/ccgPriceAnalysis`  
`cd ccgPriceAnalysis`

4. Install required dependencies:  
    `pip install -r requirements.txt`

## Running the Project
5. Open the project folder in VS Code.

6. Run the following notebooks **in order** using "Run All":  
    - wranglingMagic.ipynb
    - wranglingPokemon.ipynb
    - queries.ipynb
    - visualizations.ipynb

7. Then run these notebooks or scripts to use specific functions:
    - functionBestValue.ipynb
    - functionCardSearch.ipynb
    - *functionCardSearchAdvanced.py

## Features
This project makes it easy to:
* See which cards, sets, types, rarities, and release years hold the most consumer value.
* Determine how to get the best value when purchasing singles across multiple eCommerce websites.
* Visualize secondary MTG market value compared to Pokémon.
* Run sqlite3 queries to uncover additional insights as desired in the custom database provided.

## To Note
* "Market Price" is determined by sold value and not by listed/offer value.
* Card conditions or grades are not considered specifically, just overall market price. 
* The average market price column is project-added for each card which takes the mean of all prices available per price provider from source data.
    - Foils and non-foils, even if sharing a UUID, are considered and averaged separately.
* A small percentage of cards (less than 1% usually) may have no value or NaN in price-related columns due to the price provider(s) having no market price for those cards.
    - Each provider has their own metrics for not providing a current market price, possibly due to: 
        * a lack of sales.
        * exceptionally rare cards.
        * banned cards.
        * announced cards that are not yet on sale.

## Data Sources
Magic: The Gathering  
* cardsMagic CSV file
    - card details data
    - provided by [MTGJSON](https://mtgjson.com)
* pricesMagic CSV file
    - market data
    - provided by [MTGJSON](https://mtgjson.com)
* setsMagic CSV file
    - set names, set codes, and release dates
    - sourced from [MTG Decks](https://mtgdecks.net/prices)

Pokémon  
* cardsPokemon XLSX file
    - card details and market data from TCGPlayer's API
    - provided by [TCGCSV](https://tcgcsv.com/)
* groupsPokemon CSV file
    - set names, set codes, and release dates
    - provided by [TCGCSV](https://tcgcsv.com/)

## Acknowledgements
* ChatGPT was used for troubleshooting and debugging.

## Author
Curtis Schneider