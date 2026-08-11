# Mphasis Data Engineering Practice Questions

Use this as a drill sheet. For each question, answer in this order:

1. Clarify the data and expected output.
2. Explain the approach in plain English.
3. Write the query/code or describe the pipeline.
4. Mention validation, edge cases, and tradeoffs.
5. Connect back to AAIS only when it is truthful and relevant.

## 1. SQL: Find The Second-Highest Salary Per Department

Interviewer is testing: window functions, ranking, ties, partitioning.

Question:

Given `employees(employee_id, department_id, employee_name, salary)`, return employees with the second-highest salary in each department.

Approach:

- Partition rows by department.
- Rank salaries inside each department from highest to lowest.
- Use `DENSE_RANK()` if ties should count as the same salary level.
- Filter to rank 2.

Solution:

```sql
WITH ranked AS (
  SELECT
    employee_id,
    department_id,
    employee_name,
    salary,
    DENSE_RANK() OVER (
      PARTITION BY department_id
      ORDER BY salary DESC
    ) AS salary_rank
  FROM employees
)
SELECT
  employee_id,
  department_id,
  employee_name,
  salary
FROM ranked
WHERE salary_rank = 2;
```

How to explain:

I would use `DENSE_RANK()` because if two employees tie for the highest salary, the next distinct salary should still be considered second. If the business wants exactly the second row regardless of ties, then I would use `ROW_NUMBER()` instead.

AAIS connection:

At AAIS I used SQL for source-table profiling and validation. This kind of window function is useful for ranking, deduplication, and comparing values within business groups.

## 2. SQL: Month-Over-Month Growth With `LAG()`

Interviewer is testing: `LAG()`, date grouping, trend analysis.

Question:

Given `sales(order_date, revenue)`, calculate monthly revenue and month-over-month growth percentage.

Approach:

- Aggregate revenue by month.
- Use `LAG()` to get the previous month's revenue.
- Calculate `(current - previous) / previous`.
- Guard against null or zero previous revenue.

Solution:

```sql
WITH monthly_sales AS (
  SELECT
    DATE_TRUNC('month', order_date) AS sales_month,
    SUM(revenue) AS monthly_revenue
  FROM sales
  GROUP BY DATE_TRUNC('month', order_date)
),
with_previous AS (
  SELECT
    sales_month,
    monthly_revenue,
    LAG(monthly_revenue) OVER (
      ORDER BY sales_month
    ) AS previous_month_revenue
  FROM monthly_sales
)
SELECT
  sales_month,
  monthly_revenue,
  previous_month_revenue,
  CASE
    WHEN previous_month_revenue IS NULL OR previous_month_revenue = 0 THEN NULL
    ELSE ROUND(
      100.0 * (monthly_revenue - previous_month_revenue) / previous_month_revenue,
      2
    )
  END AS month_over_month_growth_pct
FROM with_previous
ORDER BY sales_month;
```

How to explain:

`LAG()` lets me compare the current row to a previous row after defining an order. Here, after monthly aggregation, each month can look back at the previous month. I handle the first month and zero-revenue cases so the query does not produce misleading output or divide by zero.

AAIS connection:

If I were validating a recurring billing workflow, the same pattern could compare current billing totals to prior-period totals to catch unusual changes.

## 3. SQL: Deduplicate Records And Keep The Latest Row

Interviewer is testing: duplicate handling, `ROW_NUMBER()`, business keys.

Question:

Given `customer_updates(customer_id, name, email, updated_at)`, keep only the latest row per `customer_id`.

Approach:

- Decide the business key: `customer_id`.
- Order updates by `updated_at` descending.
- Use `ROW_NUMBER()` and keep row 1.
- If timestamps can tie, add a deterministic tiebreaker if available.

Solution:

```sql
WITH deduped AS (
  SELECT
    customer_id,
    name,
    email,
    updated_at,
    ROW_NUMBER() OVER (
      PARTITION BY customer_id
      ORDER BY updated_at DESC
    ) AS rn
  FROM customer_updates
)
SELECT
  customer_id,
  name,
  email,
  updated_at
FROM deduped
WHERE rn = 1;
```

How to explain:

I would not use `SELECT DISTINCT` here because distinct removes exact duplicate rows, but it does not choose the correct latest business record. `ROW_NUMBER()` gives control over which record survives.

AAIS connection:

This connects to source-system profiling and standardization. When multiple systems represent similar entities, you need a clear business key and deterministic rules for selecting the trusted record.

## 4. PySpark: Drop Duplicates And Keep The Latest Record

Interviewer is testing: PySpark DataFrame syntax and window functions.

Question:

Given a PySpark DataFrame `updates_df` with `customer_id`, `email`, and `updated_at`, keep the latest update per customer.

Approach:

