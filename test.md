---
layout: default
---
{% for p in site.zettel %}
  <h1>{{p.title}}</h1>
  Path: {{p.path}}
  Relpath: {{p.relative_path}}
  URL: {{p.url}}
  ID: {{p.id}}
{% endfor %}
