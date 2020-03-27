import json
from urllib.parse import unquote

from django import template
from django.conf import settings
from django.template import Context

register = template.Library()


def cookiebanner_modal(parser, token):
    try:
        tag_name, template_name = token.split_contents()
    except ValueError:
        tag_name = token
        template_name = "'bootstrap4'"
    if not (template_name[0] == template_name[-1] and template_name[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
            "%r tag's argument should be in quotes" % tag_name
        )
    return CookiebannerModalNode(template_name[1:-1])


class CookiebannerModalNode(template.Node):
    def __init__(self, template_name):
        self.template_name = template_name

    def render(self, context):
        t = context.template.engine.get_template(
            f"cookiebanner/{self.template_name}.html"
        )

        cookie_groups = settings.COOKIEBANNER_GROUPS
        ctx = {
            "cookiegroups": cookie_groups,
            "cookiegroups_json": json.dumps(cookie_groups),
        }
        return t.render(Context(ctx, autoescape=context.autoescape))


register.tag("cookiebanner_modal", cookiebanner_modal)


@register.simple_tag(takes_context=True)
def cookie_accepted(context, cookie_group):
    allowed_cookies = context["request"].COOKIES.get("cookiebanner")
    if not allowed_cookies:
        return False
    return cookie_group in unquote(allowed_cookies).split(",")
