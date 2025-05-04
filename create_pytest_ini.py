# create_pytest_ini.py

content = """\
[pytest]
addopts = -ra
filterwarnings =
    ignore::DeprecationWarning:pyreadline.*
"""

with open("pytest.ini", "w") as f:
    f.write(content)

print("Файл pytest.ini успешно создан!")
