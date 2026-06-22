# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/Welcome.html

# Welcome

AWS Identity and Access Management Access Analyzer helps you to set, verify, and refine your IAM policies by providing a suite of capabilities. Its features include findings for external, internal, and unused access, basic and custom policy checks for validating policies, and policy generation to generate fine-grained policies. To start using IAM Access Analyzer to identify external, internal, or unused access, you first need to create an analyzer.

**External access analyzers** help you identify potential risks of accessing resources by enabling you to identify any resource policies that grant access to an external principal. It does this by using logic-based reasoning to analyze resource-based policies in your AWS environment. An external principal can be another AWS account, a root user, an IAM user or role, a federated user, an AWS service, or an anonymous user. You can also use IAM Access Analyzer to preview public and cross-account access to your resources before deploying permissions changes.

**Internal access analyzers** help you identify which principals within your organization or account have access to selected resources. This analysis supports implementing the principle of least privilege by ensuring that your specified resources can only be accessed by the intended principals within your organization.

**Unused access analyzers** help you identify potential identity access risks by enabling you to identify unused IAM roles, unused access keys, unused console passwords, and IAM principals with unused service and action-level permissions.

Beyond findings, IAM Access Analyzer provides basic and custom policy checks to validate IAM policies before deploying permissions changes. You can use policy generation to refine permissions by attaching a policy generated using access activity logged in CloudTrail logs. 

This guide describes the IAM Access Analyzer operations that you can call programmatically. For general information about IAM Access Analyzer, see [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) in the **IAM User Guide**.

This document was last published on June 22, 2026. 

**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Actions


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Operations.html

# Actions

The following actions are supported:

  * [ApplyArchiveRule](./API_ApplyArchiveRule.html)

  * [CancelPolicyGeneration](./API_CancelPolicyGeneration.html)

  * [CheckAccessNotGranted](./API_CheckAccessNotGranted.html)

  * [CheckNoNewAccess](./API_CheckNoNewAccess.html)

  * [CheckNoPublicAccess](./API_CheckNoPublicAccess.html)

  * [CreateAccessPreview](./API_CreateAccessPreview.html)

  * [CreateAnalyzer](./API_CreateAnalyzer.html)

  * [CreateArchiveRule](./API_CreateArchiveRule.html)

  * [DeleteAnalyzer](./API_DeleteAnalyzer.html)

  * [DeleteArchiveRule](./API_DeleteArchiveRule.html)

  * [GenerateFindingRecommendation](./API_GenerateFindingRecommendation.html)

  * [GetAccessPreview](./API_GetAccessPreview.html)

  * [GetAnalyzedResource](./API_GetAnalyzedResource.html)

  * [GetAnalyzer](./API_GetAnalyzer.html)

  * [GetArchiveRule](./API_GetArchiveRule.html)

  * [GetFinding](./API_GetFinding.html)

  * [GetFindingRecommendation](./API_GetFindingRecommendation.html)

  * [GetFindingsStatistics](./API_GetFindingsStatistics.html)

  * [GetFindingV2](./API_GetFindingV2.html)

  * [GetGeneratedPolicy](./API_GetGeneratedPolicy.html)

  * [ListAccessPreviewFindings](./API_ListAccessPreviewFindings.html)

  * [ListAccessPreviews](./API_ListAccessPreviews.html)

  * [ListAnalyzedResources](./API_ListAnalyzedResources.html)

  * [ListAnalyzers](./API_ListAnalyzers.html)

  * [ListArchiveRules](./API_ListArchiveRules.html)

  * [ListFindings](./API_ListFindings.html)

  * [ListFindingsV2](./API_ListFindingsV2.html)

  * [ListPolicyGenerations](./API_ListPolicyGenerations.html)

  * [ListTagsForResource](./API_ListTagsForResource.html)

  * [StartPolicyGeneration](./API_StartPolicyGeneration.html)

  * [StartResourceScan](./API_StartResourceScan.html)

  * [TagResource](./API_TagResource.html)

  * [UntagResource](./API_UntagResource.html)

  * [UpdateAnalyzer](./API_UpdateAnalyzer.html)

  * [UpdateArchiveRule](./API_UpdateArchiveRule.html)

  * [UpdateFindings](./API_UpdateFindings.html)

  * [ValidatePolicy](./API_ValidatePolicy.html)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Welcome

ApplyArchiveRule


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ApplyArchiveRule.html

# ApplyArchiveRule

Retroactively applies the archive rule to existing findings that meet the archive rule criteria.

## Request Syntax
    
    
    PUT /archive-rule HTTP/1.1
    Content-type: application/json
    
    {
       "analyzerArn": "string",
       "clientToken": "string",
       "ruleName": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**analyzerArn **
    

The Amazon resource name (ARN) of the analyzer.

Type: String

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**clientToken **
    

A client token.

Type: String

Required: No

**ruleName **
    

The name of the rule to apply.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ApplyArchiveRule)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ApplyArchiveRule)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ApplyArchiveRule)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ApplyArchiveRule)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ApplyArchiveRule)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ApplyArchiveRule)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ApplyArchiveRule)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ApplyArchiveRule)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ApplyArchiveRule)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ApplyArchiveRule)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Actions

CancelPolicyGeneration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CancelPolicyGeneration.html

# CancelPolicyGeneration

Cancels the requested policy generation.

## Request Syntax
    
    
    PUT /policy/generation/jobId HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**jobId **
    

The `JobId` that is returned by the `StartPolicyGeneration` operation. The `JobId` can be used with `GetGeneratedPolicy` to retrieve the generated policies or used with `CancelPolicyGeneration` to cancel the policy generation request.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/CancelPolicyGeneration)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/CancelPolicyGeneration)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CancelPolicyGeneration)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/CancelPolicyGeneration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CancelPolicyGeneration)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/CancelPolicyGeneration)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/CancelPolicyGeneration)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/CancelPolicyGeneration)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/CancelPolicyGeneration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CancelPolicyGeneration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ApplyArchiveRule

CheckAccessNotGranted


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckAccessNotGranted.html

# CheckAccessNotGranted

Checks whether the specified access isn't allowed by a policy.

## Request Syntax
    
    
    POST /policy/check-access-not-granted HTTP/1.1
    Content-type: application/json
    
    {
       "access": [ 
          { 
             "[actions](./API_Access.html#accessanalyzer-Type-Access-actions)": [ "string" ],
             "[resources](./API_Access.html#accessanalyzer-Type-Access-resources)": [ "string" ]
          }
       ],
       "policyDocument": "string",
       "policyType": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**access **
    

An access object containing the permissions that shouldn't be granted by the specified policy. If only actions are specified, IAM Access Analyzer checks for access to peform at least one of the actions on any resource in the policy. If only resources are specified, then IAM Access Analyzer checks for access to perform any action on at least one of the resources. If both actions and resources are specified, IAM Access Analyzer checks for access to perform at least one of the specified actions on at least one of the specified resources.

Type: Array of [Access](./API_Access.html) objects

Array Members: Minimum number of 0 items. Maximum number of 1 item.

Required: Yes

**policyDocument **
    

The JSON policy document to use as the content for the policy.

Type: String

Required: Yes

**policyType **
    

The type of policy. Identity policies grant permissions to IAM principals. Identity policies include managed and inline policies for IAM roles, users, and groups.

Resource policies grant permissions on AWS resources. Resource policies include trust policies for IAM roles and bucket policies for Amazon S3 buckets.

Type: String

Valid Values: `IDENTITY_POLICY | RESOURCE_POLICY`

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "message": "**_string_** ",
       "reasons": [ 
          { 
             "[description](./API_ReasonSummary.html#accessanalyzer-Type-ReasonSummary-description)": "**_string_** ",
             "[statementId](./API_ReasonSummary.html#accessanalyzer-Type-ReasonSummary-statementId)": "**_string_** ",
             "[statementIndex](./API_ReasonSummary.html#accessanalyzer-Type-ReasonSummary-statementIndex)": **_number_**
          }
       ],
       "result": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**message **
    

The message indicating whether the specified access is allowed.

Type: String

**reasons **
    

A description of the reasoning of the result.

Type: Array of [ReasonSummary](./API_ReasonSummary.html) objects

**result **
    

The result of the check for whether the access is allowed. If the result is `PASS`, the specified policy doesn't allow any of the specified permissions in the access object. If the result is `FAIL`, the specified policy might allow some or all of the permissions in the access object.

Type: String

Valid Values: `PASS | FAIL`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**InvalidParameterException**
    

The specified parameter is invalid.

HTTP Status Code: 400

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**UnprocessableEntityException**
    

The specified entity could not be processed.

HTTP Status Code: 422

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/CheckAccessNotGranted)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/CheckAccessNotGranted)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CheckAccessNotGranted)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/CheckAccessNotGranted)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CheckAccessNotGranted)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/CheckAccessNotGranted)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/CheckAccessNotGranted)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/CheckAccessNotGranted)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/CheckAccessNotGranted)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CheckAccessNotGranted)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

CancelPolicyGeneration

CheckNoNewAccess


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckNoNewAccess.html

# CheckNoNewAccess

Checks whether new access is allowed for an updated policy when compared to the existing policy.

You can find examples for reference policies and learn how to set up and run a custom policy check for new access in the [IAM Access Analyzer custom policy checks samples](https://github.com/aws-samples/iam-access-analyzer-custom-policy-check-samples) repository on GitHub. The reference policies in this repository are meant to be passed to the `existingPolicyDocument` request parameter.

## Request Syntax
    
    
    POST /policy/check-no-new-access HTTP/1.1
    Content-type: application/json
    
    {
       "existingPolicyDocument": "string",
       "newPolicyDocument": "string",
       "policyType": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**existingPolicyDocument **
    

The JSON policy document to use as the content for the existing policy.

Type: String

Required: Yes

**newPolicyDocument **
    

The JSON policy document to use as the content for the updated policy.

Type: String

Required: Yes

**policyType **
    

The type of policy to compare. Identity policies grant permissions to IAM principals. Identity policies include managed and inline policies for IAM roles, users, and groups.

Resource policies grant permissions on AWS resources. Resource policies include trust policies for IAM roles and bucket policies for Amazon S3 buckets. You can provide a generic input such as identity policy or resource policy or a specific input such as managed policy or Amazon S3 bucket policy.

Type: String

Valid Values: `IDENTITY_POLICY | RESOURCE_POLICY`

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "message": "**_string_** ",
       "reasons": [ 
          { 
             "[description](./API_ReasonSummary.html#accessanalyzer-Type-ReasonSummary-description)": "**_string_** ",
             "[statementId](./API_ReasonSummary.html#accessanalyzer-Type-ReasonSummary-statementId)": "**_string_** ",
             "[statementIndex](./API_ReasonSummary.html#accessanalyzer-Type-ReasonSummary-statementIndex)": **_number_**
          }
       ],
       "result": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**message **
    

The message indicating whether the updated policy allows new access.

Type: String

**reasons **
    

A description of the reasoning of the result.

Type: Array of [ReasonSummary](./API_ReasonSummary.html) objects

**result **
    

The result of the check for new access. If the result is `PASS`, no new access is allowed by the updated policy. If the result is `FAIL`, the updated policy might allow new access.

Type: String

Valid Values: `PASS | FAIL`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**InvalidParameterException**
    

The specified parameter is invalid.

HTTP Status Code: 400

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**UnprocessableEntityException**
    

The specified entity could not be processed.

HTTP Status Code: 422

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/CheckNoNewAccess)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/CheckNoNewAccess)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CheckNoNewAccess)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/CheckNoNewAccess)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CheckNoNewAccess)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/CheckNoNewAccess)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/CheckNoNewAccess)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/CheckNoNewAccess)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/CheckNoNewAccess)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CheckNoNewAccess)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

CheckAccessNotGranted

CheckNoPublicAccess


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckNoPublicAccess.html

# CheckNoPublicAccess

Checks whether a resource policy can grant public access to the specified resource type.

## Request Syntax
    
    
    POST /policy/check-no-public-access HTTP/1.1
    Content-type: application/json
    
    {
       "policyDocument": "string",
       "resourceType": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**policyDocument **
    

The JSON policy document to evaluate for public access.

Type: String

Required: Yes

**resourceType **
    

The type of resource to evaluate for public access. For example, to check for public access to Amazon S3 buckets, you can choose `AWS::S3::Bucket` for the resource type.

For resource types not supported as valid values, IAM Access Analyzer will return an error.

Type: String

Valid Values: `AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::EFS::FileSystem | AWS::OpenSearchService::Domain | AWS::Kinesis::Stream | AWS::Kinesis::StreamConsumer | AWS::KMS::Key | AWS::Lambda::Function | AWS::S3::Bucket | AWS::S3::AccessPoint | AWS::S3Express::DirectoryBucket | AWS::S3::Glacier | AWS::S3Outposts::Bucket | AWS::S3Outposts::AccessPoint | AWS::SecretsManager::Secret | AWS::SNS::Topic | AWS::SQS::Queue | AWS::IAM::AssumeRolePolicyDocument | AWS::S3Tables::TableBucket | AWS::ApiGateway::RestApi | AWS::CodeArtifact::Domain | AWS::Backup::BackupVault | AWS::CloudTrail::Dashboard | AWS::CloudTrail::EventDataStore | AWS::S3Tables::Table | AWS::S3Express::AccessPoint`

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "message": "**_string_** ",
       "reasons": [ 
          { 
             "[description](./API_ReasonSummary.html#accessanalyzer-Type-ReasonSummary-description)": "**_string_** ",
             "[statementId](./API_ReasonSummary.html#accessanalyzer-Type-ReasonSummary-statementId)": "**_string_** ",
             "[statementIndex](./API_ReasonSummary.html#accessanalyzer-Type-ReasonSummary-statementIndex)": **_number_**
          }
       ],
       "result": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**message **
    

The message indicating whether the specified policy allows public access to resources.

Type: String

**reasons **
    

A list of reasons why the specified resource policy grants public access for the resource type.

Type: Array of [ReasonSummary](./API_ReasonSummary.html) objects

**result **
    

The result of the check for public access to the specified resource type. If the result is `PASS`, the policy doesn't allow public access to the specified resource type. If the result is `FAIL`, the policy might allow public access to the specified resource type.

Type: String

Valid Values: `PASS | FAIL`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**InvalidParameterException**
    

The specified parameter is invalid.

HTTP Status Code: 400

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**UnprocessableEntityException**
    

The specified entity could not be processed.

HTTP Status Code: 422

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/CheckNoPublicAccess)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/CheckNoPublicAccess)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CheckNoPublicAccess)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/CheckNoPublicAccess)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CheckNoPublicAccess)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/CheckNoPublicAccess)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/CheckNoPublicAccess)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/CheckNoPublicAccess)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/CheckNoPublicAccess)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CheckNoPublicAccess)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

CheckNoNewAccess

CreateAccessPreview


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CreateAccessPreview.html

# CreateAccessPreview

Creates an access preview that allows you to preview IAM Access Analyzer findings for your resource before deploying resource permissions.

## Request Syntax
    
    
    PUT /access-preview HTTP/1.1
    Content-type: application/json
    
    {
       "analyzerArn": "string",
       "clientToken": "string",
       "configurations": { 
          "string" : { ... }
       }
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**analyzerArn **
    

The [ARN of the account analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) used to generate the access preview. You can only create an access preview for analyzers with an `Account` type and `Active` status.

Type: String

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**clientToken **
    

A client token.

Type: String

Required: No

**configurations **
    

Access control configuration for your resource that is used to generate the access preview. The access preview includes findings for external access allowed to the resource with the proposed access control configuration. The configuration must contain exactly one element.

Type: String to [Configuration](./API_Configuration.html) object map

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "id": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**id **
    

The unique ID for the access preview.

Type: String

Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**ConflictException**
    

A conflict exception error.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The resource type.

HTTP Status Code: 409

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ServiceQuotaExceededException**
    

Service quote met error.

**resourceId**
    

The resource ID.

**resourceType**
    

The resource type.

HTTP Status Code: 402

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/CreateAccessPreview)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/CreateAccessPreview)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CreateAccessPreview)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/CreateAccessPreview)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CreateAccessPreview)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/CreateAccessPreview)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/CreateAccessPreview)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/CreateAccessPreview)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/CreateAccessPreview)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CreateAccessPreview)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

CheckNoPublicAccess

CreateAnalyzer


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CreateAnalyzer.html

# CreateAnalyzer

Creates an analyzer for your account.

## Request Syntax
    
    
    PUT /analyzer HTTP/1.1
    Content-type: application/json
    
    {
       "analyzerName": "string",
       "archiveRules": [ 
          { 
             "[filter](./API_InlineArchiveRule.html#accessanalyzer-Type-InlineArchiveRule-filter)": { 
                "string" : { 
                   "[contains](./API_Criterion.html#accessanalyzer-Type-Criterion-contains)": [ "string" ],
                   "[eq](./API_Criterion.html#accessanalyzer-Type-Criterion-eq)": [ "string" ],
                   "[exists](./API_Criterion.html#accessanalyzer-Type-Criterion-exists)": boolean,
                   "[neq](./API_Criterion.html#accessanalyzer-Type-Criterion-neq)": [ "string" ]
                }
             },
             "[ruleName](./API_InlineArchiveRule.html#accessanalyzer-Type-InlineArchiveRule-ruleName)": "string"
          }
       ],
       "clientToken": "string",
       "configuration": { ... },
       "tags": { 
          "string" : "string" 
       },
       "type": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**analyzerName **
    

The name of the analyzer to create.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

**archiveRules **
    

Specifies the archive rules to add for the analyzer. Archive rules automatically archive findings that meet the criteria you define for the rule.

Type: Array of [InlineArchiveRule](./API_InlineArchiveRule.html) objects

Required: No

**clientToken **
    

A client token.

Type: String

Required: No

**configuration **
    

Specifies the configuration of the analyzer. If the analyzer is an unused access analyzer, the specified scope of unused access is used for the configuration. If the analyzer is an internal access analyzer, the specified internal access analysis rules are used for the configuration.

Type: [AnalyzerConfiguration](./API_AnalyzerConfiguration.html) object

**Note:** This object is a Union. Only one member of this object can be specified or returned.

Required: No

**tags **
    

An array of key-value pairs to apply to the analyzer. You can use the set of Unicode letters, digits, whitespace, `_`, `.`, `/`, `=`, `+`, and `-`.

For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with `aws:`.

For the tag value, you can specify a value that is 0 to 256 characters in length.

Type: String to string map

Required: No

**type **
    

The type of analyzer to create. You can create only one analyzer per account per Region. You can create up to 5 analyzers per organization per Region.

Type: String

Valid Values: `ACCOUNT | ORGANIZATION | ACCOUNT_UNUSED_ACCESS | ORGANIZATION_UNUSED_ACCESS | ACCOUNT_INTERNAL_ACCESS | ORGANIZATION_INTERNAL_ACCESS`

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "arn": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**arn **
    

The ARN of the analyzer that was created by the request.

Type: String

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**ConflictException**
    

A conflict exception error.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The resource type.

HTTP Status Code: 409

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ServiceQuotaExceededException**
    

Service quote met error.

**resourceId**
    

The resource ID.

**resourceType**
    

The resource type.

HTTP Status Code: 402

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/CreateAnalyzer)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/CreateAnalyzer)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CreateAnalyzer)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/CreateAnalyzer)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CreateAnalyzer)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/CreateAnalyzer)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/CreateAnalyzer)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/CreateAnalyzer)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/CreateAnalyzer)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CreateAnalyzer)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

CreateAccessPreview

CreateArchiveRule


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CreateArchiveRule.html

# CreateArchiveRule

Creates an archive rule for the specified analyzer. Archive rules automatically archive new findings that meet the criteria you define when you create the rule.

To learn about filter keys that you can use to create an archive rule, see [IAM Access Analyzer filter keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html) in the **IAM User Guide**.

## Request Syntax
    
    
    PUT /analyzer/analyzerName/archive-rule HTTP/1.1
    Content-type: application/json
    
    {
       "clientToken": "string",
       "filter": { 
          "string" : { 
             "[contains](./API_Criterion.html#accessanalyzer-Type-Criterion-contains)": [ "string" ],
             "[eq](./API_Criterion.html#accessanalyzer-Type-Criterion-eq)": [ "string" ],
             "[exists](./API_Criterion.html#accessanalyzer-Type-Criterion-exists)": boolean,
             "[neq](./API_Criterion.html#accessanalyzer-Type-Criterion-neq)": [ "string" ]
          }
       },
       "ruleName": "string"
    }

## URI Request Parameters

The request uses the following URI parameters.

**analyzerName **
    

The name of the created analyzer.

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**clientToken **
    

A client token.

Type: String

Required: No

**filter **
    

The criteria for the rule.

Type: String to [Criterion](./API_Criterion.html) object map

Required: Yes

**ruleName **
    

The name of the rule to create.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**ConflictException**
    

A conflict exception error.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The resource type.

HTTP Status Code: 409

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ServiceQuotaExceededException**
    

Service quote met error.

**resourceId**
    

The resource ID.

**resourceType**
    

The resource type.

HTTP Status Code: 402

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/CreateArchiveRule)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/CreateArchiveRule)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CreateArchiveRule)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/CreateArchiveRule)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CreateArchiveRule)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/CreateArchiveRule)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/CreateArchiveRule)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/CreateArchiveRule)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/CreateArchiveRule)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CreateArchiveRule)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

CreateAnalyzer

DeleteAnalyzer


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_DeleteAnalyzer.html

# DeleteAnalyzer

Deletes the specified analyzer. When you delete an analyzer, IAM Access Analyzer is disabled for the account or organization in the current or specific Region. All findings that were generated by the analyzer are deleted. You cannot undo this action.

## Request Syntax
    
    
    DELETE /analyzer/analyzerName?clientToken=clientToken HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**analyzerName **
    

The name of the analyzer to delete.

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

**clientToken **
    

A client token.

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/DeleteAnalyzer)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/DeleteAnalyzer)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/DeleteAnalyzer)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/DeleteAnalyzer)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/DeleteAnalyzer)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/DeleteAnalyzer)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/DeleteAnalyzer)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/DeleteAnalyzer)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/DeleteAnalyzer)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/DeleteAnalyzer)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

CreateArchiveRule

DeleteArchiveRule


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_DeleteArchiveRule.html

# DeleteArchiveRule

Deletes the specified archive rule.

