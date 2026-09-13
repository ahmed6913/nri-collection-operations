from operations_summary import operations_summary

final_kpi = operations_summary[
    [
        "payment_type",
        "total_orders",
        "order_share_pct",
        "delivered_orders",
        "delivery_rate_pct",
        "cancelled_orders",
        "shipped_orders",
        "rto_orders",
        "rto_rate_pct",
        "returned_orders",
        "return_rate_pct"
    ]
].copy()

final_kpi.to_csv(
    "nri_operations_kpi.csv",
    index=False
)

print(final_kpi.to_string(index=False))
print("\nSaved: nri_operations_kpi.csv")
