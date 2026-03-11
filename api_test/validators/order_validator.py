"""
Order validation functions for e-commerce API testing
Each function validates a specific aspect of order responses
"""

def validate_order_id(order_id):
    """
    Validate order ID format
    
    Business Rules:
    - Must be exactly 10 characters
    - Must start with 'ORD'
    - Remaining 7 characters must be digits
    """
    # Check length
    if len(order_id) != 10:
        return(False, f"Order ID must be exactly 10 characters, got {len(order_id)}")
    
    # Check prefix
    if not order_id.startswith("ORD"):
        actual_prefix = order_id[:3]
        return(False, f"Order ID must start with 'ORD', got '{actual_prefix}'")
    
    # Check if remaining characters are digits
    digit_section = order_id[3:]
    if not digit_section.isdigit():
        return(False, f"Order ID must have 7 digits after 'ORD', got '{digit_section}'")
    

    return(True, None)


def validate_email_format(email):
    """
    Validate customer email format
    
    Business Rules:
    - Must contain exactly one '@' symbol
    - Domain part must contain at least one '.'
    - Must not be empty before or after '@'
    """
    
    if '@' not in email:
        return(False, f"Email doesn't contain an '@' symbol.")
    
    if '.' not in email:
        return(False, f"Email doesn't contain a '.'")


def check_email_alias(email):
    """
    Check if email contains an alias (+ symbol)
    """
    # TODO: Implement check
    pass


def calculate_order_subtotal(items):
    """
    Calculate order subtotal from items
    
    Formula: sum of (price * quantity - discount) for all items
    
    Args:
        items (list): List of item dictionaries with keys:
                     'price', 'quantity', 'discount'
    
    Returns:
        float: Calculated subtotal rounded to 2 decimal places
    
    Example:
        >>> items = [
        ...     {"price": 100.00, "quantity": 2, "discount": 10.00},
        ...     {"price": 50.00, "quantity": 1, "discount": 0}
        ... ]
        >>> calculate_order_subtotal(items)
        240.0
    """
    # TODO: Calculate subtotal
    # Remember: (price * quantity) - discount for each item
    pass


def validate_order_total(order_data):
    """
    Validate that order total matches calculated total
    
    Formula: subtotal + tax + shipping_cost = total
    
    Args:
        order_data (dict): Order dictionary containing:
                          'subtotal', 'tax', 'shipping_cost', 'total'
    
    Returns:
        tuple: (is_valid: bool, expected_total: float, actual_total: float)
    
    Example:
        >>> order = {"subtotal": 100, "tax": 10, "shipping_cost": 5, "total": 115}
        >>> validate_order_total(order)
        (True, 115.0, 115.0)
    """
    # TODO: Calculate expected total
    # TODO: Compare with actual total (allow 0.01 difference for rounding)
    pass


def validate_order_status(status, expected_status="confirmed"):
    """
    Validate order status matches expected value
    
    Args:
        status (str): Actual order status
        expected_status (str): Expected order status (default: "confirmed")
    
    Returns:
        tuple: (is_valid: bool, error_message: str or None)
    """
    # TODO: Implement validation
    pass


def validate_required_fields(order_dict, required_fields):
    """
    Check if all required fields exist in order response
    
    Args:
        order_dict (dict): The order dictionary
        required_fields (list): List of required field names
    
    Returns:
        tuple: (is_valid: bool, missing_fields: list)
    
    Example:
        >>> order = {"order_id": "123", "total": 100}
        >>> validate_required_fields(order, ["order_id", "total", "email"])
        (False, ["email"])
    """
    # TODO: Check for missing fields
    pass


def validate_shipping_address(address):
    """
    Validate shipping address completeness
    
    Required fields: street, city, state, zip, country
    Additional validation:
    - ZIP must be 5 digits (for USA)
    - State must be 2 uppercase letters
    
    Args:
        address (dict): Shipping address dictionary
    
    Returns:
        tuple: (is_valid: bool, errors: list of error messages)
    """
    # TODO: Implement address validation
    pass


def validate_item_quantities(items):
    """
    Validate all items have positive quantities
    
    Business Rule: Quantity must be >= 1
    
    Args:
        items (list): List of item dictionaries
    
    Returns:
        tuple: (is_valid: bool, invalid_items: list)
    """
    # TODO: Check quantities
    pass