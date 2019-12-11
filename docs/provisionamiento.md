
# Provisionamiento de máquinas virtuales

Vamos a usar Vagrant [[1]](#vagrant0)[[2]](#vagrantComandos), un gestor de máquinas virtuales en el que podremos trabajar con entornos locales y remotos.
Vagrant funciona por omision con Virtualbox. Para ello debemos instalar Virtualbox, Vagrant y Ansible para levantar una máquina virtual y provisonarla.

   * [Vagrantfile](#vagrantfile)
   * [Ansible Playbook.yml](#playbook)
   * [Levantar la máquina, provisionar y prueba en local](#playbook)
   * [Vagrant Cloud](#vagrantcloud)


<a name="vagrantfile"></a>
## Vagrantfile

En primer lugar creamos un archivo llamado Vagrantfile [[3]](#vagrantfile). Éste es el archivo de configuración de Vagrant, en el que podremos especificar la imagen base elegida, mapeo de puertos, configuración de Ansible...

El archivo Vagrantfile es el siguiente:

```
#Versión Vagrant
Vagrant.configure("2") do |config|

#Indicamos la imagen base
  config.vm.box = "bento/ubuntu-18.04"
  # Mapeo de puertos
  config.vm.network "forwarded_port", guest: 5000, host: 5000
 # Provisionamiento con Ansible
    config.vm.provision "ansible" do |ansible|
	  ansible.playbook = "playbook.yml"
  end
end

```
 - ```Vagrant.configure("2") do |config|``` indica la versión del objeto de Vagrant con la que vamos a trabajar, versión 2, en mi caso tengo la versión 2.2.6.

 - ```config.vm.box = "bento/ubuntu-18.04" ``` especificamos la imagen base [[6]](#boxes) que tendrá nuestra máquina virtual. La imagen utilizada es bento/ubuntu-18.04, una imagen con ubuntu 18.04 lts elegida por ser una versión reciente y estable.

 - Con estas líneas indicamos que vamos a provisionar la máquina mediante Ansible, además de especificar la ubicación de nuestro archivo de provisionamiento (Playbook.yml).
   ```
      config.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yml"
   ```
-  ```config.vm.network "forwarded_port", guest: 5000, host: 5000 ```
 Permite el acceso al puerto 5000 en el invitado a través del 5000 en el host. Así que cuando ejecutemos nuestra aplicación en nuestra máquina virtual(invitado) podremos acceder desde nuestro host.


<a name="playbook"></a>
## Ansible Playbook.yml
Provisionamos mediante Ansible [[3]](#ansible) creando un archivo llamado Playbook.yml, éste contendrá todas las órdenes de instalación con lo necesario para el provisionamiento de nuestra máquina virtual. Como el lenguaje de programación, instalar git, alguna dependencia que no sea estrictamente del lenguaje de programación...

Mi archivo Playbook.yml es el siguiente:

```

- hosts: all
  become: yes

  tasks:

  - name: Actualizacion (apt-get update)
    apt: update_cache=yes  
      upgrade=yes  

  - name: Instalacion python3
    apt: name=python3-setuptools state=present

  - name: Instalacion pip3
    apt:  name=python3-pip state=present

  - name: Instalacion git
    apt: name=git state=present

  - name: Clono repositorio GestEnergy
    git:  repo=https://github.com/patriciamaldonado/GestEnergy.git clone=yes force=yes dest=GestEnergy/

  - name: Instalacion dependencias
    command: pip3 install -r GestEnergy/requirements.txt

  - name: Instalacion nodejs
    apt: name=nodejs state=present

  - name: Instalacion npm
    apt: name=npm state=present

  - name: Instalacion pm2
    command: npm install -g pm2

```
- ```hosts: all```: la máquina virtual será accesible desde todos los hosts.
- ```become: yes```: usamos permisos de superusuario para instalar nuestras tareas que se indican a continuación.
-```tasks:```: indicamos una serie de tareas  que instalarán todo lo necesario en nuestra máquina virtual para la ejecución de nuestra aplicación.

    - Actualizamos para que la máquina conozca los paquetes disponibles.

      ```
      - name: Actualizacion (apt-get update)
        apt: update_cache=yes  
          upgrade=yes
      ```
    - Instalamos python3, el lenguaje de nuestro microservicio.

      ```
      - name: Instalacion python3
        apt: name=python3-setuptools state=present update_cache=yes

      ```
    - Instalación de pip3 para instalar dependencias.

      ```
      - name: Instalacion pip3
        apt:  name=python3-pip state=present update_cache=yes

      ```
    - Instalación de git para posteriormente poder clonar el repositorio de nuestro microservicio.
      ```
      - name: Instalacion git
        apt: name=git state=present update_cache=yes
      ```
    - Clonamos el repositorio, GestEnergy
      ```
      - name: Clono repositorio GestEnergy
        git:  repo=https://github.com/patriciamaldonado/GestEnergy.git clone=yes force=yes dest=GestEnergy/
      ```
    - Instalamos dependencias definifidas en el archivo requirements.txt, gunicorn y flask necesarias para el funcionamiento de nuestra aplicación.
      ```
      - name: Instalacion dependencias
        command: pip3 install -r GestEnergy/requirements.txt

      ```
    - Además instalamos nodejs, npm y pm2 para poder lanzar el servicio.

      ```
      - name: Instalacion nodejs
        apt: name=nodejs state=present update_cache=yes

      - name: Instalacion npm
        apt: name=npm state=present update_cache=yes

      - name: Instalacion pm2
        command: npm install -g pm2

      ```
Notas:
- state=present: comprueba si está instalado, si no lo instala.
- update_cache=yes: equivale a apt-get update. Se puede ejecutar como parte de la instalación del paquete o como un paso separado.

<a name="pruebalocal"></a>
## Levantar la máquina, provisionar y prueba en local

Una vez que tenemos nuestro archivo Vagrantfile correctamente configurado usaremos el comando ```make levantar-maquina``` que se encargará de levantar la máquina con la
imagen box de ubuntu 18.04 que le hemos indicado.
Además para provisionar la máquina usaremos el comando ```make provision,``` éste instalará lo que hemos especificado en el archivo Playbook.yml de Ansible.

Accedemos a la máquina virtual mediante ```vagrant ssh```.  
Pruebo mi aplicación lanzando la orden make start que inicia el servicio mediante pm2. Y compruebo desde mi host que puedo acceder al servicio y devuelve el estado correcto.


<a name="vagrantcloud"></a>
## Vagrant Cloud
Vamos a exportar nuestra máquina virtual[[5]](#export) y subirla a la nube.

Para ello usamos el comando  ```vagrant package --output gestenergy.box ```que exporta nuestra máquina virtual.
Creamos una cuenta en Vagrant Cloud y la subimos.

> URL box: https://app.vagrantup.com/patriciamaldonado/boxes/gestenergy/



## Referencias

- <a name="vagrant0"> [[1] Vagrant desde 0](https://albertoromeu.com/vagrant-desde-cero/)</a>
- <a name="vagrantComandos"> [[2] Vagrant comandos](https://medium.com/@joaquin.villagra/vagrant-entornos-de-trabajo-independientes-replicables-y-elegantes-e49597eeeb65)</a>
- <a name="vagrantfile"> [[3] Vagrantfile](https://www.vagrantup.com/docs/vagrantfile/)</a>

- <a name="ansible"> [[4] Ansible](https://docs.ansible.com/ansible/latest/index.html/)</a>

- <a name="export"> [[5] Exportar Package Vagrant](https://www.vagrantup.com/docs/cli/package.html)</a>

- <a name="boxes"> [[6] Vagrant boxes](https://www.vagrantup.com/docs/boxes.html)</a>
