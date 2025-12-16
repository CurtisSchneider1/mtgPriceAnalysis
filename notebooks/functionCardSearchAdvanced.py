# Advanced search function with TAB autocomplete option for card name input.
# Results and autocomplete options will be shown in terminal.
# This WILL NOT work in Jupyter Notebook or the VS Code Python Interactive Window.
# It WILL work in VS Code Terminal or by running the .py file directly.
# To note, autocomplete works best when using it in the first word of the card name.

from pathlib import Path
import pandas as pd
import readline

# Ensure no output wrapping.
pd.set_option("display.expand_frame_repr", False)

# Display all rows in output.
pd.set_option('display.max_rows', None)

# Use path relative to the script and not active directory.
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / ".." / "data" / "dataMagic" / "cleanMagicIndPrices.csv"
dfm3 = pd.read_csv(DATA_PATH)

def autocomplete(options):
    """
    Enable TAB completion of card names in the terminal.
    """
    def completer(text, state):
        # Filter matches that start with the typed text.
        matches = [s for s in options if s.lower().startswith(text.lower())]
        # Return match for this state or None.
        return matches[state] if state < len(matches) else None

    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

def cardValue():
    """ 
    Search dfm3 for all instances of an individual card.
    Press TAB to autocomplete card name input.

    Args:
        str: User inputted card name.

    Returns:
        values: Card and price information when card name matches input.
    """
    
    cardList = sorted(dfm3["name"].unique())
    autocomplete(cardList)


    # Requires user input and strips unnecessary spaces.
    cardName = input("Please enter MTG card name (press TAB to autocomplete, or type esc to cancel search): ").strip()
    if cardName.lower() == "esc":
        return None
    
    # Requires valid card name.
    cardLowerList = [c.lower() for c in cardList]    
    
    while cardName.lower() not in cardLowerList:
        cardName = input("Please enter a valid card name (try TAB to autocomplete, or type esc to exit): ").strip()
        if cardName.lower() == "esc":
            return None
    
    rows = dfm3[dfm3["name"].str.lower() == cardName.lower()]
    subset = rows[["name", "setName", "priceProvider", "price", "avgMarketPrice", "cardFinish", "uuid"]]

    # Group results by cardFinish per UUID.
    subset = subset.sort_values(
        by=["uuid", "cardFinish", "priceProvider"],
        # Key transforms the column before sorting.
        # Converts text to numbers for custom mapping because 'foil' comes before 'normal' alphabetically.
        # If column name = cardFinish, then apply logic.
        # .fillna fills any potential NaN results by putting the original string value back, just in case.
        key=lambda col: (col.map({"normal": 0, "foil": 1}).fillna(col) if col.name == "cardFinish" else col))
    
    return subset

# Run the function.
# name = main so it doesn't run automatically if imported later.
# If example card names are needed: Venom, Aladdin, Buster Sword
if __name__ == "__main__":
    result = cardValue()
    if result is not None:
        print(result)