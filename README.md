# Django-agiliq

Practicas de apps con Django según https://books.agiliq.com/en/latest/
Los test ahorran dinero, tiempo y vidas.

## Carpetas

1. *books* copias en pdf de los libros (books free donwload)

2. *cookbook* contiene los ejercicios del libro *django-admin-cookbook.pdf*

3. *tdd_django* proyecto con resumenes y buenas prácticas de pruebas

## Resumen

1. Adiciona el prefijo `test_` a las pruebas
2. Cada test prueba una sola cosa
3. Para las vistas, cuando sea posible utilizar Request Factory `django.test.client.RequestFactory`
4. No escribas test que deban ser probados. Escribe test que sean lo más simple posible
5. "Don't Repeat Yourself", no aplica para los test. El método `setUp()` es realmente poderoso para generar datos reusables a través de todos los test de una clase, sin embargo algunas veces necesitamos datos similares, pero diferentes entre los metodos de prueba, en este caso es preferible hacer copy/paste y escribir el codigo similar multiples veces.
6. Es más elegante usar los metodos `Assertion`
7. Tip: puedes buscar packages y herramientas para generar datos de prueba, por ejemplo: ``factor boy, faker, model mommy`
8. Las pruebas unitarias no son las únicas pruebas que debes hacer. Por ejemplo, para probar api's externas puedes usar la libreria `Mock` creada por Michael Foord.
9. Documenta el próposito de cada cosa

## Cosas que pueden ser testeadas

- views
- models
- forms
- validators
- signals
- filters
- Template tags
- Failure (testear las pruebas que fallan)
- Misecellany: context processors, middleware, email, mixin...

¡Cualquier cosa!, deberias probar todo. Las unicas cosas que no deberias probar son las que ya estan cubiertas por el core de Django o third-party packages.

## sobre pruebas de integracion

Las pruebas de integración son cuando los módulos de software individuales se combinan y se prueban como un grupo. Esto se hace mejor después de completar las pruebas unitarias. Las pruebas de integración son una excelente manera de confirmar que "todas las piezas" están funcionando.

## continuous integration

Altamente recomendado, explorar Travis CI, o circle CI

## Pasos

- Paso 1: Comience a escribir pruebas. Ya lo hemos hecho, ¿verdad?
- Paso 2: Ejecutar pruebas y generar informe de cobertura con `coverage.py`
  - En la linea de comandos, ubucados en la raíz del proyecto escribir:
  `coverage run manage.py test --settings=config.settings.testt`
- Step 3: Generate the Report!
  - En la linea de comandos, ubucados en la raíz del proyecto escribir:
  `coverage html --omit="admin.py"`

## Alternativas a unittest

`pypi.python.org/pypi/pytest-django/`
`https://docs.djangoproject.com/en/2.1/topics/testing/`