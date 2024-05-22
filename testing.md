# Testing Dashboard Functions

This document describes the unit tests for the `dashboard` module functions: `select_subject`, `select_date_range`, and `select_resolution`. 
The tests are written using Python's `unittest` framework.

## Overview

The `test_dashboard.py` script contains unit tests for the following functions in the `src.dashboard` module:

- `select_subject`
- `select_date_range`
- `select_resolution`

These functions are used to filter and manipulate a DataFrame for a hypothetical dashboard application.

## Test Cases

### Test `select_subject`

**Functionality**: This function filters a DataFrame to include only the specified subjects.

**Test Case**: 
- **Purpose**: To ensure the function correctly filters the DataFrame based on a list of subject IDs.
- **Setup**:
  - Create a test DataFrame `test_df` with an 'Id' column.
  - Define a list of subject IDs `test_subject` to filter.
- **Execution**: Call `select_subject(test_df, test_subject)`.
- **Assertion**: Verify that the resulting DataFrame contains only the rows with the specified subject IDs.

### Test `select_date_range`

**Functionality**: This function filters a DataFrame to include only the rows within a specified date range.

**Test Case**:
- **Purpose**: To ensure the function correctly filters the DataFrame based on a date range.
- **Setup**:
  - Create a test DataFrame `test_df` with a 'DateTime' column.
  - Define a start date `test_start_date` and an end date `test_end_date` for the range.
- **Execution**: Call `select_date_range(test_df, test_start_date, test_end_date)`.
- **Assertion**: Verify that the resulting DataFrame contains only the rows within the specified date range.

### Test `select_resolution`

**Functionality**: This function aggregates the data in a DataFrame based on a specified time resolution (e.g., hourly).

**Test Case**:
- **Purpose**: To ensure the function correctly aggregates the DataFrame based on the specified resolution.
- **Setup**:
  - Create a test DataFrame `test_df` with 'Id', 'DateTime', and 'Steps' columns.
  - Define the resolution `test_resolution` to aggregate by (e.g., 'Hours').
- **Execution**: Call `select_resolution(test_df, test_resolution)`.
- **Assertion**: Verify that the resulting DataFrame correctly aggregates the 'Steps' data based on the specified resolution.

