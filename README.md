# Datadog-Python-Flask
This python backend application demonstrates the capability of Datadog in terms of Application Performance Management(APM). 

* The Metrics and Traces from this backend application will be polled by a Datadog container application, which sends all these details to the Datadog portal for creation of       interactive Dashboards.

# Please find the installation and execution instructions below

  1. Pull the Datadog Docker Image for Agent and run it in your localhost. The commands are mentioned below.

      docker run -d `
     -p 127.0.0.1:8126:8126/tcp `
     -e "DD_API_KEY=<Your Datadog API Key" `
     -e "DD_APM_ENABLED=true" `
     -e "DD_SITE=<Your Datadog Sitename>" `
     -e "DD_HOSTNAME=myhostname"
     gcr.io/datadoghq/agent:latest


  2. Run the Python application using the below command

     ddtrace-run python app.py 
