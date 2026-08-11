# Mphasis Data Engineering Interview Prep

Date researched: 2026-08-11

## Source Reliability Note

These notes are based on public candidate-report and interview-prep sources, not an official Mphasis interview rubric. Treat them as preparation signals. The exact referred role may differ by client, location, and level.

Sources checked:

- Glassdoor Mphasis interview page, updated August 2026: https://www.glassdoor.com/Interview/Mphasis-Interview-Questions-E29275.htm
- Dataford Mphasis Data Engineer guide, updated July 2026: https://dataford.io/interview-guides/mphasis/data-engineer
- InterviewQuery Mphasis Data Engineer guide, published March 2026: https://www.interviewquery.com/interview-guides/mphasis-data-engineer
- AmbitionBox Mphasis Data Engineer fresher interview page, updated April 2025: https://www.ambitionbox.com/interviews/mphasis-interview-questions/data-engineer/fresher-candidates
- LinkedIn candidate/prep posts about Mphasis data engineering interviews, crawled in 2026.
- User-provided LinkedIn post by Ranjit about Mphasis data engineering interview questions: https://www.linkedin.com/posts/ranjit-a873ba243_mphasis-data-engineering-interview-questions-ugcPost-7446583227869245440-8k0Q/
- LinkedIn posts surfaced by web search that repeat Mphasis-tagged data engineering interview themes around ADF, ADLS, Databricks, Delta Lake, SQL window functions, PySpark optimization, schema drift, and production pipeline debugging.
- Official concept references checked for calibration: Spark Structured Streaming watermarking, Microsoft Azure Data Factory watermark-based incremental copy, PostgreSQL window functions, and Databricks Delta Lake `MERGE`.

## What To Expect

Likely interview shape:

- Recruiter or referral screen about role fit, availability, location, experience, and compensation.
- One or two technical rounds, often direct and practical.
- Possible client interview because Mphasis is an IT services / consulting company.
- HR round after technical fit.

Likely technical focus:

- SQL query writing, especially joins, aggregations, window functions, ranking, duplicates, and query optimization.
- PySpark syntax, DataFrame operations, transformations vs. actions, joins, deduplication, null handling, repartitioning, and performance basics.
- ETL/ELT concepts, data quality checks, pipeline debugging, batch loads, incremental loads, and late-arriving data.
- Data warehousing and data modeling: fact/dimension tables, star vs. snowflake schema, SCD Type 1 vs. Type 2.
- Cloud and big-data stack: AWS/Azure, S3/ADLS, Glue/ADF, Spark/Databricks, data lakes, partitioning, orchestration, and pipeline monitoring.
- Resume deep dives, especially previous data engineering projects.

## Learning Map By Priority

### Tier 1 - Must Know Cold

These are the topics most consistently repeated across Mphasis-specific or Mphasis-tagged reports.

#### SQL Window Functions

Know:

- `ROW_NUMBER()`: unique sequence per partition, useful for deduping by keeping the latest row.
- `RANK()`: gives tied rows the same rank and leaves gaps.
- `DENSE_RANK()`: gives tied rows the same rank without gaps.
- `LAG()`: looks at a previous row in the ordered window, useful for month-over-month or before/after comparisons.
- `LEAD()`: looks at a following row.

Practice:

- Second-highest salary per department.
- Top 3 salaries per department with ties.
- Month-over-month growth with `LAG()`.
- Deduplicate records by business key using `ROW_NUMBER()`.

AAIS connection:

Use this when discussing table profiling, billing validation, or source-to-target checks. You do not need to claim you used `LAG()` at AAIS unless you did; say you used SQL for profiling and validation, and that window functions are a natural way to solve ranking, dedupe, and trend-analysis questions.

#### Incremental Loads And Watermarks

Know:

- A full load copies all data every run.
- An incremental load copies only new or changed data since the last successful run.
- A watermark is the saved high-water mark from the previous run, often a timestamp or increasing ID.
- A control/watermark table stores the last processed value.
- The next run reads rows greater than the old watermark and up to the new maximum watermark.
- After a successful run, update the stored watermark.

