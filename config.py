import os

class Config:
    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Используйте свою базу данных
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Добавьте следующие две строки для указания путей к папкам static и templates
    STATIC_FOLDER = 'static'
    TEMPLATE_FOLDER = 'templates'