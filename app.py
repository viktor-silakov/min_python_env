#!/usr/bin/env python3
"""
Минимальное Python приложение, которое получает случайный факт о кошках
"""

import requests
import json


def get_cat_fact():
    """Получает случайный факт о кошках из API"""
    try:
        response = requests.get('https://catfact.ninja/fact')
        response.raise_for_status()
        data = response.json()
        return data['fact']
    except requests.exceptions.RequestException as e:
        return f"Ошибка при получении данных: {e}"


def main():
    """Основная функция приложения"""
    print("🐱 Получаем случайный факт о кошках...")
    fact = get_cat_fact()
    print(f"\n💡 Факт о кошках: {fact}")


if __name__ == "__main__":
    main()