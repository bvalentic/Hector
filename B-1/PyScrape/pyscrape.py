import requests
from bs4 import BeautifulSoup

def scrape_prices(url, product_name):
    """
    Scrapes grocery prices from a given URL for a specific product.

    Args:
        url: The URL of the grocery website.
        product_name: The name of the product to search for.

    Returns:
        A list of tuples, each containing the store name and price.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "lxml")

        # Replace these selectors with the appropriate ones for the website you're scraping
        product_elements = soup.select(".product-item") # Replace with actual selector
        prices = []
        for product_element in product_elements:
            if product_name.lower() in product_element.text.lower():
                price_element = product_element.select_one(".product-price") # Replace with actual selector
                price_text = price_element.text.strip()
                prices.append((url, price_text))

        return prices

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

if __name__ == "__main__":
    product_to_search = "Apples"
    
    # Replace these URLs with the grocery websites you want to scrape
    websites = [
        "https://www.examplegrocerystore1.com/",
        "https://www.examplegrocerystore2.com/"
    ]

    all_prices = []
    for website in websites:
        prices_for_website = scrape_prices(website, product_to_search)
        all_prices.extend(prices_for_website)

    for store, price in all_prices:
        print(f"Store: {store}, Price: {price}")

