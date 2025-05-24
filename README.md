 HEAD
# datafun-03-analytics
# DataFun-03-Analytics
=======
#  DataFun-03-Analytics
  (Finalize DataFun-03 project: fetch, process, and log all data types)

A Python project to fetch, analyze, and log data from multiple formats:
- CSV
- Excel
- JSON
- Plain Text (TXT)

---

##  Project Goals

This project demonstrates how to:
- Fetch web data using `requests`
- Save data in multiple formats (CSV, Excel, JSON, TXT)
- Analyze the data using `pandas` and standard Python libraries
- Log operations using a reusable logger (`utils_logger.py`)

---

##  How to Run Each Script

1. Activate the virtual environment:

```bash
.venv\Scripts\activate
```

2. Run each script:

```bash
python example_get_csv.py
python example_get_excel.py
python example_get_json.py
python example_get_text.py
```

3. View logs:

```bash
logs/project_log.log
```

---

##  Python Files Overview

| File                   | Description                                                   |
|------------------------|---------------------------------------------------------------|
| `example_get_csv.py`   | Fetches a CSV file from the web and analyzes it               |
| `example_get_excel.py` | Downloads and analyzes an Excel file                          |
| `example_get_json.py`  | Fetches JSON data about astronauts and analyzes it            |
| `example_get_text.py`  | Downloads a Shakespeare text and performs basic text analysis |
| `utils_logger.py`      | Logger utility used by all scripts                            |

---

##  Project Structure

```
```
├── example_data/
│ ├── 2020_happiness.csv
│ ├── astros.json
│ ├── Feedback.xlsx
│ └── romeo.txt
│
├── logs/
│ └── project_log.log
│
├── example_get_csv.py
├── example_get_excel.py
├── example_get_json.py
├── example_get_text.py
│
├── example_process_csv.py
├── example_process_excel.py
├── example_process_json.py
├── example_process_text.py
│
├── happiness_ladder_score_stats.txt
├── json_astronauts_by_craft.txt
├── text_romeo_word_count.txt
│
├── main.py
├── requirements.txt
├── README.md
└── utils_logger.py



---

##  Technologies Used

- Python 3.11+
- `requests`
- `pandas`
- `logging`
- `pathlib`
- `json`

---

##  What I Learned

- How to work with different file formats
- How to use Python to automate data fetching and analysis
- How to use logging for debugging and auditability
- How to follow a professional Git + VS Code workflow

---

##  Project Purpose (Course Context)

This project is part of the **Data Fundamentals** course  
at **Northwest Missouri State University**.

It helps students:
- Practice using Python modules and functions
- Learn data processing and file handling
- Document and manage projects in a clean structure

---

##  Author

**Sabri Hamdaoui**  
Master’s Student in Data Analytics  
Northwest Missouri State University  
GitHub: [github.com/sabrouch36](https://github.com/sabrouch36)

---

##  Project Setup Process

### 1. Cloned the Repository

```bash
git clone https://github.com/YOUR_USERNAME/datafun-03-analytics.git
cd datafun-03-analytics
code .
```

### 2. Created and Activated a Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Installed Project Dependencies

```bash
pip install -r requirements.txt
```

### 4. Ran the Project

```bash
python main.py
```
