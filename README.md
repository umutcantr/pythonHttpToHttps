# Http/Https Proxy
Simple Flask based web server/proxy that redirects http/https post request to https post request. İf you have İoT system and cannot do https request becasuse of system limits or outdated ssl/tls version, you can use this simple server to do https request to any server like Firebase.
# Usage
* You should edit "url" variable to select which server you want to https request.
* After deploying the code to server, you can request http get to the web server for see server is running; You return "Hello, you requested." 
* For testing the web server you can use this [site](https://reqbin.com/).
* Finally you can do request http post. Successful request return Http 201 status code.
# Deploy
You can deploy code google cloud without need any own web server set up. 
* For deploy the code to the google cloud [follow this](https://cloud.google.com/run/docs/quickstarts).
* Also you can refer [this sample](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/db182f77a0d29dd1ee6e20516d96db8b3b72684e/appengine/standard_python3/custom-server) for deploying the code google cloud.

