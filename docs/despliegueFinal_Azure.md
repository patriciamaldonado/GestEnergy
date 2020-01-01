
# Despliegue final VM en Azure

El despliegue final de nuestra VM se subirá a Azure.

   * [Azure](#confazure)
   * [Vagrantfile](#vagrantfile)
   * [Ansible Playbook.yml](#playbook)
   * [Despliegue VM en Azure](#despliegue)

<a name="confazure"></a>
## Azure

Configurarmos Azure para posteriormente desplegar e instalamos el CLI y el plugin de Azure [[1]](#azure1)

```
	- curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

	 - vagrant plugin install vagrant-azure
```

1. Para empezar creamos un grupo de recursos en Azure [[3]](#gruporecursos)
   Vamos a indicarle que la localización sea westeurope, es importante que esté en Europa
   para protección de datos sobre todo y que cumpla la normativa.

    ```
    az group create -l westeurope -n gestenergy-azure
    ```

2. Necesitamos obtener las credenciales que luego necesitará vagrantfile para crear la máquina virtual en Azure.
[[4]](#vagrantfileAzure)
    ```
      az ad sp create-for-rbac
    ```

    Nos mostrará una salida como esta.
    ```
    Creating a role assignment under the scope of "/subscriptions/id de subscripción"
      ...
        {
          "appId": "xxx",
          "displayName": "xxx",
          "name": "xxx",
          "password": "xxx",
          "tenant": "xxx"
        }
    ```
3. Exportamos las variables de entorno de Azure para poder usarlas.
   De los datos obtenidos en el paso anterior necesitamos el appId,tenant y password, además del id de subscripción que tambien puedes cosultarlo mediante el comando ```az account list```.
    ```
      export AZURE_CLIENT_ID="xxx"
      export AZURE_TENANT_ID="xxx"
      export AZURE_CLIENT_SECRET="xxx"
      export AZURE_SUBSCRIPTION_ID="xxx"
    ```
<a name="vagrantfile"></a>
## Vagrantfile
  Este es el archivo de configuración de Vagrant, en el que vamos a especificar todo lo necesario
  para el despliegue de Azure y su provisionamiento. [[4]](#vagrantfileAzure)[[2]](#confvagrantfile)

```
#Versión Vagrant
Vagrant.configure("2") do |config|
#Indicamos la imagen base
  config.vm.box = "azure"
  config.vm.box_url = 'https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box'
  # Path de la clave privada ssh
  config.ssh.private_key_path = "~/.ssh/id_rsa"

#Configuración máquina Azure
  config.vm.provider :azure do |azure, override|
    #Credenciales Azure
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    azure.vm_image_urn = 'Canonical:UbuntuServer:18.04-LTS:latest'
    azure.vm_name = 'gestenergy-azure'
    azure.resource_group_name = 'gestenergy-azure'
    azure.location = 'westeurope'
    azure.vm_size = 'Standard_B1ms'
    azure.tcp_endpoints = '5000'

  end
#Mapeamos el puerto
  config.vm.network "forwarded_port", guest: 5000, host: 5000
 # Provisionamiento con Ansible
    config.vm.provision "ansible" do |ansible|
	     ansible.playbook = "despliegue/playbook.yml"
    end

end
```

- ```Vagrant.configure("2") do |config|``` indica la versión del objeto de Vagrant con la que vamos a trabajar, versión 2, en mi caso tengo la versión 2.2.6.

- Especificamos la dummy box que vamos a configurar en config.vm.provider.
  ```config.vm.box = "azure"
  config.vm.box_url = 'https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box'
  ```
- ```config.ssh.private_key_path = "~/.ssh/id_rsa"``` Indica la ruta a la clave privada que se utilizará para SSH en la máquina invitada.

- Credenciales necesarias para el despliegue en Azure, que exportamos anteriormente.
    ```
    config.vm.provider :azure do |azure, override|
      azure.tenant_id = ENV['AZURE_TENANT_ID']
      azure.client_id = ENV['AZURE_CLIENT_ID']
      azure.client_secret = ENV['AZURE_CLIENT_SECRET']
      azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']
    ```

- ```azure.vm_name = 'gestenergy-azure'``` Nombre que tendrá nuestra máquina virtual.
- ```azure.resource_group_name = 'gestenergy-azure''``` Nombre del grupo de recursos que va a utilizar.
- ```azure.location = 'westeurope' ``` Ubicación de Azure para compilar la VM

- ```azure.vm_size = 'Standard_B1ms'``` Indica el tamaño elegido de la máquina virtual, es una máquina serie B ideal para cargas de trabajo que no necesitan un rendimiento completo de la CPU de forma continua, como es el caso de mi aplicación. Además se ha elegido esta por ser una de las más baratas con un costo estimado de 15,06 €/mes, cuenta con 2GiB de RAM, 1 CPU y 4 GiB de almacenamiento [[5]](#azuremaquinas)

- ```azure.tcp_endpoints = '5000'``` Abrimos el puerto 5000 necesario para poder acceder a la aplicación.

- Con estas líneas indicamos que vamos a provisionar la máquina mediante Ansible, además de especificar la ubicación de nuestro archivo de provisionamiento (Playbook.yml).
  ```
     config.vm.provision "ansible" do |ansible|
     ansible.playbook = "despliegue/playbook.yml"
  ```

- ```azure.vm_image_urn = 'Canonical:UbuntuServer:18.04-LTS:latest'``` Indicamos la imagen VM elegida, obtenemos una lista de las VM de nuestra región con el comando.```az vm image list --location westeurope```
He elegido ```Canonical:UbuntuServer:18.04-LTS:latest'``` por ser una versión reciente y estable de Ubuntu.

<a name="playbook"></a>
## Ansible Playbook.yml
Provisionamos mediante Ansible creando un archivo llamado Playbook.yml, éste contendrá todas las órdenes de instalación con lo necesario para el provisionamiento de nuestra máquina virtual. Como el lenguaje de programación, instalar git, alguna dependencia que no sea estrictamente del lenguaje de programación...
Para el despliegue en Azure además de esto es necesario tener instalado git, clonar el repositorio y ejecutar la aplicación.

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

  - name: Inicia aplicación
    make:
           chdir: /home/vagrant/GestEnergy
           file: /home/vagrant/GestEnergy/Makefile
           target: start


```
- ```hosts: all```: la máquina virtual será accesible desde todos los hosts.
- ```become: yes```: usamos permisos de superusuario para instalar nuestras tareas que se indican a continuación.
- ```tasks:```: indicamos una serie de tareas  que instalarán todo lo necesario en nuestra máquina virtual para la ejecución de nuestra aplicación.

    - Actualizamos para que la máquina conozca los paquetes disponibles.

      ```
      - name: Actualizacion (apt-get update)
        apt: update_cache=yes  
          upgrade=yes
      ```
    - Instalamos python3, el lenguaje de nuestro microservicio.

      ```
      - name: Instalacion python3
        apt: name=python3-setuptools state=present

      ```
    - Instalación de pip3 para instalar dependencias.

      ```
      - name: Instalacion pip3
        apt:  name=python3-pip state=present

      ```
    - Instalación de git para posteriormente poder clonar el repositorio de nuestro microservicio.
      ```
      - name: Instalacion git
        apt: name=git state=present
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
        apt: name=nodejs state=present

      - name: Instalacion npm
        apt: name=npm state=present

      - name: Instalacion pm2
        command: npm install -g pm2

      ```
    - Ejecución de la aplicación. Se ejecutará mediante la orden creada en el Makefile con el target start, esta orden ejecuta la aplicación a través del gestor de procesos pm2 con gunicorn ```pm2 start 'gunicorn gestenergy.ge_app:app -b 0000:5000 -w 2' --name "api"```.

      ```
        - name: Inicia aplicación
          make:
                 chdir: /home/vagrant/GestEnergy
                 file: /home/vagrant/GestEnergy/Makefile
                 target: start
        ```

Notas:
- state=present: comprueba si está instalado, si no lo instala.
- update_cache=yes: equivale a apt-get update. Se puede ejecutar como parte de la instalación del paquete o como un paso separado.
<a name="despliegue"></a>
## Despliegue VM en Azure
Una vez que esté todo correctamente configurado se desplegará nuestra VM en Azure, para ello
se ha creado en el Makefile una orden llamada make fulldeployment que levantará la máquina virtual
y la provisionará.
Podemos consultar la ip pública donde se ha desplegado nuestra VM desde la Web de Azure.

La URL donde se ha desplegado es la siguiente:

  > http://40.68.146.104:5000


## Referencias
- <a name="azure1"> [[1] Azure CLI]( https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest)</a>
- <a name="confvagrantfile"> [[2]  Configuración Vagrantile  Azure](https://blog.scottlowe.org/2017/12/11/using-vagrant-with-azure/)</a>
- <a name="gruporecursos"> [[3]Crear grupo recursos Azure](https://docs.microsoft.com/en-us/cli/azure/group?view=azure-cli-latest#az-group-create)</a>
- <a name="vagrantfileAzure"> [[4] Vagrantile Azure](https://github.com/Azure/vagrant-azure)</a>
- <a name="azuremaquinas"> [[5] Maquinas Azure](https://docs.microsoft.com/es-es/azure/virtual-machines/windows/sizes-general)</a>



