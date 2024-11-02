# Evaluating Naive Probabilistic Forecasts

This project focuses on evaluating naive probabilistic forecasts using the GEFCOM dataset, which includes data on zonal prices and system loads. The aim is to generate prediction intervals and assess the empirical coverage of these forecasts.

## Project Overview

The project consists of the following key tasks:

1. **Naive Forecasting**:
   - Use forecasts from the naive #1 model to calculate 50% and 90% prediction intervals for the period from days 366 to 1082. A fixed 365-day calibration window is employed, treating each hour separately.

2. **Empirical Coverage Calculation**:
   - Calculate the empirical coverage of the obtained probabilistic forecasts to assess the reliability of the prediction intervals.

3. **Rolling Calibration Window**:
   - Repeat the above tasks using a rolling 365-day calibration window and compare the results with those obtained from the fixed calibration window.

4. **Advanced Forecasting Models**:
   - Implement forecasts from the sparse AR7 and ARX models to calculate 50% and 90% prediction intervals for days 366 to 1082, again using the 365-day rolling calibration window and treating each hour separately.

5. **Performance Metrics**:
   - Calculate performance metrics for the probabilistic forecasts, including empirical coverage, pinball score, and Winkler score.

6. **Comparison of Results**:
   - Compare the results obtained from the advanced models with those from the naive method applied in task 3 to evaluate the effectiveness of the different forecasting approaches.

## Data

The project utilizes the GEFCOM dataset, which includes columns for date (YYYYMMDD), hour (HH), zonal price, system load, zonal load, and the day of the week. This dataset provides a basis for evaluating various forecasting methods and their performance.

## Results

The outputs of the project include prediction intervals, empirical coverage calculations, and performance metrics for the different forecasting methods, facilitating a comprehensive comparison of their effectiveness.