## Request Syntax
    
    
    DELETE /analyzer/analyzerName/archive-rule/ruleName?clientToken=clientToken HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**analyzerName **
    

The name of the analyzer that associated with the archive rule to delete.

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

**clientToken **
    

A client token.

**ruleName **
    

The name of the rule to delete.

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/DeleteArchiveRule)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/DeleteArchiveRule)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/DeleteArchiveRule)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/DeleteArchiveRule)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/DeleteArchiveRule)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/DeleteArchiveRule)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/DeleteArchiveRule)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/DeleteArchiveRule)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/DeleteArchiveRule)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/DeleteArchiveRule)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

DeleteAnalyzer

GenerateFindingRecommendation


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GenerateFindingRecommendation.html

# GenerateFindingRecommendation

Creates a recommendation for an unused permissions finding.

## Request Syntax
    
    
    POST /recommendation/id?analyzerArn=analyzerArn HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) used to generate the finding recommendation.

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**id **
    

The unique ID for the finding recommendation.

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GenerateFindingRecommendation)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GenerateFindingRecommendation)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GenerateFindingRecommendation)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GenerateFindingRecommendation)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GenerateFindingRecommendation)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GenerateFindingRecommendation)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GenerateFindingRecommendation)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GenerateFindingRecommendation)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GenerateFindingRecommendation)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GenerateFindingRecommendation)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

DeleteArchiveRule

GetAccessPreview


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAccessPreview.html

# GetAccessPreview

Retrieves information about an access preview for the specified analyzer.

## Request Syntax
    
    
    GET /access-preview/accessPreviewId?analyzerArn=analyzerArn HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**accessPreviewId **
    

The unique ID for the access preview.

Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

Required: Yes

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) used to generate the access preview.

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "accessPreview": { 
          "[analyzerArn](./API_AccessPreview.html#accessanalyzer-Type-AccessPreview-analyzerArn)": "**_string_** ",
          "[configurations](./API_AccessPreview.html#accessanalyzer-Type-AccessPreview-configurations)": { 
             "**_string_** " : { ... }
          },
          "[createdAt](./API_AccessPreview.html#accessanalyzer-Type-AccessPreview-createdAt)": "**_string_** ",
          "[id](./API_AccessPreview.html#accessanalyzer-Type-AccessPreview-id)": "**_string_** ",
          "[status](./API_AccessPreview.html#accessanalyzer-Type-AccessPreview-status)": "**_string_** ",
          "[statusReason](./API_AccessPreview.html#accessanalyzer-Type-AccessPreview-statusReason)": { 
             "[code](./API_AccessPreviewStatusReason.html#accessanalyzer-Type-AccessPreviewStatusReason-code)": "**_string_** "
          }
       }
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**accessPreview **
    

An object that contains information about the access preview.

Type: [AccessPreview](./API_AccessPreview.html) object

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetAccessPreview)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetAccessPreview)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetAccessPreview)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetAccessPreview)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetAccessPreview)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetAccessPreview)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetAccessPreview)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetAccessPreview)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetAccessPreview)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetAccessPreview)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GenerateFindingRecommendation

GetAnalyzedResource


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAnalyzedResource.html

# GetAnalyzedResource

Retrieves information about a resource that was analyzed.

###### Note

This action is supported only for external access analyzers.

## Request Syntax
    
    
    GET /analyzed-resource?analyzerArn=analyzerArn&resourceArn=resourceArn HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) to retrieve information from.

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**resourceArn **
    

The ARN of the resource to retrieve information about.

Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "resource": { 
          "[actions](./API_AnalyzedResource.html#accessanalyzer-Type-AnalyzedResource-actions)": [ "**_string_** " ],
          "[analyzedAt](./API_AnalyzedResource.html#accessanalyzer-Type-AnalyzedResource-analyzedAt)": "**_string_** ",
          "[createdAt](./API_AnalyzedResource.html#accessanalyzer-Type-AnalyzedResource-createdAt)": "**_string_** ",
          "[error](./API_AnalyzedResource.html#accessanalyzer-Type-AnalyzedResource-error)": "**_string_** ",
          "[isPublic](./API_AnalyzedResource.html#accessanalyzer-Type-AnalyzedResource-isPublic)": **_boolean_** ,
          "[resourceArn](./API_AnalyzedResource.html#accessanalyzer-Type-AnalyzedResource-resourceArn)": "**_string_** ",
          "[resourceOwnerAccount](./API_AnalyzedResource.html#accessanalyzer-Type-AnalyzedResource-resourceOwnerAccount)": "**_string_** ",
          "[resourceType](./API_AnalyzedResource.html#accessanalyzer-Type-AnalyzedResource-resourceType)": "**_string_** ",
          "[sharedVia](./API_AnalyzedResource.html#accessanalyzer-Type-AnalyzedResource-sharedVia)": [ "**_string_** " ],
          "[status](./API_AnalyzedResource.html#accessanalyzer-Type-AnalyzedResource-status)": "**_string_** ",
          "[updatedAt](./API_AnalyzedResource.html#accessanalyzer-Type-AnalyzedResource-updatedAt)": "**_string_** "
       }
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**resource **
    

An `AnalyzedResource` object that contains information that IAM Access Analyzer found when it analyzed the resource.

Type: [AnalyzedResource](./API_AnalyzedResource.html) object

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetAnalyzedResource)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetAnalyzedResource)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetAnalyzedResource)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetAnalyzedResource)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetAnalyzedResource)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetAnalyzedResource)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetAnalyzedResource)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetAnalyzedResource)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetAnalyzedResource)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetAnalyzedResource)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetAccessPreview

GetAnalyzer


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAnalyzer.html

# GetAnalyzer

Retrieves information about the specified analyzer.

## Request Syntax
    
    
    GET /analyzer/analyzerName HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**analyzerName **
    

The name of the analyzer retrieved.

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "analyzer": { 
          "[arn](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-arn)": "**_string_** ",
          "[configuration](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-configuration)": { ... },
          "[createdAt](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-createdAt)": "**_string_** ",
          "[lastResourceAnalyzed](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-lastResourceAnalyzed)": "**_string_** ",
          "[lastResourceAnalyzedAt](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-lastResourceAnalyzedAt)": "**_string_** ",
          "[name](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-name)": "**_string_** ",
          "[status](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-status)": "**_string_** ",
          "[statusReason](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-statusReason)": { 
             "[code](./API_StatusReason.html#accessanalyzer-Type-StatusReason-code)": "**_string_** "
          },
          "[tags](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-tags)": { 
             "**_string_** " : "**_string_** " 
          },
          "[type](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-type)": "**_string_** "
       }
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**analyzer **
    

An `AnalyzerSummary` object that contains information about the analyzer.

Type: [AnalyzerSummary](./API_AnalyzerSummary.html) object

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetAnalyzer)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetAnalyzer)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetAnalyzer)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetAnalyzer)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetAnalyzer)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetAnalyzer)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetAnalyzer)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetAnalyzer)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetAnalyzer)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetAnalyzer)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetAnalyzedResource

GetArchiveRule


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetArchiveRule.html

# GetArchiveRule

Retrieves information about an archive rule.

To learn about filter keys that you can use to create an archive rule, see [IAM Access Analyzer filter keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html) in the **IAM User Guide**.

## Request Syntax
    
    
    GET /analyzer/analyzerName/archive-rule/ruleName HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**analyzerName **
    

The name of the analyzer to retrieve rules from.

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

**ruleName **
    

The name of the rule to retrieve.

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "archiveRule": { 
          "[createdAt](./API_ArchiveRuleSummary.html#accessanalyzer-Type-ArchiveRuleSummary-createdAt)": "**_string_** ",
          "[filter](./API_ArchiveRuleSummary.html#accessanalyzer-Type-ArchiveRuleSummary-filter)": { 
             "**_string_** " : { 
                "[contains](./API_Criterion.html#accessanalyzer-Type-Criterion-contains)": [ "**_string_** " ],
                "[eq](./API_Criterion.html#accessanalyzer-Type-Criterion-eq)": [ "**_string_** " ],
                "[exists](./API_Criterion.html#accessanalyzer-Type-Criterion-exists)": **_boolean_** ,
                "[neq](./API_Criterion.html#accessanalyzer-Type-Criterion-neq)": [ "**_string_** " ]
             }
          },
          "[ruleName](./API_ArchiveRuleSummary.html#accessanalyzer-Type-ArchiveRuleSummary-ruleName)": "**_string_** ",
          "[updatedAt](./API_ArchiveRuleSummary.html#accessanalyzer-Type-ArchiveRuleSummary-updatedAt)": "**_string_** "
       }
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**archiveRule **
    

Contains information about an archive rule. Archive rules automatically archive new findings that meet the criteria you define when you create the rule.

Type: [ArchiveRuleSummary](./API_ArchiveRuleSummary.html) object

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetArchiveRule)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetArchiveRule)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetArchiveRule)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetArchiveRule)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetArchiveRule)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetArchiveRule)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetArchiveRule)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetArchiveRule)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetArchiveRule)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetArchiveRule)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetAnalyzer

GetFinding


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetFinding.html

# GetFinding

Retrieves information about the specified finding. GetFinding and GetFindingV2 both use `access-analyzer:GetFinding` in the `Action` element of an IAM policy statement. You must have permission to perform the `access-analyzer:GetFinding` action.

###### Note

GetFinding is supported only for external access analyzers. You must use GetFindingV2 for internal and unused access analyzers.

## Request Syntax
    
    
    GET /finding/id?analyzerArn=analyzerArn HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) that generated the finding.

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**id **
    

The ID of the finding to retrieve.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "finding": { 
          "[action](./API_Finding.html#accessanalyzer-Type-Finding-action)": [ "**_string_** " ],
          "[analyzedAt](./API_Finding.html#accessanalyzer-Type-Finding-analyzedAt)": "**_string_** ",
          "[condition](./API_Finding.html#accessanalyzer-Type-Finding-condition)": { 
             "**_string_** " : "**_string_** " 
          },
          "[createdAt](./API_Finding.html#accessanalyzer-Type-Finding-createdAt)": "**_string_** ",
          "[error](./API_Finding.html#accessanalyzer-Type-Finding-error)": "**_string_** ",
          "[id](./API_Finding.html#accessanalyzer-Type-Finding-id)": "**_string_** ",
          "[isPublic](./API_Finding.html#accessanalyzer-Type-Finding-isPublic)": **_boolean_** ,
          "[principal](./API_Finding.html#accessanalyzer-Type-Finding-principal)": { 
             "**_string_** " : "**_string_** " 
          },
          "[resource](./API_Finding.html#accessanalyzer-Type-Finding-resource)": "**_string_** ",
          "[resourceControlPolicyRestriction](./API_Finding.html#accessanalyzer-Type-Finding-resourceControlPolicyRestriction)": "**_string_** ",
          "[resourceOwnerAccount](./API_Finding.html#accessanalyzer-Type-Finding-resourceOwnerAccount)": "**_string_** ",
          "[resourceType](./API_Finding.html#accessanalyzer-Type-Finding-resourceType)": "**_string_** ",
          "[sources](./API_Finding.html#accessanalyzer-Type-Finding-sources)": [ 
             { 
                "[detail](./API_FindingSource.html#accessanalyzer-Type-FindingSource-detail)": { 
                   "[accessPointAccount](./API_FindingSourceDetail.html#accessanalyzer-Type-FindingSourceDetail-accessPointAccount)": "**_string_** ",
                   "[accessPointArn](./API_FindingSourceDetail.html#accessanalyzer-Type-FindingSourceDetail-accessPointArn)": "**_string_** "
                },
                "[type](./API_FindingSource.html#accessanalyzer-Type-FindingSource-type)": "**_string_** "
             }
          ],
          "[status](./API_Finding.html#accessanalyzer-Type-Finding-status)": "**_string_** ",
          "[updatedAt](./API_Finding.html#accessanalyzer-Type-Finding-updatedAt)": "**_string_** "
       }
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**finding **
    

A `finding` object that contains finding details.

Type: [Finding](./API_Finding.html) object

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetFinding)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetFinding)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetFinding)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetFinding)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetFinding)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetFinding)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetFinding)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetFinding)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetFinding)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetFinding)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetArchiveRule

GetFindingRecommendation


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetFindingRecommendation.html

# GetFindingRecommendation

Retrieves information about a finding recommendation for the specified analyzer.

## Request Syntax
    
    
    GET /recommendation/id?analyzerArn=analyzerArn&maxResults=maxResults&nextToken=nextToken HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) used to generate the finding recommendation.

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**id **
    

The unique ID for the finding recommendation.

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

**maxResults **
    

The maximum number of results to return in the response.

Valid Range: Minimum value of 1. Maximum value of 1000.

**nextToken **
    

A token used for pagination of results returned.

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "completedAt": "**_string_** ",
       "error": { 
          "[code](./API_RecommendationError.html#accessanalyzer-Type-RecommendationError-code)": "**_string_** ",
          "[message](./API_RecommendationError.html#accessanalyzer-Type-RecommendationError-message)": "**_string_** "
       },
       "nextToken": "**_string_** ",
       "recommendationType": "**_string_** ",
       "recommendedSteps": [ 
          { ... }
       ],
       "resourceArn": "**_string_** ",
       "startedAt": "**_string_** ",
       "status": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**completedAt **
    

The time at which the retrieval of the finding recommendation was completed.

Type: Timestamp

**error **
    

Detailed information about the reason that the retrieval of a recommendation for the finding failed.

Type: [RecommendationError](./API_RecommendationError.html) object

**nextToken **
    

A token used for pagination of results returned.

Type: String

**recommendationType **
    

The type of recommendation for the finding.

Type: String

Valid Values: `UnusedPermissionRecommendation`

**recommendedSteps **
    

A group of recommended steps for the finding.

Type: Array of [RecommendedStep](./API_RecommendedStep.html) objects

**resourceArn **
    

The ARN of the resource of the finding.

Type: String

Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

**startedAt **
    

The time at which the retrieval of the finding recommendation was started.

Type: Timestamp

**status **
    

The status of the retrieval of the finding recommendation.

Type: String

Valid Values: `SUCCEEDED | FAILED | IN_PROGRESS`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetFindingRecommendation)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetFindingRecommendation)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetFindingRecommendation)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetFindingRecommendation)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetFindingRecommendation)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetFindingRecommendation)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetFindingRecommendation)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetFindingRecommendation)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetFindingRecommendation)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetFindingRecommendation)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetFinding

GetFindingsStatistics


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetFindingsStatistics.html

# GetFindingsStatistics

Retrieves a list of aggregated finding statistics for an external access or unused access analyzer.

## Request Syntax
    
    
    POST /analyzer/findings/statistics HTTP/1.1
    Content-type: application/json
    
    {
       "analyzerArn": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) used to generate the statistics.

Type: String

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "findingsStatistics": [ 
          { ... }
       ],
       "lastUpdatedAt": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**findingsStatistics **
    

A group of external access or unused access findings statistics.

Type: Array of [FindingsStatistics](./API_FindingsStatistics.html) objects

**lastUpdatedAt **
    

The time at which the retrieval of the findings statistics was last updated. If the findings statistics have not been previously retrieved for the specified analyzer, this field will not be populated.

Type: Timestamp

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetFindingsStatistics)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetFindingsStatistics)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetFindingsStatistics)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetFindingsStatistics)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetFindingsStatistics)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetFindingsStatistics)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetFindingsStatistics)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetFindingsStatistics)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetFindingsStatistics)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetFindingsStatistics)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetFindingRecommendation

GetFindingV2


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetFindingV2.html

# GetFindingV2

Retrieves information about the specified finding. GetFinding and GetFindingV2 both use `access-analyzer:GetFinding` in the `Action` element of an IAM policy statement. You must have permission to perform the `access-analyzer:GetFinding` action.

## Request Syntax
    
    
    GET /findingv2/id?analyzerArn=analyzerArn&maxResults=maxResults&nextToken=nextToken HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) that generated the finding.

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**id **
    

The ID of the finding to retrieve.

Required: Yes

**maxResults **
    

The maximum number of results to return in the response.

**nextToken **
    

A token used for pagination of results returned.

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "analyzedAt": "**_string_** ",
       "createdAt": "**_string_** ",
       "error": "**_string_** ",
       "findingDetails": [ 
          { ... }
       ],
       "findingType": "**_string_** ",
       "id": "**_string_** ",
       "nextToken": "**_string_** ",
       "resource": "**_string_** ",
       "resourceOwnerAccount": "**_string_** ",
       "resourceType": "**_string_** ",
       "status": "**_string_** ",
       "updatedAt": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**analyzedAt **
    

The time at which the resource-based policy or IAM entity that generated the finding was analyzed.

Type: Timestamp

**createdAt **
    

The time at which the finding was created.

Type: Timestamp

**error **
    

An error.

Type: String

**findingDetails **
    

A localized message that explains the finding and provides guidance on how to address it.

Type: Array of [FindingDetails](./API_FindingDetails.html) objects

**findingType **
    

The type of the finding. For external access analyzers, the type is `ExternalAccess`. For unused access analyzers, the type can be `UnusedIAMRole`, `UnusedIAMUserAccessKey`, `UnusedIAMUserPassword`, or `UnusedPermission`. For internal access analyzers, the type is `InternalAccess`.

Type: String

Valid Values: `ExternalAccess | UnusedIAMRole | UnusedIAMUserAccessKey | UnusedIAMUserPassword | UnusedPermission | InternalAccess`

**id **
    

The ID of the finding to retrieve.

Type: String

**nextToken **
    

A token used for pagination of results returned.

Type: String

**resource **
    

The resource that generated the finding.

Type: String

**resourceOwnerAccount **
    

Tye AWS account ID that owns the resource.

Type: String

**resourceType **
    

The type of the resource identified in the finding.

