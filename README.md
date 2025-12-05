# Intuit Build Challenge – Assignment 1 & Assignment 2

This repository contains my complete solution for both assignments from the Intuit Build Challenge.  
Each assignment is implemented in Python with clean structure, comments, separate test files, and console output stored inside each assignment’s `test_output.txt`.  
The solutions fully follow the requirements defined in the challenge instructions.

---

# 📁 GitHub Repository Structure

```
Intuit-Build-Challenge/
│
├── assignment1/
│   ├── producer_consumer.py
│   ├── test_producer_consumer.py
│   └── test_output.txt
│
├── assignment2/
│   ├── 100 Sales Records.csv
│   ├── sales_analysis.py
│   ├── test_sales_analysis.py
│   └── test_output.txt
│
├── .gitignore
└── README.md
```

---

# 📘 Assignment 1 – Producer–Consumer Pattern

## ✔ Requirements Implemented
- Bounded queue with blocking behavior  
- Thread synchronization with `Lock` + `Condition`  
- Producer and Consumer threads  
- Sentinel-based stopping  
- Comprehensive unit tests  

---

## ✔ Implementation Summary

### **1. BoundedQueue**
Thread-safe queue with:
- `put()` waits if full  
- `get()` waits if empty  

### **2. Producer**
Pushes items from a list into the queue.

### **3. Consumer**
Consumes queue items and stops on sentinel.

### **4. Tests**
Validates:
- Queue correctness  
- Blocking when full  
- Blocking when empty  
- Single & multiple producers  
- Stress cases  
- Sentinel stop  

### **5. Sample Output (from `test_output.txt`)**

```
=== PRODUCER–CONSUMER DEMO START ===

Producer: Starting...
Producer: putting 1 (queue size: 0)
Consumer: Starting...
Consumer: waiting... (queue size: 1)
Consumer: got 1 → dest=[1]
Producer: putting 2 (queue size: 0)
Consumer: waiting... (queue size: 1)
Consumer: got 2 → dest=[1, 2]
Producer: putting 3 (queue size: 0)
Producer: putting 4 (queue size: 1)
Consumer: waiting... (queue size: 2)
Consumer: got 3 → dest=[1, 2, 3]
Producer: putting 5 (queue size: 1)
Consumer: waiting... (queue size: 2)
Consumer: got 4 → dest=[1, 2, 3, 4]
Producer: Done
Consumer: waiting... (queue size: 2)
Consumer: got 5 → dest=[1, 2, 3, 4, 5]
Consumer: waiting... (queue size: 1)
Consumer: received sentinel, stopping
Consumer: Done

=== PRODUCER–CONSUMER DEMO END ===
```

---

## ▶️ How to Run Tests for Assignment 1

```bash
cd assignment1
python3 -m unittest -v
```

---

# 📗 Assignment 2 – Sales Data Analysis

## ✔ Requirements Implemented
- Load CSV into structured records  
- Compute:
  - revenue & profit totals  
  - revenue/profit by region  
  - revenue by item type  
  - orders by sales channel  
  - revenue by month  
  - average units  
  - top-performing region  
- Separate test file validating all logic  
- Output summary stored in `test_output.txt`  

---

## ✔ Implementation Summary

### **1. SalesRecord dataclass**
Defines the structure for each CSV row.

### **2. Analysis Functions**
Includes:
- `total_revenue()`  
- `total_profit()`  
- `revenue_by_region()`  
- `profit_by_region()`  
- `orders_by_channel()`  
- `revenue_by_item_type()`  
- `revenue_by_month()`  
- `average_units_per_order()`  
- `top_region_by_profit()`  

### **3. Tests**
Covers:
- CSV parsing  
- All summary calculations  
- Grouping accuracy  
- Month extraction  
- Edge case handling  

### **4. Sample Output (from `test_output.txt`)**

```
=== SALES ANALYSIS VERBOSE DEMO (TEST OUTPUT) ===

Loaded: 4 records
Total Revenue: 4344531.05
Total Profit: 1443941.43
Top Region: Australia and Oceania

Revenue by Region:
  Australia and Oceania: 2533654.0
  Central America and the Caribbean: 576782.8
  Europe: 1158502.59
  Sub-Saharan Africa: 75591.66

Revenue by Month:
  2010-05: 2533654.0
  2012-08: 576782.8
  2014-05: 1158502.59
  2014-06: 75591.66

=== END OF VERBOSE DEMO ===
```

---

## ▶️ How to Run Tests for Assignment 2

```bash
cd assignment2
python3 -m unittest -v
```

---

# 🤖 About AI Assistance

AI was used only for:
- Improving clarity of documentation  
- Formatting the README  
- Refining comment style and structure  

The code, logic, and tests were written manually.  
AI assisted only with readability, not implementation.

---

# ✔ Final Notes

- Both assignments fully match the challenge instructions.  
- Code is clean, tested, and easy to review.  
- Output for both assignments is stored in `test_output.txt`.  

