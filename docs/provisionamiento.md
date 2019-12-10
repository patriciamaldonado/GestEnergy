
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

 # Provisionamiento
    config.vm.provision "ansible" do |ansible|
	  ansible.playbook = "playbook.yml"
  end
end

```
 - ```Vagrant.configure("2") do |config|``` indica la versión de Vagrant con la que vamos a trabajar, versión 2, en mi caso tengo la versión 2.2.6.

 - ```config.vm.box = "bento/ubuntu-18.04" ``` especificamos la imagen base que tendrá nuestra máquina virtual. La imagen utilizada es bento/ubuntu-18.04, una imagen con ubuntu 18.04 lts elegida por ser una versión reciente y estable.

 - Con estas líneas indicamos que vamos a provisionar la máquina mediante Ansible, además de especificar la ubicación de nuestro archivo de provisionamiento (Playbook.yml).
   ```
      config.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yml"
   ```



<a name="playbook"></a>
## Ansible Playbook.yml
Provisionamos mediante Ansible [[3]](#ansible) creando un archivo llamado Playbook.yml, éste contendrá todas las órdenes de instalación con lo necesario para el provisionamiento de nuestra máquina virtual. Como el lenguaje de programación, instalar git, alguna dependencia que no sea estrictamente del lenguaje de programación.

Mi archivo Playbook.yml es el siguiente:

```

- hosts: all
  become: yes

  tasks:

  - name: Actualizacion (apt-get update)
    apt: update_cache=yes  
      upgrade=yes  

  - name: Instalacion python3
    apt: name=python3-setuptools state=present update_cache=yes

  - name: Instalacion pip3
    apt:  name=python3-pip state=present update_cache=yes

  - name: Instalacion git
    apt: name=git state=present update_cache=true

  - name: Clono repositorio GestEnergy
    git:  repo=https://github.com/patriciamaldonado/GestEnergy.git clone=yes force=yes dest=GestEnergy/

  - name: Instalacion dependencias
    command: pip3 install -r GestEnergy/requirements.txt

  - name: Instalacion nodejs
    apt: name=nodejs state=present update_cache=true

  - name: Instalacion npm
    apt: name=npm state=present update_cache=true

  - name: Instalacion pm2
    command: npm install -g pm2

```
- ```hosts: all```: va a trabajar con todos los hosts
- ```become: yes```: permisos de superusuario
-```tasks:```: indicamos una serie de tareas  que instalarán todo lo necesario en nuestra máquina virtual para la ejecución de nuestra aplicación.
    - Actualizamos
    - Instalamos python
    - Instalación de pip3
    - Clonamos el repositorio con nuestra aplicación
    - Instalamos dependencias necesarias para el funcionamiento de nuestra aplicación.
    - Además instalamos nodejs, npm y pm2 para poder lanzar el servicio.

<a name="pruebalocal"></a>
## Levantar la máquina, provisionar y prueba en local

Una vez que tenemos nuestro archivo Vagrantfile correctamente configurado usaremos el comando ```make levantar-maquina``` que se encargará de levantar la máquina con la
imagen box de ubuntu 18.04 que le hemos indicado. Además para provisionar la máquina usaremos el comando ```make provision,``` éste instalará lo que hemos especificado en el archivo Playbook.yml de Ansible.

Accedemos mediante ```vagrant ssh```. He probado la aplicación de forma local en la máquina virtual.  

<a name="vagrantcloud"></a>
## Vagrant Cloud


## Referencias

- <a name="vagrant0"> [[1] Vagrant desde 0](https://albertoromeu.com/vagrant-desde-cero/)</a>
- <a name="vagrantComandos"> [[2] Vagrant comandos](https://medium.com/@joaquin.villagra/vagrant-entornos-de-trabajo-independientes-replicables-y-elegantes-e49597eeeb65)</a>
- <a name="vagrantfile"> [[3] Vagrantfile](https://www.vagrantup.com/docs/vagrantfile/)</a>

- <a name="ansible"> [[4] Ansible](https://docs.ansible.com/ansible/latest/index.html/)</a>