Type: String

Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`

**status **
    

The status of the finding.

Type: String

Valid Values: `ACTIVE | ARCHIVED | RESOLVED`

**updatedAt **
    

The time at which the finding was updated.

Type: Timestamp

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetFindingV2)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetFindingV2)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetFindingV2)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetFindingV2)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetFindingV2)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetFindingV2)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetFindingV2)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetFindingV2)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetFindingV2)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetFindingV2)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetFindingsStatistics

GetGeneratedPolicy


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetGeneratedPolicy.html

# GetGeneratedPolicy

Retrieves the policy that was generated using `StartPolicyGeneration`. 

## Request Syntax
    
    
    GET /policy/generation/jobId?includeResourcePlaceholders=includeResourcePlaceholders&includeServiceLevelTemplate=includeServiceLevelTemplate HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**includeResourcePlaceholders **
    

The level of detail that you want to generate. You can specify whether to generate policies with placeholders for resource ARNs for actions that support resource level granularity in policies.

For example, in the resource section of a policy, you can receive a placeholder such as `"Resource":"arn:aws:s3:::${BucketName}"` instead of `"*"`.

**includeServiceLevelTemplate **
    

The level of detail that you want to generate. You can specify whether to generate service-level policies. 

IAM Access Analyzer uses `iam:servicelastaccessed` to identify services that have been used recently to create this service-level template.

**jobId **
    

The `JobId` that is returned by the `StartPolicyGeneration` operation. The `JobId` can be used with `GetGeneratedPolicy` to retrieve the generated policies or used with `CancelPolicyGeneration` to cancel the policy generation request.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "generatedPolicyResult": { 
          "[generatedPolicies](./API_GeneratedPolicyResult.html#accessanalyzer-Type-GeneratedPolicyResult-generatedPolicies)": [ 
             { 
                "[policy](./API_GeneratedPolicy.html#accessanalyzer-Type-GeneratedPolicy-policy)": "**_string_** "
             }
          ],
          "[properties](./API_GeneratedPolicyResult.html#accessanalyzer-Type-GeneratedPolicyResult-properties)": { 
             "[cloudTrailProperties](./API_GeneratedPolicyProperties.html#accessanalyzer-Type-GeneratedPolicyProperties-cloudTrailProperties)": { 
                "[endTime](./API_CloudTrailProperties.html#accessanalyzer-Type-CloudTrailProperties-endTime)": "**_string_** ",
                "[startTime](./API_CloudTrailProperties.html#accessanalyzer-Type-CloudTrailProperties-startTime)": "**_string_** ",
                "[trailProperties](./API_CloudTrailProperties.html#accessanalyzer-Type-CloudTrailProperties-trailProperties)": [ 
                   { 
                      "[allRegions](./API_TrailProperties.html#accessanalyzer-Type-TrailProperties-allRegions)": **_boolean_** ,
                      "[cloudTrailArn](./API_TrailProperties.html#accessanalyzer-Type-TrailProperties-cloudTrailArn)": "**_string_** ",
                      "[regions](./API_TrailProperties.html#accessanalyzer-Type-TrailProperties-regions)": [ "**_string_** " ]
                   }
                ]
             },
             "[isComplete](./API_GeneratedPolicyProperties.html#accessanalyzer-Type-GeneratedPolicyProperties-isComplete)": **_boolean_** ,
             "[principalArn](./API_GeneratedPolicyProperties.html#accessanalyzer-Type-GeneratedPolicyProperties-principalArn)": "**_string_** "
          }
       },
       "jobDetails": { 
          "[completedOn](./API_JobDetails.html#accessanalyzer-Type-JobDetails-completedOn)": "**_string_** ",
          "[jobError](./API_JobDetails.html#accessanalyzer-Type-JobDetails-jobError)": { 
             "[code](./API_JobError.html#accessanalyzer-Type-JobError-code)": "**_string_** ",
             "[message](./API_JobError.html#accessanalyzer-Type-JobError-message)": "**_string_** "
          },
          "[jobId](./API_JobDetails.html#accessanalyzer-Type-JobDetails-jobId)": "**_string_** ",
          "[startedOn](./API_JobDetails.html#accessanalyzer-Type-JobDetails-startedOn)": "**_string_** ",
          "[status](./API_JobDetails.html#accessanalyzer-Type-JobDetails-status)": "**_string_** "
       }
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**generatedPolicyResult **
    

A `GeneratedPolicyResult` object that contains the generated policies and associated details.

Type: [GeneratedPolicyResult](./API_GeneratedPolicyResult.html) object

**jobDetails **
    

A `GeneratedPolicyDetails` object that contains details about the generated policy.

Type: [JobDetails](./API_JobDetails.html) object

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetGeneratedPolicy)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetGeneratedPolicy)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetGeneratedPolicy)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetGeneratedPolicy)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetGeneratedPolicy)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetGeneratedPolicy)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetGeneratedPolicy)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetGeneratedPolicy)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetGeneratedPolicy)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetGeneratedPolicy)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetFindingV2

ListAccessPreviewFindings


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAccessPreviewFindings.html

# ListAccessPreviewFindings

Retrieves a list of access preview findings generated by the specified access preview.

## Request Syntax
    
    
    POST /access-preview/accessPreviewId HTTP/1.1
    Content-type: application/json
    
    {
       "analyzerArn": "string",
       "filter": { 
          "string" : { 
             "[contains](./API_Criterion.html#accessanalyzer-Type-Criterion-contains)": [ "string" ],
             "[eq](./API_Criterion.html#accessanalyzer-Type-Criterion-eq)": [ "string" ],
             "[exists](./API_Criterion.html#accessanalyzer-Type-Criterion-exists)": boolean,
             "[neq](./API_Criterion.html#accessanalyzer-Type-Criterion-neq)": [ "string" ]
          }
       },
       "maxResults": number,
       "nextToken": "string"
    }

## URI Request Parameters

The request uses the following URI parameters.

**accessPreviewId **
    

The unique ID for the access preview.

Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) used to generate the access.

Type: String

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**filter **
    

Criteria to filter the returned findings.

Type: String to [Criterion](./API_Criterion.html) object map

Required: No

**maxResults **
    

The maximum number of results to return in the response.

Type: Integer

Required: No

**nextToken **
    

A token used for pagination of results returned.

Type: String

Required: No

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "findings": [ 
          { 
             "[action](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-action)": [ "**_string_** " ],
             "[changeType](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-changeType)": "**_string_** ",
             "[condition](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-condition)": { 
                "**_string_** " : "**_string_** " 
             },
             "[createdAt](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-createdAt)": "**_string_** ",
             "[error](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-error)": "**_string_** ",
             "[existingFindingId](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-existingFindingId)": "**_string_** ",
             "[existingFindingStatus](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-existingFindingStatus)": "**_string_** ",
             "[id](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-id)": "**_string_** ",
             "[isPublic](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-isPublic)": **_boolean_** ,
             "[principal](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-principal)": { 
                "**_string_** " : "**_string_** " 
             },
             "[resource](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-resource)": "**_string_** ",
             "[resourceControlPolicyRestriction](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-resourceControlPolicyRestriction)": "**_string_** ",
             "[resourceOwnerAccount](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-resourceOwnerAccount)": "**_string_** ",
             "[resourceType](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-resourceType)": "**_string_** ",
             "[sources](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-sources)": [ 
                { 
                   "[detail](./API_FindingSource.html#accessanalyzer-Type-FindingSource-detail)": { 
                      "[accessPointAccount](./API_FindingSourceDetail.html#accessanalyzer-Type-FindingSourceDetail-accessPointAccount)": "**_string_** ",
                      "[accessPointArn](./API_FindingSourceDetail.html#accessanalyzer-Type-FindingSourceDetail-accessPointArn)": "**_string_** "
                   },
                   "[type](./API_FindingSource.html#accessanalyzer-Type-FindingSource-type)": "**_string_** "
                }
             ],
             "[status](./API_AccessPreviewFinding.html#accessanalyzer-Type-AccessPreviewFinding-status)": "**_string_** "
          }
       ],
       "nextToken": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**findings **
    

A list of access preview findings that match the specified filter criteria.

Type: Array of [AccessPreviewFinding](./API_AccessPreviewFinding.html) objects

**nextToken **
    

A token used for pagination of results returned.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**ConflictException**
    

A conflict exception error.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The resource type.

HTTP Status Code: 409

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ListAccessPreviewFindings)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ListAccessPreviewFindings)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ListAccessPreviewFindings)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ListAccessPreviewFindings)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ListAccessPreviewFindings)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ListAccessPreviewFindings)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ListAccessPreviewFindings)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ListAccessPreviewFindings)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ListAccessPreviewFindings)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ListAccessPreviewFindings)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetGeneratedPolicy

ListAccessPreviews


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAccessPreviews.html

# ListAccessPreviews

Retrieves a list of access previews for the specified analyzer.

## Request Syntax
    
    
    GET /access-preview?analyzerArn=analyzerArn&maxResults=maxResults&nextToken=nextToken HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) used to generate the access preview.

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**maxResults **
    

The maximum number of results to return in the response.

**nextToken **
    

A token used for pagination of results returned.

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "accessPreviews": [ 
          { 
             "[analyzerArn](./API_AccessPreviewSummary.html#accessanalyzer-Type-AccessPreviewSummary-analyzerArn)": "**_string_** ",
             "[createdAt](./API_AccessPreviewSummary.html#accessanalyzer-Type-AccessPreviewSummary-createdAt)": "**_string_** ",
             "[id](./API_AccessPreviewSummary.html#accessanalyzer-Type-AccessPreviewSummary-id)": "**_string_** ",
             "[status](./API_AccessPreviewSummary.html#accessanalyzer-Type-AccessPreviewSummary-status)": "**_string_** ",
             "[statusReason](./API_AccessPreviewSummary.html#accessanalyzer-Type-AccessPreviewSummary-statusReason)": { 
                "[code](./API_AccessPreviewStatusReason.html#accessanalyzer-Type-AccessPreviewStatusReason-code)": "**_string_** "
             }
          }
       ],
       "nextToken": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**accessPreviews **
    

A list of access previews retrieved for the analyzer.

Type: Array of [AccessPreviewSummary](./API_AccessPreviewSummary.html) objects

**nextToken **
    

A token used for pagination of results returned.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ListAccessPreviews)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ListAccessPreviews)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ListAccessPreviews)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ListAccessPreviews)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ListAccessPreviews)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ListAccessPreviews)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ListAccessPreviews)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ListAccessPreviews)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ListAccessPreviews)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ListAccessPreviews)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ListAccessPreviewFindings

ListAnalyzedResources


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAnalyzedResources.html

# ListAnalyzedResources

Retrieves a list of resources of the specified type that have been analyzed by the specified analyzer.

## Request Syntax
    
    
    POST /analyzed-resource HTTP/1.1
    Content-type: application/json
    
    {
       "analyzerArn": "string",
       "maxResults": number,
       "nextToken": "string",
       "resourceType": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) to retrieve a list of analyzed resources from.

Type: String

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**maxResults **
    

The maximum number of results to return in the response.

Type: Integer

Required: No

**nextToken **
    

A token used for pagination of results returned.

Type: String

Required: No

**resourceType **
    

The type of resource.

Type: String

Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`

Required: No

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "analyzedResources": [ 
          { 
             "[resourceArn](./API_AnalyzedResourceSummary.html#accessanalyzer-Type-AnalyzedResourceSummary-resourceArn)": "**_string_** ",
             "[resourceOwnerAccount](./API_AnalyzedResourceSummary.html#accessanalyzer-Type-AnalyzedResourceSummary-resourceOwnerAccount)": "**_string_** ",
             "[resourceType](./API_AnalyzedResourceSummary.html#accessanalyzer-Type-AnalyzedResourceSummary-resourceType)": "**_string_** "
          }
       ],
       "nextToken": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**analyzedResources **
    

A list of resources that were analyzed.

Type: Array of [AnalyzedResourceSummary](./API_AnalyzedResourceSummary.html) objects

**nextToken **
    

A token used for pagination of results returned.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ListAnalyzedResources)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ListAnalyzedResources)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ListAnalyzedResources)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ListAnalyzedResources)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ListAnalyzedResources)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ListAnalyzedResources)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ListAnalyzedResources)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ListAnalyzedResources)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ListAnalyzedResources)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ListAnalyzedResources)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ListAccessPreviews

ListAnalyzers


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAnalyzers.html

# ListAnalyzers

Retrieves a list of analyzers.

## Request Syntax
    
    
    GET /analyzer?maxResults=maxResults&nextToken=nextToken&type=type HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**maxResults **
    

The maximum number of results to return in the response.

**nextToken **
    

A token used for pagination of results returned.

**type **
    

The type of analyzer.

Valid Values: `ACCOUNT | ORGANIZATION | ACCOUNT_UNUSED_ACCESS | ORGANIZATION_UNUSED_ACCESS | ACCOUNT_INTERNAL_ACCESS | ORGANIZATION_INTERNAL_ACCESS`

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "analyzers": [ 
          { 
             "[arn](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-arn)": "**_string_** ",
             "[configuration](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-configuration)": { ... },
             "[createdAt](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-createdAt)": "**_string_** ",
             "[lastResourceAnalyzed](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-lastResourceAnalyzed)": "**_string_** ",
             "[lastResourceAnalyzedAt](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-lastResourceAnalyzedAt)": "**_string_** ",
             "[name](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-name)": "**_string_** ",
             "[status](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-status)": "**_string_** ",
             "[statusReason](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-statusReason)": { 
                "[code](./API_StatusReason.html#accessanalyzer-Type-StatusReason-code)": "**_string_** "
             },
             "[tags](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-tags)": { 
                "**_string_** " : "**_string_** " 
             },
             "[type](./API_AnalyzerSummary.html#accessanalyzer-Type-AnalyzerSummary-type)": "**_string_** "
          }
       ],
       "nextToken": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**analyzers **
    

The analyzers retrieved.

Type: Array of [AnalyzerSummary](./API_AnalyzerSummary.html) objects

**nextToken **
    

A token used for pagination of results returned.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ListAnalyzers)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ListAnalyzers)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ListAnalyzers)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ListAnalyzers)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ListAnalyzers)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ListAnalyzers)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ListAnalyzers)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ListAnalyzers)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ListAnalyzers)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ListAnalyzers)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ListAnalyzedResources

ListArchiveRules


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListArchiveRules.html

# ListArchiveRules

Retrieves a list of archive rules created for the specified analyzer.

## Request Syntax
    
    
    GET /analyzer/analyzerName/archive-rule?maxResults=maxResults&nextToken=nextToken HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**analyzerName **
    

The name of the analyzer to retrieve rules from.

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

**maxResults **
    

The maximum number of results to return in the request.

**nextToken **
    

A token used for pagination of results returned.

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "archiveRules": [ 
          { 
             "[createdAt](./API_ArchiveRuleSummary.html#accessanalyzer-Type-ArchiveRuleSummary-createdAt)": "**_string_** ",
             "[filter](./API_ArchiveRuleSummary.html#accessanalyzer-Type-ArchiveRuleSummary-filter)": { 
                "**_string_** " : { 
                   "[contains](./API_Criterion.html#accessanalyzer-Type-Criterion-contains)": [ "**_string_** " ],
                   "[eq](./API_Criterion.html#accessanalyzer-Type-Criterion-eq)": [ "**_string_** " ],
                   "[exists](./API_Criterion.html#accessanalyzer-Type-Criterion-exists)": **_boolean_** ,
                   "[neq](./API_Criterion.html#accessanalyzer-Type-Criterion-neq)": [ "**_string_** " ]
                }
             },
             "[ruleName](./API_ArchiveRuleSummary.html#accessanalyzer-Type-ArchiveRuleSummary-ruleName)": "**_string_** ",
             "[updatedAt](./API_ArchiveRuleSummary.html#accessanalyzer-Type-ArchiveRuleSummary-updatedAt)": "**_string_** "
          }
       ],
       "nextToken": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**archiveRules **
    

A list of archive rules created for the specified analyzer.

Type: Array of [ArchiveRuleSummary](./API_ArchiveRuleSummary.html) objects

**nextToken **
    

A token used for pagination of results returned.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ListArchiveRules)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ListArchiveRules)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ListArchiveRules)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ListArchiveRules)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ListArchiveRules)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ListArchiveRules)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ListArchiveRules)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ListArchiveRules)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ListArchiveRules)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ListArchiveRules)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ListAnalyzers

ListFindings


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListFindings.html

# ListFindings

Retrieves a list of findings generated by the specified analyzer. ListFindings and ListFindingsV2 both use `access-analyzer:ListFindings` in the `Action` element of an IAM policy statement. You must have permission to perform the `access-analyzer:ListFindings` action.

To learn about filter keys that you can use to retrieve a list of findings, see [IAM Access Analyzer filter keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html) in the **IAM User Guide**.

###### Note

ListFindings is supported only for external access analyzers. You must use ListFindingsV2 for internal and unused access analyzers.

## Request Syntax
    
    
    POST /finding HTTP/1.1
    Content-type: application/json
    
    {
       "analyzerArn": "string",
       "filter": { 
          "string" : { 
             "[contains](./API_Criterion.html#accessanalyzer-Type-Criterion-contains)": [ "string" ],
             "[eq](./API_Criterion.html#accessanalyzer-Type-Criterion-eq)": [ "string" ],
             "[exists](./API_Criterion.html#accessanalyzer-Type-Criterion-exists)": boolean,
             "[neq](./API_Criterion.html#accessanalyzer-Type-Criterion-neq)": [ "string" ]
          }
       },
       "maxResults": number,
       "nextToken": "string",
       "sort": { 
          "[attributeName](./API_SortCriteria.html#accessanalyzer-Type-SortCriteria-attributeName)": "string",
          "[orderBy](./API_SortCriteria.html#accessanalyzer-Type-SortCriteria-orderBy)": "string"
       }
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) to retrieve findings from.

Type: String

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**filter **
    

A filter to match for the findings to return.

Type: String to [Criterion](./API_Criterion.html) object map

Required: No

**maxResults **
    

The maximum number of results to return in the response.

Type: Integer

Required: No

**nextToken **
    

A token used for pagination of results returned.

Type: String

Required: No

**sort **
    

The sort order for the findings returned.

Type: [SortCriteria](./API_SortCriteria.html) object

Required: No

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "findings": [ 
          { 
             "[action](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-action)": [ "**_string_** " ],
             "[analyzedAt](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-analyzedAt)": "**_string_** ",
             "[condition](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-condition)": { 
                "**_string_** " : "**_string_** " 
             },
             "[createdAt](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-createdAt)": "**_string_** ",
             "[error](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-error)": "**_string_** ",
             "[id](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-id)": "**_string_** ",
             "[isPublic](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-isPublic)": **_boolean_** ,
             "[principal](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-principal)": { 
                "**_string_** " : "**_string_** " 
             },
             "[resource](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-resource)": "**_string_** ",
             "[resourceControlPolicyRestriction](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-resourceControlPolicyRestriction)": "**_string_** ",
             "[resourceOwnerAccount](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-resourceOwnerAccount)": "**_string_** ",
             "[resourceType](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-resourceType)": "**_string_** ",
             "[sources](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-sources)": [ 
                { 
                   "[detail](./API_FindingSource.html#accessanalyzer-Type-FindingSource-detail)": { 
                      "[accessPointAccount](./API_FindingSourceDetail.html#accessanalyzer-Type-FindingSourceDetail-accessPointAccount)": "**_string_** ",
                      "[accessPointArn](./API_FindingSourceDetail.html#accessanalyzer-Type-FindingSourceDetail-accessPointArn)": "**_string_** "
                   },
                   "[type](./API_FindingSource.html#accessanalyzer-Type-FindingSource-type)": "**_string_** "
                }
             ],
             "[status](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-status)": "**_string_** ",
             "[updatedAt](./API_FindingSummary.html#accessanalyzer-Type-FindingSummary-updatedAt)": "**_string_** "
          }
       ],
       "nextToken": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**findings **
    

A list of findings retrieved from the analyzer that match the filter criteria specified, if any.

Type: Array of [FindingSummary](./API_FindingSummary.html) objects

**nextToken **
    

A token used for pagination of results returned.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ListFindings)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ListFindings)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ListFindings)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ListFindings)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ListFindings)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ListFindings)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ListFindings)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ListFindings)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ListFindings)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ListFindings)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ListArchiveRules

ListFindingsV2


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListFindingsV2.html

# ListFindingsV2

Retrieves a list of findings generated by the specified analyzer. ListFindings and ListFindingsV2 both use `access-analyzer:ListFindings` in the `Action` element of an IAM policy statement. You must have permission to perform the `access-analyzer:ListFindings` action.

To learn about filter keys that you can use to retrieve a list of findings, see [IAM Access Analyzer filter keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html) in the **IAM User Guide**.

## Request Syntax
    
    
    POST /findingv2 HTTP/1.1
    Content-type: application/json
    
    {
       "analyzerArn": "string",
       "filter": { 
          "string" : { 
             "[contains](./API_Criterion.html#accessanalyzer-Type-Criterion-contains)": [ "string" ],
             "[eq](./API_Criterion.html#accessanalyzer-Type-Criterion-eq)": [ "string" ],
             "[exists](./API_Criterion.html#accessanalyzer-Type-Criterion-exists)": boolean,
             "[neq](./API_Criterion.html#accessanalyzer-Type-Criterion-neq)": [ "string" ]
          }
       },
       "maxResults": number,
       "nextToken": "string",
       "sort": { 
          "[attributeName](./API_SortCriteria.html#accessanalyzer-Type-SortCriteria-attributeName)": "string",
          "[orderBy](./API_SortCriteria.html#accessanalyzer-Type-SortCriteria-orderBy)": "string"
       }
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) to retrieve findings from.

Type: String

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**filter **
    

A filter to match for the findings to return.

Type: String to [Criterion](./API_Criterion.html) object map

Required: No

**maxResults **
    

The maximum number of results to return in the response.

Type: Integer

Required: No

**nextToken **
    

A token used for pagination of results returned.

Type: String

Required: No

**sort **
    

The criteria used to sort.

Type: [SortCriteria](./API_SortCriteria.html) object

Required: No

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "findings": [ 
          { 
             "[analyzedAt](./API_FindingSummaryV2.html#accessanalyzer-Type-FindingSummaryV2-analyzedAt)": "**_string_** ",
             "[createdAt](./API_FindingSummaryV2.html#accessanalyzer-Type-FindingSummaryV2-createdAt)": "**_string_** ",
             "[error](./API_FindingSummaryV2.html#accessanalyzer-Type-FindingSummaryV2-error)": "**_string_** ",
             "[findingType](./API_FindingSummaryV2.html#accessanalyzer-Type-FindingSummaryV2-findingType)": "**_string_** ",
             "[id](./API_FindingSummaryV2.html#accessanalyzer-Type-FindingSummaryV2-id)": "**_string_** ",
             "[resource](./API_FindingSummaryV2.html#accessanalyzer-Type-FindingSummaryV2-resource)": "**_string_** ",
             "[resourceOwnerAccount](./API_FindingSummaryV2.html#accessanalyzer-Type-FindingSummaryV2-resourceOwnerAccount)": "**_string_** ",
             "[resourceType](./API_FindingSummaryV2.html#accessanalyzer-Type-FindingSummaryV2-resourceType)": "**_string_** ",
             "[status](./API_FindingSummaryV2.html#accessanalyzer-Type-FindingSummaryV2-status)": "**_string_** ",
             "[updatedAt](./API_FindingSummaryV2.html#accessanalyzer-Type-FindingSummaryV2-updatedAt)": "**_string_** "
          }
       ],
       "nextToken": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**findings **
    

A list of findings retrieved from the analyzer that match the filter criteria specified, if any.

Type: Array of [FindingSummaryV2](./API_FindingSummaryV2.html) objects

**nextToken **
    

A token used for pagination of results returned.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ListFindingsV2)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ListFindingsV2)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ListFindingsV2)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ListFindingsV2)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ListFindingsV2)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ListFindingsV2)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ListFindingsV2)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ListFindingsV2)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ListFindingsV2)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ListFindingsV2)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ListFindings

ListPolicyGenerations


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListPolicyGenerations.html

# ListPolicyGenerations

Lists all of the policy generations requested in the last seven days.

## Request Syntax
    
    
    GET /policy/generation?maxResults=maxResults&nextToken=nextToken&principalArn=principalArn HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**maxResults **
    

The maximum number of results to return in the response.

Valid Range: Minimum value of 1.

**nextToken **
    

A token used for pagination of results returned.

**principalArn **
    

The ARN of the IAM entity (user or role) for which you are generating a policy. Use this with `ListGeneratedPolicies` to filter the results to only include results for a specific principal.

Pattern: `arn:[^:]*:iam::[^:]*:(role|user)/.{1,576}`

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "nextToken": "**_string_** ",
       "policyGenerations": [ 
          { 
             "[completedOn](./API_PolicyGeneration.html#accessanalyzer-Type-PolicyGeneration-completedOn)": "**_string_** ",
             "[jobId](./API_PolicyGeneration.html#accessanalyzer-Type-PolicyGeneration-jobId)": "**_string_** ",
             "[principalArn](./API_PolicyGeneration.html#accessanalyzer-Type-PolicyGeneration-principalArn)": "**_string_** ",
             "[startedOn](./API_PolicyGeneration.html#accessanalyzer-Type-PolicyGeneration-startedOn)": "**_string_** ",
             "[status](./API_PolicyGeneration.html#accessanalyzer-Type-PolicyGeneration-status)": "**_string_** "
          }
       ]
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**nextToken **
    

A token used for pagination of results returned.

Type: String

**policyGenerations **
    

A `PolicyGeneration` object that contains details about the generated policy.

Type: Array of [PolicyGeneration](./API_PolicyGeneration.html) objects

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ListPolicyGenerations)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ListPolicyGenerations)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ListPolicyGenerations)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ListPolicyGenerations)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ListPolicyGenerations)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ListPolicyGenerations)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ListPolicyGenerations)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ListPolicyGenerations)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ListPolicyGenerations)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ListPolicyGenerations)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ListFindingsV2

ListTagsForResource


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListTagsForResource.html

# ListTagsForResource

Retrieves a list of tags applied to the specified resource.

## Request Syntax
    
    
    GET /tags/resourceArn HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**resourceArn **
    

The ARN of the resource to retrieve tags from.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "tags": { 
          "**_string_** " : "**_string_** " 
       }
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**tags **
    

The tags that are applied to the specified resource.

Type: String to string map

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ListTagsForResource)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ListTagsForResource)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ListTagsForResource)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ListTagsForResource)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ListTagsForResource)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ListTagsForResource)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ListTagsForResource)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ListTagsForResource)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ListTagsForResource)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ListTagsForResource)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ListPolicyGenerations

StartPolicyGeneration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_StartPolicyGeneration.html

# StartPolicyGeneration

Starts the policy generation request.

