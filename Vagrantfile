
#Versión Vagrant
Vagrant.configure("2") do |config|

#Indicamos la imagen base
  config.vm.box = "bento/ubuntu-18.04"
#Mapeamos el puerto
  config.vm.network "forwarded_port", guest: 5000, host: 5000
 # Provisionamiento con Ansible
    config.vm.provision "ansible" do |ansible|
	  ansible.playbook = "provision/playbook.yml"
  end
end
