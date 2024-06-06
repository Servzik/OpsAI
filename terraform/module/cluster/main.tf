resource "google_container_cluster" "test_cluster" {
  name     = var.cluster_name
  location = var.region

  network    = var.network_name
  subnetwork = google_compute_subnetwork.my_subnet.name

  node_pool {
    name       = "default-pool"
    node_count = var.node_count
    machine_type = var.machine_type
  }
}
