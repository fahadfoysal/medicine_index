from django import template
import re

register = template.Library()

@register.filter
def highlight(text, query):
    if query:
        pattern = re.compile(re.escape(query), re.IGNORECASE)
        return pattern.sub(f'<span class="highlight">{query}</span>', text)
    return text