## Request Syntax
    
    
    PUT /policy/generation HTTP/1.1
    Content-type: application/json
    
    {
       "clientToken": "string",
       "cloudTrailDetails": { 
          "[accessRole](./API_CloudTrailDetails.html#accessanalyzer-Type-CloudTrailDetails-accessRole)": "string",
          "[endTime](./API_CloudTrailDetails.html#accessanalyzer-Type-CloudTrailDetails-endTime)": "string",
          "[startTime](./API_CloudTrailDetails.html#accessanalyzer-Type-CloudTrailDetails-startTime)": "string",
          "[trails](./API_CloudTrailDetails.html#accessanalyzer-Type-CloudTrailDetails-trails)": [ 
             { 
                "[allRegions](./API_Trail.html#accessanalyzer-Type-Trail-allRegions)": boolean,
                "[cloudTrailArn](./API_Trail.html#accessanalyzer-Type-Trail-cloudTrailArn)": "string",
                "[regions](./API_Trail.html#accessanalyzer-Type-Trail-regions)": [ "string" ]
             }
          ]
       },
       "policyGenerationDetails": { 
          "[principalArn](./API_PolicyGenerationDetails.html#accessanalyzer-Type-PolicyGenerationDetails-principalArn)": "string"
       }
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**clientToken **
    

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.

If you do not specify a client token, one is automatically generated by the AWS SDK.

Type: String

Required: No

**cloudTrailDetails **
    

A `CloudTrailDetails` object that contains details about a `Trail` that you want to analyze to generate policies.

Type: [CloudTrailDetails](./API_CloudTrailDetails.html) object

Required: No

**policyGenerationDetails **
    

Contains the ARN of the IAM entity (user or role) for which you are generating a policy.

Type: [PolicyGenerationDetails](./API_PolicyGenerationDetails.html) object

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "jobId": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**jobId **
    

The `JobId` that is returned by the `StartPolicyGeneration` operation. The `JobId` can be used with `GetGeneratedPolicy` to retrieve the generated policies or used with `CancelPolicyGeneration` to cancel the policy generation request.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**ConflictException**
    

A conflict exception error.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The resource type.

HTTP Status Code: 409

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ServiceQuotaExceededException**
    

Service quote met error.

**resourceId**
    

The resource ID.

**resourceType**
    

The resource type.

HTTP Status Code: 402

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/StartPolicyGeneration)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/StartPolicyGeneration)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/StartPolicyGeneration)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/StartPolicyGeneration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/StartPolicyGeneration)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/StartPolicyGeneration)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/StartPolicyGeneration)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/StartPolicyGeneration)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/StartPolicyGeneration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/StartPolicyGeneration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ListTagsForResource

StartResourceScan


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_StartResourceScan.html

# StartResourceScan

Immediately starts a scan of the policies applied to the specified resource.

###### Note

This action is supported only for external access analyzers.

## Request Syntax
    
    
    POST /resource/scan HTTP/1.1
    Content-type: application/json
    
    {
       "analyzerArn": "string",
       "resourceArn": "string",
       "resourceOwnerAccount": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) to use to scan the policies applied to the specified resource.

Type: String

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**resourceArn **
    

The ARN of the resource to scan.

Type: String

Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

Required: Yes

**resourceOwnerAccount **
    

The AWS account ID that owns the resource. For most AWS resources, the owning account is the account in which the resource was created.

Type: String

Required: No

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/StartResourceScan)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/StartResourceScan)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/StartResourceScan)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/StartResourceScan)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/StartResourceScan)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/StartResourceScan)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/StartResourceScan)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/StartResourceScan)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/StartResourceScan)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/StartResourceScan)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

StartPolicyGeneration

TagResource


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_TagResource.html

# TagResource

Adds a tag to the specified resource.

## Request Syntax
    
    
    POST /tags/resourceArn HTTP/1.1
    Content-type: application/json
    
    {
       "tags": { 
          "string" : "string" 
       }
    }

## URI Request Parameters

The request uses the following URI parameters.

**resourceArn **
    

The ARN of the resource to add the tag to.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**tags **
    

The tags to add to the resource.

Type: String to string map

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/TagResource)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/TagResource)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/TagResource)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/TagResource)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/TagResource)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/TagResource)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/TagResource)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/TagResource)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/TagResource)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/TagResource)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

StartResourceScan

UntagResource


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UntagResource.html

# UntagResource

Removes a tag from the specified resource.

## Request Syntax
    
    
    DELETE /tags/resourceArn?tagKeys=tagKeys HTTP/1.1
    

## URI Request Parameters

The request uses the following URI parameters.

**resourceArn **
    

The ARN of the resource to remove the tag from.

Required: Yes

**tagKeys **
    

The key for the tag to add.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/UntagResource)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/UntagResource)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UntagResource)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/UntagResource)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UntagResource)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/UntagResource)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/UntagResource)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/UntagResource)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/UntagResource)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UntagResource)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

TagResource

UpdateAnalyzer


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UpdateAnalyzer.html

# UpdateAnalyzer

Modifies the configuration of an existing analyzer.

###### Note

This action is not supported for external access analyzers.

## Request Syntax
    
    
    PUT /analyzer/analyzerName HTTP/1.1
    Content-type: application/json
    
    {
       "configuration": { ... }
    }

## URI Request Parameters

The request uses the following URI parameters.

**analyzerName **
    

The name of the analyzer to modify.

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**configuration **
    

Contains information about the configuration of an analyzer for an AWS organization or account.

Type: [AnalyzerConfiguration](./API_AnalyzerConfiguration.html) object

**Note:** This object is a Union. Only one member of this object can be specified or returned.

Required: No

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "configuration": { ... }
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**configuration **
    

Contains information about the configuration of an analyzer for an AWS organization or account.

Type: [AnalyzerConfiguration](./API_AnalyzerConfiguration.html) object

**Note:** This object is a Union. Only one member of this object can be specified or returned.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**ConflictException**
    

A conflict exception error.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The resource type.

HTTP Status Code: 409

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/UpdateAnalyzer)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/UpdateAnalyzer)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UpdateAnalyzer)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/UpdateAnalyzer)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UpdateAnalyzer)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/UpdateAnalyzer)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/UpdateAnalyzer)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/UpdateAnalyzer)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/UpdateAnalyzer)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UpdateAnalyzer)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

UntagResource

UpdateArchiveRule


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UpdateArchiveRule.html

# UpdateArchiveRule

Updates the criteria and values for the specified archive rule.

## Request Syntax
    
    
    PUT /analyzer/analyzerName/archive-rule/ruleName HTTP/1.1
    Content-type: application/json
    
    {
       "clientToken": "string",
       "filter": { 
          "string" : { 
             "[contains](./API_Criterion.html#accessanalyzer-Type-Criterion-contains)": [ "string" ],
             "[eq](./API_Criterion.html#accessanalyzer-Type-Criterion-eq)": [ "string" ],
             "[exists](./API_Criterion.html#accessanalyzer-Type-Criterion-exists)": boolean,
             "[neq](./API_Criterion.html#accessanalyzer-Type-Criterion-neq)": [ "string" ]
          }
       }
    }

## URI Request Parameters

The request uses the following URI parameters.

**analyzerName **
    

The name of the analyzer to update the archive rules for.

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

**ruleName **
    

The name of the rule to update.

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**clientToken **
    

A client token.

Type: String

Required: No

**filter **
    

A filter to match for the rules to update. Only rules that match the filter are updated.

Type: String to [Criterion](./API_Criterion.html) object map

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/UpdateArchiveRule)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/UpdateArchiveRule)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UpdateArchiveRule)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/UpdateArchiveRule)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UpdateArchiveRule)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/UpdateArchiveRule)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/UpdateArchiveRule)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/UpdateArchiveRule)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/UpdateArchiveRule)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UpdateArchiveRule)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

UpdateAnalyzer

UpdateFindings


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UpdateFindings.html

# UpdateFindings

Updates the status for the specified findings.

## Request Syntax
    
    
    PUT /finding HTTP/1.1
    Content-type: application/json
    
    {
       "analyzerArn": "string",
       "clientToken": "string",
       "ids": [ "string" ],
       "resourceArn": "string",
       "status": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**analyzerArn **
    

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) that generated the findings to update.

Type: String

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**clientToken **
    

A client token.

Type: String

Required: No

**ids **
    

The IDs of the findings to update.

Type: Array of strings

Required: No

**resourceArn **
    

The ARN of the resource identified in the finding.

Type: String

Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

Required: No

**status **
    

The state represents the action to take to update the finding Status. Use `ARCHIVE` to change an Active finding to an Archived finding. Use `ACTIVE` to change an Archived finding to an Active finding.

Type: String

Valid Values: `ACTIVE | ARCHIVED`

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The specified resource could not be found.

**resourceId**
    

The ID of the resource.

**resourceType**
    

The type of the resource.

HTTP Status Code: 404

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/UpdateFindings)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/UpdateFindings)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UpdateFindings)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/UpdateFindings)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UpdateFindings)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/UpdateFindings)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/UpdateFindings)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/UpdateFindings)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/UpdateFindings)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UpdateFindings)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

UpdateArchiveRule

ValidatePolicy


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidatePolicy.html

# ValidatePolicy

Requests the validation of a policy and returns a list of findings. The findings help you identify issues and provide actionable recommendations to resolve the issue and enable you to author functional policies that meet security best practices. 

## Request Syntax
    
    
    POST /policy/validation?maxResults=maxResults&nextToken=nextToken HTTP/1.1
    Content-type: application/json
    
    {
       "locale": "string",
       "policyDocument": "string",
       "policyType": "string",
       "validatePolicyResourceType": "string"
    }

## URI Request Parameters

The request uses the following URI parameters.

**maxResults **
    

The maximum number of results to return in the response.

**nextToken **
    

A token used for pagination of results returned.

## Request Body

The request accepts the following data in JSON format.

**locale **
    

The locale to use for localizing the findings.

Type: String

Valid Values: `DE | EN | ES | FR | IT | JA | KO | PT_BR | ZH_CN | ZH_TW`

Required: No

**policyDocument **
    

The JSON policy document to use as the content for the policy.

Type: String

Required: Yes

**policyType **
    

The type of policy to validate. Identity policies grant permissions to IAM principals. Identity policies include managed and inline policies for IAM roles, users, and groups.

Resource policies grant permissions on AWS resources. Resource policies include trust policies for IAM roles and bucket policies for Amazon S3 buckets. You can provide a generic input such as identity policy or resource policy or a specific input such as managed policy or Amazon S3 bucket policy. 

Service control policies (SCPs) are a type of organization policy attached to an AWS organization, organizational unit (OU), or an account.

Type: String

Valid Values: `IDENTITY_POLICY | RESOURCE_POLICY | SERVICE_CONTROL_POLICY | RESOURCE_CONTROL_POLICY`

Required: Yes

**validatePolicyResourceType **
    

The type of resource to attach to your resource policy. Specify a value for the policy validation resource type only if the policy type is `RESOURCE_POLICY`. For example, to validate a resource policy to attach to an Amazon S3 bucket, you can choose `AWS::S3::Bucket` for the policy validation resource type.

For resource types not supported as valid values, IAM Access Analyzer runs policy checks that apply to all resource policies. For example, to validate a resource policy to attach to a KMS key, do not specify a value for the policy validation resource type and IAM Access Analyzer will run policy checks that apply to all resource policies.

Type: String

Valid Values: `AWS::S3::Bucket | AWS::S3::AccessPoint | AWS::S3::MultiRegionAccessPoint | AWS::S3ObjectLambda::AccessPoint | AWS::IAM::AssumeRolePolicyDocument | AWS::DynamoDB::Table`

Required: No

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "findings": [ 
          { 
             "[findingDetails](./API_ValidatePolicyFinding.html#accessanalyzer-Type-ValidatePolicyFinding-findingDetails)": "**_string_** ",
             "[findingType](./API_ValidatePolicyFinding.html#accessanalyzer-Type-ValidatePolicyFinding-findingType)": "**_string_** ",
             "[issueCode](./API_ValidatePolicyFinding.html#accessanalyzer-Type-ValidatePolicyFinding-issueCode)": "**_string_** ",
             "[learnMoreLink](./API_ValidatePolicyFinding.html#accessanalyzer-Type-ValidatePolicyFinding-learnMoreLink)": "**_string_** ",
             "[locations](./API_ValidatePolicyFinding.html#accessanalyzer-Type-ValidatePolicyFinding-locations)": [ 
                { 
                   "[path](./API_Location.html#accessanalyzer-Type-Location-path)": [ 
                      { ... }
                   ],
                   "[span](./API_Location.html#accessanalyzer-Type-Location-span)": { 
                      "[end](./API_Span.html#accessanalyzer-Type-Span-end)": { 
                         "[column](./API_Position.html#accessanalyzer-Type-Position-column)": **_number_** ,
                         "[line](./API_Position.html#accessanalyzer-Type-Position-line)": **_number_** ,
                         "[offset](./API_Position.html#accessanalyzer-Type-Position-offset)": **_number_**
                      },
                      "[start](./API_Span.html#accessanalyzer-Type-Span-start)": { 
                         "[column](./API_Position.html#accessanalyzer-Type-Position-column)": **_number_** ,
                         "[line](./API_Position.html#accessanalyzer-Type-Position-line)": **_number_** ,
                         "[offset](./API_Position.html#accessanalyzer-Type-Position-offset)": **_number_**
                      }
                   }
                }
             ]
          }
       ],
       "nextToken": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**findings **
    

The list of findings in a policy returned by IAM Access Analyzer based on its suite of policy checks.

Type: Array of [ValidatePolicyFinding](./API_ValidatePolicyFinding.html) objects

**nextToken **
    

A token used for pagination of results returned.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**
    

Internal server error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 500

**ThrottlingException**
    

Throttling limit exceeded error.

**retryAfterSeconds**
    

The seconds to wait to retry.

HTTP Status Code: 429

**ValidationException**
    

Validation exception error.

**fieldList**
    

A list of fields that didn't validate.

**reason**
    

The reason for the exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ValidatePolicy)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ValidatePolicy)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ValidatePolicy)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ValidatePolicy)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ValidatePolicy)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ValidatePolicy)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ValidatePolicy)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ValidatePolicy)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ValidatePolicy)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ValidatePolicy)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

UpdateFindings

Data Types


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Types.html

# Data Types

The IAM Access Analyzer API contains several data types that various actions use. This section describes each data type in detail.

###### Note

The order of each element in a data type structure is not guaranteed. Applications should not assume a particular order.

The following data types are supported:

  * [Access](./API_Access.html)

  * [AccessPreview](./API_AccessPreview.html)

  * [AccessPreviewFinding](./API_AccessPreviewFinding.html)

  * [AccessPreviewStatusReason](./API_AccessPreviewStatusReason.html)

  * [AccessPreviewSummary](./API_AccessPreviewSummary.html)

  * [AclGrantee](./API_AclGrantee.html)

  * [AnalysisRule](./API_AnalysisRule.html)

  * [AnalysisRuleCriteria](./API_AnalysisRuleCriteria.html)

  * [AnalyzedResource](./API_AnalyzedResource.html)

  * [AnalyzedResourceSummary](./API_AnalyzedResourceSummary.html)

  * [AnalyzerConfiguration](./API_AnalyzerConfiguration.html)

  * [AnalyzerSummary](./API_AnalyzerSummary.html)

  * [ArchiveRuleSummary](./API_ArchiveRuleSummary.html)

  * [CloudTrailDetails](./API_CloudTrailDetails.html)

  * [CloudTrailProperties](./API_CloudTrailProperties.html)

  * [Configuration](./API_Configuration.html)

  * [Criterion](./API_Criterion.html)

  * [DynamodbStreamConfiguration](./API_DynamodbStreamConfiguration.html)

  * [DynamodbTableConfiguration](./API_DynamodbTableConfiguration.html)

  * [EbsSnapshotConfiguration](./API_EbsSnapshotConfiguration.html)

  * [EcrRepositoryConfiguration](./API_EcrRepositoryConfiguration.html)

  * [EfsFileSystemConfiguration](./API_EfsFileSystemConfiguration.html)

  * [ExternalAccessDetails](./API_ExternalAccessDetails.html)

  * [ExternalAccessFindingsStatistics](./API_ExternalAccessFindingsStatistics.html)

  * [Finding](./API_Finding.html)

  * [FindingAggregationAccountDetails](./API_FindingAggregationAccountDetails.html)

  * [FindingDetails](./API_FindingDetails.html)

  * [FindingSource](./API_FindingSource.html)

  * [FindingSourceDetail](./API_FindingSourceDetail.html)

  * [FindingsStatistics](./API_FindingsStatistics.html)

  * [FindingSummary](./API_FindingSummary.html)

  * [FindingSummaryV2](./API_FindingSummaryV2.html)

  * [GeneratedPolicy](./API_GeneratedPolicy.html)

  * [GeneratedPolicyProperties](./API_GeneratedPolicyProperties.html)

  * [GeneratedPolicyResult](./API_GeneratedPolicyResult.html)

  * [IamRoleConfiguration](./API_IamRoleConfiguration.html)

  * [InlineArchiveRule](./API_InlineArchiveRule.html)

  * [InternalAccessAnalysisRule](./API_InternalAccessAnalysisRule.html)

  * [InternalAccessAnalysisRuleCriteria](./API_InternalAccessAnalysisRuleCriteria.html)

  * [InternalAccessConfiguration](./API_InternalAccessConfiguration.html)

  * [InternalAccessDetails](./API_InternalAccessDetails.html)

  * [InternalAccessFindingsStatistics](./API_InternalAccessFindingsStatistics.html)

  * [InternalAccessResourceTypeDetails](./API_InternalAccessResourceTypeDetails.html)

  * [InternetConfiguration](./API_InternetConfiguration.html)

  * [JobDetails](./API_JobDetails.html)

  * [JobError](./API_JobError.html)

  * [KmsGrantConfiguration](./API_KmsGrantConfiguration.html)

  * [KmsGrantConstraints](./API_KmsGrantConstraints.html)

  * [KmsKeyConfiguration](./API_KmsKeyConfiguration.html)

  * [Location](./API_Location.html)

  * [NetworkOriginConfiguration](./API_NetworkOriginConfiguration.html)

  * [PathElement](./API_PathElement.html)

  * [PolicyGeneration](./API_PolicyGeneration.html)

  * [PolicyGenerationDetails](./API_PolicyGenerationDetails.html)

  * [Position](./API_Position.html)

  * [RdsDbClusterSnapshotAttributeValue](./API_RdsDbClusterSnapshotAttributeValue.html)

  * [RdsDbClusterSnapshotConfiguration](./API_RdsDbClusterSnapshotConfiguration.html)

  * [RdsDbSnapshotAttributeValue](./API_RdsDbSnapshotAttributeValue.html)

  * [RdsDbSnapshotConfiguration](./API_RdsDbSnapshotConfiguration.html)

  * [ReasonSummary](./API_ReasonSummary.html)

  * [RecommendationError](./API_RecommendationError.html)

  * [RecommendedStep](./API_RecommendedStep.html)

  * [ResourceTypeDetails](./API_ResourceTypeDetails.html)

  * [S3AccessPointConfiguration](./API_S3AccessPointConfiguration.html)

  * [S3BucketAclGrantConfiguration](./API_S3BucketAclGrantConfiguration.html)

  * [S3BucketConfiguration](./API_S3BucketConfiguration.html)

  * [S3ExpressDirectoryAccessPointConfiguration](./API_S3ExpressDirectoryAccessPointConfiguration.html)

  * [S3ExpressDirectoryBucketConfiguration](./API_S3ExpressDirectoryBucketConfiguration.html)

  * [S3PublicAccessBlockConfiguration](./API_S3PublicAccessBlockConfiguration.html)

  * [SecretsManagerSecretConfiguration](./API_SecretsManagerSecretConfiguration.html)

  * [SnsTopicConfiguration](./API_SnsTopicConfiguration.html)

  * [SortCriteria](./API_SortCriteria.html)

  * [Span](./API_Span.html)

  * [SqsQueueConfiguration](./API_SqsQueueConfiguration.html)

  * [StatusReason](./API_StatusReason.html)

  * [Substring](./API_Substring.html)

  * [Trail](./API_Trail.html)

  * [TrailProperties](./API_TrailProperties.html)

  * [UnusedAccessConfiguration](./API_UnusedAccessConfiguration.html)

  * [UnusedAccessFindingsStatistics](./API_UnusedAccessFindingsStatistics.html)

  * [UnusedAccessTypeStatistics](./API_UnusedAccessTypeStatistics.html)

  * [UnusedAction](./API_UnusedAction.html)

  * [UnusedIamRoleDetails](./API_UnusedIamRoleDetails.html)

  * [UnusedIamUserAccessKeyDetails](./API_UnusedIamUserAccessKeyDetails.html)

  * [UnusedIamUserPasswordDetails](./API_UnusedIamUserPasswordDetails.html)

  * [UnusedPermissionDetails](./API_UnusedPermissionDetails.html)

  * [UnusedPermissionsRecommendedStep](./API_UnusedPermissionsRecommendedStep.html)

  * [ValidatePolicyFinding](./API_ValidatePolicyFinding.html)

  * [ValidationExceptionField](./API_ValidationExceptionField.html)

  * [VpcConfiguration](./API_VpcConfiguration.html)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ValidatePolicy

Access


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Access.html

# Access

Contains information about actions and resources that define permissions to check against a policy.

## Contents

**actions**
    

A list of actions for the access permissions. Any strings that can be used as an action in an IAM policy can be used in the list of actions to check.

Type: Array of strings

Array Members: Minimum number of 0 items. Maximum number of 100 items.

Required: No

**resources**
    

A list of resources for the access permissions. Any strings that can be used as an Amazon Resource Name (ARN) in an IAM policy can be used in the list of resources to check. You can only use a wildcard in the portion of the ARN that specifies the resource ID.

Type: Array of strings

Array Members: Minimum number of 0 items. Maximum number of 100 items.

Length Constraints: Minimum length of 0. Maximum length of 2048.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/Access)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/Access)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/Access)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Data Types

AccessPreview


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AccessPreview.html

# AccessPreview

Contains information about an access preview.

## Contents

**analyzerArn**
    

The ARN of the analyzer used to generate the access preview.

Type: String

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**configurations**
    

A map of resource ARNs for the proposed resource configuration.

Type: String to [Configuration](./API_Configuration.html) object map

Required: Yes

**createdAt**
    

