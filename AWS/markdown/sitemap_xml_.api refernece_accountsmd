# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/Welcome.html

# Welcome

The API operations in the Account Management (`account`) namespace enable you to modify your AWS account.

Every AWS account supports metadata with information about the account, including information about up to three alternate contacts associated with the account. These are in addition to the email address associated with the [root user](https://docs.aws.amazon.com/accounts/latest/reference/root-user.html) of the account. You can specify only one of each of the following contact types associated with an account.

  * Billing contact

  * Operations contact

  * Security contact




By default, the API operations discussed in this guide apply directly to the account that calls the operation. The [identity](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the account that is calling the operation is typically an IAM role or IAM user and must have permission applied by an IAM policy to call the API operation. Alternatively, you can call these API operations from an identity in an AWS Organizations management account and specify the account ID number for any AWS account that is a member of the organization.

**API version**

This version of the Accounts API Reference documents the Account Management API version 2021-02-01.

###### Note

As an alternative to using the API directly, you can use one of the AWS SDKs, which consist of libraries and sample code for various programming languages and platforms (Java, Ruby, .NET, iOS, Android, and more). The SDKs provide a convenient way to create programmatic access to Account Management. For example, the SDKs take care of cryptographically signing requests, managing errors, and retrying requests automatically. For more information about the AWS SDKs, including how to download and install them, see [Tools for Amazon Web Services](https://console.aws.amazon.com/).

We recommend that you use the AWS SDKs to make programmatic API calls to the Account Management service. However, you also can use the Account Management Query API to make direct calls to the Account Management web service. To learn more about the Account Management Query API, see [Calling the API by making HTTP Query requests](https://docs.aws.amazon.com/accounts/latest/reference/query-requests.html) in the AWS Account Management Reference Guide. Account Management supports GET and POST requests for all actions. That is, the API does not require you to use GET for some actions and POST for others. However, GET requests are subject to the limitation size of a URL. Therefore, for operations that require larger sizes, use a POST request.

**Signing requests**

When you send HTTP requests to AWS, you must sign the requests so that AWS can identify who sent them. You sign requests with your AWS access key, which consists of an access key ID and a secret access key. We strongly recommend that you do not create an access key for your root account. Anyone who has the access key for your root account has unrestricted access to all the resources in your account. Instead, create an access key for an IAM user that has administrative privileges. As another option, use AWS Security Token Service to generate temporary security credentials, and use those credentials to sign requests.

To sign requests, we recommend that you use Signature Version 4. If you have an existing application that uses Signature Version 2, you do not have to update it to use Signature Version 4. However, some operations now require Signature Version 4. The documentation for operations that require version 4 indicates this requirement. For more information, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in the _IAM User Guide_.

When you use the AWS Command Line Interface (AWS CLI) or one of the AWS SDKs to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools.

**Support and feedback for Account Management**

We welcome your feedback. Send your comments to [feedback-awsaccounts@amazon.com](mailto://feedback-awsaccounts@amazon.com) or post your feedback and questions in the [Account Management support forum](http://forums.aws.amazon.com/forum.jspa?forumID=219). For more information about the AWS support forums, see [Forums Help](http://forums.aws.amazon.com/help.jspa).

**How examples are presented**

The JSON returned by Account Management in response to your requests is a single long string without line breaks or formatting whitespace. Both line breaks and whitespace are shown in the examples in this guide to improve readability. When example input parameters also would result in long strings that would extend beyond the screen, we insert line breaks to enhance readability. You should always submit the input as a single JSON text string.

**Recording API Requests**

Account Management supports CloudTrail, a service that records AWS API calls for your AWS account and delivers log files to an Amazon S3 bucket. By using information collected by CloudTrail, you can determine which requests were successfully made to Account Management, who made the request, when it was made, and so on. For more about Account Management and its support for CloudTrail, see [Logging AWS Account Management API calls using AWS CloudTrail](https://docs.aws.amazon.com/accounts/latest/reference/monitoring-cloudtrail.html). To learn more about CloudTrail, including how to turn it on and find your log files, see the [CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

This document was last published on June 22, 2026. 

**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Actions


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_Operations.html

# Actions

The following actions are supported:

  * [AcceptPrimaryEmailUpdate](./API_AcceptPrimaryEmailUpdate.html)

  * [DeleteAlternateContact](./API_DeleteAlternateContact.html)

  * [DisableRegion](./API_DisableRegion.html)

  * [EnableRegion](./API_EnableRegion.html)

  * [GetAccountInformation](./API_GetAccountInformation.html)

  * [GetAlternateContact](./API_GetAlternateContact.html)

  * [GetContactInformation](./API_GetContactInformation.html)

  * [GetGovCloudAccountInformation](./API_GetGovCloudAccountInformation.html)

  * [GetPrimaryEmail](./API_GetPrimaryEmail.html)

  * [GetRegionOptStatus](./API_GetRegionOptStatus.html)

  * [ListRegions](./API_ListRegions.html)

  * [PutAccountName](./API_PutAccountName.html)

  * [PutAlternateContact](./API_PutAlternateContact.html)

  * [PutContactInformation](./API_PutContactInformation.html)

  * [StartPrimaryEmailUpdate](./API_StartPrimaryEmailUpdate.html)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Welcome

AcceptPrimaryEmailUpdate


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_AcceptPrimaryEmailUpdate.html

# AcceptPrimaryEmailUpdate

Accepts the request that originated from [StartPrimaryEmailUpdate](./API_StartPrimaryEmailUpdate.html) to update the primary email address (also known as the root user email address) for the specified account.

## Request Syntax
    
    
    POST /acceptPrimaryEmailUpdate HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string",
       "Otp": "string",
       "PrimaryEmail": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

This operation can only be called from the management account or the delegated administrator account of an organization for a member account.

###### Note

The management account can't specify its own `AccountId`.

Type: String

Pattern: `\d{12}`

Required: Yes

**Otp **
    

The OTP code sent to the `PrimaryEmail` specified on the `StartPrimaryEmailUpdate` API call.

Type: String

Pattern: `[a-zA-Z0-9]{6}`

Required: Yes

**PrimaryEmail **
    

The new primary email address for use with the specified account. This must match the `PrimaryEmail` from the `StartPrimaryEmailUpdate` API call.

Type: String

Length Constraints: Minimum length of 5. Maximum length of 64.

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "Status": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**Status **
    

Retrieves the status of the accepted primary email update request.

Type: String

Valid Values: `PENDING | ACCEPTED`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**ConflictException**
    

The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an accountâs root user email to an email address which is already in use.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 409

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The operation failed because it specified a resource that can't be found.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 404

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/AcceptPrimaryEmailUpdate)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/AcceptPrimaryEmailUpdate)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/AcceptPrimaryEmailUpdate)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/AcceptPrimaryEmailUpdate)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/AcceptPrimaryEmailUpdate)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/AcceptPrimaryEmailUpdate)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/AcceptPrimaryEmailUpdate)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/AcceptPrimaryEmailUpdate)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/AcceptPrimaryEmailUpdate)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/AcceptPrimaryEmailUpdate)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Actions