Practice answer:

For a batch pipeline, I would choose a reliable `last_updated_at` or increasing ID as the watermark column, store the last processed value in a control table, query only rows where the watermark column is greater than the old value and less than or equal to the current max, validate the load, then update the control table only after success.

AAIS connection:

Connect this to the 24-hour data latency and recurring workflow language. Say your AAIS work involved repeatable production data availability, and you understand that a watermark pattern is how many batch ETL systems avoid expensive full reloads.

#### PySpark DataFrame Syntax

Know exact syntax for:

- `spark.read.option(...).csv(...)`
- `select`, `filter`, `where`
- `withColumn`
- `dropDuplicates`
- `groupBy().agg(...)`
- joins
- null handling with `isNull`, `isNotNull`, `fillna`
- `when(...).otherwise(...)`
- `to_timestamp`
- window functions with `Window.partitionBy(...).orderBy(...)`

Practice:

- Remove duplicates by key while keeping the latest record.
- Add a risk/category column with `when().otherwise()`.
- Join two DataFrames and aggregate results.
- Read malformed CSV data and route bad rows.

AAIS connection:

Use the billing workflow as the anchor: PySpark was the right tool because the data size was production-scale and Glue could run Spark processing in a managed environment.

#### PySpark Optimization

Know:

- Filter early and select only needed columns.
- Avoid unnecessary `collect()` on large data.
- Use broadcast joins when one table is small enough to send to executors.
- Repartition by join key before large joins when useful.
- Use `coalesce()` to reduce partitions after filtering.
- Understand data skew and why one partition can become much slower than others.
- AQE means Adaptive Query Execution, where Spark can adjust parts of the physical plan at runtime.

AAIS connection:

You can say you worked with large-scale PySpark/Glue workflows and are prepared to reason through optimization by checking data size, partitioning, joins, filters, and shuffle-heavy steps. Do not overclaim deep Spark cluster tuning unless asked; answer from principles.

### Tier 2 - Very Likely If Role Is Azure/Databricks Or Client-Facing

These were common in Mphasis-tagged LinkedIn posts. They may matter more if the client stack is Azure.

#### ADF / ADLS / Databricks Pipeline Shape

Know:

- ADF: orchestration and data movement.
- ADLS: Azure Data Lake Storage, similar role to S3 for lake storage.
- Databricks: Spark-based processing platform.
- Delta Lake: storage layer/table format with transaction log, schema evolution, time travel, and `MERGE` support.
- Power BI/Synapse: consumption/reporting/warehouse layer.
- Bronze/Silver/Gold: raw, cleaned/conformed, curated/business-ready layers.

How to answer without Azure production experience:

I have stronger hands-on AWS Glue/S3/PySpark experience, but the architecture maps well. In AWS I used Glue for managed Spark ETL and S3 for durable pipeline outputs. In Azure terms, ADF would orchestrate/copy, ADLS would store raw and curated files, Databricks would run Spark transformations, and downstream BI/warehouse tools would consume the curated layer.

#### Delta Lake `MERGE` / UPSERT

Know:

- `MERGE` updates existing rows and inserts new rows based on a match condition.
- Useful for incremental loads, SCD Type 2, deduped updates, and CDC-style processing.
- You must prevent ambiguous matches where multiple source rows match one target row.

Practice answer:

For incremental data, I would dedupe the incoming source by business key and latest timestamp first, then `MERGE` into the target. Matched rows get updated, unmatched rows get inserted, and the job updates audit columns or control-table state after validation.

#### SCD Type 1 vs Type 2

Know:

- Type 1 overwrites history. Good when only the current value matters.
- Type 2 preserves history by expiring the old row and inserting a new current row.
- Typical columns: `effective_date`, `end_date`, `is_current`, maybe a hash for change detection.

AAIS connection:

