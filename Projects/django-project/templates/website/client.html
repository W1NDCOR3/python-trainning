{% extends 'base.html' %}

{% block content %}
  {% for cart in carts %}
    <div>
      <h2>Cart #{{ cart.id }}</h2>
      <ul>
        {% for product in cart.products %}
          <li>
            {{ product.name }}: ${{ product.price }} | <a href="{% url 'remove_product' client_id cart.id product.id %}">Remove</a>
        </li>
        {% endfor %}
      </ul>
      <h3>Suggested products</h3>
      <ul>
        {% for missing_product in cart.missing_products %}
          <li>
            {{ missing_product.name }} | <a href="{% url 'add_product' client_id cart.id missing_product.id %}">Add</a>
          </li>
        {% empty %}
          <li>No suggestions!</li>
        {% endfor %}
      </ul>
    </div>
  {% endfor %}
{% endblock %}