The time at which the access preview was created.

Type: Timestamp

Required: Yes

**id**
    

The unique ID for the access preview.

Type: String

Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

Required: Yes

**status**
    

The status of the access preview.

  * `Creating` \- The access preview creation is in progress.

  * `Completed` \- The access preview is complete. You can preview findings for external access to the resource.

  * `Failed` \- The access preview creation has failed.




Type: String

Valid Values: `COMPLETED | CREATING | FAILED`

Required: Yes

**statusReason**
    

Provides more details about the current status of the access preview.

For example, if the creation of the access preview fails, a `Failed` status is returned. This failure can be due to an internal issue with the analysis or due to an invalid resource configuration.

Type: [AccessPreviewStatusReason](./API_AccessPreviewStatusReason.html) object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AccessPreview)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AccessPreview)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AccessPreview)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Access

AccessPreviewFinding


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AccessPreviewFinding.html

# AccessPreviewFinding

An access preview finding generated by the access preview.

## Contents

**changeType**
    

Provides context on how the access preview finding compares to existing access identified in IAM Access Analyzer.

  * `New` \- The finding is for newly-introduced access.

  * `Unchanged` \- The preview finding is an existing finding that would remain unchanged.

  * `Changed` \- The preview finding is an existing finding with a change in status.




For example, a `Changed` finding with preview status `Resolved` and existing status `Active` indicates the existing `Active` finding would become `Resolved` as a result of the proposed permissions change.

Type: String

Valid Values: `CHANGED | NEW | UNCHANGED`

Required: Yes

**createdAt**
    

The time at which the access preview finding was created.

Type: Timestamp

Required: Yes

**id**
    

The ID of the access preview finding. This ID uniquely identifies the element in the list of access preview findings and is not related to the finding ID in Access Analyzer.

Type: String

Required: Yes

**resourceOwnerAccount**
    

The AWS account ID that owns the resource. For most AWS resources, the owning account is the account in which the resource was created.

Type: String

Required: Yes

**resourceType**
    

The type of the resource that can be accessed in the finding.

Type: String

Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`

Required: Yes

**status**
    

The preview status of the finding. This is what the status of the finding would be after permissions deployment. For example, a `Changed` finding with preview status `Resolved` and existing status `Active` indicates the existing `Active` finding would become `Resolved` as a result of the proposed permissions change.

Type: String

Valid Values: `ACTIVE | ARCHIVED | RESOLVED`

Required: Yes

**action**
    

The action in the analyzed policy statement that an external principal has permission to perform.

Type: Array of strings

Required: No

**condition**
    

The condition in the analyzed policy statement that resulted in a finding.

Type: String to string map

Required: No

**error**
    

An error.

Type: String

Required: No

**existingFindingId**
    

The existing ID of the finding in IAM Access Analyzer, provided only for existing findings.

Type: String

Required: No

**existingFindingStatus**
    

The existing status of the finding, provided only for existing findings.

Type: String

Valid Values: `ACTIVE | ARCHIVED | RESOLVED`

Required: No

**isPublic**
    

Indicates whether the policy that generated the finding allows public access to the resource.

Type: Boolean

Required: No

**principal**
    

The external principal that has access to a resource within the zone of trust.

Type: String to string map

Required: No

**resource**
    

The resource that an external principal has access to. This is the resource associated with the access preview.

Type: String

Required: No

**resourceControlPolicyRestriction**
    

The type of restriction applied to the finding by the resource owner with an Organizations resource control policy (RCP).

Type: String

Valid Values: `APPLICABLE | FAILED_TO_EVALUATE_RCP | NOT_APPLICABLE | APPLIED`

Required: No

**sources**
    

The sources of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.

Type: Array of [FindingSource](./API_FindingSource.html) objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AccessPreviewFinding)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AccessPreviewFinding)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AccessPreviewFinding)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AccessPreview

AccessPreviewStatusReason


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AccessPreviewStatusReason.html

# AccessPreviewStatusReason

Provides more details about the current status of the access preview. For example, if the creation of the access preview fails, a `Failed` status is returned. This failure can be due to an internal issue with the analysis or due to an invalid proposed resource configuration.

## Contents

**code**
    

The reason code for the current status of the access preview.

Type: String

Valid Values: `INTERNAL_ERROR | INVALID_CONFIGURATION`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AccessPreviewStatusReason)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AccessPreviewStatusReason)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AccessPreviewStatusReason)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AccessPreviewFinding

AccessPreviewSummary


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AccessPreviewSummary.html

# AccessPreviewSummary

Contains a summary of information about an access preview.

## Contents

**analyzerArn**
    

The ARN of the analyzer used to generate the access preview.

Type: String

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**createdAt**
    

The time at which the access preview was created.

Type: Timestamp

Required: Yes

**id**
    

The unique ID for the access preview.

Type: String

Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

Required: Yes

**status**
    

The status of the access preview.

  * `Creating` \- The access preview creation is in progress.

  * `Completed` \- The access preview is complete and previews the findings for external access to the resource.

  * `Failed` \- The access preview creation has failed.




Type: String

Valid Values: `COMPLETED | CREATING | FAILED`

Required: Yes

**statusReason**
    

Provides more details about the current status of the access preview. For example, if the creation of the access preview fails, a `Failed` status is returned. This failure can be due to an internal issue with the analysis or due to an invalid proposed resource configuration.

Type: [AccessPreviewStatusReason](./API_AccessPreviewStatusReason.html) object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AccessPreviewSummary)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AccessPreviewSummary)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AccessPreviewSummary)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AccessPreviewStatusReason

AclGrantee


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AclGrantee.html

# AclGrantee

You specify each grantee as a type-value pair using one of these types. You can specify only one type of grantee. For more information, see [PutBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html).

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**id**
    

The value specified is the canonical user ID of an AWS account.

Type: String

Required: No

**uri**
    

Used for granting permissions to a predefined group.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AclGrantee)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AclGrantee)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AclGrantee)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AccessPreviewSummary

AnalysisRule


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AnalysisRule.html

# AnalysisRule

Contains information about analysis rules for the analyzer. Analysis rules determine which entities will generate findings based on the criteria you define when you create the rule.

## Contents

**exclusions**
    

A list of rules for the analyzer containing criteria to exclude from analysis. Entities that meet the rule criteria will not generate findings.

Type: Array of [AnalysisRuleCriteria](./API_AnalysisRuleCriteria.html) objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AnalysisRule)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AnalysisRule)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AnalysisRule)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AclGrantee

AnalysisRuleCriteria


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AnalysisRuleCriteria.html

# AnalysisRuleCriteria

The criteria for an analysis rule for an analyzer. The criteria determine which entities will generate findings.

## Contents

**accountIds**
    

A list of AWS account IDs to apply to the analysis rule criteria. The accounts cannot include the organization analyzer owner account. Account IDs can only be applied to the analysis rule criteria for organization-level analyzers. The list cannot include more than 2,000 account IDs.

Type: Array of strings

Required: No

**resourceTags**
    

An array of key-value pairs to match for your resources. You can use the set of Unicode letters, digits, whitespace, `_`, `.`, `/`, `=`, `+`, and `-`.

For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with `aws:`.

For the tag value, you can specify a value that is 0 to 256 characters in length. If the specified tag value is 0 characters, the rule is applied to all principals with the specified tag key.

Type: Array of string to string maps

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AnalysisRuleCriteria)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AnalysisRuleCriteria)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AnalysisRuleCriteria)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AnalysisRule

AnalyzedResource


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AnalyzedResource.html

# AnalyzedResource

Contains details about the analyzed resource.

## Contents

**analyzedAt**
    

The time at which the resource was analyzed.

Type: Timestamp

Required: Yes

**createdAt**
    

The time at which the finding was created.

Type: Timestamp

Required: Yes

**isPublic**
    

Indicates whether the policy that generated the finding grants public access to the resource.

Type: Boolean

Required: Yes

**resourceArn**
    

The ARN of the resource that was analyzed.

Type: String

Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

Required: Yes

**resourceOwnerAccount**
    

The AWS account ID that owns the resource.

Type: String

Required: Yes

**resourceType**
    

The type of the resource that was analyzed.

Type: String

Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`

Required: Yes

**updatedAt**
    

The time at which the finding was updated.

Type: Timestamp

Required: Yes

**actions**
    

The actions that an external principal is granted permission to use by the policy that generated the finding.

Type: Array of strings

Required: No

**error**
    

An error message.

Type: String

Required: No

**sharedVia**
    

Indicates how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.

Type: Array of strings

Required: No

**status**
    

The current status of the finding generated from the analyzed resource.

Type: String

Valid Values: `ACTIVE | ARCHIVED | RESOLVED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AnalyzedResource)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AnalyzedResource)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AnalyzedResource)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AnalysisRuleCriteria

AnalyzedResourceSummary


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AnalyzedResourceSummary.html

# AnalyzedResourceSummary

Contains the ARN of the analyzed resource.

## Contents

**resourceArn**
    

The ARN of the analyzed resource.

Type: String

Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

Required: Yes

**resourceOwnerAccount**
    

The AWS account ID that owns the resource.

Type: String

Required: Yes

**resourceType**
    

The type of resource that was analyzed.

Type: String

Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AnalyzedResourceSummary)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AnalyzedResourceSummary)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AnalyzedResourceSummary)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AnalyzedResource

AnalyzerConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AnalyzerConfiguration.html

# AnalyzerConfiguration

Contains information about the configuration of an analyzer for an AWS organization or account.

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**internalAccess**
    

Specifies the configuration of an internal access analyzer for an AWS organization or account. This configuration determines how the analyzer evaluates access within your AWS environment.

Type: [InternalAccessConfiguration](./API_InternalAccessConfiguration.html) object

Required: No

**unusedAccess**
    

Specifies the configuration of an unused access analyzer for an AWS organization or account.

Type: [UnusedAccessConfiguration](./API_UnusedAccessConfiguration.html) object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AnalyzerConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AnalyzerConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AnalyzerConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AnalyzedResourceSummary

AnalyzerSummary


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AnalyzerSummary.html

# AnalyzerSummary

Contains information about the analyzer.

## Contents

**arn**
    

The ARN of the analyzer.

Type: String

Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`

Required: Yes

**createdAt**
    

A timestamp for the time at which the analyzer was created.

Type: Timestamp

Required: Yes

**name**
    

The name of the analyzer.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

**status**
    

The status of the analyzer. An `Active` analyzer successfully monitors supported resources and generates new findings. The analyzer is `Disabled` when a user action, such as removing trusted access for AWS Identity and Access Management Access Analyzer from AWS Organizations, causes the analyzer to stop generating new findings. The status is `Creating` when the analyzer creation is in progress and `Failed` when the analyzer creation has failed. 

Type: String

Valid Values: `ACTIVE | CREATING | DISABLED | FAILED`

Required: Yes

**type**
    

The type represents the zone of trust or scope for the analyzer.

Type: String

Valid Values: `ACCOUNT | ORGANIZATION | ACCOUNT_UNUSED_ACCESS | ORGANIZATION_UNUSED_ACCESS | ACCOUNT_INTERNAL_ACCESS | ORGANIZATION_INTERNAL_ACCESS`

Required: Yes

**configuration**
    

Specifies if the analyzer is an external access, unused access, or internal access analyzer. The [GetAnalyzer](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAnalyzer.html) action includes this property in its response if a configuration is specified, while the [ListAnalyzers](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAnalyzers.html) action omits it.

Type: [AnalyzerConfiguration](./API_AnalyzerConfiguration.html) object

**Note:** This object is a Union. Only one member of this object can be specified or returned.

Required: No

**lastResourceAnalyzed**
    

The resource that was most recently analyzed by the analyzer.

Type: String

Required: No

**lastResourceAnalyzedAt**
    

The time at which the most recently analyzed resource was analyzed.

Type: Timestamp

Required: No

**statusReason**
    

The `statusReason` provides more details about the current status of the analyzer. For example, if the creation for the analyzer fails, a `Failed` status is returned. For an analyzer with organization as the type, this failure can be due to an issue with creating the service-linked roles required in the member accounts of the AWS organization.

Type: [StatusReason](./API_StatusReason.html) object

Required: No

**tags**
    

An array of key-value pairs applied to the analyzer. The key-value pairs consist of the set of Unicode letters, digits, whitespace, `_`, `.`, `/`, `=`, `+`, and `-`.

The tag key is a value that is 1 to 128 characters in length and cannot be prefixed with `aws:`.

The tag value is a value that is 0 to 256 characters in length.

Type: String to string map

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AnalyzerSummary)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AnalyzerSummary)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AnalyzerSummary)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AnalyzerConfiguration

ArchiveRuleSummary


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ArchiveRuleSummary.html

# ArchiveRuleSummary

Contains information about an archive rule. Archive rules automatically archive new findings that meet the criteria you define when you create the rule.

## Contents

**createdAt**
    

The time at which the archive rule was created.

Type: Timestamp

Required: Yes

**filter**
    

A filter used to define the archive rule.

Type: String to [Criterion](./API_Criterion.html) object map

Required: Yes

**ruleName**
    

The name of the archive rule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

**updatedAt**
    

The time at which the archive rule was last updated.

Type: Timestamp

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ArchiveRuleSummary)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ArchiveRuleSummary)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ArchiveRuleSummary)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AnalyzerSummary

CloudTrailDetails


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CloudTrailDetails.html

# CloudTrailDetails

Contains information about CloudTrail access.

## Contents

**accessRole**
    

The ARN of the service role that IAM Access Analyzer uses to access your CloudTrail trail and service last accessed information.

Type: String

Pattern: `arn:[^:]*:iam::[^:]*:role/.{1,576}`

Required: Yes

**startTime**
    

The start of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp before this time are not considered to generate a policy.

Type: Timestamp

Required: Yes

**trails**
    

A `Trail` object that contains settings for a trail.

Type: Array of [Trail](./API_Trail.html) objects

Required: Yes

**endTime**
    

The end of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp after this time are not considered to generate a policy. If this is not included in the request, the default value is the current time.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CloudTrailDetails)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CloudTrailDetails)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CloudTrailDetails)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ArchiveRuleSummary

CloudTrailProperties


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CloudTrailProperties.html

# CloudTrailProperties

Contains information about CloudTrail access.

## Contents

**endTime**
    

The end of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp after this time are not considered to generate a policy. If this is not included in the request, the default value is the current time.

Type: Timestamp

Required: Yes

**startTime**
    

The start of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp before this time are not considered to generate a policy.

Type: Timestamp

Required: Yes

**trailProperties**
    

A `TrailProperties` object that contains settings for trail properties.

Type: Array of [TrailProperties](./API_TrailProperties.html) objects

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CloudTrailProperties)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CloudTrailProperties)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CloudTrailProperties)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

CloudTrailDetails

Configuration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Configuration.html

# Configuration

Access control configuration structures for your resource. You specify the configuration as a type-value pair. You can specify only one type of access control configuration.

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**dynamodbStream**
    

The access control configuration is for a DynamoDB stream.

Type: [DynamodbStreamConfiguration](./API_DynamodbStreamConfiguration.html) object

Required: No

**dynamodbTable**
    

The access control configuration is for a DynamoDB table or index.

Type: [DynamodbTableConfiguration](./API_DynamodbTableConfiguration.html) object

Required: No

**ebsSnapshot**
    

The access control configuration is for an Amazon EBS volume snapshot.

Type: [EbsSnapshotConfiguration](./API_EbsSnapshotConfiguration.html) object

Required: No

**ecrRepository**
    

The access control configuration is for an Amazon ECR repository.

Type: [EcrRepositoryConfiguration](./API_EcrRepositoryConfiguration.html) object

Required: No

**efsFileSystem**
    

The access control configuration is for an Amazon EFS file system.

Type: [EfsFileSystemConfiguration](./API_EfsFileSystemConfiguration.html) object

Required: No

**iamRole**
    

The access control configuration is for an IAM role. 

Type: [IamRoleConfiguration](./API_IamRoleConfiguration.html) object

Required: No

**kmsKey**
    

The access control configuration is for a KMS key. 

Type: [KmsKeyConfiguration](./API_KmsKeyConfiguration.html) object

Required: No

**rdsDbClusterSnapshot**
    

The access control configuration is for an Amazon RDS DB cluster snapshot.

Type: [RdsDbClusterSnapshotConfiguration](./API_RdsDbClusterSnapshotConfiguration.html) object

Required: No

**rdsDbSnapshot**
    

The access control configuration is for an Amazon RDS DB snapshot.

Type: [RdsDbSnapshotConfiguration](./API_RdsDbSnapshotConfiguration.html) object

Required: No

**s3Bucket**
    

The access control configuration is for an Amazon S3 bucket. 

Type: [S3BucketConfiguration](./API_S3BucketConfiguration.html) object

Required: No

**s3ExpressDirectoryBucket**
    

The access control configuration is for an Amazon S3 directory bucket.

Type: [S3ExpressDirectoryBucketConfiguration](./API_S3ExpressDirectoryBucketConfiguration.html) object

Required: No

**secretsManagerSecret**
    

The access control configuration is for a Secrets Manager secret.

Type: [SecretsManagerSecretConfiguration](./API_SecretsManagerSecretConfiguration.html) object

Required: No

**snsTopic**
    

The access control configuration is for an Amazon SNS topic

Type: [SnsTopicConfiguration](./API_SnsTopicConfiguration.html) object

Required: No

**sqsQueue**
    

The access control configuration is for an Amazon SQS queue. 

Type: [SqsQueueConfiguration](./API_SqsQueueConfiguration.html) object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/Configuration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/Configuration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/Configuration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

CloudTrailProperties

Criterion


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Criterion.html

# Criterion

The criteria to use in the filter that defines the archive rule. For more information on available filter keys, see [IAM Access Analyzer filter keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html).

## Contents

**contains**
    

A "contains" operator to match for the filter used to create the rule.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 20 items.

Required: No

**eq**
    

An "equals" operator to match for the filter used to create the rule.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 20 items.

Required: No

**exists**
    

An "exists" operator to match for the filter used to create the rule. 

Type: Boolean

Required: No

**neq**
    

A "not equals" operator to match for the filter used to create the rule.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 20 items.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/Criterion)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/Criterion)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/Criterion)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Configuration

DynamodbStreamConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_DynamodbStreamConfiguration.html

# DynamodbStreamConfiguration

The proposed access control configuration for a DynamoDB stream. You can propose a configuration for a new DynamoDB stream or an existing DynamoDB stream that you own by specifying the policy for the DynamoDB stream. For more information, see [PutResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutResourcePolicy.html).

  * If the configuration is for an existing DynamoDB stream and you do not specify the DynamoDB policy, then the access preview uses the existing DynamoDB policy for the stream.

  * If the access preview is for a new resource and you do not specify the policy, then the access preview assumes a DynamoDB stream without a policy.

  * To propose deletion of an existing DynamoDB stream policy, you can specify an empty string for the DynamoDB policy.




## Contents

**streamPolicy**
    

The proposed resource policy defining who can access or manage the DynamoDB stream.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/DynamodbStreamConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/DynamodbStreamConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/DynamodbStreamConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Criterion

DynamodbTableConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_DynamodbTableConfiguration.html

# DynamodbTableConfiguration

The proposed access control configuration for a DynamoDB table or index. You can propose a configuration for a new DynamoDB table or index or an existing DynamoDB table or index that you own by specifying the policy for the DynamoDB table or index. For more information, see [PutResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutResourcePolicy.html).

  * If the configuration is for an existing DynamoDB table or index and you do not specify the DynamoDB policy, then the access preview uses the existing DynamoDB policy for the table or index.

  * If the access preview is for a new resource and you do not specify the policy, then the access preview assumes a DynamoDB table without a policy.

  * To propose deletion of an existing DynamoDB table or index policy, you can specify an empty string for the DynamoDB policy.




## Contents

**tablePolicy**
    

The proposed resource policy defining who can access or manage the DynamoDB table.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/DynamodbTableConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/DynamodbTableConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/DynamodbTableConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

DynamodbStreamConfiguration

EbsSnapshotConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_EbsSnapshotConfiguration.html

# EbsSnapshotConfiguration

The proposed access control configuration for an Amazon EBS volume snapshot. You can propose a configuration for a new Amazon EBS volume snapshot or an Amazon EBS volume snapshot that you own by specifying the user IDs, groups, and optional AWS KMS encryption key. For more information, see [ModifySnapshotAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySnapshotAttribute.html).

## Contents

**groups**
    

The groups that have access to the Amazon EBS volume snapshot. If the value `all` is specified, then the Amazon EBS volume snapshot is public.

  * If the configuration is for an existing Amazon EBS volume snapshot and you do not specify the `groups`, then the access preview uses the existing shared `groups` for the snapshot.

  * If the access preview is for a new resource and you do not specify the `groups`, then the access preview considers the snapshot without any `groups`.

  * To propose deletion of existing shared `groups`, you can specify an empty list for `groups`.




Type: Array of strings

Required: No

**kmsKeyId**
    

The KMS key identifier for an encrypted Amazon EBS volume snapshot. The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

  * If the configuration is for an existing Amazon EBS volume snapshot and you do not specify the `kmsKeyId`, or you specify an empty string, then the access preview uses the existing `kmsKeyId` of the snapshot.

  * If the access preview is for a new resource and you do not specify the `kmsKeyId`, the access preview considers the snapshot as unencrypted.




Type: String

Required: No

**userIds**
    

The IDs of the AWS accounts that have access to the Amazon EBS volume snapshot.

  * If the configuration is for an existing Amazon EBS volume snapshot and you do not specify the `userIds`, then the access preview uses the existing shared `userIds` for the snapshot.

  * If the access preview is for a new resource and you do not specify the `userIds`, then the access preview considers the snapshot without any `userIds`.

  * To propose deletion of existing shared `accountIds`, you can specify an empty list for `userIds`.




Type: Array of strings

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/EbsSnapshotConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/EbsSnapshotConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/EbsSnapshotConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

DynamodbTableConfiguration

EcrRepositoryConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_EcrRepositoryConfiguration.html

# EcrRepositoryConfiguration

The proposed access control configuration for an Amazon ECR repository. You can propose a configuration for a new Amazon ECR repository or an existing Amazon ECR repository that you own by specifying the Amazon ECR policy. For more information, see [Repository](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Repository.html).

  * If the configuration is for an existing Amazon ECR repository and you do not specify the Amazon ECR policy, then the access preview uses the existing Amazon ECR policy for the repository.

  * If the access preview is for a new resource and you do not specify the policy, then the access preview assumes an Amazon ECR repository without a policy.

  * To propose deletion of an existing Amazon ECR repository policy, you can specify an empty string for the Amazon ECR policy.




