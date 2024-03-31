import argparse
import sys
import time
import requests
from dmacheck import opsgenie_utils

# Etherscan API endpoint for gas oracle
etherscan_api_url = "https://api.etherscan.io/api"

# Ethereum gas threshold
gas_threshold = 20 * 10**9  # 20 Gwei in Wei


# Function to check Ethereum gas price using Etherscan API
def check_gas_price(etherscan_api_key):
    params = {
        "module": "gastracker",
        "action": "gasoracle",
        "apikey": etherscan_api_key,
    }
    response = requests.get(etherscan_api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "1":
            safe_gas_price = int(data["result"]["SafeGasPrice"])
            return safe_gas_price < gas_threshold
    return False


# Function to create Opsgenie alert
def create_opsgenie_alert(opsgenie_api_key, etherscan_api_key):
    if check_gas_price(etherscan_api_key):
        alert_payload = opsgenie_utils.create_alert_payload(
            "EthereumGasCheck", ["monitor_id1", "monitor_id2"]
        )  # Provide monitor IDs
        client = opsgenie_utils.get_alert_client(opsgenie_api_key)
        response = client.create_alert(create_alert_payload=alert_payload)
        print("Opsgenie alert created:", response)


# Main function
def main(opsgenie_api_key, etherscan_api_key):
    while True:
        create_opsgenie_alert(opsgenie_api_key, etherscan_api_key)
        time.sleep(300)  # Check every 5 minutes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check Ethereum gas price and create Opsgenie alert if it's below 20 Gwei."
    )
    parser.add_argument("--opsgenie-api-key", required=True, help="Opsgenie API key")
    parser.add_argument("--etherscan-api-key", required=True, help="Etherscan API key")
    args = parser.parse_args()

    try:
        main(args.opsgenie_api_key, args.etherscan_api_key)
    except Exception as e:
        print("Error:", e, file=sys.stderr)
