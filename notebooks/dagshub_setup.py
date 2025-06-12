import mlflow
import dagshub

mlflow.set_tracking_uri("https://dagshub.com/imakash665/mlops-mini-project.mlflow")
dagshub.init(repo_owner='imakash665', repo_name='mlops-mini-project', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)