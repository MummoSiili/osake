import yfinance as yf
import json

msft = yf.Ticker('MSFT')
#print(json.dumps(msft.info, indent=3))

msft.info
history = msft.history(period='1mo')
print(json.dumps(msft.history_metadata, indent=3))

# show financials:
# - income statement
income = msft.income_stmt
msft.quarterly_income_stmt
# - balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet
# - cash flow statement
msft.cashflow
msft.quarterly_cashflow

print(json.dumps(income, indent=3))
print(json.dumps(msft.quarterly_income_stmt, indent=3))
print(json.dumps(msft.balance_sheet, indent=3))
print(json.dumps(msft.quarterly_balance_sheet, indent=3))
print(json.dumps(msft.cashflow, indent=3))
print(json.dumps(msft.quarterly_cashflow, indent=3))