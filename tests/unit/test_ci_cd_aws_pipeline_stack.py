import aws_cdk as core
import aws_cdk.assertions as assertions

from ci_cd_aws_pipeline.ci_cd_aws_pipeline_stack import CiCdAwsPipelineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ci_cd_aws_pipeline/ci_cd_aws_pipeline_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CiCdAwsPipelineStack(app, "ci-cd-aws-pipeline")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
