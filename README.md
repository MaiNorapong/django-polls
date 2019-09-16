# django-polls

An application created following Django's tutorial with some modifications.

## Requirements

This project requires:

* `Python 3.6` or newer
* `Django 2.1.2` or newer
* Python add-on modules as in [requirements.txt](requirements.txt)

## How to run

1. From the directory root, install required packages using the command `pip install -r requirements.txt`
2. Create `.env` text file in the project directory root and configure settings value
3. Start the server using the command `python manage.py runserver`
4. Server should be up (default) at localhost port 8000

> **Note:** A required configuration value for `.env` is `SECRET_KEY`.
> Useful tool to generate one: https://www.miniwebtool.com/django-secret-key-generator/.
> 
> **Example:** (a line in `.env`)
> ```text
> SECRET_KEY=c07(7b9676lfo8l6xwe#mn(ua%%bpt4c0bh)9jcr0p+v4fs*8k
> ```

### Progress

- [x] Part 1: Requests and responses
- [x] Part 2: Models and the admin site
- [x] Part 3: Views and templates
- [x] Part 4: Forms and generic views
- [x] Part 5: Testing
- [ ] Part 6: Static files
- [ ] Part 7: Customizing the admin site
