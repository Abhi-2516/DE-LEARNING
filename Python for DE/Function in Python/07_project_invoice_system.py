"""
PROJECT 2: Invoice Generation System
=====================================
Problem: Create a professional invoice generator using *args and **kwargs

Requirements:
- Accept customer name, variable items, and variable charges
- Calculate totals including taxes
- Generate formatted invoice
- Support multiple discount and charge types
"""

def calculate_subtotal(*items_prices) -> float:
    \"\"\"
    Calculate subtotal from item prices.
    
    Parameters:
        *items_prices: Variable number of item prices
    
    Returns:
        float: Sum of all item prices
    \"\"\"
    return sum(items_prices)


def apply_discount(amount: float, discount_percent: float = 0.0) -> float:
    \"\"\"
    Apply discount to amount.
    
    Parameters:
        amount (float): Original amount
        discount_percent (float): Discount percentage
    
    Returns:
        float: Amount after discount
    \"\"\"
    return amount * (1 - discount_percent / 100)


def apply_taxes(amount: float, tax_rate: float = 0.18) -> float:
    \"\"\"
    Apply taxes to amount.
    
    Parameters:
        amount (float): Amount before tax
        tax_rate (float): Tax rate (default: 18% GST)
    
    Returns:
        float: Amount including tax
    \"\"\"
    return amount + (amount * tax_rate)


def generate_invoice(customer_name: str = "Guest", *items: str, **charges: float) -> str:
    \"\"\"
    Generate professional invoice with flexible parameters.
    
    Parameters:
        customer_name (str): Customer name (default: "Guest")
        *items (str): Item names/descriptions
        **charges (float): Named charges (price, tax, delivery, discount, etc.)
    
    Returns:
        str: Formatted invoice
    \"\"\"
    total = 0.0
    invoice_lines = []
    
    # Header
    invoice_lines.append("=" * 55)
    invoice_lines.append("INVOICE")
    invoice_lines.append("=" * 55)
    invoice_lines.append(f"Customer: {customer_name.upper()}")
    invoice_lines.append("-" * 55)
    
    # Items section
    if items:
        invoice_lines.append("\nItems Purchased:")
        invoice_lines.append("-" * 55)
        for idx, item in enumerate(items, 1):
            invoice_lines.append(f"  {idx}. {item}")
    
    # Charges section
    if charges:
        invoice_lines.append("\nCharges & Details:")
        invoice_lines.append("-" * 55)
        
        for label, amount in charges.items():
            formatted_label = label.replace('_', ' ').title()
            # Format amount with proper sign
            amount_str = f"₹{amount:>8.2f}"
            invoice_lines.append(f"  {formatted_label:<30} {amount_str}")
            total += amount
    
    # Total
    invoice_lines.append("-" * 55)
    invoice_lines.append(f"{'TOTAL AMOUNT DUE':<30} ₹{total:>8.2f}")
    invoice_lines.append("=" * 55)
    invoice_lines.append("\nThank you for your business!")
    
    return "\n".join(invoice_lines)


def generate_detailed_invoice(
    customer_name: str = "Guest",
    *items: str,
    **charges: float
) -> str:
    \"\"\"
    Generate detailed invoice with itemized breakdown and tax calculation.
    
    Parameters:
        customer_name (str): Customer name
        *items (str): Item names
        **charges (float): Itemized charges (subtotal, tax, delivery, discount, etc.)
    
    Returns:
        str: Detailed formatted invoice
    \"\"\"
    
    subtotal = charges.get('subtotal', 0)
    discount = charges.get('discount', 0)
    delivery = charges.get('delivery', 0)
    tax = charges.get('tax', 0)
    
    # Calculate if tax not explicitly provided
    if tax == 0 and subtotal > 0:
        taxable_amount = subtotal - discount
        tax = taxable_amount * 0.18  # 18% GST
    
    final_total = subtotal - discount + delivery + tax
    
    invoice_lines = []
    
    # Header
    invoice_lines.append("╔" + "═" * 53 + "╗")
    invoice_lines.append("║" + " " * 15 + "PROFESSIONAL INVOICE" + " " * 18 + "║")
    invoice_lines.append("╚" + "═" * 53 + "╝")
    invoice_lines.append(f"\nCustomer: {customer_name}")
    invoice_lines.append("\n" + "-" * 55)
    
    # Items
    if items:
        invoice_lines.append("ITEMS ORDERED:")
        for idx, item in enumerate(items, 1):
            invoice_lines.append(f"  {idx}. {item}")
    
    # Breakdown
    invoice_lines.append("\n" + "-" * 55)
    invoice_lines.append("PAYMENT BREAKDOWN:")
    invoice_lines.append("-" * 55)
    
    invoice_lines.append(f"  Subtotal            ₹{subtotal:>10.2f}")
    
    if discount > 0:
        invoice_lines.append(f"  Discount (-18%)    -₹{discount:>10.2f}")
    
    if delivery > 0:
        invoice_lines.append(f"  Delivery Charges    ₹{delivery:>10.2f}")
    
    if tax > 0:
        invoice_lines.append(f"  Tax (18% GST)       ₹{tax:>10.2f}")
    
    invoice_lines.append("-" * 55)
    invoice_lines.append(f"  {'TOTAL DUE':<20} ₹{final_total:>10.2f}")
    invoice_lines.append("-" * 55)
    
    return "\n".join(invoice_lines)


# ============================================================================
# MAIN EXECUTION - EXAMPLES
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("INVOICE GENERATION SYSTEM")
    print("=" * 60)
    print()
    
    # EXAMPLE 1: Simple Invoice
    print("\n📄 EXAMPLE 1: Simple Invoice")
    print()
    
    simple_invoice = generate_invoice(
        "Aman Kumar",
        "Masala Chai",
        "Samosa",
        "Biscuit",
        chai=50,
        samosa=30,
        biscuit=20,
        tax=18.00
    )
    print(simple_invoice)
    
    
    # EXAMPLE 2: Invoice with Discounts
    print("\n\n📄 EXAMPLE 2: Invoice with Discount")
    print()
    
    invoice_with_discount = generate_invoice(
        "Priya Sharma",
        "Green Tea",
        "Croissant",
        "Juice",
        subtotal=200,
        discount=36,
        tax=29.52,
        delivery=50
    )
    print(invoice_with_discount)
    
    
    # EXAMPLE 3: Detailed Invoice
    print("\n\n📄 EXAMPLE 3: Detailed Invoice with Breakdown")
    print()
    
    detailed_invoice = generate_detailed_invoice(
        "Raj Patel",
        "Cappuccino",
        "Pastry",
        "Sandwich",
        subtotal=450,
        discount=81,
        delivery=60,
        tax=66.42
    )
    print(detailed_invoice)
    
    
    # EXAMPLE 4: Large Order Invoice
    print("\n\n📄 EXAMPLE 4: Large Order for Event")
    print()
    
    large_order = generate_invoice(
        "XYZ Event Management",
        "Chai (50 cups)",
        "Coffee (30 cups)",
        "Samosas (100 pieces)",
        "Cookies (200 pieces)",
        chai_service=2500,
        coffee_service=1800,
        samosa_service=1500,
        cookies_service=800,
        setup_charges=500,
        delivery=300,
        tax=2076,
    )
    print(large_order)
    
    
    print("\n\n" + "=" * 60)
    print("✓ Invoice generation system demonstration complete!")
    print("=" * 60)
