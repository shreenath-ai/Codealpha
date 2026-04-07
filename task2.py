import csv
import os
from datetime import datetime

# ============================================
#   STOCK PORTFOLIO TRACKER
#   CodeAlpha Internship Task 2
#   Author: Python Intern
# ============================================

# Hardcoded stock prices dictionary
STOCK_PRICES = {
    "AAPL":  180,   # Apple
    "TSLA":  250,   # Tesla
    "GOOGL": 140,   # Google
    "AMZN":  175,   # Amazon
    "MSFT":  380,   # Microsoft
    "META":  500,   # Meta
    "NFLX":  620,   # Netflix
    "NVDA":  875,   # NVIDIA
}


def show_available_stocks():
    """Display all available stocks with their prices."""
    print("\n📊 Available Stocks:")
    print("-" * 35)
    print(f"  {'Symbol':<10} {'Company':<15} {'Price ($)'}")
    print("-" * 35)
    companies = {
        "AAPL": "Apple", "TSLA": "Tesla", "GOOGL": "Google",
        "AMZN": "Amazon", "MSFT": "Microsoft", "META": "Meta",
        "NFLX": "Netflix", "NVDA": "NVIDIA"
    }
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<10} {companies[symbol]:<15} ${price}")
    print("-" * 35)


def get_portfolio():
    """Get stock inputs from the user."""
    portfolio = {}
    print("\n📝 Enter your stocks (type 'done' when finished):")

    while True:
        symbol = input("\n  Enter stock symbol (e.g. AAPL): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  ⚠️  '{symbol}' not found. Please choose from the available stocks above.")
            continue

        try:
            quantity = int(input(f"  Enter quantity for {symbol}: ").strip())
            if quantity <= 0:
                print("  ⚠️  Quantity must be a positive number.")
                continue
        except ValueError:
            print("  ⚠️  Please enter a valid number.")
            continue

        if symbol in portfolio:
            portfolio[symbol] += quantity
            print(f"  ✅ Updated {symbol}: total {portfolio[symbol]} shares.")
        else:
            portfolio[symbol] = quantity
            print(f"  ✅ Added {symbol} x{quantity}")

    return portfolio


def display_portfolio(portfolio):
    """Display the portfolio summary."""
    if not portfolio:
        print("\n⚠️  No stocks in portfolio.")
        return 0

    print("\n" + "=" * 55)
    print("         📈 YOUR STOCK PORTFOLIO SUMMARY")
    print("=" * 55)
    print(f"  {'Symbol':<10} {'Qty':<8} {'Price ($)':<14} {'Value ($)'}")
    print("-" * 55)

    total = 0
    rows = []
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        print(f"  {symbol:<10} {qty:<8} ${price:<13} ${value:,.2f}")
        rows.append((symbol, qty, price, value))

    print("-" * 55)
    print(f"  {'TOTAL INVESTMENT':<32} ${total:,.2f}")
    print("=" * 55)

    return total, rows


def save_to_csv(portfolio_rows, total):
    """Save portfolio to a CSV file."""
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price ($)", "Value ($)"])
        for row in portfolio_rows:
            writer.writerow(row)
        writer.writerow([])
        writer.writerow(["TOTAL", "", "", f"${total:,.2f}"])
    print(f"\n  ✅ Portfolio saved to '{filename}'")


def save_to_txt(portfolio_rows, total):
    """Save portfolio to a TXT file."""
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write("=" * 55 + "\n")
        f.write("       STOCK PORTFOLIO SUMMARY\n")
        f.write(f"       Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 55 + "\n")
        f.write(f"{'Symbol':<10} {'Qty':<8} {'Price ($)':<14} {'Value ($)'}\n")
        f.write("-" * 55 + "\n")
        for symbol, qty, price, value in portfolio_rows:
            f.write(f"{symbol:<10} {qty:<8} ${price:<13} ${value:,.2f}\n")
        f.write("-" * 55 + "\n")
        f.write(f"{'TOTAL INVESTMENT':<32} ${total:,.2f}\n")
        f.write("=" * 55 + "\n")
    print(f"\n  ✅ Portfolio saved to '{filename}'")


def main():
    print("=" * 55)
    print("   💹 STOCK PORTFOLIO TRACKER — CodeAlpha Task 2")
    print("=" * 55)

    while True:
        # Show available stocks
        show_available_stocks()

        # Get portfolio from user
        portfolio = get_portfolio()

        if not portfolio:
            print("\n⚠️  You didn't add any stocks. Exiting.")
            break

        # Display summary
        result = display_portfolio(portfolio)
        if result == 0:
            break
        total, rows = result

        # Ask to save
        print("\n💾 Would you like to save your portfolio?")
        print("  1. Save as CSV")
        print("  2. Save as TXT")
        print("  3. Don't save")
        choice = input("\n  Enter choice (1/2/3): ").strip()

        if choice == "1":
            save_to_csv(rows, total)
        elif choice == "2":
            save_to_txt(rows, total)
        else:
            print("\n  Portfolio not saved.")

        # Play again?
        again = input("\n🔄 Track another portfolio? (yes/no): ").lower().strip()
        if again not in ("yes", "y"):
            print("\nThank you for using Stock Portfolio Tracker! 👋")
            break


if __name__ == "__main__":
    main()