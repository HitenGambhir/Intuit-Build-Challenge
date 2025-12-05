# Intuit Build Challenge – Assignment 1 & Assignment 2

This repository contains my complete solution for both assignments from the Intuit Build Challenge.  
Each assignment is implemented in Python with clean structure, comments, and separate test files.  
The solutions fully match the requirements described in the challenge instructions.

---

# 📘 Assignment 1 – Producer–Consumer Pattern

## ✔ What the assignment required
- Implement the classic Producer–Consumer pattern  
- Use a bounded queue with blocking behavior  
- Use locks + condition variables for synchronization  
- Implement Producer and Consumer classes  
- Stop consumers using a sentinel value  
- Provide unit tests validating behavior  

All these requirements are implemented exactly as described.

---

## ✔ What I implemented

### **1. BoundedQueue**
- Thread-safe queue  
- `put()` waits when full  
- `get()` waits when empty  
- Uses `Lock()` and `Condition()`  

### **2. Producer**
- Reads items from a list  
- Pushes them to the queue  

### **3. Consumer**
- Reads items from the queue  
- Stops when sentinel received  

### **4. Tests (`test_producer_consumer.py`)**
Covers:
- Basic queue operations  
- Blocking behavior  
- Correct producer/consumer workflow  
- Multiple producers  
- Stress test with many items  
- Successful stopping using sentinel  

### **5. Test Output**
A clean demonstration log is saved 


This shows queue sizes, consumption order, and thread behavior.

---

## ▶️ How to Run / Test Assignment 1

Go to the folder:
```bash
cd assignment1
python3 -m unittest -v
```

# 📗 Assignment 2 – Sales Data Analysis

## ✔ What the assignment required
- Read and process the “100 Sales Records” CSV file  
- Convert each row into a usable data structure  
- Compute the following:
  - Total revenue
  - Total profit
  - Revenue by region
  - Profit by region
  - Revenue by item type
  - Orders by sales channel
  - Monthly revenue
  - Average units per order
  - Top region by profit  
- Keep code simple and well-commented  
- Add a full separate test file  
- Produce clean output of results  

All requirements are completed exactly as described in the challenge instructions.

---

## ✔ What I implemented

### **1. Data Loading**
- A `SalesRecord` dataclass is used for each row.  
- `read_sales()` loads the CSV, parses numeric values, and returns a list of records.

### **2. Analysis Functions**
Implemented:
- `total_revenue()`
- `total_profit()`
- `revenue_by_region()`
- `profit_by_region()`
- `revenue_by_item_type()`
- `orders_by_channel()`
- `revenue_by_month()`
- `average_units_per_order()`
- `top_region_by_profit()`

All processing logic aligns with the challenge requirements.

### **3. Tests (test_sales_analysis.py)**
Covers:
- CSV parsing accuracy  
- Correct revenue & profit totals  
- Grouping by region, item type, channel  
- Monthly aggregates  
- Average units  
- Top region correctness  

### **4. Output Demonstration**
The test file prints a summary and stores the output in:

```
assignment2/test_output.txt
```

---

## ▶️ How to Run / Test Assignment 2

Move into the folder:
```bash
cd assignment2
```

Run the tests:
```bash
python3 -m unittest -v
```
---

# ✔ Final Notes

Both assignments have been implemented according to the requirements described in the challenge instructions.  
Each assignment includes clean Python code, comments explaining the logic, and separate test files that fully validate the functionality.

The project is structured for easy navigation and review, and each assignment can be run and tested independently.  
All calculations, threading behavior, and outputs were verified through automated unit tests.

---

# 🤖 About AI Assistance

AI was used only to assist with:
- Improving clarity of documentation  
- Helping format this README  
- Suggesting better comment structure  
- Helping organize the project explanation  

All code, logic, algorithms, and tests were written and verified manually.  
AI was not used to generate the core implementations — only as a support tool for writing, clarity, and presentation.

This ensures the work reflects my own understanding while benefiting from clearer communication.

---







