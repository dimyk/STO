from setuptools import setup

setup(
    name='sto',
    version='1.0',
    description='Система обліку обслуговування автомобілів',
    author='dimyk',
    py_modules=['lab1_uip', 'test_lab3'],  # ім’я .py файлу без розширення
    entry_points={
        'console_scripts': [
            'sto = lab1_uip:main',
            'tests = test_lab3:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
