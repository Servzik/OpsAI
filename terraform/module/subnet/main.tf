resource "google_compute_subnetwork" "test_subnet" {
  name          = var.subnet_name
  ip_cidr_range = var.subnet_cidr
  network       = var.network_name
  region        = var.region
}
