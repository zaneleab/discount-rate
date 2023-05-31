#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:41:37 2023

@author: zaneleakibo-betts
"""

class DiscountRate:
    PREMIUM_DISCOUNT_RATE = 0.2
    GOLD_DISCOUNT_RATE = 0.15
    SILVER_DISCOUNT_RATE = 0.1
    PRODUCT_DISCOUNT_RATE = 0.1

    @classmethod
    def getServiceDiscountRate(cls, customer):
        member_type = customer.get_member_type
        if member_type == "Premium":
            return cls.PREMIUM_DISCOUNT_RATE
        elif member_type == "Gold":
            return cls.GOLD_DISCOUNT_RATE
        elif member_type == "Silver":
            return cls.SILVER_DISCOUNT_RATE
        else:
            return 0

    @classmethod
    def getProductDiscountRate(cls, customer): 
        if customer.isMember():
            return cls.PRODUCT_DISCOUNT_RATE
        else:
            return 0