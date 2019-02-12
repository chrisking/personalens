# Integrating Amazon Personalize with Django

Now that your campaign is active it is time to update your local installation of Django
to interact with it.

This is managed via the `personalens\settings.py` file in your Cloud9 environment.

Open it and scroll to the bottom until you find:

```python3
CAMPAIGN_ARN = None
```

Change this to:

```python3
CAMPAIGN_ARN = "arn:aws:personalize:us-east-1:059124553121:campaign/
```

Replacing the value to be the Campaign ARN from the notebook you just finished.

Finally save the file. Now your interactions with the application will show recommendations
powered by Amazon Personalize.

For a sample visit the application and click on any user to see their recommendations.

The final portion of this workshop will focus on enabling click stream events that allow
for you to define a session for the user and then generate even more focused recommendations based
on their behavior within the application.
