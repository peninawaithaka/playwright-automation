"""
Real-world E-commerce API Response Validation Suite
Use Case: Testing a shopping cart API that returns order details, user info, and payment status.
"""

import pytest
from datetime import datetime


class TestOrderResponseValidation:
    
    def test_successful_order_response_validation(self):
        """
        Scenario: Validate a successful order creation response
        
        Business Rules:
        - Order must have a valid order_id (alphanumeric, 10 chars)
        - Customer email must be in valid format
        - Total must match sum of item prices
        - Order status should be 'confirmed' for successful orders
        """
        # Simulated API response
        api_response = {
            "status": "success",
            "order": {
                "order_id": "ORD1234567",
                "customer_email": "sarah.chen+shopping@email.com",
                "items": [
                    {"name": "Laptop", "price": 999.99, "quantity": 1},
                    {"name": "Mouse", "price": 29.99, "quantity": 2}
                ],
                "shipping_address": {
                    "street": "123 Main St",
                    "city": "San Francisco",
                    "state": "CA",
                    "zip": "94102"
                },
                "total": 1059.97,
                "currency": "USD",
                "order_status": "confirmed",
                "created_at": "2024-02-05T10:30:00Z"
            },
            "message": "Order placed successfully"
        }
        
        #order id validation
        order_id = api_response['order']['order_id'] 
        assert len(order_id) == 10
        assert order_id.startswith("ORD")
        
        #customer email validation
        customer_email =  api_response["order"]['customer_email']
        email_parts =   customer_email.split('@')
        assert len(email_parts) == 2
        assert '.' in email_parts[1]
        
        has_email_alias = '+' in customer_email  
        assert has_email_alias is True

        #Totals validation
        order_total = api_response["order"]["total"]
        orders_made_total = api_response["order"]["items"]

        calculated_total = 0

        for item in orders_made_total:
            calculated_total += item['price'] * item['quantity']

        assert calculated_total == order_total

        #order status validation
        status = api_response["order"]["order_status"]
        assert status == "confirmed", f"Expected: {"confirmed"} but found: {status}"

if __name__ == "__main__":
    test_instance = TestOrderResponseValidation()
    test_instance.test_successful_order_response_validation()