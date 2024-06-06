provider "google" {
  credentials = file("path/service-account-key.json") #path of the service account
  project     = "test-project-id"
  region      = "us-central1"
}
