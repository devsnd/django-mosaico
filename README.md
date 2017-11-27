# django-mosaico

django-mosaico is a django app that contains the
[mosaico](http://mosaico.io) frontend and implements the mosaico backend
in python.

This is a fork from [tubaman/django-mosaico](https://github.com/tubaman/django-mosaico) that contains some fixes and
improvements to make this work on newer django versions.

NOTE: It uses django's postgres JSONField and it's not backwards compatible to tubaman's original project as the whole
migration history was scrapped.


## Quick start

   1. Add "jsonify" and "mosaico" to your `INSTALLED_APPS` setting like this:

       ```python
       INSTALLED_APPS = [
           ...
           'jsonify',
           'mosaico',
       ]
       ```

   1. Include the mosaico URLconf in your project urls.py like this:

       ```python
       url(r'^mosaico/', include('mosaico.urls')),
       ```

   1. Setup [`MEDIA_ROOT` and `MEDIA_URL`](https://docs.djangoproject.com/en/1.10/howto/static-files/#serving-uploaded-files-in-development)
   1. Run `python manage.py migrate` to create the mosaico models.
   1. Login to the django admin
   1. Go to the Django admin here: http://127.0.0.1:8000/admin/mosaico/template/
   1. Create a new template in mosaico by clicking the `Add Template from Mosaico` button.
   1. When you're done, click "Save to Server".  Now that template should be listed in the Django admin under [templates](http://127.0.0.1:8000/admin/mosaico/template/).
