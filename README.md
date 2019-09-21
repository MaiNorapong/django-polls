# django-polls

An application created following Django's tutorial with some modifications.

## Requirements

This project requires:

* `Python 3.6` or newer
* `Django 2.1.2` or newer
* Python add-on modules as in [requirements.txt](requirements.txt)

## How to run

Here is how to setup the polls app:

1. From the directory root, install required packages using the following command:  
   `$ pip install -r requirements.txt`
2. Create `.env` text file in the project directory root and configure settings value for Django
3. Create the database using the following command:  
   `$ python manage.py migrate`
4. (Optional) Create sample poll data using the following command:  
   `$ python manage.py loaddata sample_poll_data`
5. Start the server using the following command:  
   `$ python manage.py runserver`

> **Note:** A required configuration value for `.env` is `SECRET_KEY`.
> Useful tool to generate one: https://www.miniwebtool.com/django-secret-key-generator/.
> 
> **Example:** (a line in `.env`)
> ```
> SECRET_KEY=c07(7b9676lfo8l6xwe#mn(ua%%bpt4c0bh)9jcr0p+v4fs*8k
> ```

The server should be up at localhost on port 8000.  
Go to the polls app at `polls/` and the admin site at `admin/`.  

> **Note:** To use the admin site, you must have an account that can login to it.
> See the [Django documentation](https://docs.djangoproject.com/en/2.2/intro/tutorial02/#creating-an-admin-user)
> on how to create one.

## Progress

- [x] Part 1: Requests and responses
- [x] Part 2: Models and the admin site
- [x] Part 3: Views and templates
- [x] Part 4: Forms and generic views
- [x] Part 5: Testing
- [ ] Part 6: Static files
- [ ] Part 7: Customizing the admin site
