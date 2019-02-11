# Loading Data Into the Database

### Warning:

Before starting this portion, ensure that you have completed [Getting Started with Cloud9](GettingStartedCloud9.md).


## Using Jupyter with Cloud9

Jupyter notebooks are a powerful tool for quickly prototyping out solutions with Python, developing ML algorithms (like with Sagemaker), and
make great documents for repeating technical proceeses. You will be using them here to configure your datasets locally, as well as configure Personalize.

To get started, open your Cloud9 environment if it is not already open in your browser.

Once there, open a terminal and enter:

```
workon personalens
```

Again you will need the IP address if your Cloud9 instance so write it down after getting the output of:

```
curl http://169.254.169.254/latest/meta-data/public-ipv4
```

To launch the Jupyter Notebook server:

```
jupyter notebook --ip=0.0.0.0
```

Pay attention to the output, you should see a key resembling: 
`?token=f8853b4ae844f33b6e7f6ca1bf6225d1f38ef7595f4f8ff9`

Take this key, and open a new tab in your browser consisting of `http://YOUR.IP.ADDRESS.HERE:8888?token=f8853b4ae844f33b6e7f6ca1bf6225d1f38ef7595f4f8ff9`
Where the IP and token are the values from your environment.

An example would be http://54.144.226.110:8888?token=f8853b4ae844f33b6e7f6ca1bf6225d1f38ef7595f4f8ff9

If the request times out or you have connectivity problems, validate that you have your Security Group settings
defined correctly. For specific instructions see [here](GettingStartedCloud9.md).


## Actually Loading Data

The real work will take place inside Jupyter, in your Jupyter window, open the  `DataLoader.ipynb` file by clicking on it.

Follow the rest of the instructions in the notebook. To execute cells you can press `shift` + `Enter` or cilck the `Run` button in the menu bar. Read each cell carefully before executing and update
any values where you are prompted.

When you have completed it move onto the next step: [Loading the data into Amazon Personalize](LoadingDataIntoAmazonPersonalize.md)
