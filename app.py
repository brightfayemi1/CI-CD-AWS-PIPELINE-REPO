#!/usr/bin/env python3
import aws_cdk as cdk
from ci_cd_aws_pipeline.ci_cd_aws_pipeline_stack import MyPipelineStack

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack",
    env=cdk.Environment(account="777833739537", region="us-east-1")
)

app.synth()