DeleteAlternateContact


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_DeleteAlternateContact.html

# DeleteAlternateContact

Deletes the specified alternate contact from an AWS account.

For complete details about how to use the alternate contact operations, see [Update the alternate contacts for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html).

###### Note

Before you can update the alternate contact information for an AWS account that is managed by AWS Organizations, you must first enable integration between AWS Account Management and Organizations. For more information, see [Enable trusted access for AWS Account Management](https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html).

## Request Syntax
    
    
    POST /deleteAlternateContact HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string",
       "AlternateContactType": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12 digit account ID number of the AWS account that you want to access or modify with this operation.

If you do not specify this parameter, it defaults to the AWS account of the identity used to call the operation.

To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html) enabled for the Account Management service, and optionally a [delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

###### Note

The management account can't specify its own `AccountId`; it must call the operation in standalone context by not including the `AccountId` parameter.

To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

**AlternateContactType **
    

Specifies which of the alternate contacts to delete. 

Type: String

Valid Values: `BILLING | OPERATIONS | SECURITY`

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The operation failed because it specified a resource that can't be found.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 404

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## Examples

### Example 1

The following example deletes the security alternate contact for the account whose credentials are used to call the operation. 

#### Sample Request
    
    
    POST / HTTP/1.1
    X-Amz-Target: AWSAccountV20210201.DeleteAlternateContact
    
    {
       "AccountName":"MyAccount"
    }

#### Sample Response
    
    
    HTTP/1.1 200 OK
    Content-Type: application/json

### Example 2

The following example deletes the billing alternate contact for the specified member account in an organization. You must use credentials from either the organization's management account or from the Account Management service's delegated admin account.

#### Sample Request
    
    
    POST / HTTP/1.1
    X-Amz-Target: AWSAccountV20210201.DeleteAlternateContact
    
    {
       "AccountId":"123456789012",
       "AlternateContactType":"BILLING"
    }

#### Sample Response
    
    
    HTTP/1.1 200 OK
    Content-Type: application/json

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/DeleteAlternateContact)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/DeleteAlternateContact)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/DeleteAlternateContact)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/DeleteAlternateContact)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/DeleteAlternateContact)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/DeleteAlternateContact)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/DeleteAlternateContact)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/DeleteAlternateContact)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/DeleteAlternateContact)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/DeleteAlternateContact)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AcceptPrimaryEmailUpdate

DisableRegion


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_DisableRegion.html

# DisableRegion

Disables (opts-out) a particular Region for an account.

###### Note

The act of disabling a Region will remove all IAM access to any resources that reside in that Region.

## Request Syntax
    
    
    POST /disableRegion HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string",
       "RegionName": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

###### Note

The management account can't specify its own `AccountId`. It must call the operation in standalone context by not including the `AccountId` parameter.

To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

**RegionName **
    

Specifies the Region-code for a given Region name (for example, `af-south-1`). When you disable a Region, AWS performs actions to deactivate that Region in your account, such as destroying IAM resources in the Region. This process takes a few minutes for most accounts, but this can take several hours. You cannot enable the Region until the disabling process is fully completed.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**ConflictException**
    

The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an accountâs root user email to an email address which is already in use.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 409

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/DisableRegion)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/DisableRegion)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/DisableRegion)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/DisableRegion)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/DisableRegion)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/DisableRegion)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/DisableRegion)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/DisableRegion)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/DisableRegion)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/DisableRegion)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

