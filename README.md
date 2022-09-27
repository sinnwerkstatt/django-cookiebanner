# Django-Cookiebanner

## Installation

`pip install django-cookiebanner`


## Usage

* Add `cookiebanner` to your `INSTALLED_APPS`

* in your settings (`settings.py`) specify the different Cookie Groups:
```python
from django.utils.translation import gettext_lazy as _

COOKIEBANNER = {
    "title": _("Cookie settings"),
    "header_text": _("We are using cookies on this website. A few are essential, others are not."),
    "footer_text": _("Please accept our cookies"),
    "footer_links": [
        {"title": _("Imprint"), "href": "/imprint"},
        {"title": _("Privacy"), "href": "/privacy"},
    ],
    "groups": [
        {
            "id": "essential",
            "name": _("Essential"),
            "description": _("Essential cookies allow this page to work."),
            "cookies": [
                {
                    "pattern": "cookiebanner",
                    "description": _("Meta cookie for the cookies that are set."),
                },
                {
                    "pattern": "csrftoken",
                    "description": _("This cookie prevents Cross-Site-Request-Forgery attacks."),
                },
                {
                    "pattern": "sessionid",
                    "description": _("This cookie is necessary to allow logging in, for example."),
                },
            ],
        },
        {
            "id": "analytics",
            "name": _("Analytics"),
            "optional": True,
            "cookies": [
                {
                    "pattern": "_pk_.*",
                    "description": _("Matomo cookie for website analysis."),
                },
            ],
        },
    ],
}
```

* In your base template add the banner and the conditionals:
```djangotemplate
{% load cookiebanner %}
...
<body>
{% cookiebanner_modal 'vanilla' %}
...


{% cookie_accepted 'analytics' as cookie_analytics %}
{% if cookie_analytics %}
<script>... javascript for matomo ...</script>
{% endif %}
</body>
```


### Custom Template

You can create a custom template and use that instead of the default one. 
* Create a folder `cookiebanner/` and a file in one of your `templates/`-folders, e.g.: `templates/cookiebanner/mytemplate.html`
* Use `{% cookiebanner_modal 'mytemplate' %}`
