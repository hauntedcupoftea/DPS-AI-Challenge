# DPS AI Engineer Challenge

This repository contains code for my work submitted as part of the selection process for the DPS 2025 March batch.
All work is my own.

## Task

The task at hand was to create a forecasting model with an API endpoint that operates on the following schema:
Request:

```json
{
    "year": 2020,
    "month": 10
}
```

Response:

```json
{
    "prediction": "value"
}
```

## My implementation

My implementation of the project runs on Docker, using fastAPI and [Prophet](https://facebook.github.io/prophet/) to forecast accident values.
The statistics of the final forecaster are as follows:

```txt
Test Data Results
Mean Absolute Error: 7.863451865241231,
Root Mean Square Error: 9.552909667483597,
R2 Score: 0.5537502048161292
```

Note: These results have been generated on unseen data, using the rows after 2020 as instructued in the challenge guidelines.

## Tasks

### Task 1: Visualiation, EDA, and Model Creation

The Exploratory data analysis for the project can be found [here](/experimentation/EDA.ipynb).
It contains all the code that was used to create the visualisations as seen throughout this README.
The first visualization mentioned in the challenge was to plot all accident values grouped by the category (column 1).
There were two feasible ways of doing this. The first was a stacked bar chart for the entire time-series and the second being line charts for each category. Both can be found below.

![Figure 1: Plotting accident values by category](/img/stacked_bar_and_line.png)

Further analysis of the data can result in the following visualizations:

1. A closer look at the value of Alkoholunfälle accidents (since the values are relatively too small to see in the full plot).

    ![Figure 2: Plotting just the data in question](/img/value_over_time.png)

2. Since the task is to forecast predictions based on year and month alone, we can create a plot to see their correlation. This helps us understand relationships between the three variables.

    ![Figure 3: Correlation heatmap of all important variables](/img/correlation_heatmap.png)

3. Finally, a distribution of the target variable (y) shows that the data is relatively normal, and does not need to be normalized in pre-processing (as well as in the pipeline).

    ![Figure 4: A distribution curve of y](/img/y_distribution.png)

From these, we can make a relative simple and effective Prophet model that can be runed with hyperparameter tuning. The code for the specific param_grid can be found [here](/experimentation/model_training.ipynb), which wasn't expanded further due to time limitations. (The output of that cell has been cleared to remove logs that are no longer useful).

The prophet model was created with cross-validation on the dataset, with a horizon of 1 year. This means that one param was trained on 20 windows of the dataset. The testing metrics are all derived from data after 2020, in the same dataset. The dataset file has been removed, but the folder is kept in case the dataset is ever updated and this model needs to be trained by anyone else.

The prophet plot of the model looks like this:

![Figure 5: Prophet plot of the model](/img/prophet_plot.png)

### Task 2: Publishing & Deploying application

Configuring a project with poetry makes it relatively simple to dockerize and deploy an application. A simple FastAPI application can be created to serve 3 endpoints. Docs for the project can be seen [here](https://dps-ai-challenge-ys81.onrender.com/docs/)

1. Forecast (try it out by sending a POST request [here](https://dps-ai-challenge-ys81.onrender.com/forecast/)!)

    According to the challenge requirements.

    ![Figure 6: Forecasting Endpoint Postman Test](/img/forecast.png)

2. Model Performance (see response [here](https://dps-ai-challenge-ys81.onrender.com/model/performance))
    A simple get request that returns the statistics for the current model. This is made in case I ever add an MLOps pipeline to this project that watches the dataset and updates the model whenever the dataset is updated, but will return a static response for now.

    ![Figure 7: Model Performance](/img/performance.png)

3. Model Params (see response [here](https://dps-ai-challenge-ys81.onrender.com/model/hyper-params))
    Another static get request that returns the best params from the hyperparameter tuning. Also part of the MLOps pipeline, which returns a static response for now.

    ![Figure 8: Model Hyperparameters](/img/hyper-params.png)
