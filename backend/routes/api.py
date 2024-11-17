from flask import Blueprint, send_file
import yfinance as yf
import matplotlib.pyplot as plt
import io
import base64


api_bp = Blueprint("api", __name__)

@api_bp.route("/api/investments", methods=["GET"])
def api_investments():
    return {"investments": []}  # Example JSON response

def get_company_investment_data_and_graph(tickers):
    plt.figure(figsize= (10,6))
    images = []  # List to store base64 images
    print("TICKERS: ")
    print(tickers)
    for ticker in tickers:
        
        # Get the stock data for the last 5 years (5y)
        data = yf.download(ticker, period='5y')

        # Create a new plot for each stock
        plt.figure(figsize=(10, 6))

        # Plot the closing price for the current stock
        plt.plot(data.index, data['Close'], label=ticker)
        plt.title(f"Stock Prices for {ticker} (Last 5 Years)")
        plt.xlabel("Date")
        plt.ylabel("Stock Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot to a bytes buffer and encode it as base64
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        images.append(img_base64)  # Append the image to the list

    return images