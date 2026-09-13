from operations_summary import operations_summary

prepaid_rto_rate = (
    operations_summary.loc[
        operations_summary["payment_type"] == "Prepaid",
        "rto_rate_pct"
    ].iloc[0] / 100
)

cod_shipped = (
    operations_summary.loc[
        operations_summary["payment_type"] == "COD",
        "shipped_orders"
    ].iloc[0]
)

expected_cod_rto = cod_shipped * prepaid_rto_rate

actual_cod_rto = (
    operations_summary.loc[
        operations_summary["payment_type"] == "COD",
        "rto_orders"
    ].iloc[0]
)

potential_rto_reduction = actual_cod_rto - expected_cod_rto

print("Actual COD RTO:", actual_cod_rto)
print("Expected COD RTO at Prepaid rate:", round(expected_cod_rto))
print("Potential RTO reduction:", round(potential_rto_reduction))
