# 💎 NRI Collection — COD vs Prepaid Operations Analytics

> **Data Analytics Portfolio Project | Python + Power BI | E-commerce Operations Analytics**

![Python](https://img.shields.io/badge/Python-Data%20Analysis-blue)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![Focus](https://img.shields.io/badge/Focus-Operations%20Analytics-purple)

---

## 📌 Project Overview

NRI Collection is a jewellery retail business. This portfolio project analyzes **12,000 simulated e-commerce orders** to understand how **COD vs Prepaid payment behavior affects delivery, RTO, and customer returns**.

The project follows a practical business analytics workflow:

**Raw Excel Data → Python Analysis → Power BI/DAX → Interactive Dashboard → Business Recommendations**

---

## 🎯 Business Problem

COD is widely used in Indian e-commerce, but it can introduce additional operational risk because customers do not pay until delivery.

The key business question is:

> **How does COD vs Prepaid payment behavior impact NRI Collection's delivery, RTO and return performance, and what can the business do to improve operations?**

---

## 🎯 Project Objectives

- Measure COD vs Prepaid order mix
- Compare delivery performance
- Measure RTO volume and RTO rate
- Compare customer return rates
- Identify operational risk
- Estimate a potential RTO-reduction opportunity
- Translate findings into actionable business recommendations

---

# 📊 Dataset

The project uses a simulated NRI Collection e-commerce dataset created for portfolio and analytical practice.

| Dataset | Records |
|---|---:|
| Orders | 12,000 |
| Order Items | ~19,400 |
| Customers | 4,500 |
| Products | 120 |
| Returns/RTO | ~2,604 |
| Expenses | ~3,648 |
| Couriers | 6 |
| Locations | 29 |
| Date Range | Jan 2025 – Aug 2026 |

### Relevant Order Fields

- `order_id`
- `customer_id`
- `order_date`
- `payment_method`
- `payment_type`
- `order_status`
- `courier`
- `location`

---

# 💳 Payment Classification

For operational analysis, payment methods were grouped into two categories:

| Original Payment Method | Analysis Group |
|---|---|
| COD | COD |
| Prepaid | Prepaid |
| UPI | Prepaid |

This creates a simple comparison between **COD** and **non-COD/prepaid orders**.

---

# 🐍 Python Analysis

### Python and Pandas were used for data preparation, validation and operational analysis.



- Analysis Workflow
- Load the orders dataset
- Create COD vs Prepaid classification
- Calculate order volume
- Calculate payment-method share
- Analyze delivery performance
- Calculate shipped orders
- Analyze RTO performance
- Analyze customer returns
- Create final KPI summary
- Run RTO opportunity scenario analysis