DeleteAlternateContact

EnableRegion


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_EnableRegion.html

# EnableRegion

Enables (opts-in) a particular Region for an account.

## Request Syntax
    
    
    POST /enableRegion HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string",
       "RegionName": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

###### Note

The management account can't specify its own `AccountId`. It must call the operation in standalone context by not including the `AccountId` parameter.

To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

**RegionName **
    

Specifies the Region-code for a given Region name (for example, `af-south-1`). When you enable a Region, AWS performs actions to prepare your account in that Region, such as distributing your IAM resources to the Region. This process takes a few minutes for most accounts, but it can take several hours. You cannot use the Region until this process is complete. Furthermore, you cannot disable the Region until the enabling process is fully completed.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**ConflictException**
    

The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an accountâs root user email to an email address which is already in use.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 409

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/EnableRegion)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/EnableRegion)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/EnableRegion)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/EnableRegion)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/EnableRegion)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/EnableRegion)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/EnableRegion)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/EnableRegion)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/EnableRegion)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/EnableRegion)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

DisableRegion

GetAccountInformation


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_GetAccountInformation.html

# GetAccountInformation

Retrieves information about the specified account including its account name, account ID, account creation date and time, and account state. To use this API, an IAM user or role must have the `account:GetAccountInformation` IAM permission. 

## Request Syntax
    
    
    POST /getAccountInformation HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12 digit account ID number of the AWS account that you want to access or modify with this operation.

If you do not specify this parameter, it defaults to the AWS account of the identity used to call the operation.

