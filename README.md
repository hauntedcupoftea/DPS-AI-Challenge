# DPS AI Engineer Challenge

This repository contains code for my work submitted as part of the selection process for the DPS 2025 March batch.
All work is my own.

## The Problem

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

From these, we can make a relative simple and effective Prophet model that can be runed with hyperparameter tuning. For the sake of experimentation, I have also included some other model's results on test data, which performed significantly wrose. The deployed endpoint uses just prophet. The code for the specific param_grid can be found [here](/experimentation/model_training.ipynb), which wasn't expanded further due to time limitations. (The output of that cell has been disabled to remove excessive spam logs).

The prophet model was created with cross-validation on the dataset, with a horizon of 1 year. This means that one param was trained on 20 windows of the dataset. The testing metrics are all derived from data after 2020, in the same dataset. The dataset file has been removed, but the folder is kept in case the dataset is ever updated and this model needs to be trained by anyone else.

The prophet plot of the model on training data looks like this:

![Figure 5: Prophet plot of the training data](/img/prophet_train_plot.png)

While on unseen ground truth data, it outperformend all the other models significantly.

![Figure 6: Prophet plot of all the data](/img/prophet_test_plot.png)

### Task 2: Publishing & Deploying application

Configuring a project with poetry makes it relatively simple to dockerize and deploy an application. A simple FastAPI application can be created to serve 3 endpoints. Docs for the project can be seen [here](https://dps-ai-challenge-ys81.onrender.com/docs/)

1. Forecast (try it out by sending a POST request [here](https://dps-ai-challenge-ys81.onrender.com/forecast/)!)

    According to the challenge requirements.

    ![Figure 7: Forecasting Endpoint Postman Test](/img/forecast.png)

2. Model Performance (see response [here](https://dps-ai-challenge-ys81.onrender.com/model/performance))
    A simple get request that returns the statistics for the current model. This is made in case I ever add an MLOps pipeline to this project that watches the dataset and updates the model whenever the dataset is updated, but will return a static response for now.

3. Model Params (see response [here](https://dps-ai-challenge-ys81.onrender.com/model/hyper-params))
    Another static get request that returns the best params from the hyperparameter tuning. Also part of the MLOps pipeline, which returns a static response for now.

### Deployment

#### Render

The project is curently hosted on [Render](https://render.com), at the URL attached to the top of the repository. It currently runs inside a docker container. Please note that render spins down containers with inactivity, so your first load/request might take some time (~1 minute) to respond. However, subsequent responses will be at full speed for a while.

#### Self-Hosting

The project is bundled with poetry and can be self hosted should one wish, with a simple poetry command.
After installing poetry itself, if need be, install all dependencies with

```sh
poetry install
```

Then host the local server with

```sh
poetry run start
```

...And go to [http://localhost:8000](http://localhost:8000) to view and interact with the local API.

### Task 3: Submitting the Challenge

The final submission of the project as done at `Sat, 30 Nov 2024 10:38:10 GMT` and can be verified below.

![Figure 8: Task 3 Submission](/img/task3.png)
