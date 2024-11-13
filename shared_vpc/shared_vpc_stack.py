from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    CfnOutput
)
from constructs import Construct

class SharedVpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "SharedVPC",
            ip_addresses = ec2.IpAddresses.cidr("10.100.0.0/16"),
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public",
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    name="Private",
                    cidr_mask=24
                )
            ]
        )

        CfnOutput(self, "VpcId", value=vpc.vpc_id, export_name="SharedVpcId")

        CfnOutput(self, "VpcCidr", value=vpc.vpc_cidr_block, export_name="SharedVpcCidr")
        
        CfnOutput(
            self, "AvailabilityZones", value=", ".join(vpc.availability_zones), 
            export_name="SharedAvailabilityZones")

        CfnOutput(
            self, "PublicSubnetIds", 
            value=",".join([subnet.subnet_id for subnet in vpc.public_subnets]), 
            export_name="SharedPublicSubnetIds"
            )
            
        CfnOutput(
            self, "PrivateSubnetIds", 
            value=",".join([subnet.subnet_id for subnet in vpc.private_subnets]), 
            export_name="SharedPrivateSubnetIds"
            )

        CfnOutput(
            self, "PublicRouteTableIds",
            value=','.join([public_subnet.route_table.route_table_id for public_subnet in vpc.public_subnets]),
            export_name="SharedPublicRouteTableIds"
        )

        CfnOutput(
            self, "PrivateRouteTableIds",
            value=','.join([private_subnet.route_table.route_table_id for private_subnet in vpc.private_subnets]),
            export_name="SharedPrivateRouteTableIds"
        )