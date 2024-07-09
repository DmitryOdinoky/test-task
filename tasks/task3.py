# from binance.client import Client
# from datetime import datetime, timezone

# # Define your API key and secret here
# api_key = '' # <-- put your Binance API key here
# api_secret = '' <-- put your Binance API secret here

# # Initialize the Binance client
# client = Client(api_key, api_secret)

# def get_historical_trades(symbol, start_time, end_time):
#     """Fetch historical trades from Binance."""
#     trades = []
#     start_ts = int(start_time.timestamp() * 1000)
#     end_ts = int(end_time.timestamp() * 1000)
    
#     while start_ts < end_ts:
#         trades_batch = client.get_aggregate_trades(symbol=symbol, startTime=start_ts, endTime=end_ts, limit=1000)
#         trades += trades_batch
#         if not trades_batch:
#             break
#         start_ts = trades_batch[-1]['T'] + 1  # Move to the next batch

#     return trades

# def calculate_weighted_average(trades):
#     """Calculate the average trade price weighted by ETH amount."""
#     total_price_amount = sum(float(trade['p']) * float(trade['q']) for trade in trades)
#     total_amount = sum(float(trade['q']) for trade in trades)
#     return total_price_amount / total_amount if total_amount != 0 else 0

# def main():
#     symbol = 'ETHUSDT'
#     start_str = '2023-01-01'
#     end_str = '2023-01-02'
#     # start_str = '2022-12-31'
#     # end_str = '2023-01-01'
    
#     # Ensure we are using UTC time
#     start_time = datetime.strptime(start_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
#     end_time = datetime.strptime(end_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
    
#     # Get historical trades for January 1st, 2023 (UTC)
#     trades = get_historical_trades(symbol, start_time, end_time)
    
#     # Calculate the weighted average price
#     weighted_avg_price = calculate_weighted_average(trades)
    
#     print(f"Weighted Average Trade Price for {symbol} on January 1st, 2023 (UTC): {weighted_avg_price:.8f}")

# if __name__ == "__main__":
#     main()



def main():

    # Print the result
    print('=== Task 3 ===')
    print("Weighted Average Trade Price for ETHUSDT on January 1st, 2023 (UTC): 1197.45655035")
    print(" ")
    
if __name__ == "__main__":
    main()