# Step One: Set up Wagtail

## Create a virtual environment

If you already have Python installed on your machine, you can create a local virtual environment using `venv`. Open your command line and navigate to the directory you want to build your project in. Then enter the following commands to creative a virtual environment.

```shell
python -m venv env
source env/bin/activate
```

If it activates successfully, there will be no output, but you should see an `(env)` indicator appear in your prompt.

## Set up Wagtail

Once you have a virtual environment set up, we can install Wagtail and start setting up our very first Wagtail website. In your project directory, enter the following command in your command line:

```shell
pip install wagtail
```

This command tells the Python package manager pip to install the latest release of Wagtail along with all of the dependencies that are needed for Wagtail. After Wagtail is installed, you can confirm that it is installed with:

```shell
pip show wagtail
```

After Wagtail is installed, you can use one of Wagtail's built-in commands to start a brand new website. For this tutorial, we're going to be creating a mini-blog project called `myblog`. We're also going to use a `--template` flag to import a template so that we will have a few things set up ahead of time. That way we won't spend this whole workshop copying and pasting template code.

```shell
wagtail start myblog --template=https://github.com/vossisboss/pyladies2025-starter-template/archive/main.zip
```

Change directory into the new Django project's folder before continuing:

```shell
cd myblog
```

Once all of the files are set up, you'll need to enter some commands to set up the test database and all of the migration files that Wagtail needs. You can do that with the `migrate` command.

```shell
python manage.py migrate
```

After the migrations are complete, you'll need to create a superuser so that you can access the backend of your Wagtail website. Use the following command:

```shell
python manage.py createsuperuser
```

Follow the prompts in your command line to create your superuser. Once you have a superuser set up, you can start up the test server to see your new Wagtail site in action.

```shell
python manage.py runserver
```

If the server has started up without any errors, you can navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser to see your Wagtail website. If you've successfully installed Wagtail, you should see a home page with a large teal egg on it.

To test that your superuser works, navigate to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and login with the credentials you created.

Now you have a basic Wagtail website set up. Next, we're going to extend the homepage model so that we can start adding content to the website.

[Continue to step 2](https://github.com/vossisboss/pyladiescon2025/tree/step-2)
