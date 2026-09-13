import pandas as pd

file_path = "NRI_Collection_Dummy_Dataset.xlsx"
orders = pd.read_excel(file_path, sheet_name="orders")

orders["payment_type"] = orders["payment_method"].apply(
    lambda x: "COD" if x == "COD" else "Prepaid"
)

status = "order_status"

operations_summary = (
    orders.groupby("payment_type")
    .agg(
        total_orders=("order_id", "count"),
        delivered_orders=(status, lambda x: (x == "Delivered").sum()),
        cancelled_orders=(status, lambda x: (x == "Cancelled").sum()),
        rto_orders=(status, lambda x: (x == "RTO").sum()),
        returned_orders=(status, lambda x: (x == "Returned").sum())
    )
    .reset_index()
)

# Shipped orders
operations_summary["shipped_orders"] = (
    operations_summary["total_orders"]
    - operations_summary["cancelled_orders"]
)

# Order share
operations_summary["order_share_pct"] = (
    operations_summary["total_orders"]
    / operations_summary["total_orders"].sum()
    * 100
).round(2)

# Delivery rate
operations_summary["delivery_rate_pct"] = (
    operations_summary["delivered_orders"]
    / operations_summary["total_orders"]
    * 100
).round(2)

# RTO rate
operations_summary["rto_rate_pct"] = (
    operations_summary["rto_orders"]
    / operations_summary["shipped_orders"]
    * 100
).round(2)

# Return rate
operations_summary["return_rate_pct"] = (
    operations_summary["returned_orders"]
    / operations_summary["delivered_orders"]
    * 100
).round(2)

if __name__ == "__main__":
    print(operations_summary.to_string(index=False))
