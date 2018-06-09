---
layout: home
title: Matir's Knowledge Base
---
{% assign navigation = site.data.navigation["main"] %}

<div id="home" class="nav__list">
  <ul class="nav__items">
    {% for nav in navigation %}
      <li>
        {% if nav.url %}
          {% comment %} internal/external URL check {% endcomment %}
          {% if nav.url contains "://" %}
            {% assign nav_url = nav.url %}
          {% else %}
            {% assign nav_url = nav.url | relative_url %}
          {% endif %}

          <a
            {% if nav_url %}
            href="{{ nav_url }}"
            {% endif %}
            ><span class="nav__sub-title">{{ nav.title }}</span></a>
        {% else %}
          <span class="nav__sub-title">{{ nav.title }}</span>
        {% endif %}

        {% if nav.children != null %}
        <ul>
          {% for child in nav.children %}
            {% comment %} internal/external URL check {% endcomment %}
            {% if child.url contains "://" %}
              {% assign child_url = child.url %}
            {% else %}
              {% assign child_url = child.url | relative_url %}
            {% endif %}

            {% comment %} set "active" class on current page {% endcomment %}
            {% if child.url == page.url %}
              {% assign active = "active" %}
            {% else %}
              {% assign active = "" %}
            {% endif %}

            <li><a
              {% if child_url %}
              href="{{ child_url }}"
              {% endif %}
              class="{{ active }}">{{ child.title }}</a></li>
                {% if child.children != null %}
                <ul>
                {% for subchild in child.children %}
                    {% comment %} internal/external URL check {% endcomment %}
                    {% if subchild.url contains "://" %}
                    {% assign child_url = subchild.url %}
                    {% else %}
                    {% assign child_url = subchild.url | relative_url %}
                    {% endif %}

                    {% comment %} set "active" class on current page {% endcomment %}
                    {% if subchild.url == page.url %}
                    {% assign active = "active" %}
                    {% else %}
                    {% assign active = "" %}
                    {% endif %}

                    <li><a
                    {% if child_url %}
                    href="{{ child_url }}"
                    {% endif %}
                    class="{{ active }}">{{ subchild.title }}</a></li>
                {% endfor %}
                </ul>
                {% endif %}
            {% endfor %}
            </ul>
            {% endif %}
      </li>
    {% endfor %}
  </ul>
</div>