Use the MDM migration story. You can say MDM/data-domain work made you familiar with the need for stable business entities and history decisions, even if your resume does not claim you implemented SCD Type 2 directly.

#### Schema Drift

Know:

- Schema drift means source columns/types change unexpectedly.
- Risks: failed loads, missing data, bad downstream models.
- Response: validate schema, allow safe schema evolution only where appropriate, default new nullable columns, alert on breaking changes, document/communicate contract changes.

AAIS connection:

Tie this to profiling 160+ tables across systems. Different source systems rarely align perfectly; schema inspection and mapping are the first defense.

### Tier 3 - Good To Know, But Do Not Overclaim

- Azure Data Factory Mapping Data Flows.
- ADLS ACLs and Managed Identity.
- Databricks job scheduling.
- Delta Lake time travel and vacuum.
- Kafka streaming design.
- Airflow and dbt.
- Snowflake virtual warehouses, micro-partitions, clustering, and time travel.
- Power BI filters/reporting.

Use these only if the interviewer asks conceptually or if the exact JD mentions them. Be direct about hands-on depth: stronger in AWS Glue/S3/PySpark/SQL; conceptually familiar with Azure/Databricks patterns.

## Highest-Priority Questions To Practice

Worked examples with approaches and sample solutions are included below in this document.

### SQL

- Write a query to find the second-highest salary overall and per department.
- Explain `RANK()` vs. `DENSE_RANK()` vs. `ROW_NUMBER()`.
- Find duplicate records in a table and keep only the latest row per business key.
- Write month-over-month growth using `LAG()`.
- Explain `UNION` vs. `UNION ALL`.
- Explain inner, left, right, full outer, cross, and self joins.
- Explain `GROUP BY` vs. `HAVING`.
- Optimize a slow query joining two large tables.
- Explain when indexes help and when they do not.

AAIS answer anchor:

Use the 160+ table profiling and MDM migration story. Say you used SQL to inspect source-table structures, validate outputs, compare cross-system patterns, and support mapping into cleaner MDM domains.

### PySpark / Spark

- Drop duplicate rows in a PySpark DataFrame based on specific columns.
- Add a conditional column using `when().otherwise()`.
- Convert a string column to a timestamp.
- Group by a column and calculate max/count/sum.
- Read CSV data with schema inference and bad-record handling.
- Explain transformations vs. actions and lazy evaluation.
- Explain `repartition()` vs. `coalesce()`.
- Explain broadcast joins and when to use them.
- Explain how to handle skewed data.
- Explain how to debug a failed Spark job.

AAIS answer anchor:

Use the 20+ TB billing workflow. Say PySpark was appropriate because the billing data was too large for local/Pandas-style processing, and Glue let the job run as a managed Spark-based workflow.

### ETL / Pipeline Design

- Describe an ETL pipeline you built.
- Explain full load vs. incremental load.
- How would you design an incremental load with a watermark?
- How do you handle late-arriving data?
- What data quality checks do you add?
- How do you log failures and bad records?
- How do you validate source-to-target counts?
- How do you decide file partitioning?

AAIS answer anchor:

Use billing automation, Pentaho-to-Glue modernization, reverse ETL, and validation workflows. Keep the story practical: extract from enterprise sources, transform with business logic, store in S3/MDM-ready structures, validate outputs, and control access.

### Data Modeling / Warehousing

- What is a fact table?
- What is a dimension table?
- Star schema vs. snowflake schema.
- SCD Type 1 vs. Type 2.
- What is MDM and why does it matter?
- What is a data lake vs. a data warehouse?
- Why are Parquet/columnar formats useful for big data?

AAIS answer anchor:

Use the 25-domain MDM migration. Explain that MDM is about creating trusted, standardized views of important business entities across systems. Your role was profiling and mapping messy source tables into a maintainable domain taxonomy.

### Cloud / AWS / Security