To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html) enabled for the Account Management service, and optionally a [delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

###### Note

The management account can't specify its own `AccountId`; it must call the operation in standalone context by not including the `AccountId` parameter.

To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "AccountCreatedDate": "**_string_** ",
       "AccountId": "**_string_** ",
       "AccountName": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**AccountCreatedDate **
    

The date and time the account was created.

Type: Timestamp

**AccountId **
    

Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

This operation can only be called from the management account or the delegated administrator account of an organization for a member account.

###### Note

The management account can't specify its own `AccountId`.

Type: String

Pattern: `\d{12}`

**AccountName **
    

The name of the account.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[ -;=?-~]+`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## Examples

### Example 1

The following example retrieves the account information for the account whose credentials are used to call the operation. 

#### Sample Request
    
    
    POST / HTTP/1.1
    X-Amz-Target: AWSAccountV20210201.GetAccountInformation
                        
    {}

#### Sample Response
    
    
    HTTP/1.1 200 OK
    Content-Type: application/json
                        
    {
       "AccountId": "123456789012",
       "AccountName": "MyAccount",
       "AccountCreatedDate": "2020-11-30T17:44:37Z",
       "AccountState": "ACTIVE"
    }

### Example 2

The following example retrieves the account information for the specified member account in an organization. You must use credentials from either the organization's management account or from the Account Management service's delegated admin account. 

#### Sample Request
    
    
    POST / HTTP/1.1
    X-Amz-Target: AWSAccountV20210201.GetAccountInformation
                        
    {
       "AccountId": "123456789012" 
    }

#### Sample Response
    
    
    HTTP/1.1 200 OK
    Content-Type: application/json
                        
    {
       "AccountId": "123456789012",
       "AccountName": "MyMemberAccount",
       "AccountCreatedDate": "2020-11-30T17:44:37Z",
       "AccountState": "ACTIVE"
    }

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/GetAccountInformation)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/GetAccountInformation)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/GetAccountInformation)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/GetAccountInformation)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/GetAccountInformation)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/GetAccountInformation)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/GetAccountInformation)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/GetAccountInformation)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/GetAccountInformation)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/GetAccountInformation)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

EnableRegion

GetAlternateContact


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_GetAlternateContact.html

# GetAlternateContact

Retrieves the specified alternate contact attached to an AWS account.

For complete details about how to use the alternate contact operations, see [Update the alternate contacts for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html).

###### Note

Before you can update the alternate contact information for an AWS account that is managed by AWS Organizations, you must first enable integration between AWS Account Management and Organizations. For more information, see [Enable trusted access for AWS Account Management](https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html).

## Request Syntax
    
    
    POST /getAlternateContact HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string",
       "AlternateContactType": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12 digit account ID number of the AWS account that you want to access or modify with this operation.

If you do not specify this parameter, it defaults to the AWS account of the identity used to call the operation.

To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html) enabled for the Account Management service, and optionally a [delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

###### Note

The management account can't specify its own `AccountId`; it must call the operation in standalone context by not including the `AccountId` parameter.

To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

**AlternateContactType **
    

Specifies which alternate contact you want to retrieve.

Type: String

Valid Values: `BILLING | OPERATIONS | SECURITY`

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "AlternateContact": { 
          "[AlternateContactType](./API_AlternateContact.html#accounts-Type-AlternateContact-AlternateContactType)": "**_string_** ",
          "[EmailAddress](./API_AlternateContact.html#accounts-Type-AlternateContact-EmailAddress)": "**_string_** ",
          "[Name](./API_AlternateContact.html#accounts-Type-AlternateContact-Name)": "**_string_** ",
          "[PhoneNumber](./API_AlternateContact.html#accounts-Type-AlternateContact-PhoneNumber)": "**_string_** ",
          "[Title](./API_AlternateContact.html#accounts-Type-AlternateContact-Title)": "**_string_** "
       }
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**AlternateContact **
    

A structure that contains the details for the specified alternate contact.

Type: [AlternateContact](./API_AlternateContact.html) object

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The operation failed because it specified a resource that can't be found.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 404

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## Examples

### Example 1

The following example retrieves the security alternate contact for the account whose credentials are used to call the operation. 

#### Sample Request
    
    
    POST / HTTP/1.1
    X-Amz-Target: AWSAccountV20210201.GetAlternateContact
    
    {
       "AlternateContactType":"SECURITY"
    }

#### Sample Response
    
    
    HTTP/1.1 200 OK
    Content-Type: application/json
    
    {
       "AlternateContact":{
          "Name":"Anika",
          "Title":"COO",
          "EmailAddress":"anika@example.com",
          "PhoneNumber":"206-555-0198",
          "AlternateContactType":"Security"
       }
    }

### Example 2

The following example retrieves the operations alternate contact for the specified member account in an organization. You must use credentials from either the organization's management account or from the Account Management service's delegated admin account.

#### Sample Request
    
    
    POST / HTTP/1.1
    X-Amz-Target: AWSAccountV20210201.GetAlternateContact
    
    {
       "AccountId":"123456789012",
       "AlternateContactType":"Operations"
    }

#### Sample Response
    
    
    HTTP/1.1 200 OK
    Content-Type: application/json
    
    {
       "AlternateContact":{
          "Name":"Anika",
          "Title":"COO",
          "EmailAddress":"anika@example.com",
          "PhoneNumber":"206-555-0198",
          "AlternateContactType":"Operations"
       }
    }

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/GetAlternateContact)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/GetAlternateContact)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/GetAlternateContact)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/GetAlternateContact)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/GetAlternateContact)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/GetAlternateContact)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/GetAlternateContact)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/GetAlternateContact)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/GetAlternateContact)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/GetAlternateContact)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetAccountInformation

GetContactInformation


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_GetContactInformation.html

# GetContactInformation

Retrieves the primary contact information of an AWS account.

For complete details about how to use the primary contact operations, see [Update the primary contact for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html).

## Request Syntax
    
    
    POST /getContactInformation HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

###### Note

The management account can't specify its own `AccountId`. It must call the operation in standalone context by not including the `AccountId` parameter.

To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "ContactInformation": { 
          "[AddressLine1](./API_ContactInformation.html#accounts-Type-ContactInformation-AddressLine1)": "**_string_** ",
          "[AddressLine2](./API_ContactInformation.html#accounts-Type-ContactInformation-AddressLine2)": "**_string_** ",
          "[AddressLine3](./API_ContactInformation.html#accounts-Type-ContactInformation-AddressLine3)": "**_string_** ",
          "[City](./API_ContactInformation.html#accounts-Type-ContactInformation-City)": "**_string_** ",
          "[CompanyName](./API_ContactInformation.html#accounts-Type-ContactInformation-CompanyName)": "**_string_** ",
          "[CountryCode](./API_ContactInformation.html#accounts-Type-ContactInformation-CountryCode)": "**_string_** ",
          "[DistrictOrCounty](./API_ContactInformation.html#accounts-Type-ContactInformation-DistrictOrCounty)": "**_string_** ",
          "[FullName](./API_ContactInformation.html#accounts-Type-ContactInformation-FullName)": "**_string_** ",
          "[PhoneNumber](./API_ContactInformation.html#accounts-Type-ContactInformation-PhoneNumber)": "**_string_** ",
          "[PostalCode](./API_ContactInformation.html#accounts-Type-ContactInformation-PostalCode)": "**_string_** ",
          "[StateOrRegion](./API_ContactInformation.html#accounts-Type-ContactInformation-StateOrRegion)": "**_string_** ",
          "[WebsiteUrl](./API_ContactInformation.html#accounts-Type-ContactInformation-WebsiteUrl)": "**_string_** "
       }
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**ContactInformation **
    

Contains the details of the primary contact information associated with an AWS account.

Type: [ContactInformation](./API_ContactInformation.html) object

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The operation failed because it specified a resource that can't be found.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 404

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/GetContactInformation)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/GetContactInformation)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/GetContactInformation)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/GetContactInformation)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/GetContactInformation)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/GetContactInformation)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/GetContactInformation)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/GetContactInformation)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/GetContactInformation)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/GetContactInformation)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetAlternateContact

GetGovCloudAccountInformation


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_GetGovCloudAccountInformation.html

# GetGovCloudAccountInformation

Retrieves information about the GovCloud account linked to the specified standard account (if it exists) including the GovCloud account ID and state. To use this API, an IAM user or role must have the `account:GetGovCloudAccountInformation` IAM permission. 

## Request Syntax
    
    
    POST /getGovCloudAccountInformation HTTP/1.1
    Content-type: application/json
    
    {
       "StandardAccountId": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**StandardAccountId **
    

Specifies the 12 digit account ID number of the AWS account that you want to access or modify with this operation.

If you do not specify this parameter, it defaults to the AWS account of the identity used to call the operation.

To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html) enabled for the Account Management service, and optionally a [delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

###### Note

The management account can't specify its own `AccountId`; it must call the operation in standalone context by not including the `AccountId` parameter.

To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "AccountState": "**_string_** ",
       "GovCloudAccountId": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**AccountState **
    

The account state of the linked GovCloud account.

Type: String

Valid Values: `PENDING_ACTIVATION | ACTIVE | SUSPENDED | CLOSED`

**GovCloudAccountId **
    

The 12-digit account ID number of the linked GovCloud account.

Type: String

Pattern: `\d{12}`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The operation failed because it specified a resource that can't be found.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 404

**ResourceUnavailableException**
    

The operation failed because it specified a resource that is not currently available.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 424

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## Examples

### Example 1

The following example retrieves the linked GovCloud account information for the account whose credentials are used to call the operation. 

#### Sample Request
    
    
    POST / HTTP/1.1
    X-Amz-Target: AWSAccountV20210201.GetGovCloudAccountInformation
                        
    {}

#### Sample Response
    
    
    HTTP/1.1 200 OK
    Content-Type: application/json
                        
    {
       "GovCloudAccountId": "123456789012",
       "AccountState": "ACTIVE"
    }

### Example 2

The following example retrieves the linked GovCloud account information for the specified member account in an organization. You must use credentials from either the organization's management account or from the Account Management service's delegated admin account. 

#### Sample Request
    
    
    POST / HTTP/1.1
    X-Amz-Target: AWSAccountV20210201.GetGovCloudAccountInformation
                        
    {
       "StandardAccountId": "111111111111" 
    }

#### Sample Response
    
    
    HTTP/1.1 200 OK
    Content-Type: application/json
                        
    {
       "GovCloudAccountId": "123456789012",
       "AccountState": "ACTIVE"
    }

### Example 3

The following example attempts to retrieve the linked GovCloud account information for a standard account that is not linked to a GovCloud account. 

#### Sample Request
    
    
    POST / HTTP/1.1
    X-Amz-Target: AWSAccountV20210201.GetGovCloudAccountInformation
                        
    {
       "StandardAccountId": "222222222222" 
    }

#### Sample Response
    
    
    HTTP/1.1 404
    Content-Type: application/json
                        
    {
       "message":"GovCloud Account ID not found for Standard Account - 222222222222."
    }

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/GetGovCloudAccountInformation)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/GetGovCloudAccountInformation)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/GetGovCloudAccountInformation)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/GetGovCloudAccountInformation)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/GetGovCloudAccountInformation)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/GetGovCloudAccountInformation)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/GetGovCloudAccountInformation)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/GetGovCloudAccountInformation)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/GetGovCloudAccountInformation)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/GetGovCloudAccountInformation)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetContactInformation

GetPrimaryEmail


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_GetPrimaryEmail.html

# GetPrimaryEmail

Retrieves the primary email address for the specified account.

## Request Syntax
    
    
    POST /getPrimaryEmail HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

This operation can only be called from the management account or the delegated administrator account of an organization for a member account.

###### Note

The management account can't specify its own `AccountId`.

Type: String

Pattern: `\d{12}`

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "PrimaryEmail": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**PrimaryEmail **
    

Retrieves the primary email address associated with the specified account.

Type: String

Length Constraints: Minimum length of 5. Maximum length of 64.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The operation failed because it specified a resource that can't be found.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 404

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/GetPrimaryEmail)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/GetPrimaryEmail)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/GetPrimaryEmail)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/GetPrimaryEmail)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/GetPrimaryEmail)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/GetPrimaryEmail)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/GetPrimaryEmail)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/GetPrimaryEmail)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/GetPrimaryEmail)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/GetPrimaryEmail)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetGovCloudAccountInformation

GetRegionOptStatus


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_GetRegionOptStatus.html

# GetRegionOptStatus

Retrieves the opt-in status of a particular Region.

## Request Syntax
    
    
    POST /getRegionOptStatus HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string",
       "RegionName": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

###### Note

The management account can't specify its own `AccountId`. It must call the operation in standalone context by not including the `AccountId` parameter.

To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

**RegionName **
    

Specifies the Region-code for a given Region name (for example, `af-south-1`). This function will return the status of whatever Region you pass into this parameter. 

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "RegionName": "**_string_** ",
       "RegionOptStatus": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**RegionName **
    

The Region code that was passed in.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

**RegionOptStatus **
    

One of the potential statuses a Region can undergo (Enabled, Enabling, Disabled, Disabling, Enabled_By_Default).

Type: String

Valid Values: `ENABLED | ENABLING | DISABLING | DISABLED | ENABLED_BY_DEFAULT`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/GetRegionOptStatus)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/GetRegionOptStatus)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/GetRegionOptStatus)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/GetRegionOptStatus)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/GetRegionOptStatus)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/GetRegionOptStatus)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/GetRegionOptStatus)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/GetRegionOptStatus)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/GetRegionOptStatus)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/GetRegionOptStatus)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetPrimaryEmail

ListRegions


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_ListRegions.html

# ListRegions

Lists all the Regions for a given account and their respective opt-in statuses. Optionally, this list can be filtered by the `region-opt-status-contains` parameter. 

## Request Syntax
    
    
    POST /listRegions HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string",
       "MaxResults": number,
       "NextToken": "string",
       "RegionOptStatusContains": [ "string" ]
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

###### Note

The management account can't specify its own `AccountId`. It must call the operation in standalone context by not including the `AccountId` parameter.

To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

**MaxResults **
    

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. Do not use the `NextToken` response element directly outside of the AWS CLI. For usage examples, see [Pagination](http://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the _AWS Command Line Interface User Guide_. 

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 50.

Required: No

**NextToken **
    

A token used to specify where to start paginating. This is the `NextToken` from a previously truncated response. For usage examples, see [Pagination](http://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the _AWS Command Line Interface User Guide_.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1000.

Required: No

**RegionOptStatusContains **
    

A list of Region statuses (Enabling, Enabled, Disabling, Disabled, Enabled_by_default) to use to filter the list of Regions for a given account. For example, passing in a value of ENABLING will only return a list of Regions with a Region status of ENABLING.

Type: Array of strings

Valid Values: `ENABLED | ENABLING | DISABLING | DISABLED | ENABLED_BY_DEFAULT`

Required: No

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "NextToken": "**_string_** ",
       "Regions": [ 
          { 
             "[RegionName](./API_Region.html#accounts-Type-Region-RegionName)": "**_string_** ",
             "[RegionOptStatus](./API_Region.html#accounts-Type-Region-RegionOptStatus)": "**_string_** "
          }
       ]
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**NextToken **
    

If there is more data to be returned, this will be populated. It should be passed into the `next-token` request parameter of `list-regions`.

Type: String

**Regions **
    

This is a list of Regions for a given account, or if the filtered parameter was used, a list of Regions that match the filter criteria set in the `filter` parameter.

Type: Array of [Region](./API_Region.html) objects

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/ListRegions)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/ListRegions)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/ListRegions)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/ListRegions)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/ListRegions)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/ListRegions)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/ListRegions)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/ListRegions)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/ListRegions)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/ListRegions)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

GetRegionOptStatus

PutAccountName


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_PutAccountName.html

# PutAccountName

Updates the account name of the specified account. To use this API, IAM principals must have the `account:PutAccountName` IAM permission. 

## Request Syntax
    
    
    POST /putAccountName HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string",
       "AccountName": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12 digit account ID number of the AWS account that you want to access or modify with this operation.

If you do not specify this parameter, it defaults to the AWS account of the identity used to call the operation.

To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html) enabled for the Account Management service, and optionally a [delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

###### Note

The management account can't specify its own `AccountId`; it must call the operation in standalone context by not including the `AccountId` parameter.

To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

**AccountName **
    

The name of the account.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[ -;=?-~]+`

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## Examples

### Example 1

The following example updates the name for the account whose credentials are used to call the operation. 

#### Sample Request
    
    
    POST / HTTP/1.1
    X-Amz-Target: AWSAccountV20210201.PutAccountName
                        
    {
       "AccountName":"MyAccount"
    }

#### Sample Response
    
    
    HTTP/1.1 200 OK
    Content-Type: application/json

### Example 2

The following example updates the account name for the specified member account in an organization. You must use credentials from either the organization's management account or from the Account Management service's delegated admin account. 

#### Sample Request
    
    
    POST / HTTP/1.1
    X-Amz-Target: AWSAccountV20210201.PutAccountName
                        
    {
       "AccountId": "123456789012",
       "AccountName": "MyMemberAccount"
    }

#### Sample Response
    
    
    HTTP/1.1 200 OK
    Content-Type: application/json

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/PutAccountName)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/PutAccountName)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/PutAccountName)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/PutAccountName)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/PutAccountName)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/PutAccountName)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/PutAccountName)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/PutAccountName)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/PutAccountName)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/PutAccountName)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ListRegions