- Use `Window.partitionBy("customer_id").orderBy(col("updated_at").desc())`.
- Add a row number.
- Filter to row 1.
- Drop helper column.

Solution:

```python
from pyspark.sql import functions as F
from pyspark.sql.window import Window

window_spec = Window.partitionBy("customer_id").orderBy(F.col("updated_at").desc())

latest_updates_df = (
    updates_df
    .withColumn("rn", F.row_number().over(window_spec))
    .filter(F.col("rn") == 1)
    .drop("rn")
)
```

How to explain:

`dropDuplicates(["customer_id"])` would remove duplicates, but it would not guarantee I kept the latest row. The window function makes the deduplication rule explicit.

AAIS connection:

For data-standardization work, the important part is not only removing duplicates. It is choosing the correct survivor record based on a business rule.

## 5. PySpark: Add A Conditional Column

Interviewer is testing: `withColumn`, `when().otherwise()`, readable business rules.

Question:

Given `patients_df(patient_id, age, condition)`, create `risk_category`:

- `High` if age > 60 and condition is `Diabetes` or `Heart Disease`
- `Medium` if age is between 40 and 60 inclusive
- `Low` otherwise

Approach:

- Use `withColumn`.
- Use chained `when()` conditions.
- Put the most specific rule first.

Solution:

```python
from pyspark.sql import functions as F

risk_df = patients_df.withColumn(
    "risk_category",
    F.when(
        (F.col("age") > 60) &
        (F.col("condition").isin("Diabetes", "Heart Disease")),
        F.lit("High")
    ).when(
        (F.col("age") >= 40) & (F.col("age") <= 60),
        F.lit("Medium")
    ).otherwise(F.lit("Low"))
)
```

How to explain:

I would translate the business rule directly into readable conditions. I also put the high-risk rule first because it is more specific. In production, I would confirm null behavior for age and condition with the business owner.

## 6. PySpark: Group And Aggregate

Interviewer is testing: common DataFrame transformations.

Question:

Given `transactions_df(company_id, amount, transaction_date)`, calculate total billing amount and transaction count per company.

Approach:

- Group by `company_id`.
- Aggregate `sum(amount)` and `count(*)`.
- Alias output columns clearly.

Solution:

```python
from pyspark.sql import functions as F

company_billing_df = (
    transactions_df
    .groupBy("company_id")
    .agg(
        F.sum("amount").alias("total_billing_amount"),
        F.count("*").alias("transaction_count")
    )
)
```

How to explain:

This is the core shape of many billing and reporting transformations: group by the business entity, apply aggregations, and produce a clean output for downstream users.

AAIS connection:

This maps directly to how I would describe the AAIS billing workflow at a high level: process production data, group and calculate charges for member companies, then validate the output.

## 7. Incremental Load With A Watermark

Interviewer is testing: production pipeline thinking.

Question:

Design an incremental load from `source_orders` into a data lake. The source table has `last_updated_at`.

Approach:

- Store the previous successful watermark in a control table.
- Read the old watermark.
- Get the new maximum `last_updated_at` from source.
- Extract records between old and new watermark.
- Write the batch.
- Validate counts and bad records.
- Update the watermark only after success.

SQL sketch:

```sql
-- Old watermark from control table
SELECT watermark_value
FROM etl_watermarks
WHERE pipeline_name = 'orders_incremental_load';

-- New watermark from source
SELECT MAX(last_updated_at) AS new_watermark
FROM source_orders;

-- Incremental extract
SELECT *
FROM source_orders
WHERE last_updated_at > :old_watermark
  AND last_updated_at <= :new_watermark;

-- Update only after successful write and validation
UPDATE etl_watermarks
SET watermark_value = :new_watermark,
    updated_at = CURRENT_TIMESTAMP
WHERE pipeline_name = 'orders_incremental_load';
```

How to explain:

The key is not just filtering by timestamp. The key is when the watermark gets updated. I would update it only after the load writes successfully and validation passes. Otherwise, a failed run could skip data on the next run.

AAIS connection:

At AAIS I worked on recurring data workflows and 24-hour data availability. A watermark pattern is one practical way to keep recurring batch pipelines efficient without reprocessing all historical data every run.

## 8. PySpark Optimization: Slow Join Between Large And Small DataFrames

Interviewer is testing: Spark performance basics.

Question:

A PySpark job joins a large transactions DataFrame with a small lookup DataFrame and runs slowly. How would you optimize it?

Approach:

- Confirm size of both DataFrames.
- Select only needed columns.
- Filter early.
- Broadcast the small lookup table if it fits memory.
- Repartition large data on join key if needed.
- Check for skewed keys.
- Avoid collecting large data to the driver.

Solution sketch:

```python
from pyspark.sql import functions as F

filtered_txn_df = (
    transactions_df
    .filter(F.col("transaction_date") >= F.lit("2026-01-01"))
    .select("company_id", "transaction_id", "amount", "transaction_date")
)

lookup_small_df = company_lookup_df.select("company_id", "company_type")

joined_df = filtered_txn_df.join(
    F.broadcast(lookup_small_df),
    on="company_id",
    how="left"
)
```

How to explain:

If one table is small, broadcasting avoids a large shuffle because each executor gets a copy of the small table. I would still confirm it is actually small enough, because broadcasting a large table can cause memory problems.

AAIS connection:

Because my AAIS data work involved large production datasets, I would approach performance by checking data size, join keys, partitioning, filters, and shuffle-heavy steps rather than guessing.

## 9. Data Quality Checks For A Pipeline

Interviewer is testing: whether you think beyond moving data.

Question:

What data quality checks would you add to an ETL pipeline?

Approach:

Cover four categories:

- Completeness
- Uniqueness
- Validity
- Reconciliation

Answer:

I would add checks at multiple points:

- Null checks on required columns.
- Duplicate checks on business keys.
- Schema checks for expected columns and data types.
- Range checks, such as non-negative amounts or valid dates.
- Referential checks if the data joins to dimensions or lookup tables.
- Source-to-target count checks.
- Aggregate reconciliation, such as total billing amount before and after transformation.
- Bad-record logging with enough context to debug failures.
- Pipeline audit fields like run ID, start time, end time, row counts, and status.

How to explain:

Data quality is not just checking if the job ran. It is checking whether the output is trustworthy for the next system or user.

AAIS connection:

This maps well to AAIS because billing and MDM workflows needed validated, reliable outputs. In a billing context, row counts and total amounts are especially important because small errors can affect member-company charges.

## 10. SCD Type 1 vs. Type 2

Interviewer is testing: data warehousing history handling.

Question:

Explain SCD Type 1 and Type 2. How would you implement Type 2?

Approach:

- Define both types.
- Explain when to use each.
- For Type 2, explain expiring old rows and inserting new rows.
- Mention audit columns.

Answer:

Type 1 overwrites the old value. It is simple and useful when history does not matter.

Type 2 preserves history. When a tracked attribute changes, the current row is expired and a new current row is inserted.

Example columns:

- `business_key`
- tracked attributes such as `customer_name` or `status`
- `effective_date`
- `end_date`
- `is_current`
- `record_hash`

SQL-style sketch:

```sql
-- 1. Expire changed current records
UPDATE dim_customer AS target
SET
  end_date = CURRENT_DATE - INTERVAL '1 day',
  is_current = false
FROM staged_customer AS source
WHERE target.customer_id = source.customer_id
  AND target.is_current = true
  AND target.record_hash <> source.record_hash;

-- 2. Insert new current records
INSERT INTO dim_customer (
  customer_id,
  customer_name,
  status,
  effective_date,
  end_date,
  is_current,
  record_hash
)
SELECT
  source.customer_id,
  source.customer_name,
  source.status,
  CURRENT_DATE,
  DATE '9999-12-31',
  true,
  source.record_hash
FROM staged_customer AS source
LEFT JOIN dim_customer AS target
  ON source.customer_id = target.customer_id
 AND target.is_current = true
WHERE target.customer_id IS NULL
   OR target.record_hash <> source.record_hash;
```

How to explain:

I would use Type 2 when downstream users need to know what was true at a point in time. The hash helps detect whether tracked attributes changed without comparing every column manually.

AAIS connection:

I should not claim I implemented SCD Type 2 unless confirmed. I can connect this concept to MDM: master data often needs clear rules about current trusted values and, in some cases, historical changes.

## 11. Schema Drift In A Pipeline

Interviewer is testing: production debugging and communication.

Question:

A source system adds a new column and changes one column type. Your pipeline starts failing. What do you do?

Approach:

- Identify the failure.
- Compare actual schema to expected schema.
- Classify change as compatible or breaking.
- Apply safe schema evolution only if acceptable.
- Communicate with source/downstream owners.
- Add monitoring so it is caught earlier next time.

Answer:

First I would check the error, logs, and the input schema from the failed run. Then I would compare the actual schema against the expected contract. If a new nullable column was added, that may be compatible and could be handled with schema evolution or an explicit default. If an existing column changed type, that is more dangerous because downstream transformations may break or produce incorrect values. I would not silently cast it without confirming the business meaning.

For prevention, I would add schema validation and alerting before the transformation step, plus a bad-record or quarantine path if the pipeline needs to keep running.

AAIS connection:

At AAIS, profiling 160+ tables across different source systems showed why schema inspection matters. Source systems often differ in naming, types, and meaning, so a pipeline needs validation before trusting the data.

## 12. Explain Your End-To-End AAIS Billing Pipeline