- What did you use AWS Glue for?
- What is S3's role in data pipelines?
- What is IAM and why is it important?
- What is Lambda useful for in data engineering?
- How do you secure sensitive data in a pipeline?
- How do you explain PII tokenization?

AAIS answer anchor:

Use Glue for ETL orchestration, S3 for durable pipeline outputs, IAM for controlled access, Lambda for event-driven validation, and hashing/tokenization for safer handling of PII before downstream movement.

## Resume Deep-Dive Answers To Prepare

### Billing Automation

Short answer:

At AAIS, I automated a manual SQL billing workflow using Python, PySpark, and AWS Glue. The pipeline processed 20+ TB of golden-table insurance data and calculated charges for 700+ member companies. The main value was making the workflow repeatable, scalable, and less dependent on manual SQL execution.

Follow-up details to know:

- What were the inputs?
- What business rules determined charges?
- How did you validate counts, totals, or output correctness?
- What made PySpark/Glue better than manual SQL?
- How would you improve the pipeline now?

### 160+ Table Profiling / MDM Migration

Short answer:

I profiled 160+ MySQL, Oracle, and Impala tables using Python, Pandas, SQL, and JDBC. The goal was to understand source-system relationships and map similar fields into a 25-domain MDM taxonomy so the migration could be more maintainable.

Follow-up details to know:

- How did you compare source tables?
- What kinds of schema or naming differences appeared?
- How did you decide two fields were similar?
- What did the 25-domain taxonomy represent?
- How did this support Semarchy MDM?

### Pentaho To AWS Glue

Short answer:

AAIS had many legacy Pentaho ETL jobs. I helped replace 160+ of those workflows with AWS Glue ETL jobs and partitioned S3 pipelines for Semarchy MDM. The benefit was more maintainable, cloud-native data movement.

Follow-up details to know:

- What did Pentaho do in the old process?
- How did Glue jobs differ from the legacy jobs?
- Why partition S3 outputs?
- How did Semarchy consume or use the outputs?

### Reverse ETL / Validation / IAM

Short answer:

I worked on reverse-ETL and validation workflows where processed data needed to be made available back to downstream users or systems. IAM roles helped control who or what could access the data, and validation helped reduce manual errors and support 24-hour latency.

Follow-up details to know:

- What data moved back downstream?
- What validation checks ran?
- What did IAM restrict?
- What did 24-hour latency mean operationally?

### Software Internship SQL Generation

Short answer:

In my earlier AAIS software internship, I used Python and JSON-based generation logic to parse insurance taxonomies and generate 1,000+ production SQL tables across MySQL, Oracle, PostgreSQL, and 10+ insurance lines. That helped standardize data-model delivery instead of manually creating each table.

Follow-up details to know:

- What was the input JSON/taxonomy structure?
- How did the script generate table definitions?
- How did you handle database-specific SQL differences?
- How did you validate generated SQL?

## One-Week Prep Order

1. SQL window functions, joins, duplicates, CTEs, ranking, and query optimization.
2. PySpark DataFrame syntax: read, select, filter, withColumn, groupBy, joins, dropDuplicates, null handling.
3. ETL storytelling from AAIS: billing automation, MDM profiling, Pentaho-to-Glue, reverse ETL.
4. Data modeling: fact/dimension, star/snowflake, SCD, MDM, data lake vs. warehouse.
5. Cloud/AWS: Glue, S3, IAM, Lambda, partitioning, validation, security.
6. Mock interview: answer each AAIS resume bullet out loud in 60-90 seconds.

## Questions To Ask Mphasis

- Is this role tied to a specific client or internal Mphasis data platform team?
- What is the main stack: AWS Glue/Spark, Azure Data Factory/Databricks, Snowflake, dbt, Airflow, or something else?
- Is the work mostly migration, batch ETL, streaming, data warehousing, or analytics enablement?
- How much of the role is SQL/PySpark development versus orchestration/support?
- What does a successful first 90 days look like for this data engineering role?

## Worked Practice Questions

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
