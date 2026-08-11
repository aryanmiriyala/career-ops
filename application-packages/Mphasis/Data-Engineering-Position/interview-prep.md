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
