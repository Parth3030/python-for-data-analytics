# 🐍 Module 01 — Python Foundations

> **Sessions 1, 2, 3, 4** | Variables · Data Types · Strings · Data Cleaning

---

## 📁 Folder Structure

```
01_python_foundations/
│
├── 01_02_variables_and_data_types/     ← Sessions 1 & 2 combined
│   ├── variables_intro.py
│   ├── naming_conventions.py
│   ├── dynamic_typing.py
│   └── ...
│
├── 03_data_types_analysis/             ← Session 3
│   ├── int_float_operations.py
│   ├── type_casting_real_data.py
│   ├── boolean_business_logic.py
│   └── ...
│
└── 04_strings_for_data_cleaning/       ← Session 4
    ├── string_methods.py
    ├── slicing_order_ids.py
    ├── fstrings_invoice.py
    └── ...
```

---

## 📚 What I Learned — Session by Session

### Sessions 1 & 2 — Introduction, Syntax, Variables
**Folder:** `01_02_variables_and_data_types/`

| Topic | What it does | Analytics use |
|-------|-------------|---------------|
| `print()` | Display output | Print reports, summaries |
| Variables | Store named values | `monthly_sales`, `customer_id` |
| Naming conventions | `snake_case` rules | Clean, readable analytics code |
| Dynamic typing | Variables can change type | CSV data changes from str → float |
| Comments `#` | Explain logic | Document every business rule |
| Multiple assignment | `a = b = c = 0` | Set base values for multiple zones |

**Key concept:** In data analytics, variable names must describe the business data they hold — not `x` or `temp`, but `monthly_revenue` or `rejection_rate`.

---

### Session 3 — Data Types in Python
**Folder:** `03_data_types_analysis/`

| Type | Example | When I use it |
|------|---------|---------------|
| `int` | `quantity = 150` | Counts, quantities, whole numbers |
| `float` | `unit_price = 1850.50` | Prices, percentages, OEE scores |
| `str` | `product = "CNC Part A"` | Names, IDs, labels |
| `bool` | `is_returned = False` | Flags, eligibility checks |
| `type()` | `type(variable)` | Audit data types in a dataset |
| `int()`, `float()`, `str()` | Type casting | Fix messy CSV data |

**Key concept:** Real-world data arrives with wrong types — a price stored as `'2499'` (string) instead of `2499.0` (float). Type casting is one of the most common data cleaning tasks.

---

### Session 4 — Strings & Data Cleaning
**Folder:** `04_strings_for_data_cleaning/`

| Method | What it does | Analytics use |
|--------|-------------|---------------|
| `.strip()` | Remove extra spaces | Clean customer names from forms |
| `.lower()` / `.upper()` / `.title()` | Normalise case | Standardise city/product names |
| `.replace()` | Swap characters | Fix separators, remove symbols |
| `.split()` | Break string into list | Parse CSV rows, extract fields |
| `string[start:end]` | Slice characters | Extract year from date, city from ID |
| f-strings `f'{var}'` | Format output | Build invoices, reports, dashboards |
| `.find()` / `in` | Search inside string | Check if keyword exists in a field |

**Key concept:** Before any analysis, data must be clean. String methods are the first tool data analysts use when raw data arrives from CSV files, web scrapes, or form submissions.

---

## 💡 My Approach

Every file in this module applies concepts to **real business problems** — not textbook examples.

Instead of:
```python
x = 5
print(x)
```

I write:
```python
# Track monthly revenue for Ahmedabad factory
monthly_revenue = 300000   # 150 parts x Rs.2000 per part
monthly_target  = 360000

gap = monthly_target - monthly_revenue
print(f"Revenue: Rs.{monthly_revenue:,} | Gap to target: Rs.{gap:,}")
```

---

## 🔑 Key Takeaways

- **Naming matters** — `customer_id` beats `x` every time. Recruiters read your variable names.
- **Types matter** — `'2500'` and `2500.0` look the same but behave completely differently in calculations.
- **Strings are data** — 80% of raw data arrives as strings. Cleaning them is a core analyst skill.
- **Comments are your voice** — code runs without them, but no one (including future you) knows why you wrote it.

---

## 🗂️ Files at a Glance

| File | Key concept | Business scenario |
|------|------------|-------------------|
| `01_02_variables_and_data_types/` | Variables, naming, types | Factory sales tracking |
| `03_data_types_analysis/` | int, float, bool, casting | Price cleaning, flag logic |
| `04_strings_for_data_cleaning/` | String methods, slicing, f-strings | Customer data cleaning pipeline |

---

## ➡️ Next Module

**[02\_data\_structures →](../02_data_structures/)**
Lists, Tuples, Dictionaries, Sets — storing and organising collections of data.

---

*Part of [python-for-data-analytics](../README.md) | Parth Parikh | Ahmedabad*
