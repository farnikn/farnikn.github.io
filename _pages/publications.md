---
layout: page
permalink: /publications/
title: publications
header: publications
description: Here is my <a href='https://ui.adsabs.harvard.edu/search/q=%20author%3A%22nikakhtar%2C%20f%22&sort=date%20desc%2C%20bibcode%20desc&p_=0'>NASA ADS list</a>. 

categories: ['Peer Reviewed Journals', 'Data Release Papers', 'Conference Proceedings']
catprint: ['', 'Peer Reviewed Journals', 'Data Release Papers', 'Conference Proceedings']

years: [2015, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
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
