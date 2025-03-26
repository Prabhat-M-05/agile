# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 10:53:10 2025

@author: Prabhat
"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class UserManager:
    def __init__(self):
        self.users = []
    def add_user(self, user):
        self.users.append(user)
    def get_user_count(self):
        return len(self.users)
    def get_average_age(self):
        if not self.users:
            return 0
        return sum(user.age for user in self.users) / len(self.users)