PutAlternateContact


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_PutAlternateContact.html

# PutAlternateContact

Modifies the specified alternate contact attached to an AWS account.

For complete details about how to use the alternate contact operations, see [Update the alternate contacts for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html).

###### Note

Before you can update the alternate contact information for an AWS account that is managed by AWS Organizations, you must first enable integration between AWS Account Management and Organizations. For more information, see [Enable trusted access for AWS Account Management](https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html).

## Request Syntax
    
    
    POST /putAlternateContact HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string",
       "AlternateContactType": "string",
       "EmailAddress": "string",
       "Name": "string",
       "PhoneNumber": "string",
       "Title": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12 digit account ID number of the AWS account that you want to access or modify with this operation.

If you do not specify this parameter, it defaults to the AWS account of the identity used to call the operation.

To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html) enabled for the Account Management service, and optionally a [delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

###### Note

The management account can't specify its own `AccountId`; it must call the operation in standalone context by not including the `AccountId` parameter.

To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

**AlternateContactType **
    

Specifies which alternate contact you want to create or update.

Type: String

Valid Values: `BILLING | OPERATIONS | SECURITY`

Required: Yes

**EmailAddress **
    

Specifies an email address for the alternate contact. 

Type: String

Length Constraints: Minimum length of 1. Maximum length of 254.

Pattern: `[\s]*[\w+=.#|!&-]+@[\w.-]+\.[\w]+[\s]*`

Required: Yes

**Name **
    

Specifies a name for the alternate contact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Required: Yes

**PhoneNumber **
    

Specifies a phone number for the alternate contact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 25.

Pattern: `[\s0-9()+-]+`

Required: Yes

**Title **
    

Specifies a title for the alternate contact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## Examples

### Example 1

The following example sets the billing alternate contact for the account whose credentials are used to call the operation.

#### Sample Request
    
    
    POST / HTTP/1.1
    X-Amz-Target: AWSAccountV20210201.PutAlternateContact
    
    {
        "AlternateContactType": "Billing",
        "Name": "Carlos Salazar",
        "Title": "CFO",
        "EmailAddress": "carlos@example.com",
        "PhoneNumber": "206-555-0199"
    }

#### Sample Response
    
    
    HTTP/1.1 200 OK
    Content-Type: application/json

### Example 2

The following example sets or overwrites the billing alternate contact for the specified member account in an organization. You must use credentials from either the organization's management account or from the Account Management service's delegated admin account.

#### Sample Request
    
    
    POST / HTTP/1.1
    X-Amz-Target: AWSAccountV20210201.PutAlternateContact
    
    {
        "AccountId": "123456789012",
        "AlternateContactType": "Billing",
        "Name": "Carlos Salazar",
        "Title": "CFO",
        "EmailAddress": "carlos@example.com",
        "PhoneNumber": "206-555-0199"
    }

#### Sample Response
    
    
    HTTP/1.1 200 OK
    Content-Type: application/json

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/PutAlternateContact)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/PutAlternateContact)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/PutAlternateContact)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/PutAlternateContact)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/PutAlternateContact)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/PutAlternateContact)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/PutAlternateContact)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/PutAlternateContact)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/PutAlternateContact)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/PutAlternateContact)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

