# Weather ETL Pipeline with Python & PostgreSQL

## Project Overview

This project implements a complete **ETL (Extract -- Transform -- Load)
data pipeline** designed to teach the fundamentals of **Data
Engineering** through a real-world use case: weather data processing.

The pipeline collects real-time and forecast weather data from
**WeatherAPI**, cleans and standardizes the raw data, and loads it into
a **PostgreSQL** database for storage and analysis.

This project focuses on **learning-by-doing** and emphasizes clean
architecture, robustness, and industry best practices.

------------------------------------------------------------------------

## Learning Objectives

By completing this project, you will learn how to: - Design a complete
ETL pipeline from scratch - Extract data from an external REST API -
Handle API errors, rate limits, and unreliable networks - Transform raw
JSON data into clean, structured datasets - Design and populate a
relational database (PostgreSQL) - Separate configuration, logic, and
secrets properly - Build a reusable and maintainable data pipeline

------------------------------------------------------------------------

## Tech Stack

-   Python
-   WeatherAPI (REST API)
-   PostgreSQL
-   Pandas
-   psycopg2 / SQLAlchemy
-   dotenv
-   YAML
-   Logging

------------------------------------------------------------------------

## ETL Architecture Overview

    WeatherAPI → API Client → Raw Data → Transform → Clean Data → PostgreSQL
         (E)                          (T)                     (L)

------------------------------------------------------------------------

## Step-by-Step Project Execution

### Step 1 --- Define the Pipeline Scope

**Goal:** Clearly define what the pipeline will do.

Tasks: - Choose WeatherAPI as the data source - Decide which endpoints
to use (current weather, forecast) - Define the list of cities - Decide
execution frequency (hourly, daily) - Create project structure - Prepare
configuration files (`config.yaml`, `.env`)

Deliverables: - Project structure - Configuration files - Clear
understanding of pipeline behavior

------------------------------------------------------------------------

### Step 2 --- Build the API Client (Extract)

**Goal:** Reliably fetch data from WeatherAPI.

Tasks: - Load API key securely from `.env` - Build request URLs
dynamically - Send HTTP requests with timeouts - Handle network errors
and HTTP status codes - Implement retries with backoff - Validate API
responses - Return clean raw JSON data

Deliverables: - Reusable WeatherAPI client - Robust error handling -
Logged API interactions

------------------------------------------------------------------------

### Step 3 --- Data Ingestion

**Goal:** Collect and store raw data.

Tasks: - Loop through all configured cities - Call the API client - Save
raw JSON responses to `data/raw/` - Timestamp each dataset - Log
successful and failed fetches

Deliverables: - Raw weather data files - Ingestion logs

------------------------------------------------------------------------

### Step 4 --- Data Transformation

**Goal:** Clean and standardize raw data.

Tasks: - Parse nested JSON structures - Convert temperature units -
Normalize city and country names - Handle missing or invalid values -
Convert timestamps to standard formats - Output clean Pandas DataFrames

Deliverables: - Clean, structured datasets - Transformation logic

------------------------------------------------------------------------

### Step 5 --- Database Design

**Goal:** Prepare PostgreSQL for loading data.

Tasks: - Design relational schema - Create tables for locations, current
weather, forecasts - Define primary and foreign keys - Add indexes for
performance

Deliverables: - SQL schema file - Running PostgreSQL database

------------------------------------------------------------------------

### Step 6 --- Load Data into PostgreSQL

**Goal:** Store transformed data safely.

Tasks: - Establish database connection - Insert data using
transactions - Avoid duplicate records - Handle load failures gracefully

Deliverables: - Populated PostgreSQL tables - Load logs

------------------------------------------------------------------------

### Step 7 --- Pipeline Orchestration

**Goal:** Run the ETL as a single workflow.

Tasks: - Create a pipeline orchestrator - Run Extract → Transform → Load
sequentially - Add global error handling - Enable CLI execution

Deliverables: - Executable pipeline script

------------------------------------------------------------------------

### Step 8 --- Automation & Scheduling

**Goal:** Run the pipeline automatically.

Tasks: - Schedule pipeline with cron or Task Scheduler - Parameterize
run modes (hourly/daily) - Monitor execution

Deliverables: - Automated ETL pipeline

------------------------------------------------------------------------

### Step 9 --- Logging & Monitoring

**Goal:** Observe pipeline health.

Tasks: - Add structured logging - Track execution time and errors -
Monitor API usage - Prepare data for dashboards

Deliverables: - Logs - Monitoring-ready pipeline

------------------------------------------------------------------------

## Project Outcomes

After completing this project, you will have: - A production-style ETL
pipeline - Hands-on experience with APIs and databases - A strong
foundation in Data Engineering - A portfolio-ready project

------------------------------------------------------------------------

## Future Improvements

-   Add Airflow or Dagster
-   Add data quality checks
-   Create dashboards (Metabase, Grafana)
-   Add historical data ingestion
