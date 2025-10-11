import click # type: ignore
from pipelines.training_pipeline import ml_pipeline
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri # type: ignore

strategy_class = None
@click.command()
def main():
    """
    Run the ML pipeline and start the MLflow UI for experiment tracking.
    """
    # Run the pipeline
    if strategy_class is None:
        raise ValueError("No strategy class provided.")
    run = ml_pipeline(strategy_class)

    # You can uncomment and customize the following lines if you want to retrieve and inspect the trained model:
    # trained_model = run["model_building_step"]  # Replace with actual step name if different
    # print(f"Trained Model Type: {type(trained_model)}")

    print(
        "Now run \n "
        f"    mlflow ui --backend-store-uri '{get_tracking_uri()}'\n"
        "To inspect your experiment runs within the mlflow UI.\n"
        "You can find your runs tracked within the experiment."
    )


if __name__ == "__main__":
    print(
    """
    1. Linear Regression
    2. SVR
    3. Decision Tree Regressor
    4. Random Forest Regressor
    5. XGBoost Regressor
    """)
    strategy = input("Enter the regression model to use (1-5): ")
    model_options = {
        "1": "linear_regression",
        "2": "svr",
        "3": "decision_tree",
        "4": "random_forest",
        "5": "xgboost",
    }
    if strategy not in model_options:
        raise ValueError("Invalid option. Please choose a number between 1 and 5.")
    strategy_class = model_options[strategy]
    main()

# to start this use zenml init then register stack using notepad code and then active the stack then run python file