PutAccountName

PutContactInformation


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_PutContactInformation.html

# PutContactInformation

Updates the primary contact information of an AWS account.

For complete details about how to use the primary contact operations, see [Update the primary contact for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html).

## Request Syntax
    
    
    POST /putContactInformation HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string",
       "ContactInformation": { 
          "[AddressLine1](./API_ContactInformation.html#accounts-Type-ContactInformation-AddressLine1)": "string",
          "[AddressLine2](./API_ContactInformation.html#accounts-Type-ContactInformation-AddressLine2)": "string",
          "[AddressLine3](./API_ContactInformation.html#accounts-Type-ContactInformation-AddressLine3)": "string",
          "[City](./API_ContactInformation.html#accounts-Type-ContactInformation-City)": "string",
          "[CompanyName](./API_ContactInformation.html#accounts-Type-ContactInformation-CompanyName)": "string",
          "[CountryCode](./API_ContactInformation.html#accounts-Type-ContactInformation-CountryCode)": "string",
          "[DistrictOrCounty](./API_ContactInformation.html#accounts-Type-ContactInformation-DistrictOrCounty)": "string",
          "[FullName](./API_ContactInformation.html#accounts-Type-ContactInformation-FullName)": "string",
          "[PhoneNumber](./API_ContactInformation.html#accounts-Type-ContactInformation-PhoneNumber)": "string",
          "[PostalCode](./API_ContactInformation.html#accounts-Type-ContactInformation-PostalCode)": "string",
          "[StateOrRegion](./API_ContactInformation.html#accounts-Type-ContactInformation-StateOrRegion)": "string",
          "[WebsiteUrl](./API_ContactInformation.html#accounts-Type-ContactInformation-WebsiteUrl)": "string"
       }
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html) enabled for the Account Management service, and optionally a [delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

###### Note

The management account can't specify its own `AccountId`. It must call the operation in standalone context by not including the `AccountId` parameter.

To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

**ContactInformation **
    

Contains the details of the primary contact information associated with an AWS account.

Type: [ContactInformation](./API_ContactInformation.html) object

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/PutContactInformation)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/PutContactInformation)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/PutContactInformation)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/PutContactInformation)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/PutContactInformation)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/PutContactInformation)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/PutContactInformation)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/PutContactInformation)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/PutContactInformation)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/PutContactInformation)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

