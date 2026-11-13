Vagrant.configure("2") do |config|
  # Nodo Coordinador
  config.vm.define "coordinador" do |coord|
    coord.vm.box = "ubuntu/jammy64"
    coord.vm.network "private_network", ip: "192.168.56.10"
    coord.vm.hostname = "coordinador"
  end

  # Nodo Worker 1
  config.vm.define "worker1" do |w1|
    w1.box = "ubuntu/jammy64"
    w1.network "private_network", ip: "192.168.56.11"
    w1.hostname = "worker1"
  end

  # Nodo Worker 2
  config.vm.define "worker2" do |w2|
    w2.box = "ubuntu/jammy64"
    w2.network "private_network", ip: "192.168.56.12"
    w2.hostname = "worker2"
  end
end
