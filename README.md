# Ethereum Gas Alert Module

This module continuously checks the Ethereum gas price and sends alerts to Opsgenie when the gas price is below 20 Gwei.

## Installation

To use this module, you need to install the required dependencies listed in `requirements.txt`. You can install them using pip:

```bash
pip install -r requirements.txt
```

## Usage

Obtain your Opsgenie API key and Etherscan API key.
Run the module with the necessary arguments:

```bash
python app.py --opsgenie-api-key YOUR_OPSGENIE_API_KEY --etherscan-api-key YOUR_ETHERSCAN_API_KEY
```

Replace YOUR_OPSGENIE_API_KEY with your Opsgenie API key and YOUR_ETHERSCAN_API_KEY with your Etherscan API key.

The module will continuously monitor Ethereum gas prices and send alerts to Opsgenie when the gas price falls below 20 Gwei.

```bash
Ctrl+c for quit the app
```