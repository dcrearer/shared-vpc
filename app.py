#!/usr/bin/env python3
import os

import aws_cdk as cdk

from shared_vpc.shared_vpc_stack import SharedVpcStack


app = cdk.App()
SharedVpcStack(app, "SharedVpcStack",
    #AWS Account and Region that are implied by the current CLI configuration.
    env=cdk.Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'), 
        region=os.getenv('CDK_DEFAULT_REGION')
    )
)

app.synth()