#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:41:37 2023

@author: zaneleakibo-betts
"""

class Customer:
    def __init__(self, name, member_type=None):
        self.__name = name
        self.__member_type = member_type
        
    def __repr__(self):
        """Return a string representation of the customer name and member type"""
        return f"Customer(name='{self.__name}', member_type={self.__member_type})"
                
    def isMember(self):
        return self.__member_type is not None and self.__member_type != ""
    @property
    def get_name(self):
        return self.__name
    
    def setname(self,name):
        self.name = name
    @property
    def get_member_type(self):
        return self.__member_type
    
    def setMember_type(self, member_type):
        self.member_type = member_type