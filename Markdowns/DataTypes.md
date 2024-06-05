# Overview of Key Data Types for Machine Learning

## Data Types

### Structured Data
Structured data is highly organized and easily searchable in databases using fixed schemas. It is typically stored in tables with rows and columns.

**Examples:**
- Spreadsheets (Excel, CSV)
- SQL Databases

**Characteristics:**
- Defined data types (integer, string, float)
- Easily searchable
- Relational (tables with relationships)

### Unstructured Data
Unstructured data lacks a predefined format or organization, making it more challenging to process and analyze.

**Examples:**
- Text documents
- Images
- Videos
- Audio files

**Characteristics:**
- No fixed schema
- Requires advanced techniques for processing (NLP for text, computer vision for images)

### Time-Series Data
Time-series data is a sequence of data points collected or recorded at specific time intervals.

**Examples:**
- Stock prices
- Weather data
- Sensor readings

**Characteristics:**
- Temporal dependency (order of data points matters)
- Often requires specialized techniques (e.g., ARIMA, LSTM)

## Data Factors

### Missing Data
Missing data occurs when some values are not recorded. It can lead to biased results if not handled properly.

**Types of Missing Data:**
- Missing Completely at Random (MCAR): No pattern in missing data.
- Missing at Random (MAR): Missing data is related to observed data.
- Missing Not at Random (MNAR): Missing data is related to unobserved data.

**Handling Techniques:**
- Deletion (listwise or pairwise)
- Imputation (mean, median, mode, regression, KNN)

### Continuous vs. Categorical Data

**Continuous Data:**
Continuous data can take any value within a range. It is often associated with measurements.

**Examples:**
- Height
- Weight
- Temperature

**Characteristics:**
- Infinite possibilities within a range
- Represented by real numbers

**Categorical Data:**
Categorical data represents discrete values or categories. It can be further divided into nominal and ordinal data.

**Examples:**
- Nominal: Gender, Colors
- Ordinal: Education level, Satisfaction rating

**Characteristics:**
- Finite set of values
- No inherent order (nominal) or ordered (ordinal)

## Conclusion
Understanding different data types and factors is crucial for selecting appropriate machine learning techniques and handling data effectively. Structured and unstructured data, time-series data, handling missing data, and distinguishing between continuous and categorical data are key considerations for developing valid statistical models.