# Personalens: Amazon Personalize + movieLens data


This repository exists to be an educational tool for understanding how to integrate Amazon Personalize with a traditional
web application. It is expected to be deployed on a standalone workstation or demo resource, none of the usual production ready proccesses 
have been followed in creating this project.

## Overview

1. [Getting Started with Cloud9](docs/GettingStartedCloud9.md)
2. [Loading the data into the database](docs/LoadingDataIntotheDatabase.md)
3. [Loading the data into Amazon Personalize](docs/LoadingDataIntoAmazonPersonalize.md)
4. [Integrating Amazon Personalize with Django](docs/IntegratingAmazonPersonalizeWithDjango.md)
5. [Integrating clickstream data](docs/IntegratingClickstreamData.md)

## Special Thanks

This project would not have been possible without the service team at AWS building Amazon Personalize.

All of the data comes from the fine folks working on [movielens](https://movielens.org).

Getting a local copy of the posters is a bit tricky, a large thank you to [@babu-thomas](https://github.com/babu-thomas) for his work on [this project](https://github.com/babu-thomas/movielens-posters) that 
allows you to scrape all of the posters and cache them locally.

