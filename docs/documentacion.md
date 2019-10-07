# Proyecto IV - GestEnergy
Documentación más específica del proyecto.

## Integración contínua

Para integración contínua se va a usar Travis CI. Clona el repositorio a un entorno virtual para construir y probar tu código. Es fundamental detectar todos los fallos para posteriormente desplegar una versión correcta.

### Configuración Travis para Python

1. Para empezar hay que ingresar con nuestra cuenta de Github en [Travis](https://travis-ci.com/) y permitir el acceso al repositorio del proyecto.
2. Añadir un archivo .travis.yml en la raíz de nuestro repositorio, en este archivo se incluye el lenguaje, las versiones de python a probar,instalar librerias, ejecución de test.

    - Con respecto a las versiones elegidas para probar nuestro código en python, no es recomendable usar inferiores a la 3.0   ya que la versión 2.7 no podrá utlizarse a partir de 2020. Por este motivo se probará en las versiones 3.X.
    - Podemos añadir comandos para que se ejecuten antes de la instalación (before_install): instalar la útima versión de pip (pip install -U pip), versión en la que se está ejecutando (python --version)

3. Una vez que tengamos configurado nuestro archivo .travis.yml correctamente, cada vez que hagamos git push se verificará si se pasan los test o fallan.


