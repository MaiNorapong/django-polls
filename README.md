# django-polls

An application created following Django's tutorial with some modifications.

## Requirements

This project requires:

* `Python 3.6` or newer
* `Django 2.1.2` or newer
* Other Python packages as in [requirements.txt](requirements.txt)

## How to run

### Setup

From the directory root, install required packages using the following command:

```shell script
$ pip install -r requirements.txt
```

Create [`.env`](#env) text file in the project directory root and configure settings value for Django.

Create the database using the following command:

```shell script
$ python manage.py migrate
```

(Optional) Create sample poll data using the following command:

```shell script
$ python manage.py loaddata sample_poll_data
```

You're all set now!

> <strong id="env">Note:</strong> A required configuration value for `.env` is `SECRET_KEY`.  
> A useful tool to generate one: https://www.miniwebtool.com/django-secret-key-generator/.
> 
> **Example:**
> ```text
> # A line in `project_directory/.env`
> SECRET_KEY=c07(7b9676lfo8l6xwe#mn(ua%%bpt4c0bh)9jcr0p+v4fs*8k
> ```

### Running

Start the server using the following command:

```shell script
$ python manage.py runserver
```

The server should be up at localhost on port 8000.  
Go to the polls app at `polls/` and the [admin site](#admin-site) at `admin/`.  

If you choose to use the sample data, an account with admin privileges will have
already been created for you:

Username: `admin`  
Password: `password`

If for some reason port 8000 is not available, simply specify another port like so:

```shell script
$ python manage.py runserver 8001
```

You can use any port that's available, not just 8001 like shown.

> <strong id="admin-site">Note:</strong> To use the admin site, you must have an
> account that can login to it.  
> See the [Django documentation](https://docs.djangoproject.com/en/2.2/intro/tutorial02/#creating-an-admin-user)
> on how to create one.

## Progress

- [x] Part 1: Requests and responses
- [x] Part 2: Models and the admin site
- [x] Part 3: Views and templates
- [x] Part 4: Forms and generic views
- [x] Part 5: Testing
- [x] Part 6: Static files
- [ ] Part 7: Customizing the admin site

## FAQ

##### 1. Unrecognized command   

If you see error messages like 
`'python' is not recognized as an internal or external command, operable program
or batch file.` or `Command not found: pip`, you might not have Python and pip
correctly installed and/or included in your path. Such problems are not in the
scope of this README.

Copy your error message and search it on Google (or other search engines) and 
there should be plenty of answers in sites like Stack Overflow.
