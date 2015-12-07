{% extends "section.md" %}

{% block body %}

<ul class="list-group">
{% for item in items %}

	<li class="list-group-item">
	{% if item.employer is defined %}
		<h4 class="list-group-item-heading">
			{{ item.employer }}
			{% if item.location is defined %}, {{ item.location }}{% endif %}
		</h4>
	{% elif item.topic is defined %}
		<h4 class="list-group-item-heading">
			{{ item.topic }}
		</h4>
	{% endif %}

	{% if item.date is defined %}
	<div class="pull-right">
		<p class="list-group-item-text"><i>
			{{ item.date }}
		</i></p>
	</div>
	{% endif %}

	{% if item.about is defined %}
		<p class="list-group-item-text">
			{{ item.about }}
		</p>
	{% endif %}

	<ul>
	{% for note in item.notes %}
		<li style="padding-top:0px">
		  {{ note }}
		</li>
	{% endfor %}
	</ul>

	</li>
{% endfor %}
</ul>

{% endblock body %}
