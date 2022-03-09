provider "aws" {
  region = var.aws_secondary_region
  alias = "secondary"
}


module "application-cluster"{
  source = "./modules/appkluster"
}

module "data-cluster"{
  source = "./modules/datakluster"
}

module "data_endpoints" {
  source = "./modules/dataendpoint"
}

module "postgres" {
  source = "./modules/postgres"
}
