
#Versión Vagrant
Vagrant.configure("2") do |config|
#Indicamos la imagen base
  config.vm.box = "azure"
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'
  config.ssh.private_key_path = "~/.ssh/id_rsa"

  config.vm.provider :azure do |azure, override|
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    azure.vm_name = 'gestenergy-azure'
    azure.resource_group_name = 'gestenergy-azure'
    azure.location = 'westeurope'
    azure.vm_size = 'Standard_B1s'
    azure.tcp_endpoints = '5000'
    azure.vm_image_urn = 'Canonical:UbuntuServer:18.04-LTS:latest'
  end
#Mapeamos el puerto
  config.vm.network "forwarded_port", guest: 5000, host: 5000
 # Provisionamiento con Ansible
    config.vm.provision "ansible" do |ansible|
	     ansible.playbook = "despliegue/playbook.yml"
    end

end
