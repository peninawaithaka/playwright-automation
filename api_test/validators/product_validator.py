"""
Product search validation functions
"""

def filter_in_stock_products(products):
    """
    Filter products that are in stock
    
    Args:
        products (list): List of product dictionaries
    
    Returns:
        list: Products where in_stock is True
    
    Use list comprehension
    """
    # TODO: Implement filter
    pass


def sort_products_by_price(products, ascending=True):
    """
    Sort products by price
    
    Args:
        products (list): List of product dictionaries
        ascending (bool): Sort order (default: True)
    
    Returns:
        list: Sorted products
    
    Use sorted() with lambda function
    """
    # TODO: Implement sorting
    pass


def extract_product_ids(products):
    """
    Extract list of product IDs
    
    Args:
        products (list): List of product dictionaries
    
    Returns:
        list: List of product IDs (strings)
    
    Use list comprehension
    """
    # TODO: Implement extraction
    pass


def find_cheapest_product(products):
    """
    Find the product with lowest price
    
    Args:
        products (list): List of product dictionaries
    
    Returns:
        dict: Product with lowest price
    
    Use min() with lambda function
    """
    # TODO: Implement search
    pass


def calculate_average_price(products):
    """
    Calculate average price of products
    
    Args:
        products (list): List of product dictionaries
    
    Returns:
        float: Average price rounded to 2 decimal places
    """
    # TODO: Implement calculation
    pass


def filter_by_price_range(products, min_price, max_price):
    """
    Filter products within price range
    
    Args:
        products (list): List of product dictionaries
        min_price (float): Minimum price (inclusive)
        max_price (float): Maximum price (inclusive)
    
    Returns:
        list: Products within price range
    """
    # TODO: Implement filter
    pass


def filter_by_rating(products, min_rating):
    """
    Filter products with rating >= min_rating
    
    Args:
        products (list): List of product dictionaries
        min_rating (float): Minimum rating threshold
    
    Returns:
        list: Products meeting rating requirement
    """
    # TODO: Implement filter
    pass


def get_out_of_stock_count(products):
    """
    Count how many products are out of stock
    
    Args:
        products (list): List of product dictionaries
    
    Returns:
        int: Number of out-of-stock products
    """
    # TODO: Implement count
    pass