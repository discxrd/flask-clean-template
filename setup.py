from setuptools import setup
import os

app_name = "Example App"

packages = []
for dirname, dirnames, filenames in os.walk(app_name):
        if '__init__.py' in filenames:
            packages.append(dirname.replace('/', '.'))

requires = (
    'flask',
    'flask-sqlalchemy',
    'flask-wtf'
)

setup(
    # Информация о приложении:
    name=app_name,
    version='1.0',
    author='ExampleAuthor',

    description='Description example',
    long_description='Doc example',
    
    license='MIT',
    
    packages=packages,
    
    include_package_data=True,
    zip_safe=False,
    
    # Зависимости
    install_requires=requires,
    
    # Данные о разработке разработки
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Framework :: Flask',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Russian',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only'
        ]
)