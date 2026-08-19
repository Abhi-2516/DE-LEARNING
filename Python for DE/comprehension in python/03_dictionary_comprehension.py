"""Dictionary comprehensions: create dictionaries from an iterable."""


def convert_prices_to_usd(prices_inr: dict[str, int], exchange_rate: float = 80) -> dict[str, float]:
    """Convert prices from INR to USD using the supplied exchange rate."""
    return {tea: round(price / exchange_rate, 2) for tea, price in prices_inr.items()}


def word_lengths(words: list[str]) -> dict[str, int]:
    """Map each word to its length."""
    return {word: len(word) for word in words}


if __name__ == "__main__":
    tea_prices = {"masala chai": 40, "green tea": 50, "tulsi tea": 80}
    print("Prices in USD:", convert_prices_to_usd(tea_prices))
    print("Word lengths:", word_lengths(["tea", "coffee", "water"]))