## Contents

**repositoryPolicy**
    

The JSON repository policy text to apply to the Amazon ECR repository. For more information, see [Private repository policy examples](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html) in the _Amazon ECR User Guide_.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/EcrRepositoryConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/EcrRepositoryConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/EcrRepositoryConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

EbsSnapshotConfiguration

EfsFileSystemConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_EfsFileSystemConfiguration.html

# EfsFileSystemConfiguration

The proposed access control configuration for an Amazon EFS file system. You can propose a configuration for a new Amazon EFS file system or an existing Amazon EFS file system that you own by specifying the Amazon EFS policy. For more information, see [Using file systems in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/using-fs.html).

  * If the configuration is for an existing Amazon EFS file system and you do not specify the Amazon EFS policy, then the access preview uses the existing Amazon EFS policy for the file system.

  * If the access preview is for a new resource and you do not specify the policy, then the access preview assumes an Amazon EFS file system without a policy.

  * To propose deletion of an existing Amazon EFS file system policy, you can specify an empty string for the Amazon EFS policy.




## Contents

**fileSystemPolicy**
    

The JSON policy definition to apply to the Amazon EFS file system. For more information on the elements that make up a file system policy, see [Amazon EFS Resource-based policies](https://docs.aws.amazon.com/efs/latest/ug/access-control-overview.html#access-control-manage-access-intro-resource-policies).

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/EfsFileSystemConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/EfsFileSystemConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/EfsFileSystemConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

EcrRepositoryConfiguration

ExternalAccessDetails


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ExternalAccessDetails.html

# ExternalAccessDetails

Contains information about an external access finding.

## Contents

**condition**
    

The condition in the analyzed policy statement that resulted in an external access finding.

Type: String to string map

Required: Yes

**action**
    

The action in the analyzed policy statement that an external principal has permission to use.

Type: Array of strings

Required: No

**isPublic**
    

Specifies whether the external access finding is public.

Type: Boolean

Required: No

**principal**
    

The external principal that has access to a resource within the zone of trust.

Type: String to string map

Required: No

**resourceControlPolicyRestriction**
    

The type of restriction applied to the finding by the resource owner with an Organizations resource control policy (RCP).

  * `APPLICABLE`: There is an RCP present in the organization but IAM Access Analyzer does not include it in the evaluation of effective permissions. For example, if `s3:DeleteObject` is blocked by the RCP and the restriction is `APPLICABLE`, then `s3:DeleteObject` would still be included in the list of actions for the finding.

  * `FAILED_TO_EVALUATE_RCP`: There was an error evaluating the RCP.

  * `NOT_APPLICABLE`: There was no RCP present in the organization, or there was no RCP applicable to the resource. For example, the resource being analyzed is an Amazon RDS snapshot and there is an RCP in the organization, but the RCP only impacts Amazon S3 buckets.

  * `APPLIED`: This restriction is not currently available for external access findings. 




Type: String

Valid Values: `APPLICABLE | FAILED_TO_EVALUATE_RCP | NOT_APPLICABLE | APPLIED`

Required: No

**sources**
    

The sources of the external access finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.

Type: Array of [FindingSource](./API_FindingSource.html) objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ExternalAccessDetails)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ExternalAccessDetails)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ExternalAccessDetails)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

EfsFileSystemConfiguration

ExternalAccessFindingsStatistics


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ExternalAccessFindingsStatistics.html

# ExternalAccessFindingsStatistics

Provides aggregate statistics about the findings for the specified external access analyzer.

## Contents

**resourceTypeStatistics**
    

The total number of active cross-account and public findings for each resource type of the specified external access analyzer.

Type: String to [ResourceTypeDetails](./API_ResourceTypeDetails.html) object map

Valid Keys: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`

Required: No

**totalActiveFindings**
    

The number of active findings for the specified external access analyzer.

Type: Integer

Required: No

**totalArchivedFindings**
    

The number of archived findings for the specified external access analyzer.

Type: Integer

Required: No

**totalResolvedFindings**
    

The number of resolved findings for the specified external access analyzer.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ExternalAccessFindingsStatistics)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ExternalAccessFindingsStatistics)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ExternalAccessFindingsStatistics)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ExternalAccessDetails

Finding


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Finding.html

# Finding

Contains information about a finding.

## Contents

**analyzedAt**
    

The time at which the resource was analyzed.

Type: Timestamp

Required: Yes

**condition**
    

The condition in the analyzed policy statement that resulted in a finding.

Type: String to string map

Required: Yes

**createdAt**
    

The time at which the finding was generated.

Type: Timestamp

Required: Yes

**id**
    

The ID of the finding.

Type: String

Required: Yes

**resourceOwnerAccount**
    

The AWS account ID that owns the resource.

Type: String

Required: Yes

**resourceType**
    

The type of the resource identified in the finding.

Type: String

Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`

Required: Yes

**status**
    

The current status of the finding.

Type: String

Valid Values: `ACTIVE | ARCHIVED | RESOLVED`

Required: Yes

**updatedAt**
    

The time at which the finding was updated.

Type: Timestamp

Required: Yes

**action**
    

The action in the analyzed policy statement that an external principal has permission to use.

Type: Array of strings

Required: No

**error**
    

An error.

Type: String

Required: No

**isPublic**
    

Indicates whether the policy that generated the finding allows public access to the resource.

Type: Boolean

Required: No

**principal**
    

The external principal that has access to a resource within the zone of trust.

Type: String to string map

Required: No

**resource**
    

The resource that an external principal has access to.

Type: String

Required: No

**resourceControlPolicyRestriction**
    

The type of restriction applied to the finding by the resource owner with an Organizations resource control policy (RCP).

Type: String

Valid Values: `APPLICABLE | FAILED_TO_EVALUATE_RCP | NOT_APPLICABLE | APPLIED`

Required: No

**sources**
    

The sources of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.

Type: Array of [FindingSource](./API_FindingSource.html) objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/Finding)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/Finding)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/Finding)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ExternalAccessFindingsStatistics

FindingAggregationAccountDetails


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingAggregationAccountDetails.html

# FindingAggregationAccountDetails

Contains information about the findings for an AWS account in an organization unused access analyzer.

## Contents

**account**
    

The ID of the AWS account for which unused access finding details are provided.

Type: String

Required: No

**details**
    

Provides the number of active findings for each type of unused access for the specified AWS account.

Type: String to integer map

Required: No

**numberOfActiveFindings**
    

The number of active unused access findings for the specified AWS account.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingAggregationAccountDetails)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingAggregationAccountDetails)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingAggregationAccountDetails)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Finding

FindingDetails


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingDetails.html

# FindingDetails

Contains information about an external access or unused access finding. Only one parameter can be used in a `FindingDetails` object.

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**externalAccessDetails**
    

The details for an external access analyzer finding.

Type: [ExternalAccessDetails](./API_ExternalAccessDetails.html) object

Required: No

**internalAccessDetails**
    

The details for an internal access analyzer finding. This contains information about access patterns identified within your AWS organization or account.

Type: [InternalAccessDetails](./API_InternalAccessDetails.html) object

Required: No

**unusedIamRoleDetails**
    

The details for an unused access analyzer finding with an unused IAM role finding type.

Type: [UnusedIamRoleDetails](./API_UnusedIamRoleDetails.html) object

Required: No

**unusedIamUserAccessKeyDetails**
    

The details for an unused access analyzer finding with an unused IAM user access key finding type.

Type: [UnusedIamUserAccessKeyDetails](./API_UnusedIamUserAccessKeyDetails.html) object

Required: No

**unusedIamUserPasswordDetails**
    

The details for an unused access analyzer finding with an unused IAM user password finding type.

Type: [UnusedIamUserPasswordDetails](./API_UnusedIamUserPasswordDetails.html) object

Required: No

**unusedPermissionDetails**
    

The details for an unused access analyzer finding with an unused permission finding type.

Type: [UnusedPermissionDetails](./API_UnusedPermissionDetails.html) object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingDetails)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingDetails)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingDetails)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

FindingAggregationAccountDetails

FindingSource


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingSource.html

# FindingSource

The source of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.

## Contents

**type**
    

Indicates the type of access that generated the finding.

Type: String

Valid Values: `POLICY | BUCKET_ACL | S3_ACCESS_POINT | S3_ACCESS_POINT_ACCOUNT`

Required: Yes

**detail**
    

Includes details about how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.

Type: [FindingSourceDetail](./API_FindingSourceDetail.html) object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingSource)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingSource)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingSource)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

FindingDetails

FindingSourceDetail


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingSourceDetail.html

# FindingSourceDetail

Includes details about how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.

## Contents

**accessPointAccount**
    

The account of the cross-account access point that generated the finding.

Type: String

Required: No

**accessPointArn**
    

The ARN of the access point that generated the finding. The ARN format depends on whether the ARN represents an access point or a multi-region access point.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingSourceDetail)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingSourceDetail)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingSourceDetail)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

FindingSource

FindingsStatistics


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingsStatistics.html

# FindingsStatistics

Contains information about the aggregate statistics for an external or unused access analyzer. Only one parameter can be used in a `FindingsStatistics` object.

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**externalAccessFindingsStatistics**
    

The aggregate statistics for an external access analyzer.

Type: [ExternalAccessFindingsStatistics](./API_ExternalAccessFindingsStatistics.html) object

Required: No

**internalAccessFindingsStatistics**
    

The aggregate statistics for an internal access analyzer. This includes information about active, archived, and resolved findings related to internal access within your AWS organization or account.

Type: [InternalAccessFindingsStatistics](./API_InternalAccessFindingsStatistics.html) object

Required: No

**unusedAccessFindingsStatistics**
    

The aggregate statistics for an unused access analyzer.

Type: [UnusedAccessFindingsStatistics](./API_UnusedAccessFindingsStatistics.html) object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingsStatistics)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingsStatistics)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingsStatistics)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

FindingSourceDetail

FindingSummary


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingSummary.html

# FindingSummary

Contains information about a finding.

## Contents

**analyzedAt**
    

The time at which the resource-based policy that generated the finding was analyzed.

Type: Timestamp

Required: Yes

**condition**
    

The condition in the analyzed policy statement that resulted in a finding.

Type: String to string map

Required: Yes

**createdAt**
    

The time at which the finding was created.

Type: Timestamp

Required: Yes

**id**
    

The ID of the finding.

Type: String

Required: Yes

**resourceOwnerAccount**
    

The AWS account ID that owns the resource.

Type: String

Required: Yes

**resourceType**
    

The type of the resource that the external principal has access to.

Type: String

Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`

Required: Yes

**status**
    

The status of the finding.

Type: String

Valid Values: `ACTIVE | ARCHIVED | RESOLVED`

Required: Yes

**updatedAt**
    

The time at which the finding was most recently updated.

Type: Timestamp

Required: Yes

**action**
    

The action in the analyzed policy statement that an external principal has permission to use.

Type: Array of strings

Required: No

**error**
    

The error that resulted in an Error finding.

Type: String

Required: No

**isPublic**
    

Indicates whether the finding reports a resource that has a policy that allows public access.

Type: Boolean

Required: No

**principal**
    

The external principal that has access to a resource within the zone of trust.

Type: String to string map

Required: No

**resource**
    

The resource that the external principal has access to.

Type: String

Required: No

**resourceControlPolicyRestriction**
    

The type of restriction applied to the finding by the resource owner with an Organizations resource control policy (RCP).

Type: String

Valid Values: `APPLICABLE | FAILED_TO_EVALUATE_RCP | NOT_APPLICABLE | APPLIED`

Required: No

**sources**
    

The sources of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.

Type: Array of [FindingSource](./API_FindingSource.html) objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingSummary)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingSummary)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingSummary)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

FindingsStatistics

FindingSummaryV2


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingSummaryV2.html

# FindingSummaryV2

Contains information about a finding.

## Contents

**analyzedAt**
    

The time at which the resource-based policy or IAM entity that generated the finding was analyzed.

Type: Timestamp

Required: Yes

**createdAt**
    

The time at which the finding was created.

Type: Timestamp

Required: Yes

**id**
    

The ID of the finding.

Type: String

Required: Yes

**resourceOwnerAccount**
    

The AWS account ID that owns the resource.

Type: String

Required: Yes

**resourceType**
    

The type of the resource that the external principal has access to.

Type: String

Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`

Required: Yes

**status**
    

The status of the finding.

Type: String

Valid Values: `ACTIVE | ARCHIVED | RESOLVED`

Required: Yes

**updatedAt**
    

The time at which the finding was most recently updated.

Type: Timestamp

Required: Yes

**error**
    

The error that resulted in an Error finding.

Type: String

Required: No

**findingType**
    

The type of the access finding. For external access analyzers, the type is `ExternalAccess`. For unused access analyzers, the type can be `UnusedIAMRole`, `UnusedIAMUserAccessKey`, `UnusedIAMUserPassword`, or `UnusedPermission`. For internal access analyzers, the type is `InternalAccess`.

Type: String

Valid Values: `ExternalAccess | UnusedIAMRole | UnusedIAMUserAccessKey | UnusedIAMUserPassword | UnusedPermission | InternalAccess`

Required: No

**resource**
    

The resource that the external principal has access to.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingSummaryV2)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingSummaryV2)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingSummaryV2)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

FindingSummary

GeneratedPolicy


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GeneratedPolicy.html

# GeneratedPolicy

Contains the text for the generated policy.

## Contents

**policy**
    

The text to use as the content for the new policy. The policy is created using the [CreatePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicy.html) action.

Type: String

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GeneratedPolicy)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GeneratedPolicy)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GeneratedPolicy)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

FindingSummaryV2

GeneratedPolicyProperties


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GeneratedPolicyProperties.html

# GeneratedPolicyProperties

Contains the generated policy details.

## Contents

**principalArn**
    

The ARN of the IAM entity (user or role) for which you are generating a policy.

Type: String

Pattern: `arn:[^:]*:iam::[^:]*:(role|user)/.{1,576}`

Required: Yes

**cloudTrailProperties**
    

Lists details about the `Trail` used to generated policy.

Type: [CloudTrailProperties](./API_CloudTrailProperties.html) object

Required: No

**isComplete**
    

This value is set to `true` if the generated policy contains all possible actions for a service that IAM Access Analyzer identified from the CloudTrail trail that you specified, and `false` otherwise.

Type: Boolean

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GeneratedPolicyProperties)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GeneratedPolicyProperties)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GeneratedPolicyProperties)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GeneratedPolicy

GeneratedPolicyResult


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GeneratedPolicyResult.html

# GeneratedPolicyResult

Contains the text for the generated policy and its details.

## Contents

**properties**
    

A `GeneratedPolicyProperties` object that contains properties of the generated policy.

Type: [GeneratedPolicyProperties](./API_GeneratedPolicyProperties.html) object

Required: Yes

**generatedPolicies**
    

The text to use as the content for the new policy. The policy is created using the [CreatePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicy.html) action.

Type: Array of [GeneratedPolicy](./API_GeneratedPolicy.html) objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GeneratedPolicyResult)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GeneratedPolicyResult)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GeneratedPolicyResult)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GeneratedPolicyProperties

IamRoleConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_IamRoleConfiguration.html

# IamRoleConfiguration

The proposed access control configuration for an IAM role. You can propose a configuration for a new IAM role or an existing IAM role that you own by specifying the trust policy. If the configuration is for a new IAM role, you must specify the trust policy. If the configuration is for an existing IAM role that you own and you do not propose the trust policy, the access preview uses the existing trust policy for the role. The proposed trust policy cannot be an empty string. For more information about role trust policy limits, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html).

## Contents

**trustPolicy**
    

The proposed trust policy for the IAM role.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/IamRoleConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/IamRoleConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/IamRoleConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GeneratedPolicyResult

InlineArchiveRule


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_InlineArchiveRule.html

# InlineArchiveRule

An criterion statement in an archive rule. Each archive rule may have multiple criteria.

## Contents

**filter**
    

The condition and values for a criterion.

Type: String to [Criterion](./API_Criterion.html) object map

Required: Yes

**ruleName**
    

The name of the rule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `[A-Za-z][A-Za-z0-9_.-]*`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/InlineArchiveRule)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/InlineArchiveRule)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/InlineArchiveRule)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

IamRoleConfiguration

InternalAccessAnalysisRule


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_InternalAccessAnalysisRule.html

# InternalAccessAnalysisRule

Contains information about analysis rules for the internal access analyzer. Analysis rules determine which entities will generate findings based on the criteria you define when you create the rule.

## Contents

**inclusions**
    

A list of rules for the internal access analyzer containing criteria to include in analysis. Only resources that meet the rule criteria will generate findings.

Type: Array of [InternalAccessAnalysisRuleCriteria](./API_InternalAccessAnalysisRuleCriteria.html) objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/InternalAccessAnalysisRule)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/InternalAccessAnalysisRule)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/InternalAccessAnalysisRule)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

InlineArchiveRule

InternalAccessAnalysisRuleCriteria


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_InternalAccessAnalysisRuleCriteria.html

# InternalAccessAnalysisRuleCriteria

The criteria for an analysis rule for an internal access analyzer.

## Contents

**accountIds**
    

A list of AWS account IDs to apply to the internal access analysis rule criteria. Account IDs can only be applied to the analysis rule criteria for organization-level analyzers.

Type: Array of strings

Required: No

**resourceArns**
    

A list of resource ARNs to apply to the internal access analysis rule criteria. The analyzer will only generate findings for resources that match these ARNs.

Type: Array of strings

Required: No

**resourceTypes**
    

A list of resource types to apply to the internal access analysis rule criteria. The analyzer will only generate findings for resources of these types. These resource types are currently supported for internal access analyzers:

  * `AWS::S3::Bucket`

  * `AWS::RDS::DBSnapshot`

  * `AWS::RDS::DBClusterSnapshot`

  * `AWS::S3Express::DirectoryBucket`

  * `AWS::DynamoDB::Table`

  * `AWS::DynamoDB::Stream`




Type: Array of strings

Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/InternalAccessAnalysisRuleCriteria)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/InternalAccessAnalysisRuleCriteria)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/InternalAccessAnalysisRuleCriteria)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

InternalAccessAnalysisRule

InternalAccessConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_InternalAccessConfiguration.html

# InternalAccessConfiguration

Specifies the configuration of an internal access analyzer for an AWS organization or account. This configuration determines how the analyzer evaluates internal access within your AWS environment.

## Contents

**analysisRule**
    

Contains information about analysis rules for the internal access analyzer. These rules determine which resources and access patterns will be analyzed.

Type: [InternalAccessAnalysisRule](./API_InternalAccessAnalysisRule.html) object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/InternalAccessConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/InternalAccessConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/InternalAccessConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

InternalAccessAnalysisRuleCriteria

InternalAccessDetails


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_InternalAccessDetails.html

# InternalAccessDetails

Contains information about an internal access finding. This includes details about the access that was identified within your AWS organization or account.

## Contents

**accessType**
    

The type of internal access identified in the finding. This indicates how the access is granted within your AWS environment.

Type: String

Valid Values: `INTRA_ACCOUNT | INTRA_ORG`

Required: No

**action**
    

The action in the analyzed policy statement that has internal access permission to use.

Type: Array of strings

Required: No

**condition**
    

The condition in the analyzed policy statement that resulted in an internal access finding.

Type: String to string map

Required: No

**principal**
    

The principal that has access to a resource within the internal environment.

Type: String to string map

Required: No

**principalOwnerAccount**
    

The AWS account ID that owns the principal identified in the internal access finding.

Type: String

Required: No

**principalType**
    

The type of principal identified in the internal access finding, such as IAM role or IAM user.

Type: String

Valid Values: `IAM_ROLE | IAM_USER`

Required: No

**resourceControlPolicyRestriction**
    

The type of restriction applied to the finding by the resource owner with an AWS Organizations resource control policy (RCP).

  * `APPLICABLE`: There is an RCP present in the organization but IAM Access Analyzer does not include it in the evaluation of effective permissions. For example, if `s3:DeleteObject` is blocked by the RCP and the restriction is `APPLICABLE`, then `s3:DeleteObject` would still be included in the list of actions for the finding. Only applicable to internal access findings with the account as the zone of trust. 

  * `FAILED_TO_EVALUATE_RCP`: There was an error evaluating the RCP.

  * `NOT_APPLICABLE`: There was no RCP present in the organization. For internal access findings with the account as the zone of trust, `NOT_APPLICABLE` could also indicate that there was no RCP applicable to the resource.

  * `APPLIED`: An RCP is present in the organization and IAM Access Analyzer included it in the evaluation of effective permissions. For example, if `s3:DeleteObject` is blocked by the RCP and the restriction is `APPLIED`, then `s3:DeleteObject` would not be included in the list of actions for the finding. Only applicable to internal access findings with the organization as the zone of trust. 




Type: String

Valid Values: `APPLICABLE | FAILED_TO_EVALUATE_RCP | NOT_APPLICABLE | APPLIED`

Required: No

**serviceControlPolicyRestriction**
    

The type of restriction applied to the finding by an AWS Organizations service control policy (SCP).

  * `APPLICABLE`: There is an SCP present in the organization but IAM Access Analyzer does not include it in the evaluation of effective permissions. Only applicable to internal access findings with the account as the zone of trust. 

  * `FAILED_TO_EVALUATE_SCP`: There was an error evaluating the SCP.

  * `NOT_APPLICABLE`: There was no SCP present in the organization. For internal access findings with the account as the zone of trust, `NOT_APPLICABLE` could also indicate that there was no SCP applicable to the principal.

  * `APPLIED`: An SCP is present in the organization and IAM Access Analyzer included it in the evaluation of effective permissions. Only applicable to internal access findings with the organization as the zone of trust. 




Type: String

Valid Values: `APPLICABLE | FAILED_TO_EVALUATE_SCP | NOT_APPLICABLE | APPLIED`

Required: No

**sources**
    

The sources of the internal access finding. This indicates how the access that generated the finding is granted within your AWS environment.