PutAlternateContact

StartPrimaryEmailUpdate


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_StartPrimaryEmailUpdate.html

# StartPrimaryEmailUpdate

Starts the process to update the primary email address for the specified account.

## Request Syntax
    
    
    POST /startPrimaryEmailUpdate HTTP/1.1
    Content-type: application/json
    
    {
       "AccountId": "string",
       "PrimaryEmail": "string"
    }

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**AccountId **
    

Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

This operation can only be called from the management account or the delegated administrator account of an organization for a member account.

###### Note

The management account can't specify its own `AccountId`.

Type: String

Pattern: `\d{12}`

Required: Yes

**PrimaryEmail **
    

The new primary email address (also known as the root user email address) to use in the specified account.

Type: String

Length Constraints: Minimum length of 5. Maximum length of 64.

Required: Yes

## Response Syntax
    
    
    HTTP/1.1 200
    Content-type: application/json
    
    {
       "Status": "**_string_** "
    }

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**Status **
    

The status of the primary email update request.

Type: String

Valid Values: `PENDING | ACCEPTED`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
    

The operation failed because the calling identity doesn't have the minimum required permissions.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**ConflictException**
    

The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an accountâs root user email to an email address which is already in use.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 409

**InternalServerException**
    

The operation failed because of an error internal to AWS. Try your operation again later.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**ResourceNotFoundException**
    

