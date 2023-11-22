# How to Create an HTTPS Certificate for Azure Container Instance using Let's Encrypt

Deploy [this image](https://hub.docker.com/repository/docker/liamca/aci-lets-encrypt/general) to the container instance you wish to create the certificate for. Here is an example of an AZ command (enter valid values for resource group, domain name and region)

```
az container create --resource-group <RESOURCE_GROUP> --name <DOMAIN_NAME> --image liamca/aci-lets-encrypt --cpu 1 --memory 4 --dns-name-label <DOMAIN_NAME> --ports 80 --location
```

Then download certbot (https://certbot.eff.org/) to your local computer and run the following (from a command prompt with Administrator access) replacing the Domain Name and the region:

```
certbot certonly --manual -d <DOMAIN_NAME>.<AZURE_REGION>.azurecontainer.io
```

This will give you the challenge response string that needs to be added to this Azure Container Instance. From a browser enter this challenge response string to: 

```
http://<DOMAIN_NAME>.<AZURE_REGION>.azurecontainer.io/save_challenge/<CHALLENGE_STRING>
```

You should see a message indicating it saved the challenge response string.

Go back to the certbot process and press <ENTER> to let certbot validate your challenge response string

Make note of the location where the certificate and keys are stored.

At this point you can delete the Azure Container Instance.
