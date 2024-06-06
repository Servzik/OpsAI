module "network" {
  source       = "./network"
  network_name = "test-network"
}

module "subnet" {
  source      = "./subnet"
  subnet_name = "test-subnet"
  subnet_cidr = "10.0.0.0/24"
  region      = "us-central1"
}

module "gke" {
  source       = "./gke"
  cluster_name = "test-gke-cluster"
  node_count   = 2
  machine_type = "n1-standard-2"
}
