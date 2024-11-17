from flask import Blueprint, send_file, request, jsonify
import yfinance as yf
import matplotlib.pyplot as plt
import io
import base64
import os
import dotenv
import openai

api_bp = Blueprint("api", __name__)

@api_bp.route("/api/fyp", methods = ["POST"])
def get_company_summary(company):
    client = openai.OpenAI(
        api_key=os.environ.get("SAMBANOVA_API_KEY"),
        base_url="https://api.sambanova.ai/v1",
    )
    prompt = f"Looking at {company}, analyze its past performance in the stock market and give an evaluation on its future and if it is a worthy investment in a short summary and rating."
    response = client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=[{"role":"system","content":"You are an expert stock analyzer"},{"role":"user","content": prompt}],
        temperature =  0.1,
        top_p = 0.1
    )
    print(response)
    return response.choices[0].message.content

@api_bp.route("/api/accounts", methods = ["POST"])
def get_loan_summary():
    data = request.json
    amount = data.get("amount", 0)
    money = data.get("money", 0)
    credit_history = data.get("credit_history", 0)
    client = openai.OpenAI(
        api_key=os.environ.get("SAMBANOVA_API_KEY"),
        base_url="https://api.sambanova.ai/v1",
    )
    prompt = (
            f"You are a banker specializing in microloans designed to help individuals with limited credit history or "
            f"those starting a business. A client has requested a microloan with the following details:\n\n"
            f"- Loan Amount: {amount}\n"
            f"- Asset Value: {money}\n"
            f"- Credit History: {credit_history}\n\n"
            "Evaluate if the applicant qualifies for the loan based on the following criteria:\n"
            "1. Credit History: Consider the applicant's credit score but focus on their potential to improve rather than penalizing them for a low score. "
            "Assess if they have been making efforts to build their credit (e.g., timely payments, reducing debts).\n"
            "2. Assets and Financial Position: Review any assets or financial stability they can demonstrate, even if modest. "
            "For example, small savings, a business plan, or proof of income.\n"
            "3. Purpose of the Loan: Understand the reason for the loan. Is it for starting a small business, paying off an emergency expense, or investing in education? "
            "Prioritize applications that align with the microloan mission to provide opportunities for growth.\n"
            "4. Potential to Repay: Evaluate their ability to repay the loan within the specified period. Consider factors like "
            "future earning potential or expected business growth rather than focusing only on past financial records.\n\n"
            "You must provide:\n"
            "- A decision on whether the applicant qualifies for the loan (approved or not approved).\n"
            "- A brief explanation of your reasoning.\n"
            "- Encouragement if the applicant does not qualify, including advice on how they can improve their situation to qualify in the future.\n"
            "Use a professional and supportive tone throughout. Limit it to 6 sentences. Remember, the goal of microloans is to empower individuals and businesses with limited resources."
    )
    response = client.chat.completions.create(
    model='Meta-Llama-3.1-8B-Instruct',
    messages=[{"role":"system","content":"You are an expert stock analyzer"},{"role":"user","content": prompt}],
    temperature =  0.1,
    top_p = 0.1
    )
    result = response.choices[0].message.content
    print(result)
    return jsonify({"response": result})

def get_current_stock_price(ticker_symbols):
    current_prices = []
    for ticker_symbol in ticker_symbols:
        ticker = yf.Ticker(ticker_symbol)
        curr = str(ticker.history(period="1d")["Close"].iloc[-1])
        if '.' in curr:
            curr = curr[:curr.index('.') + 3]
        current_prices.append(curr)
    return current_prices


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
