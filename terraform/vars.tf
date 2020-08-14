variable "env" {
  type = string
}

variable "app" {
  type    = string
  default = "domain-manager"
}

variable "region" {
  type    = string
  default = "us-east-1"
}

variable "vpc_id" {
  type = string
}

variable "private_subnet_ids" {
  type = list(string)
}

variable "public_subnet_ids" {
  type = list(string)
}

variable "docdb_instance_class" {
  type    = string
  default = "db.r5.large"
}

variable "ssm_hosted_zone_id_arn" {
  type = string
}

variable "image_repo" {
  type = string
}

variable "image_tag" {
  type = string
}
