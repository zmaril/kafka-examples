# vi: set ft=ruby

VAGRANTFILE_API_VERSION = "2"

SSH_PORT = 2232

Vagrant.require_version ">= 1.5.0"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    #config.vm.box = "chef/ubuntu-14.04"
    config.vm.box = "chef/debian-7.8" 
    # awkward fix for SSH reassignment issue (re-evaluate w/ Vagrant 1.5.4)
    config.vm.network :forwarded_port, guest: 22, host: 2222, id: "ssh", disabled: true
    config.vm.network :forwarded_port, guest: 22, host: SSH_PORT, auto_correct: true

    config.vm.define "python" do |python|
        python.vm.network "private_network", ip: "10.42.2.105"

        python.vm.synced_folder "scripts", "/python/scripts"
        
        python.vm.provider "virtualbox" do |v| 
            v.name = "python"
        end

        python.vm.provision "ansible" do |ansible|
            ansible.playbook = "ansible/python.yml"
            ansible.inventory_path = "ansible/hosts.vagrant"
            ansible.limit = "all"
            # needed for common tasks to avoid EBS & checkout over synced_folders
            ansible.extra_vars = { deploy_type: "vagrant" }
            # seems to avoid the delay with private IP not being available
            ansible.verbose = 'vvvv'
            ansible.raw_arguments = ["-T 30"]
            ansible.host_key_checking = false
        end
    end

    config.vm.define "kafka" do |kafka|
        kafka.vm.network "private_network", ip: "10.42.2.106"

        kafka.vm.provider "virtualbox" do |v| 
            v.name = "kafka"
        end

        kafka.vm.provision "ansible" do |ansible|
            ansible.playbook = "ansible/kafka.yml"
            ansible.inventory_path = "ansible/hosts.vagrant"
            ansible.limit = "all"
            # needed for common tasks to avoid EBS & checkout over synced_folders
            ansible.extra_vars = { deploy_type: "vagrant" }
            # seems to avoid the delay with private IP not being available
            ansible.verbose = 'vvvv'
            ansible.raw_arguments = ["-T 30"]
            ansible.host_key_checking = false
        end
    end

    config.vm.define "postgres" do |postgres|
        postgres.vm.network "private_network", ip: "10.42.2.107"        

        postgres.vm.provider "virtualbox" do |v| 
            v.name = "postgres"
        end

        postgres.vm.provision "ansible" do |ansible|
            ansible.playbook = "ansible/postgres.yml"
            ansible.inventory_path = "ansible/hosts.vagrant"
            ansible.limit = "all"
            # needed for common tasks to avoid EBS & checkout over synced_folders
            ansible.extra_vars = { deploy_type: "vagrant" }
            # seems to avoid the delay with private IP not being available
            ansible.verbose = 'vvvv'
            ansible.raw_arguments = ["-T 30"]
            ansible.host_key_checking = false
        end
    end
end