The operation failed because it specified a resource that can't be found.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 404

**TooManyRequestsException**
    

The operation failed because it was called too frequently and exceeded a throttle limit.

**errorType**
    

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**
    

The operation failed because one of the input parameters was invalid.

**fieldList**
    

The field where the invalid entry was detected.

**message**
    

The message that informs you about what was invalid about the request.

**reason**
    

The reason that validation failed.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/StartPrimaryEmailUpdate)

  * [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/StartPrimaryEmailUpdate)

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/StartPrimaryEmailUpdate)

  * [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/StartPrimaryEmailUpdate)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/StartPrimaryEmailUpdate)

  * [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/StartPrimaryEmailUpdate)

  * [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/StartPrimaryEmailUpdate)

  * [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/StartPrimaryEmailUpdate)

  * [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/StartPrimaryEmailUpdate)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/StartPrimaryEmailUpdate)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

PutContactInformation

Data Types


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_Types.html

# Data Types

The AWS Account Management API contains several data types that various actions use. This section describes each data type in detail.

###### Note

The order of each element in a data type structure is not guaranteed. Applications should not assume a particular order.

The following data types are supported:

  * [AlternateContact](./API_AlternateContact.html)

  * [ContactInformation](./API_ContactInformation.html)

  * [Region](./API_Region.html)

  * [ValidationExceptionField](./API_ValidationExceptionField.html)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

StartPrimaryEmailUpdate

AlternateContact


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_AlternateContact.html

# AlternateContact

A structure that contains the details of an alternate contact associated with an AWS account

## Contents

**AlternateContactType**
    

The type of alternate contact.

Type: String

Valid Values: `BILLING | OPERATIONS | SECURITY`

Required: No

**EmailAddress**
    

The email address associated with this alternate contact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 254.

Pattern: `[\s]*[\w+=.#|!&-]+@[\w.-]+\.[\w]+[\s]*`

Required: No

**Name**
    

The name associated with this alternate contact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Required: No

**PhoneNumber**
    

The phone number associated with this alternate contact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 25.

Pattern: `[\s0-9()+-]+`

Required: No

**Title**
    

The title associated with this alternate contact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/AlternateContact)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/AlternateContact)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/AlternateContact)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Data Types

ContactInformation


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_ContactInformation.html

# ContactInformation

Contains the details of the primary contact information associated with an AWS account.

## Contents

**AddressLine1**
    

The first line of the primary contact address.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 60.

Required: Yes

**City**
    

The city of the primary contact address.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: Yes

**CountryCode**
    

The ISO-3166 two-letter country code for the primary contact address.

Type: String

Length Constraints: Fixed length of 2.

Required: Yes

**FullName**
    

The full name of the primary contact address.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: Yes

**PhoneNumber**
    

The phone number of the primary contact information. The number will be validated and, in some countries, checked for activation.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 20.

Pattern: `[+][\s0-9()-]+`

Required: Yes

**PostalCode**
    

The postal code of the primary contact address.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 20.

Required: Yes

**AddressLine2**
    

The second line of the primary contact address, if any.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 60.

Required: No

**AddressLine3**
    

The third line of the primary contact address, if any.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 60.

Required: No

**CompanyName**
    

The name of the company associated with the primary contact information, if any.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: No

**DistrictOrCounty**
    

The district or county of the primary contact address, if any.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: No

**StateOrRegion**
    

The state or region of the primary contact address. If the mailing address is within the United States (US), the value in this field can be either a two character state code (for example, `NJ`) or the full state name (for example, `New Jersey`). This field is required in the following countries: `US`, `CA`, `GB`, `DE`, `JP`, `IN`, and `BR`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: No

**WebsiteUrl**
    

The URL of the website associated with the primary contact information, if any.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/ContactInformation)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/ContactInformation)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/ContactInformation)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AlternateContact

Region


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_Region.html

# Region

This is a structure that expresses the Region for a given account, consisting of a name and opt-in status.

## Contents

**RegionName**
    

The Region code of a given Region (for example, `us-east-1`).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Required: No

**RegionOptStatus**
    

One of potential statuses a Region can undergo (Enabled, Enabling, Disabled, Disabling, Enabled_By_Default).

Type: String

Valid Values: `ENABLED | ENABLING | DISABLING | DISABLED | ENABLED_BY_DEFAULT`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/Region)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/Region)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/Region)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

ContactInformation

ValidationExceptionField


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/API_ValidationExceptionField.html

# ValidationExceptionField

The input failed to meet the constraints specified by the AWS service in a specified field.

## Contents

**message**
    

A message about the validation exception.

Type: String

Required: Yes

**name**
    

The field name where the invalid entry was detected.

Type: String

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

  * [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/ValidationExceptionField)

  * [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/ValidationExceptionField)

  * [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/ValidationExceptionField)




**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Region

Common Parameters


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/CommonParameters.html

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

ValidationExceptionField

Common Error Types


---
# Page: https://docs.aws.amazon.com/accounts/latest/APIReference/CommonErrors.html

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
