#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:22:30 2023

@author: zaneleakibo-betts
"""

from CustomerClass import Customer

from DiscountRateClass import DiscountRate

class Visit:
    def __init__(self, customer, date):
        self.customer = customer
        self.date = date
        self.services = {}
        self.products = []
    def add_service(self, service_name, price):
        self.services[service_name] = price

    def add_product(self, product_price):
        self.products.append(product_price)

    def get_services_total(self):
        return sum(self.services.values())

    def get_products_total(self):
        return sum(self.products)

    def get_subtotal(self):
        return self.get_services_total() + self.get_products_total()

    def get_total(self):
        service_discount_rate = DiscountRate.getServiceDiscountRate(self.customer)
        product_discount_rate = DiscountRate.getProductDiscountRate(self.customer) # pass customer object
        services_total = self.get_services_total() * (1 - service_discount_rate)
        products_total = self.get_products_total() * (1 - product_discount_rate)
        return services_total + products_total

import json

with open("dataQ3.json", "r") as fd:
    data = json.load(fd)

for customer_data in data["Customer"]:
    customer = Customer(customer_data["name"], customer_data["member_type"])
    visit = Visit(customer, customer_data["date"])
    visit.add_service("Service", float(customer_data["service_expense"]))
    visit.add_product(float(customer_data["product_expense"]))
    subtotal_cost = round(visit.get_subtotal(), 2)
    total_cost = round(visit.get_total(), 2)
    print(f"**********************\n---{customer.get_name} Reciept--- \n Member Type   |{customer.get_member_type} \n Visited       | {visit.date}\n Total price   | £{subtotal_cost:.2f} \n Discount price| £{total_cost:.2f}")
