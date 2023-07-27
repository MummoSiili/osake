import yfinance as yf
import matplotlib.pyplot as plt
import json


ticker = "BTC-USD"
start = "2023-01-18"
end = "2023-01-19"
interval = "1h"
data = yf.download(ticker, start=start, end=end, interval=interval)

# 4h data
print(data['Open'][0])
print(data['Close'][3])


'''
plt.plot(data['Close'])
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Closing Price of Stock')
plt.show()
'''
'''
def get_latest_closing_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1h")
        return data["Close"][0]
    except Exception as e:
        print("Failed to get required data.", e)


ticker = "BTC-USD"  # Facebook
print(f"Latest closing price for {ticker} is: ${get_latest_closing_price(ticker):.2f}")
'''
