import os

from constructs import Construct
from aws_cdk import Stack, aws_lambda as _lambda


class IacStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        GRAPH_MICROSOFT_ENDPOINT = os.environ.get("GRAPH_MICROSOFT_ENDPOINT", None)

        # Creating a Authorizer Lambda
        authorizer_lambda = _lambda.Function(
            self,
            "AuthorizerLambda",
            runtime=_lambda.Runtime.PYTHON_3_11,
            code=_lambda.Code.from_asset("../src"),
            handler="microsoft_authorizer.lambda_handler",
            code=_lambda.Code.from_asset("lambda/authorizer"),
            environment={
                "GRAPH_MICROSOFT_ENDPOINT": GRAPH_MICROSOFT_ENDPOINT,
            },
        )
