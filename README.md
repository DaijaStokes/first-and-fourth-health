# First & Fourth Health

**Status:** In Progress

First & Fourth Health is a maternal health data engineering and analytics portfolio project focused on turning public health data into reliable, analytics-ready datasets.

The project is designed to demonstrate an end-to-end data engineering workflow: source selection, ingestion, validation, cleaning, transformation, modeling, testing, and analytics delivery.

## Business Question

**How do maternal health risk factors, prenatal-care patterns, and demographic characteristics differ across preterm birth and low-birth-weight outcomes in the United States?**

Version 1 begins with U.S. natality data and establishes a trusted baseline dataset before additional maternal-risk and prenatal-care data is incorporated.

## Data Source

The initial source is public **CDC/NCHS Natality** data covering **2020–2024**.

The baseline extract includes:

| Source Column | Expected Data Type |
| --- | --- |
| Year | Integer |
| Year Code | Integer |
| Mother's Single Race | String |
| Mother's Single Race Code | String |
| Age of Mother 10 | String |
| Age of Mother 10 Code | String |
| OE Gestational Age Weekly | String |
| OE Gestational Age Weekly Code | Integer |
| Infant Birth Weight 12 | String |
| Infant Birth Weight 12 Code | Integer |
| Births | Integer |
| % of Total Births | Decimal / Numeric |

Source terminology is preserved in the raw layer. Business-friendly names and derived fields will be introduced in later transformation layers.

## Current Progress

Completed:

- Defined the project purpose and primary business question
- Selected CDC/NCHS Natality as the Version 1 source
- Created a 2020–2024 baseline extract
- Validated that the source file opens successfully
- Confirmed expected years and columns
- Recorded the raw row count
- Reviewed expected data types for all source columns

Current phase:

**Raw data profiling**

Next step:

**Profile missing and null values before beginning data cleaning.**

## Planned Pipeline

```text
CDC/NCHS Source Data
        ↓
Raw / Bronze Layer
        ↓
Validation & Data Quality Checks
        ↓
Cleaned / Silver Layer
        ↓
Business Logic & Derived Measures
        ↓
Analytics / Gold Layer
        ↓
Reporting & Insights
```

Planned derived measures include:

- Preterm Birth Flag
- Low Birth Weight Flag

## Planned Technology

As the project develops, the pipeline will incorporate:

- Python
- SQL
- PySpark
- Databricks
- Git / GitHub
- Data quality testing
- Dimensional modeling
- Pipeline orchestration

Technologies will be added to the implementation only as they are actually used.

## Why This Project

This project applies concepts from production data engineering—data ingestion, validation, transformation, reconciliation, troubleshooting, and downstream analytics—to the independent design of a healthcare-focused data pipeline.

The goal is to build both technical skills and a clear, reproducible data engineering project from source data through analytics-ready outputs.