Type: Array of [FindingSource](./API_FindingSource.html) objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/InternalAccessDetails)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/InternalAccessDetails)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/InternalAccessDetails)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

InternalAccessConfiguration

InternalAccessFindingsStatistics


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_InternalAccessFindingsStatistics.html

# InternalAccessFindingsStatistics

Provides aggregate statistics about the findings for the specified internal access analyzer. This includes counts of active, archived, and resolved findings.

## Contents

**resourceTypeStatistics**
    

The total number of active findings for each resource type of the specified internal access analyzer.

Type: String to [InternalAccessResourceTypeDetails](./API_InternalAccessResourceTypeDetails.html) object map

Valid Keys: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`

Required: No

**totalActiveFindings**
    

The number of active findings for the specified internal access analyzer.

Type: Integer

Required: No

**totalArchivedFindings**
    

The number of archived findings for the specified internal access analyzer.

Type: Integer

Required: No

**totalResolvedFindings**
    

The number of resolved findings for the specified internal access analyzer.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/InternalAccessFindingsStatistics)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/InternalAccessFindingsStatistics)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/InternalAccessFindingsStatistics)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

InternalAccessDetails

InternalAccessResourceTypeDetails


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_InternalAccessResourceTypeDetails.html

# InternalAccessResourceTypeDetails

Contains information about the total number of active, archived, and resolved findings for a resource type of an internal access analyzer.

## Contents

**totalActiveFindings**
    

The total number of active findings for the resource type in the internal access analyzer.

Type: Integer

Required: No

**totalArchivedFindings**
    

The total number of archived findings for the resource type in the internal access analyzer.

Type: Integer

Required: No

**totalResolvedFindings**
    

The total number of resolved findings for the resource type in the internal access analyzer.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/InternalAccessResourceTypeDetails)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/InternalAccessResourceTypeDetails)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/InternalAccessResourceTypeDetails)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

InternalAccessFindingsStatistics

InternetConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_InternetConfiguration.html

# InternetConfiguration

This configuration sets the network origin for the Amazon S3 access point or multi-region access point to `Internet`.

## Contents

The members of this exception structure are context-dependent.

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/InternetConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/InternetConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/InternetConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

InternalAccessResourceTypeDetails

JobDetails


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_JobDetails.html

# JobDetails

Contains details about the policy generation request.

## Contents

**jobId**
    

The `JobId` that is returned by the `StartPolicyGeneration` operation. The `JobId` can be used with `GetGeneratedPolicy` to retrieve the generated policies or used with `CancelPolicyGeneration` to cancel the policy generation request.

Type: String

Required: Yes

**startedOn**
    

A timestamp of when the job was started.

Type: Timestamp

Required: Yes

**status**
    

The status of the job request.

Type: String

Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED | CANCELED`

Required: Yes

**completedOn**
    

A timestamp of when the job was completed.

Type: Timestamp

Required: No

**jobError**
    

The job error for the policy generation request.

Type: [JobError](./API_JobError.html) object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/JobDetails)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/JobDetails)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/JobDetails)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

InternetConfiguration

JobError


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_JobError.html

# JobError

Contains the details about the policy generation error.

## Contents

**code**
    

The job error code.

Type: String

Valid Values: `AUTHORIZATION_ERROR | RESOURCE_NOT_FOUND_ERROR | SERVICE_QUOTA_EXCEEDED_ERROR | SERVICE_ERROR`

Required: Yes

**message**
    

Specific information about the error. For example, which service quota was exceeded or which resource was not found.

Type: String

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/JobError)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/JobError)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/JobError)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

JobDetails

KmsGrantConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_KmsGrantConfiguration.html

# KmsGrantConfiguration

A proposed grant configuration for a KMS key. For more information, see [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html).

## Contents

**granteePrincipal**
    

The principal that is given permission to perform the operations that the grant permits.

Type: String

Required: Yes

**issuingAccount**
    

The AWS account under which the grant was issued. The account is used to propose AWS KMS grants issued by accounts other than the owner of the key.

Type: String

Required: Yes

**operations**
    

A list of operations that the grant permits.

Type: Array of strings

Valid Values: `CreateGrant | Decrypt | DescribeKey | Encrypt | GenerateDataKey | GenerateDataKeyPair | GenerateDataKeyPairWithoutPlaintext | GenerateDataKeyWithoutPlaintext | GetPublicKey | ReEncryptFrom | ReEncryptTo | RetireGrant | Sign | Verify`

Required: Yes

**constraints**
    

Use this structure to propose allowing [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) in the grant only when the operation request includes the specified [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context).

Type: [KmsGrantConstraints](./API_KmsGrantConstraints.html) object

Required: No

**retiringPrincipal**
    

The principal that is given permission to retire the grant by using [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) operation.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/KmsGrantConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/KmsGrantConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/KmsGrantConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

JobError

KmsGrantConstraints


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_KmsGrantConstraints.html

# KmsGrantConstraints

Use this structure to propose allowing [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) in the grant only when the operation request includes the specified [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context). You can specify only one type of encryption context. An empty map is treated as not specified. For more information, see [GrantConstraints](https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html).

## Contents

**encryptionContextEquals**
    

A list of key-value pairs that must match the encryption context in the [cryptographic operation](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) request. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint.

Type: String to string map

Required: No

**encryptionContextSubset**
    

A list of key-value pairs that must be included in the encryption context of the [cryptographic operation](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) request. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs.

Type: String to string map

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/KmsGrantConstraints)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/KmsGrantConstraints)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/KmsGrantConstraints)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

KmsGrantConfiguration

KmsKeyConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_KmsKeyConfiguration.html

# KmsKeyConfiguration

Proposed access control configuration for a KMS key. You can propose a configuration for a new KMS key or an existing KMS key that you own by specifying the key policy and AWS KMS grant configuration. If the configuration is for an existing key and you do not specify the key policy, the access preview uses the existing policy for the key. If the access preview is for a new resource and you do not specify the key policy, then the access preview uses the default key policy. The proposed key policy cannot be an empty string. For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default). For more information about key policy limits, see [Resource quotas](https://docs.aws.amazon.com/kms/latest/developerguide/resource-limits.html).

## Contents

**grants**
    

A list of proposed grant configurations for the KMS key. If the proposed grant configuration is for an existing key, the access preview uses the proposed list of grant configurations in place of the existing grants. Otherwise, the access preview uses the existing grants for the key.

Type: Array of [KmsGrantConfiguration](./API_KmsGrantConfiguration.html) objects

Required: No

**keyPolicies**
    

Resource policy configuration for the KMS key. The only valid value for the name of the key policy is `default`. For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default).

Type: String to string map

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/KmsKeyConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/KmsKeyConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/KmsKeyConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

KmsGrantConstraints

Location


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Location.html

# Location

A location in a policy that is represented as a path through the JSON representation and a corresponding span.

## Contents

**path**
    

A path in a policy, represented as a sequence of path elements.

Type: Array of [PathElement](./API_PathElement.html) objects

Required: Yes

**span**
    

A span in a policy.

Type: [Span](./API_Span.html) object

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/Location)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/Location)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/Location)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

KmsKeyConfiguration

NetworkOriginConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_NetworkOriginConfiguration.html

# NetworkOriginConfiguration

The proposed `InternetConfiguration` or `VpcConfiguration` to apply to the Amazon S3 access point. You can make the access point accessible from the internet, or you can specify that all requests made through that access point must originate from a specific virtual private cloud (VPC). You can specify only one type of network configuration. For more information, see [Creating access points](https://docs.aws.amazon.com/AmazonS3/latest/dev/creating-access-points.html).

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**internetConfiguration**
    

The configuration for the Amazon S3 access point or multi-region access point with an `Internet` origin.

Type: [InternetConfiguration](./API_InternetConfiguration.html) object

Required: No

**vpcConfiguration**
    

The proposed virtual private cloud (VPC) configuration for the Amazon S3 access point. VPC configuration does not apply to multi-region access points. For more information, see [VpcConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_VpcConfiguration.html). 

Type: [VpcConfiguration](./API_VpcConfiguration.html) object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/NetworkOriginConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/NetworkOriginConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/NetworkOriginConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Location

PathElement


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_PathElement.html

# PathElement

A single element in a path through the JSON representation of a policy.

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**index**
    

Refers to an index in a JSON array.

Type: Integer

Required: No

**key**
    

Refers to a key in a JSON object.

Type: String

Required: No

**substring**
    

Refers to a substring of a literal string in a JSON object.

Type: [Substring](./API_Substring.html) object

Required: No

**value**
    

Refers to the value associated with a given key in a JSON object.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/PathElement)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/PathElement)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/PathElement)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

NetworkOriginConfiguration

PolicyGeneration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_PolicyGeneration.html

# PolicyGeneration

Contains details about the policy generation status and properties.

## Contents

**jobId**
    

The `JobId` that is returned by the `StartPolicyGeneration` operation. The `JobId` can be used with `GetGeneratedPolicy` to retrieve the generated policies or used with `CancelPolicyGeneration` to cancel the policy generation request.

Type: String

Required: Yes

**principalArn**
    

The ARN of the IAM entity (user or role) for which you are generating a policy.

Type: String

Pattern: `arn:[^:]*:iam::[^:]*:(role|user)/.{1,576}`

Required: Yes

**startedOn**
    

A timestamp of when the policy generation started.

Type: Timestamp

Required: Yes

**status**
    

The status of the policy generation request.

