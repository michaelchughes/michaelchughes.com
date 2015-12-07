{% extends "section.md" %}

{% block body %}

<ul class="list-group">
{% for pub in items %}

	<li class="list-group-item">
		{% if pub.url is defined %}
			<p class="list-group-item-text">
			<a href="{{pub.url}}">
				{{ pub.title }}
			</a></p>
		{% else %}
			<p class="list-group-item-text">{{ pub.title }}</p>
		{% endif %}
		<p class="list-group-item-text">{{ pub.authors }}</p>
		<p class="list-group-item-text">
			<i>{{ pub.venuetype }} {{ pub.venue }}</i>, {{ pub.year }}
		</p>
	</li>
{% endfor %}
</ul>

{% endblock body %}
