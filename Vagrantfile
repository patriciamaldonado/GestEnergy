
#Versión Vagrant
Vagrant.configure("2") do |config|
#Indicamos la imagen base
  config.vm.box = "bento/ubuntu-18.04"

 # Provisionamiento con Ansible
    config.vm.provision "ansible" do |ansible|
	  ansible.playbook = "playbook.yml"
  end
end
