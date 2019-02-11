# Getting Started with Personalens and Cloud9

In order to allow you to experiment with Amazon Personalize in a contained
environment we will use Amazon's cloud based IDE Cloud9. This environment
will serve as your platform for developing and running the Personalens application
as well as a hosting platform for Jupyter notebooks to configure Amazon Personalize.

## Creating a Cloud9 Instance

To begin you will need to create a Cloud9 instance, first open a new browser tab and sign
into your AWS console. 

Next, validate that you are working inside `us-east-1` looking in the top right corner and ensuring the location says
`N. Virginia`, if it does not, click the current location and change it to `N. Virginia`.

Once there, click inside the "Find Services" search box and enter `Cloud9`, then click the service to go to the Cloud9 homepage.

Now click the `Create Environment` button on the right side of the page, this will be an EC2 instance that will house everything other than the content
inside Amazon Personalize and a few database exports placed in Amazon S3.

Enter in any name that you desire as well as a description, then click `Next Step`.

Select `Create a new instance for environment (EC2)` and any instance type you would like to use. If you would like your instance to automatically shut down after a period of 
inactivity to save on costs, select the duration under `Cost-saving setting`. After this click `Next Step`.

Review all of the settings and then click `Create Environment`, this process will take a few minutes to complete. Once it has completed your Cloud9 IDE will load in your browser.

## Configuring Security Group Settings

Each Cloud9 instance running in AWS is powered by an EC2 Instance or virtual machine, you will need to open a few ports in order to view the application
and Jupyter notebooks later.

Open a new tab in your browser and visit https://console.aws.amazon.com/

From this page, again search for `Cloud9` and visit the service page. Click the `View Details` button on this page, note the section for `Security Groups` and
copy the value, for example `sg-076c818588c59b781`.

Click `Services` at the top of the page and search for `EC2` then click it. 

Click the link in the left column titled `Security Groups`. Paste your copied value in the search bar and press enter.

Once selected, click the `Inbound` tab at the bottom. Next, click the `Edit` button.

Add 2 rules with the following settings:

#### Rule 1

Custom TCP Rule, Port Range: 8000, Source: My IP, Description: Django Application

#### Rule 2

Custom TCP Rule, Port Range: 8888, Source: My IP, Description: Jupyter Notebooks

After adding them, click `Save`

You may now close your tab and go back to the Cloud9 IDE window. You have enabled access for your computer. 

If you change locations and subsequently IP addresses you can always go back to this page and update the rules with your new
connection information.


## Configuring Your Cloud9 Instance for Development

Any commands in this session will be formatted like this:

```
pwd
```

These commands should be entered in a terminal session inside your Cloud9 IDE. You can start one by clicking the `+` tab and selecting `New Terminal`.

The very first thing is to install the Python utility virtualenvwrapper. It allows you to quickly activate isolated Python environments.

```
pip install virtualenvwrapper
```

Now update your terminal's bash profile with nano:

```
nano ~/.bashrc
```

If you are unfamiliar with using Nano, take a quick look at the basics here: https://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/

Mainly you will need to know how to save a file, and that is by pressing `ctrl + x` or `cmd + x` ( Control or Command and then the x key) then pressing enter and following the directions.

Once open, add the following to the end of the file:

```
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

Once saved and nano has closed, update your terminal's configuration with:

```
source ~/.bashrc
```

You can see that this is successful by a series of lines like the following being returned:

```
function
virtualenvwrapper.user_scripts creating /home/ec2-user/.virtualenvs/premkproject
virtualenvwrapper.user_scripts creating /home/ec2-user/.virtualenvs/postmkproject
virtualenvwrapper.user_scripts creating /home/ec2-user/.virtualenvs/initialize
virtualenvwrapper.user_scripts creating /home/ec2-user/.virtualenvs/premkvirtualenv
virtualenvwrapper.user_scripts creating /home/ec2-user/.virtualenvs/postmkvirtualenv.....
```

After this you are now ready to create the virtualenv for Personalens enter the following:

```
mkvirtualenv -p python3 personalens
```

Finally you are ready to clone the code and install its dependencies:

```
git clone https://github.com/chrisking/personalens.git
cd personalens
pip install -r requirements.txt
```

Given the movie posters are quite large, they are not placed inside the git repository and must be downloaded separately.

```
cd static
wget https://s3.amazonaws.com/chriskingpartnershare/img.zip
unzip img.zip
rm -f img.zip
cp -R img ../data/ml-100k/ 
```

The last thing to define before running thes application is the Django configuration for this environment. Paste these lines to finish the configuration


```
echo '# Django Config' >> ~/.virtualenvs/personalens/bin/postactivate
echo 'export PYTHONPATH=.:/home/ec2-user/environment/personalens' >> ~/.virtualenvs/personalens/bin/postactivate
echo 'export DJANGO_SETTINGS_MODULE=personalens.settings' >> ~/.virtualenvs/personalens/bin/postactivate
echo 'cd /home/ec2-user/environment/personalens' >> ~/.virtualenvs/personalens/bin/postactivate
workon personalens
```

You will need to create a database first and then a super user, do so with the following commands. Any username or passwords are your choice, but save them for later.

```
django-admin.py migrate
django-admin.py createsuperuser
```


In order to view your running application you will need to identify your instance's external IP address, to do that:

```
curl http://169.254.169.254/latest/meta-data/public-ipv4
```

Then run the server with:

```
django-admin.py runserver 0.0.0.0:8000
```

Once it is running, open another browser tab on your computer and visit: `http://the.externa.ip.address:8000`

For example if the curl command returned `54.144.226.110` you would visit: http://54.144.226.110:8000

## Next: Loading Data Into the Database

Continue [here:](LoadingDataIntotheDatabase.md)


