{% extends "section.md" %}

{% block body %}

<ul class="list-group">

{% for school in items %}
	<li class="list-group-item">
	<h4 class="list-group-item-heading">
	{{school.school}}
	</h4>

	<div class="pull-right"><p class="list-group-item-text"><i>
		{{school.date}}
	</i></p></div>

		<p class="list-group-item-text">
			{{ school.major }}  
		</p>

	{% if school.gpa is defined %}
		<p class="list-group-item-text">
			<strong>GPA:</strong>
			{{ school.gpa }}
		</p>
		{% endif %}

{% endfor %}
</ul>

{% endblock body %}
