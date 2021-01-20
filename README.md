# stepik_autotests_final_tasks
 repo for final project on course of automatisation testing using selenium and python
 
software versions and env:

win10x64

python 3.6.8

pytest 6.2.1


# запуск теста
доступные параметры:

language, язык (en, ru, fr, sp), по умолчанию es.

browser_name, тип браузера (хром, firefox), по умолчанию - хром.


пример запуска, если запуск теста происходит напрямую в директории:

pytest --language=fr


или pytest -s --language=fr, если требуется добавить в output вывод принтов из кода


или напрямую с указанием имени файла

pytest --language=es test_items.py
