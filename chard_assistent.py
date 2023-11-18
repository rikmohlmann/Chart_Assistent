import yfinance as yf
import matplotlib.pyplot as plt
import openai

# Define your OpenAI API key
openai.api_key = 'my-api-key-here'

# Fetch YTD stock data for NVDA and TSLA
nvda = yf.download('NVDA', start='2023-01-01')
tsla = yf.download('TSLA', start='2023-01-01')

# Normalize the data to the starting price of the year
nvda_normalized = nvda['Close'] / nvda['Close'].iloc[0]
tsla_normalized = tsla['Close'] / tsla['Close'].iloc[0]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(nvda_normalized, label='NVDA')
plt.plot(tsla_normalized, label='TSLA')

# Enhancing the graph
plt.title('YTD Stock Price Change: NVDA vs TSLA')
plt.xlabel('Date')
plt.ylabel('Normalized Price')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

# Example of using OpenAI API for a simple text-based interaction
# (Modify as per your project's requirements)
def get_openai_response(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
question = "write a poem about the generated graph displpayed in this script."
print(get_openai_response(question))
