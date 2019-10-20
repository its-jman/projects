---
layout: base
---
{% for page in site.mypages %}
<article>
    <a href="{{ page.url }}"><h2>{{ page.title }}</h2></a>
    <p>{{ page.excerpt | markdownify }}</p>
</article>
{% endfor %}
