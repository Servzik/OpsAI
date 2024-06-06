
variable "network_name" {
  description = "Name of the network"
  type        = string
}

variable "subnet_name" {
  description = "Name of the subnet"
  type        = string
}

variable "subnet_cidr" {
  description = "CIDR range for the subnet"
  type        = string
}

variable "cluster_name" {
  description = "Name of the GKE cluster"
  type        = string
}

variable "node_count" {
  description = "number of nodes in the node pool"
  type        = number
}

variable "machine_type" {
  description = "Type of machine to use for nodes"
  type        = string
}
