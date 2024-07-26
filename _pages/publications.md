---
layout: page
permalink: /publications/
title: publications
header: publications
description: 

categories: ['Peer Reviewed Journals', 'Data Release Papers', 'Conference Proceedings']
catprint: ['', 'Peer Reviewed Journals', 'Data Release Papers', 'Conference Proceedings']

years: [2015, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
nav: true
nav_order: 3
---
<!-- _pages/publications.md -->
<div class="publications">

{% for cat_ in page.categories  %}
  {% assign ind = forloop.index %}

  {%- capture cat -%}
  {{ page.catprint[ind] }}
  {%- endcapture -%}
  
  <br>
  <h4 class="font-weight-bolder">{{cat}}</h4>
  {% for y in page.years reversed  %}
    {%- capture citecount -%}
    {% bibliography_count -f papers -q @*[kind={{cat_}} && year={{y}}]* %}
    {%- endcapture -%}

    {% if citecount != "0"  %}
      <h2 class="year">{{y}}</h2>
      {% bibliography -f papers -q @*[kind={{cat_}} && year={{y}}]* %}
    {% endif %}
  {% endfor %}
{% endfor %}

</div>