Type: String

Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED | CANCELED`

Required: Yes

**completedOn**
    

A timestamp of when the policy generation was completed.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/PolicyGeneration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/PolicyGeneration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/PolicyGeneration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

PathElement

PolicyGenerationDetails


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_PolicyGenerationDetails.html

# PolicyGenerationDetails

Contains the ARN details about the IAM entity for which the policy is generated.

## Contents

**principalArn**
    

The ARN of the IAM entity (user or role) for which you are generating a policy.

Type: String

Pattern: `arn:[^:]*:iam::[^:]*:(role|user)/.{1,576}`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/PolicyGenerationDetails)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/PolicyGenerationDetails)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/PolicyGenerationDetails)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

PolicyGeneration

Position


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Position.html

# Position

A position in a policy.

## Contents

**column**
    

The column of the position, starting from 0.

Type: Integer

Required: Yes

**line**
    

The line of the position, starting from 1.

Type: Integer

Required: Yes

**offset**
    

The offset within the policy that corresponds to the position, starting from 0.

Type: Integer

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/Position)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/Position)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/Position)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

PolicyGenerationDetails

RdsDbClusterSnapshotAttributeValue


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_RdsDbClusterSnapshotAttributeValue.html

# RdsDbClusterSnapshotAttributeValue

The values for a manual Amazon RDS DB cluster snapshot attribute.

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**accountIds**
    

The AWS account IDs that have access to the manual Amazon RDS DB cluster snapshot. If the value `all` is specified, then the Amazon RDS DB cluster snapshot is public and can be copied or restored by all AWS accounts.

  * If the configuration is for an existing Amazon RDS DB cluster snapshot and you do not specify the `accountIds` in `RdsDbClusterSnapshotAttributeValue`, then the access preview uses the existing shared `accountIds` for the snapshot.

  * If the access preview is for a new resource and you do not specify the specify the `accountIds` in `RdsDbClusterSnapshotAttributeValue`, then the access preview considers the snapshot without any attributes.

  * To propose deletion of existing shared `accountIds`, you can specify an empty list for `accountIds` in the `RdsDbClusterSnapshotAttributeValue`.




Type: Array of strings

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/RdsDbClusterSnapshotAttributeValue)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/RdsDbClusterSnapshotAttributeValue)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/RdsDbClusterSnapshotAttributeValue)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Position

RdsDbClusterSnapshotConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_RdsDbClusterSnapshotConfiguration.html

# RdsDbClusterSnapshotConfiguration

The proposed access control configuration for an Amazon RDS DB cluster snapshot. You can propose a configuration for a new Amazon RDS DB cluster snapshot or an Amazon RDS DB cluster snapshot that you own by specifying the `RdsDbClusterSnapshotAttributeValue` and optional AWS KMS encryption key. For more information, see [ModifyDBClusterSnapshotAttribute](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBClusterSnapshotAttribute.html).

## Contents

**attributes**
    

The names and values of manual DB cluster snapshot attributes. Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore a manual DB cluster snapshot. The only valid value for `AttributeName` for the attribute map is `restore`

Type: String to [RdsDbClusterSnapshotAttributeValue](./API_RdsDbClusterSnapshotAttributeValue.html) object map

Required: No

**kmsKeyId**
    

The KMS key identifier for an encrypted Amazon RDS DB cluster snapshot. The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

  * If the configuration is for an existing Amazon RDS DB cluster snapshot and you do not specify the `kmsKeyId`, or you specify an empty string, then the access preview uses the existing `kmsKeyId` of the snapshot.

  * If the access preview is for a new resource and you do not specify the specify the `kmsKeyId`, then the access preview considers the snapshot as unencrypted.




Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/RdsDbClusterSnapshotConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/RdsDbClusterSnapshotConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/RdsDbClusterSnapshotConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

RdsDbClusterSnapshotAttributeValue

RdsDbSnapshotAttributeValue


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_RdsDbSnapshotAttributeValue.html

# RdsDbSnapshotAttributeValue

The name and values of a manual Amazon RDS DB snapshot attribute. Manual DB snapshot attributes are used to authorize other AWS accounts to restore a manual DB snapshot.

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**accountIds**
    

The AWS account IDs that have access to the manual Amazon RDS DB snapshot. If the value `all` is specified, then the Amazon RDS DB snapshot is public and can be copied or restored by all AWS accounts.

  * If the configuration is for an existing Amazon RDS DB snapshot and you do not specify the `accountIds` in `RdsDbSnapshotAttributeValue`, then the access preview uses the existing shared `accountIds` for the snapshot.

  * If the access preview is for a new resource and you do not specify the specify the `accountIds` in `RdsDbSnapshotAttributeValue`, then the access preview considers the snapshot without any attributes.

  * To propose deletion of an existing shared `accountIds`, you can specify an empty list for `accountIds` in the `RdsDbSnapshotAttributeValue`.




Type: Array of strings

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/RdsDbSnapshotAttributeValue)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/RdsDbSnapshotAttributeValue)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/RdsDbSnapshotAttributeValue)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

RdsDbClusterSnapshotConfiguration

RdsDbSnapshotConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_RdsDbSnapshotConfiguration.html

# RdsDbSnapshotConfiguration

The proposed access control configuration for an Amazon RDS DB snapshot. You can propose a configuration for a new Amazon RDS DB snapshot or an Amazon RDS DB snapshot that you own by specifying the `RdsDbSnapshotAttributeValue` and optional AWS KMS encryption key. For more information, see [ModifyDBSnapshotAttribute](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBSnapshotAttribute.html).

## Contents

**attributes**
    

The names and values of manual DB snapshot attributes. Manual DB snapshot attributes are used to authorize other AWS accounts to restore a manual DB snapshot. The only valid value for `attributeName` for the attribute map is restore.

Type: String to [RdsDbSnapshotAttributeValue](./API_RdsDbSnapshotAttributeValue.html) object map

Required: No

**kmsKeyId**
    

The KMS key identifier for an encrypted Amazon RDS DB snapshot. The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.

  * If the configuration is for an existing Amazon RDS DB snapshot and you do not specify the `kmsKeyId`, or you specify an empty string, then the access preview uses the existing `kmsKeyId` of the snapshot.

  * If the access preview is for a new resource and you do not specify the specify the `kmsKeyId`, then the access preview considers the snapshot as unencrypted.




Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/RdsDbSnapshotConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/RdsDbSnapshotConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/RdsDbSnapshotConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

RdsDbSnapshotAttributeValue

ReasonSummary


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ReasonSummary.html

# ReasonSummary

Contains information about the reasoning why a check for access passed or failed.

## Contents

**description**
    

A description of the reasoning of a result of checking for access.

Type: String

Required: No

**statementId**
    

The identifier for the reason statement.

Type: String

Required: No

**statementIndex**
    

The index number of the reason statement.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ReasonSummary)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ReasonSummary)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ReasonSummary)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

RdsDbSnapshotConfiguration

RecommendationError


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_RecommendationError.html

# RecommendationError

Contains information about the reason that the retrieval of a recommendation for a finding failed.

## Contents

**code**
    

The error code for a failed retrieval of a recommendation for a finding.

Type: String

Required: Yes

**message**
    

The error message for a failed retrieval of a recommendation for a finding.

Type: String

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/RecommendationError)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/RecommendationError)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/RecommendationError)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ReasonSummary

RecommendedStep


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_RecommendedStep.html

# RecommendedStep

Contains information about a recommended step for an unused access analyzer finding.

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**unusedPermissionsRecommendedStep**
    

A recommended step for an unused permissions finding.

Type: [UnusedPermissionsRecommendedStep](./API_UnusedPermissionsRecommendedStep.html) object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/RecommendedStep)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/RecommendedStep)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/RecommendedStep)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

RecommendationError

ResourceTypeDetails


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ResourceTypeDetails.html

# ResourceTypeDetails

Contains information about the total number of active cross-account and public findings for a resource type of an external access analyzer.

## Contents

**totalActiveCrossAccount**
    

The total number of active cross-account findings for the resource type.

Type: Integer

Required: No

**totalActiveErrors**
    

The total number of active errors for the resource type.

Type: Integer

Required: No

**totalActivePublic**
    

The total number of active public findings for the resource type.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ResourceTypeDetails)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ResourceTypeDetails)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ResourceTypeDetails)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

RecommendedStep

S3AccessPointConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_S3AccessPointConfiguration.html

# S3AccessPointConfiguration

The configuration for an Amazon S3 access point or multi-region access point for the bucket. You can propose up to 10 access points or multi-region access points per bucket. If the proposed Amazon S3 access point configuration is for an existing bucket, the access preview uses the proposed access point configuration in place of the existing access points. To propose an access point without a policy, you can provide an empty string as the access point policy. For more information, see [Creating access points](https://docs.aws.amazon.com/AmazonS3/latest/dev/creating-access-points.html). For more information about access point policy limits, see [Access points restrictions and limitations](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points-restrictions-limitations.html).

## Contents

**accessPointPolicy**
    

The access point or multi-region access point policy.

Type: String

Required: No

**networkOrigin**
    

The proposed `Internet` and `VpcConfiguration` to apply to this Amazon S3 access point. `VpcConfiguration` does not apply to multi-region access points. If the access preview is for a new resource and neither is specified, the access preview uses `Internet` for the network origin. If the access preview is for an existing resource and neither is specified, the access preview uses the existing network origin.

Type: [NetworkOriginConfiguration](./API_NetworkOriginConfiguration.html) object

**Note:** This object is a Union. Only one member of this object can be specified or returned.

Required: No

**publicAccessBlock**
    

The proposed `S3PublicAccessBlock` configuration to apply to this Amazon S3 access point or multi-region access point.

Type: [S3PublicAccessBlockConfiguration](./API_S3PublicAccessBlockConfiguration.html) object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/S3AccessPointConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/S3AccessPointConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/S3AccessPointConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ResourceTypeDetails

S3BucketAclGrantConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_S3BucketAclGrantConfiguration.html

# S3BucketAclGrantConfiguration

A proposed access control list grant configuration for an Amazon S3 bucket. For more information, see [How to Specify an ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#setting-acls).

## Contents

**grantee**
    

The grantee to whom youâre assigning access rights.

Type: [AclGrantee](./API_AclGrantee.html) object

**Note:** This object is a Union. Only one member of this object can be specified or returned.

Required: Yes

**permission**
    

The permissions being granted.

Type: String

Valid Values: `READ | WRITE | READ_ACP | WRITE_ACP | FULL_CONTROL`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/S3BucketAclGrantConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/S3BucketAclGrantConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/S3BucketAclGrantConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

S3AccessPointConfiguration

S3BucketConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_S3BucketConfiguration.html

# S3BucketConfiguration

Proposed access control configuration for an Amazon S3 bucket. You can propose a configuration for a new Amazon S3 bucket or an existing Amazon S3 bucket that you own by specifying the Amazon S3 bucket policy, bucket ACLs, bucket BPA settings, Amazon S3 access points, and multi-region access points attached to the bucket. If the configuration is for an existing Amazon S3 bucket and you do not specify the Amazon S3 bucket policy, the access preview uses the existing policy attached to the bucket. If the access preview is for a new resource and you do not specify the Amazon S3 bucket policy, the access preview assumes a bucket without a policy. To propose deletion of an existing bucket policy, you can specify an empty string. For more information about bucket policy limits, see [Bucket Policy Examples](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html).

## Contents

**accessPoints**
    

The configuration of Amazon S3 access points or multi-region access points for the bucket. You can propose up to 10 new access points per bucket.

Type: String to [S3AccessPointConfiguration](./API_S3AccessPointConfiguration.html) object map

Key Pattern: `arn:[^:]*:s3:[^:]*:[^:]*:accesspoint/.*`

Required: No

**bucketAclGrants**
    

The proposed list of ACL grants for the Amazon S3 bucket. You can propose up to 100 ACL grants per bucket. If the proposed grant configuration is for an existing bucket, the access preview uses the proposed list of grant configurations in place of the existing grants. Otherwise, the access preview uses the existing grants for the bucket.

Type: Array of [S3BucketAclGrantConfiguration](./API_S3BucketAclGrantConfiguration.html) objects

Required: No

**bucketPolicy**
    

The proposed bucket policy for the Amazon S3 bucket.

Type: String

Required: No

**bucketPublicAccessBlock**
    

The proposed block public access configuration for the Amazon S3 bucket.

Type: [S3PublicAccessBlockConfiguration](./API_S3PublicAccessBlockConfiguration.html) object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/S3BucketConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/S3BucketConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/S3BucketConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

S3BucketAclGrantConfiguration

S3ExpressDirectoryAccessPointConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_S3ExpressDirectoryAccessPointConfiguration.html

# S3ExpressDirectoryAccessPointConfiguration

Proposed configuration for an access point attached to an Amazon S3 directory bucket. You can propose up to 10 access points per bucket. If the proposed access point configuration is for an existing Amazon S3 directory bucket, the access preview uses the proposed access point configuration in place of the existing access points. To propose an access point without a policy, you can provide an empty string as the access point policy. For more information about access points for Amazon S3 directory buckets, see [Managing access to directory buckets with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html) in the Amazon Simple Storage Service User Guide.

## Contents

**accessPointPolicy**
    

The proposed access point policy for an Amazon S3 directory bucket access point.

Type: String

Required: No

**networkOrigin**
    

The proposed `InternetConfiguration` or `VpcConfiguration` to apply to the Amazon S3 access point. You can make the access point accessible from the internet, or you can specify that all requests made through that access point must originate from a specific virtual private cloud (VPC). You can specify only one type of network configuration. For more information, see [Creating access points](https://docs.aws.amazon.com/AmazonS3/latest/dev/creating-access-points.html).

Type: [NetworkOriginConfiguration](./API_NetworkOriginConfiguration.html) object

**Note:** This object is a Union. Only one member of this object can be specified or returned.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/S3ExpressDirectoryAccessPointConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/S3ExpressDirectoryAccessPointConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/S3ExpressDirectoryAccessPointConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

S3BucketConfiguration

S3ExpressDirectoryBucketConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_S3ExpressDirectoryBucketConfiguration.html

# S3ExpressDirectoryBucketConfiguration

Proposed access control configuration for an Amazon S3 directory bucket. You can propose a configuration for a new Amazon S3 directory bucket or an existing Amazon S3 directory bucket that you own by specifying the Amazon S3 bucket policy. If the configuration is for an existing Amazon S3 directory bucket and you do not specify the Amazon S3 bucket policy, the access preview uses the existing policy attached to the directory bucket. If the access preview is for a new resource and you do not specify the Amazon S3 bucket policy, the access preview assumes an directory bucket without a policy. To propose deletion of an existing bucket policy, you can specify an empty string. For more information about Amazon S3 directory bucket policies, see [Example bucket policies for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam-example-bucket-policies.html) in the Amazon Simple Storage Service User Guide.

## Contents

**accessPoints**
    

The proposed access points for the Amazon S3 directory bucket.

Type: String to [S3ExpressDirectoryAccessPointConfiguration](./API_S3ExpressDirectoryAccessPointConfiguration.html) object map

Key Pattern: `arn:[^:]*:s3express:[^:]*:[^:]*:accesspoint/.*`

Required: No

**bucketPolicy**
    

The proposed bucket policy for the Amazon S3 directory bucket.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/S3ExpressDirectoryBucketConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/S3ExpressDirectoryBucketConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/S3ExpressDirectoryBucketConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

S3ExpressDirectoryAccessPointConfiguration

S3PublicAccessBlockConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_S3PublicAccessBlockConfiguration.html

# S3PublicAccessBlockConfiguration

The `PublicAccessBlock` configuration to apply to this Amazon S3 bucket. If the proposed configuration is for an existing Amazon S3 bucket and the configuration is not specified, the access preview uses the existing setting. If the proposed configuration is for a new bucket and the configuration is not specified, the access preview uses `false`. If the proposed configuration is for a new access point or multi-region access point and the access point BPA configuration is not specified, the access preview uses `true`. For more information, see [PublicAccessBlockConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-publicaccessblockconfiguration.html). 

## Contents

**ignorePublicAcls**
    

Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket. 

Type: Boolean

Required: Yes

**restrictPublicBuckets**
    

Specifies whether Amazon S3 should restrict public bucket policies for this bucket. 

Type: Boolean

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/S3PublicAccessBlockConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/S3PublicAccessBlockConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/S3PublicAccessBlockConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

S3ExpressDirectoryBucketConfiguration

SecretsManagerSecretConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_SecretsManagerSecretConfiguration.html

# SecretsManagerSecretConfiguration

The configuration for a Secrets Manager secret. For more information, see [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html).

You can propose a configuration for a new secret or an existing secret that you own by specifying the secret policy and optional AWS KMS encryption key. If the configuration is for an existing secret and you do not specify the secret policy, the access preview uses the existing policy for the secret. If the access preview is for a new resource and you do not specify the policy, the access preview assumes a secret without a policy. To propose deletion of an existing policy, you can specify an empty string. If the proposed configuration is for a new secret and you do not specify the KMS key ID, the access preview uses the AWS managed key `aws/secretsmanager`. If you specify an empty string for the KMS key ID, the access preview uses the AWS managed key of the AWS account. For more information about secret policy limits, see [Quotas for AWS Secrets Manager.](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_limits.html).

## Contents

**kmsKeyId**
    

The proposed ARN, key ID, or alias of the KMS key.

Type: String

Required: No

**secretPolicy**
    

The proposed resource policy defining who can access or manage the secret.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/SecretsManagerSecretConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/SecretsManagerSecretConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/SecretsManagerSecretConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

S3PublicAccessBlockConfiguration

SnsTopicConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_SnsTopicConfiguration.html

# SnsTopicConfiguration

The proposed access control configuration for an Amazon SNS topic. You can propose a configuration for a new Amazon SNS topic or an existing Amazon SNS topic that you own by specifying the policy. If the configuration is for an existing Amazon SNS topic and you do not specify the Amazon SNS policy, then the access preview uses the existing Amazon SNS policy for the topic. If the access preview is for a new resource and you do not specify the policy, then the access preview assumes an Amazon SNS topic without a policy. To propose deletion of an existing Amazon SNS topic policy, you can specify an empty string for the Amazon SNS policy. For more information, see [Topic](https://docs.aws.amazon.com/sns/latest/api/API_Topic.html).

## Contents

**topicPolicy**
    

The JSON policy text that defines who can access an Amazon SNS topic. For more information, see [Example cases for Amazon SNS access control](https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-use-cases.html) in the _Amazon SNS Developer Guide_.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 30720.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/SnsTopicConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/SnsTopicConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/SnsTopicConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

SecretsManagerSecretConfiguration

SortCriteria


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_SortCriteria.html

# SortCriteria

The criteria used to sort.

## Contents

**attributeName**
    

The name of the attribute to sort on.

Type: String

Required: No

**orderBy**
    

The sort order, ascending or descending.

Type: String

Valid Values: `ASC | DESC`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/SortCriteria)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/SortCriteria)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/SortCriteria)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

SnsTopicConfiguration

Span


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Span.html

# Span

A span in a policy. The span consists of a start position (inclusive) and end position (exclusive).

## Contents

**end**
    

The end position of the span (exclusive).

Type: [Position](./API_Position.html) object

Required: Yes

**start**
    

The start position of the span (inclusive).

Type: [Position](./API_Position.html) object

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/Span)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/Span)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/Span)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

SortCriteria

SqsQueueConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_SqsQueueConfiguration.html

# SqsQueueConfiguration

The proposed access control configuration for an Amazon SQS queue. You can propose a configuration for a new Amazon SQS queue or an existing Amazon SQS queue that you own by specifying the Amazon SQS policy. If the configuration is for an existing Amazon SQS queue and you do not specify the Amazon SQS policy, the access preview uses the existing Amazon SQS policy for the queue. If the access preview is for a new resource and you do not specify the policy, the access preview assumes an Amazon SQS queue without a policy. To propose deletion of an existing Amazon SQS queue policy, you can specify an empty string for the Amazon SQS policy. For more information about Amazon SQS policy limits, see [Quotas related to policies](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-policies.html).

## Contents

**queuePolicy**
    

The proposed resource policy for the Amazon SQS queue. 

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/SqsQueueConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/SqsQueueConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/SqsQueueConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Span

StatusReason


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_StatusReason.html

# StatusReason

Provides more details about the current status of the analyzer. For example, if the creation for the analyzer fails, a `Failed` status is returned. For an analyzer with organization as the type, this failure can be due to an issue with creating the service-linked roles required in the member accounts of the AWS organization.

## Contents

**code**
    

The reason code for the current status of the analyzer.

Type: String

Valid Values: `AWS_SERVICE_ACCESS_DISABLED | DELEGATED_ADMINISTRATOR_DEREGISTERED | ORGANIZATION_DELETED | SERVICE_LINKED_ROLE_CREATION_FAILED`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/StatusReason)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/StatusReason)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/StatusReason)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

SqsQueueConfiguration

Substring


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Substring.html

# Substring

A reference to a substring of a literal string in a JSON document.

## Contents

**length**
    

The length of the substring.

Type: Integer

Required: Yes

**start**
    

The start index of the substring, starting from 0.

Type: Integer

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/Substring)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/Substring)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/Substring)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

StatusReason

Trail


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Trail.html

# Trail

Contains details about the CloudTrail trail being analyzed to generate a policy.

## Contents

**cloudTrailArn**
    

Specifies the ARN of the trail. The format of a trail ARN is `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`.

Type: String

Pattern: `arn:[^:]*:cloudtrail:[^:]*:[^:]*:trail/.{1,576}`

Required: Yes

**allRegions**
    

Possible values are `true` or `false`. If set to `true`, IAM Access Analyzer retrieves CloudTrail data from all regions to analyze and generate a policy.

Type: Boolean

Required: No

**regions**
    

A list of regions to get CloudTrail data from and analyze to generate a policy.

Type: Array of strings

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/Trail)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/Trail)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/Trail)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Substring

TrailProperties


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_TrailProperties.html

# TrailProperties

Contains details about the CloudTrail trail being analyzed to generate a policy.

## Contents

**cloudTrailArn**
    

Specifies the ARN of the trail. The format of a trail ARN is `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`.

Type: String

Pattern: `arn:[^:]*:cloudtrail:[^:]*:[^:]*:trail/.{1,576}`

Required: Yes

**allRegions**
    

Possible values are `true` or `false`. If set to `true`, IAM Access Analyzer retrieves CloudTrail data from all regions to analyze and generate a policy.

Type: Boolean

Required: No

**regions**
    

A list of regions to get CloudTrail data from and analyze to generate a policy.

Type: Array of strings

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/TrailProperties)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/TrailProperties)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/TrailProperties)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Trail

UnusedAccessConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedAccessConfiguration.html

# UnusedAccessConfiguration

Contains information about an unused access analyzer.

## Contents

**analysisRule**
    

Contains information about analysis rules for the analyzer. Analysis rules determine which entities will generate findings based on the criteria you define when you create the rule.

Type: [AnalysisRule](./API_AnalysisRule.html) object

Required: No

**unusedAccessAge**
    

The specified access age in days for which to generate findings for unused access. For example, if you specify 90 days, the analyzer will generate findings for IAM entities within the accounts of the selected organization for any access that hasn't been used in 90 or more days since the analyzer's last scan. You can choose a value between 1 and 365 days.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedAccessConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedAccessConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedAccessConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

TrailProperties

UnusedAccessFindingsStatistics


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedAccessFindingsStatistics.html

# UnusedAccessFindingsStatistics

Provides aggregate statistics about the findings for the specified unused access analyzer.

## Contents

**topAccounts**
    

A list of one to ten AWS accounts that have the most active findings for the unused access analyzer.

Type: Array of [FindingAggregationAccountDetails](./API_FindingAggregationAccountDetails.html) objects

Array Members: Minimum number of 1 item. Maximum number of 10 items.

Required: No

**totalActiveFindings**
    

The total number of active findings for the unused access analyzer.

Type: Integer

Required: No

**totalArchivedFindings**
    

The total number of archived findings for the unused access analyzer.

Type: Integer

Required: No

**totalResolvedFindings**
    

The total number of resolved findings for the unused access analyzer.

Type: Integer

Required: No

**unusedAccessTypeStatistics**
    

A list of details about the total number of findings for each type of unused access for the analyzer. 

Type: Array of [UnusedAccessTypeStatistics](./API_UnusedAccessTypeStatistics.html) objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedAccessFindingsStatistics)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedAccessFindingsStatistics)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedAccessFindingsStatistics)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

UnusedAccessConfiguration

UnusedAccessTypeStatistics


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedAccessTypeStatistics.html

# UnusedAccessTypeStatistics

Contains information about the total number of findings for a type of unused access.

## Contents

**total**
    

The total number of findings for the specified unused access type.

Type: Integer

Required: No

**unusedAccessType**
    

The type of unused access.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedAccessTypeStatistics)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedAccessTypeStatistics)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedAccessTypeStatistics)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

UnusedAccessFindingsStatistics

UnusedAction


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedAction.html

# UnusedAction

Contains information about an unused access finding for an action. IAM Access Analyzer charges for unused access analysis based on the number of IAM roles and users analyzed per month. For more details on pricing, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing).

## Contents

**action**
    

The action for which the unused access finding was generated.

Type: String

Required: Yes

**lastAccessed**
    

The time at which the action was last accessed.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedAction)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedAction)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedAction)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

UnusedAccessTypeStatistics

UnusedIamRoleDetails


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedIamRoleDetails.html

# UnusedIamRoleDetails

Contains information about an unused access finding for an IAM role. IAM Access Analyzer charges for unused access analysis based on the number of IAM roles and users analyzed per month. For more details on pricing, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing).

## Contents

**lastAccessed**
    

The time at which the role was last accessed.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedIamRoleDetails)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedIamRoleDetails)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedIamRoleDetails)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

UnusedAction

UnusedIamUserAccessKeyDetails


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedIamUserAccessKeyDetails.html

# UnusedIamUserAccessKeyDetails

Contains information about an unused access finding for an IAM user access key. IAM Access Analyzer charges for unused access analysis based on the number of IAM roles and users analyzed per month. For more details on pricing, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing).

## Contents

**accessKeyId**
    

The ID of the access key for which the unused access finding was generated.

Type: String

Required: Yes

**lastAccessed**
    

The time at which the access key was last accessed.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedIamUserAccessKeyDetails)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedIamUserAccessKeyDetails)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedIamUserAccessKeyDetails)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

UnusedIamRoleDetails

UnusedIamUserPasswordDetails


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedIamUserPasswordDetails.html

# UnusedIamUserPasswordDetails

Contains information about an unused access finding for an IAM user password. IAM Access Analyzer charges for unused access analysis based on the number of IAM roles and users analyzed per month. For more details on pricing, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing).

## Contents

**lastAccessed**
    

The time at which the password was last accessed.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedIamUserPasswordDetails)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedIamUserPasswordDetails)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedIamUserPasswordDetails)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

UnusedIamUserAccessKeyDetails

UnusedPermissionDetails


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedPermissionDetails.html

# UnusedPermissionDetails

Contains information about an unused access finding for a permission. IAM Access Analyzer charges for unused access analysis based on the number of IAM roles and users analyzed per month. For more details on pricing, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing).

## Contents

**serviceNamespace**
    

The namespace of the AWS service that contains the unused actions.

Type: String

Required: Yes

**actions**
    

A list of unused actions for which the unused access finding was generated.

Type: Array of [UnusedAction](./API_UnusedAction.html) objects

Required: No

**lastAccessed**
    

The time at which the permission was last accessed.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedPermissionDetails)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedPermissionDetails)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedPermissionDetails)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

UnusedIamUserPasswordDetails

UnusedPermissionsRecommendedStep


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedPermissionsRecommendedStep.html

# UnusedPermissionsRecommendedStep

Contains information about the action to take for a policy in an unused permissions finding.

## Contents

**recommendedAction**
    

A recommendation of whether to create or detach a policy for an unused permissions finding.

Type: String

Valid Values: `CREATE_POLICY | DETACH_POLICY`

Required: Yes

**existingPolicyId**
    

If the recommended action for the unused permissions finding is to detach a policy, the ID of an existing policy to be detached.

Type: String

Required: No

**policyUpdatedAt**
    

The time at which the existing policy for the unused permissions finding was last updated.

Type: Timestamp

Required: No

**recommendedPolicy**
    

If the recommended action for the unused permissions finding is to replace the existing policy, the contents of the recommended policy to replace the policy specified in the `existingPolicyId` field.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedPermissionsRecommendedStep)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedPermissionsRecommendedStep)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedPermissionsRecommendedStep)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

UnusedPermissionDetails

ValidatePolicyFinding


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidatePolicyFinding.html

# ValidatePolicyFinding

A finding in a policy. Each finding is an actionable recommendation that can be used to improve the policy.

## Contents

**findingDetails**
    

A localized message that explains the finding and provides guidance on how to address it.

Type: String

Required: Yes

**findingType**
    

The impact of the finding.

Security warnings report when the policy allows access that we consider overly permissive.

Errors report when a part of the policy is not functional.

Warnings report non-security issues when a policy does not conform to policy writing best practices.

Suggestions recommend stylistic improvements in the policy that do not impact access.

Type: String

Valid Values: `ERROR | SECURITY_WARNING | SUGGESTION | WARNING`

Required: Yes

**issueCode**
    

The issue code provides an identifier of the issue associated with this finding.

Type: String

Required: Yes

**learnMoreLink**
    

A link to additional documentation about the type of finding.

Type: String

Required: Yes

**locations**
    

The list of locations in the policy document that are related to the finding. The issue code provides a summary of an issue identified by the finding.

Type: Array of [Location](./API_Location.html) objects

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ValidatePolicyFinding)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ValidatePolicyFinding)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ValidatePolicyFinding)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

UnusedPermissionsRecommendedStep

ValidationExceptionField


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidationExceptionField.html

# ValidationExceptionField

Contains information about a validation exception.

## Contents

**message**
    

A message about the validation exception.

Type: String

Required: Yes

**name**
    

The name of the validation exception.

Type: String

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ValidationExceptionField)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ValidationExceptionField)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ValidationExceptionField)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ValidatePolicyFinding

VpcConfiguration


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_VpcConfiguration.html

# VpcConfiguration

The proposed virtual private cloud (VPC) configuration for the Amazon S3 access point. VPC configuration does not apply to multi-region access points. For more information, see [VpcConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_VpcConfiguration.html). 

## Contents

**vpcId**
    

If this field is specified, this access point will only allow connections from the specified VPC ID. 

Type: String

Pattern: `vpc-([0-9a-f]){8}(([0-9a-f]){9})?`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/VpcConfiguration)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/VpcConfiguration)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/VpcConfiguration)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ValidationExceptionField

Common Parameters


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/CommonParameters.html

# Common Parameters

The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string. Any action-specific parameters are listed in the topic for that action. For more information about Signature Version 4, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in the _IAM User Guide_.

**X-Amz-Algorithm**
    

The hash algorithm that you used to create the request signature.

Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.

Type: string

Valid Values: `AWS4-HMAC-SHA256`

Required: Conditional

**X-Amz-Credential**
    

The credential scope value, which is a string that includes your access key, the date, the region you are targeting, the service you are requesting, and a termination string ("aws4_request"). The value is expressed in the following format: _access_key_ /_YYYYMMDD_ /_region_ /_service_ /aws4_request.

For more information, see [Create a signed AWS API request](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html) in the _IAM User Guide_.

Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.

Type: string

Required: Conditional

**X-Amz-Date**
    

The date that is used to create the signature. The format must be ISO 8601 basic format (YYYYMMDD'T'HHMMSS'Z'). For example, the following date time is a valid X-Amz-Date value: `20120325T120000Z`.

Condition: X-Amz-Date is optional for all requests; it can be used to override the date used for signing requests. If the Date header is specified in the ISO 8601 basic format, X-Amz-Date is not required. When X-Amz-Date is used, it always overrides the value of the Date header. For more information, see [Elements of an AWS API request signature](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-signing-elements.html) in the _IAM User Guide_.

Type: string

Required: Conditional

**X-Amz-Security-Token**
    

The temporary security token that was obtained through a call to AWS Security Token Service (AWS STS). For a list of services that support temporary security credentials from AWS STS, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the _IAM User Guide_.

Condition: If you're using temporary security credentials from AWS STS, you must include the security token.

Type: string

Required: Conditional

**X-Amz-Signature**
    

Specifies the hex-encoded signature that was calculated from the string to sign and the derived signing key.

Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.

Type: string

Required: Conditional

**X-Amz-SignedHeaders**
    

Specifies all the HTTP headers that were included as part of the canonical request. For more information about specifying signed headers, see [Create a signed AWS API request](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html) in the _IAM User Guide_.

Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.

Type: string

Required: Conditional

**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

VpcConfiguration

Common Error Types


---
# Page: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/CommonErrors.html

# Common Error Types

This section lists common error types that this AWS service may return. Not all services return all error types listed here. For errors specific to an API action for this service, see the topic for that API action.

**AccessDeniedException**
    

You don't have permission to perform this action. Verify that your IAM policy includes the required permissions.

HTTP Status Code: 403

**ExpiredTokenException**
    

The security token included in the request has expired. Request a new security token and try again.

HTTP Status Code: 403

**IncompleteSignature**
    

The request signature doesn't conform to AWS standards. Verify that you're using valid AWS credentials and that your request is properly formatted. If you're using an SDK, ensure it's up to date.

HTTP Status Code: 403

**InternalFailure**
    

The request can't be processed right now because of an internal server issue. Try again later. If the problem persists, contact AWS Support.

HTTP Status Code: 500

**MalformedHttpRequestException**
    

The request body can't be processed. This typically happens when the request body can't be decompressed using the specified content encoding algorithm. Verify that the content encoding header matches the compression format used.

HTTP Status Code: 400

**NotAuthorized**
    

You don't have permissions to perform this action. Verify that your IAM policy includes the required permissions.

HTTP Status Code: 401

**OptInRequired**
    

Your AWS account needs a subscription for this service. Verify that you've enabled the service in your account.

HTTP Status Code: 403

**RequestAbortedException**
    

The request was aborted before a response could be returned. This typically happens when the client closes the connection.

HTTP Status Code: 400

**RequestEntityTooLargeException**
    

The request entity is too large. Reduce the size of the request body and try again.

HTTP Status Code: 413

**RequestTimeoutException**
    

The request timed out. The server didn't receive the complete request within the expected time frame. Try again.

HTTP Status Code: 408

**ServiceUnavailable**
    

The service is temporarily unavailable. Try again later.

HTTP Status Code: 503

**ThrottlingException**
    

Your request rate is too high. The AWS SDKs automatically retry requests that receive this exception. Reduce the frequency of requests.

HTTP Status Code: 400

**UnknownOperationException**
    

The action or operation isn't recognized. Verify that the action name is spelled correctly and that it's supported by the API version you're using.

HTTP Status Code: 404

**UnrecognizedClientException**
    

The X.509 certificate or AWS access key ID you provided doesn't exist in our records. Verify that you're using valid credentials and that they haven't expired.

HTTP Status Code: 403

**ValidationError**
    

The input doesn't meet the required format or constraints. Check that all required parameters are included and that values are valid.

HTTP Status Code: 400

**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Common Parameters


---
