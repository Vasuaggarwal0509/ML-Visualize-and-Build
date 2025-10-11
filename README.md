# This is zenml+mlflow  based automated eda visualize and model builder
You can visualize and save plots by handling missing values, outlier detection and removals,univariate analysis,
multivariate analysis,bivariate analysis,etc
# step1. Create a venv and select interpreter(recommended python 3.10)
```
python -m venv venv
```
# step2. check venv must be empty 
venv sometimes copies packages from gloabal env so we need to uninstall packages and make it clean
```
pip freeze | ForEach-Object { pip uninstall -y $_ }
```
# step3. install required packages
```
pip install -r requirements.txt
```
# step4. remove existing zip file and add your zip file
If your zip has multiple csvs then it will use most recent file
so make sure it must have one csv or manage it accordingly.

# step5. Run python command to visualize plots and performing automated EDA 
```
python analysis/eda.py
```
# step6. zenml initialization
Before model building we need to initialize zenml and register experiment_tracker and make the stack active
Sub steps involve
To initialize zenml [it creates a .zenml folder]
```
zenml init
```
To check stacks made by zenml and registered 
```
zenml stack list
```
If there is no regisered mlflow tracker , register it 
```
zenml experiment-tracker register <mlflow_tracker_name> --flavor=mlflow
```
After registering experiment_tracker, register your stack
```
zenml stack register <mlflow_tracker_name> -a local_artifact_store -o local_orchestrator -e mlflow_tracker
```
if you other components exit then it will run but if not then run :
```
zenml artifact-store register local_artifact_store --flavor=local
zenml orchestrator register local_orchestrator --flavor=local
```
Activate the stack [mlflow_stack_name : which you gave by your own in above step]
```
zenml stack set <mlflow_stack_name>
```
Confirm it all worked
```
zenml describe
```
* You should see like this in blocks 
Active stack: my_stack
  Artifact Store: local_artifact_store (flavor: local)
  Orchestrator: local_orchestrator (flavor: local)
  Experiment Tracker: mlflow_tracker (flavor: mlflow)

# Yeahhh!!! now all set .lesgoo.


# step6. Model Building step
Model building step is automated and you just need to take care of hyperparameters though i have used default.
```
python run_pipeline.py
```
To access mlflow dashboard
```
mlflow ui
```
ctrl+click on url shown in powershell
