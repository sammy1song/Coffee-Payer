# Coffee Payer Application

The Coffee Payer Application is a simple Tkinter-based GUI program designed to fairly decide who among a group of coworkers pays for coffee. It takes into account each person's coffee preferences and prices, ensuring an equitable rotation based on cumulative costs.

## Features

- Displays who should pay for coffee next, based on past payments and coffee prices.
- Allows updating coffee prices and preferences through a simple GUI.
- Provides a reset feature to start the tracking anew.
- Shows the total cost for the current coffee run.

## Assumptions

- Each participant always orders the same coffee.
- The program is reset manually before starting a new testing or tracking period.
- Coffee prices are manually updated through the GUI as needed.

## Requirements

- Python 3.x

## Installation

No installation is necessary beyond ensuring you have a compatible version of Python installed. Download the \`coffee_payer.py\` script to your preferred directory.

## Running the Application

1. Open a terminal or command prompt.
2. Navigate to the directory containing \`coffee_payer.py\`.
3. Run the script with Python:

```bash
python coffee_payer.py
```

The GUI should launch, displaying the application window.

## Usage

- **Decide Who Pays**: Click this button to calculate and display who should pay for coffee next.
- **Update Coffee Prices**: Opens a new window where you can adjust the prices for each coffee type.
- **Reset State**: Resets all payment tracking and totals. Use this feature with caution as it will erase all current data.

### Adding or Removing Participants

To add or remove participants or change their coffee preferences, you'll need to modify the \`coffee_prices\` dictionary within the \`coffee_payer.py\` script directly. Here's the format:

```python
coffee_prices = {
    'Name': price,  # Example: 'Bob': 6.50
    # Add or remove entries as needed
}
```

After making your changes, save the file and restart the application.

## Data Entry

The application automatically tracks payments and calculates totals based on the defined coffee prices. Initial data or changes to the participant list and coffee preferences require manual entry in the script as described above.
