#!/usr/bin/env python3
import os

import aws_cdk as cdk

from iac.iac_stack import IacStack


app = cdk.App()

tags = {
    "project": "MicrosoftAuthorizer",
    "stage": "prod",
    "stack": "BACK",
    "owner": "DevCommunity",
}

IacStack(
    app,
    "MicrosoftAuthorizerStack",
    env=cdk.Environment(
        account=os.environ["AWS_ACCOUNT_ID"], region=os.environ["AWS_REGION"]
    ),
    tags=tags,
)

app.synth()