Interviewer is testing: resume depth and whether you can explain real work.

Question:

Walk me through the billing automation project on your resume.

Approach:

- Start with business problem.
- Describe inputs.
- Describe processing.
- Describe outputs.
- Describe validation and impact.
- Avoid unsupported implementation details.

Answer:

At AAIS, the billing workflow was previously manual and SQL-heavy. The goal was to calculate charges for 700+ member companies from production golden-table insurance data. I built automation using Python, PySpark, and AWS Glue so the workflow could run as a repeatable managed data job instead of relying on manual SQL execution.

At a high level, the pipeline read the relevant production data, applied the billing logic, generated company-level charge outputs, and supported validation around the processed results. The scale was 20+ TB, so PySpark and Glue were a better fit than local processing. The value was making the workflow more scalable, repeatable, and maintainable.

If asked for deeper detail:

- Inputs: production golden-table insurance data from enterprise sources.
- Processing: PySpark transformations inside AWS Glue.
- Output: calculated charges for member companies.
- Validation: explain only checks you can defend; safe examples include row counts, aggregate totals, schema checks, and spot checks against expected SQL/manual results.

Strong closing:

The lesson I took from that project is that data engineering is not just moving data. It is understanding the business calculation, making the run repeatable, and validating the output enough that downstream users can trust it.

## 13. Explain Your 160+ Table MDM Profiling Work

Interviewer is testing: data modeling, messy data, migration reasoning.

Question:

What does it mean that you profiled 160+ tables and mapped them into 25 MDM domains?

Approach:

- Define profiling.
- Explain source systems.
- Explain mapping.
- Explain MDM/domain purpose.
- Explain why it mattered.

Answer:

The project involved understanding data across MySQL, Oracle, and Impala tables before migration into a master data management structure. Profiling meant inspecting schemas, columns, data types, row patterns, naming differences, and similarities across source systems using Python, Pandas, SQL, and JDBC.

The goal was to map related source data into a cleaner 25-domain taxonomy for Semarchy MDM. In plain English, instead of treating 160+ legacy tables as isolated objects, we tried to understand how they related to common business domains so the migration could be more maintainable.

Strong closing:

That project taught me that migration is not only a technical load process. The hard part is understanding what the data means across systems and defining a structure that downstream users can trust.

## 14. Full Load vs. Incremental Load vs. Reverse ETL

Interviewer is testing: conceptual clarity.

Question:

Explain full load, incremental load, and reverse ETL.

Answer:

A full load reloads the entire dataset each run. It is simple but expensive and often unnecessary for large datasets.

An incremental load processes only new or changed records since the last successful run. This is usually tracked with a watermark column such as `last_updated_at` or an increasing ID.

Reverse ETL moves curated or processed data back out to operational systems, applications, or users. Traditional ETL moves data into a warehouse or lake; reverse ETL makes trusted data usable outside that central store.

AAIS connection:

At AAIS, my data engineering work included recurring ETL workflows, validation, and reverse-ETL/data access patterns. I would explain that the goal was not only storing data but making validated data available to downstream workflows in a controlled way.

## 15. How To Answer When They Ask About Azure But Your Experience Is AWS

Interviewer is testing: adaptability and honesty.

Question:

Have you worked with ADF, ADLS, Databricks, and Delta Lake?

Answer:

My strongest hands-on production experience is with AWS Glue, S3, PySpark, IAM, and Lambda rather than Azure Data Factory or ADLS. The architecture maps closely, though. Glue handled managed Spark-based ETL, S3 was the durable storage layer, IAM controlled access, and PySpark handled large-scale transformations.

In Azure terms, I understand ADF as the orchestration and copy layer, ADLS as the data lake storage layer, Databricks as the Spark processing layer, and Delta Lake as a table format that supports ACID transactions, schema evolution, time travel, and `MERGE` for upserts. I would be ready to ramp quickly because the pipeline concepts are the same: ingest, transform, validate, store, and serve curated data.

Why this works:

This answer is honest. It does not pretend you used Azure in production, but it shows you understand the data-engineering pattern.

## 16. How To Answer If You Do Not Know A Tool

Interviewer is testing: honesty under pressure.

Question:

Have you used dbt or Airflow?

Answer:

I have not used dbt or Airflow in production. My hands-on orchestration experience is stronger with AWS Glue Workflows, and my transformation experience is stronger with Python, SQL, and PySpark. Conceptually, I understand Airflow as a DAG-based orchestration tool and dbt as a SQL transformation framework focused on modular models, testing, documentation, and lineage. If the role uses those tools, I would connect them to the same fundamentals I have used: dependency ordering, repeatable transformations, validation, and clear handoff to downstream users.

Why this works:

You avoid overclaiming and still show you understand the purpose of the tools.
