module "data-endpoints" {
  source = "terraform-aws-modules/vpc/aws//modules/vpc-endpoints"

  vpc_id             = module.datavpc.vpc_id
  security_group_ids = ["sg-123456789"]

  endpoints = {
    s3 = {
      # interface endpoint
      service             = "s3"
      tags                = { Name = "s3-vpc-endpoint" }
    },
    }

  tags = {
    Owner       = "user"
    Environment = "prod"
  }
}

resource "aws_vpc_endpoint" "ec2" {
  vpc_id            = module.datavpc.vpc_id
  vpc_endpoint_type = "Interface"
  service_name      = "com.amazonaws.eu-west-1.ec2"

  security_group_ids = [
    aws_security_group.datavpc.id
  ]

  subnet_ids = local.subnets

  private_dns_enabled = true

  tags = {
      "Name"       = "ec2",
      "service"    = "network"
      "prod"       = "prod" 
    }
}
