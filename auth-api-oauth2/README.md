# Auth Api

**_WIP_**: This partial implementation of OAuth 2.0 is the first step towards authorization for jman.me,
though the end goal is implementing OpenID Connect as the full authentication and authorization suite.
This API depends on the user management api to supply the groundwork for auth. Built using the
[Serverless Framework](https://serverless.com/) and hosted on [Amazon Web Services](https://aws.amazon.com/)
using AWS Lambda, DynamoDB, and API Gateway.

## Getting Started

These instructions will get you a copy of the project up and running through your AWS account.

### Prerequisites

This setup is to ensure the serverless framework has everything it needs to function.

1. Node.js v6.5.0 or later.
2. An AWS account. If you don't already have one, you can sign up for a [free trial](https://aws.amazon.com/s/dm/optimization/server-side-test/free-tier/free_np/)
   that includes 1 million free Lambda requests per month.
3. Set-up your Provider Credentials -> Watch the [video](https://www.youtube.com/watch?v=KngM5bfpttA)
   on setting up credentials

### Installing

This project depends on the [User Management](https://github.com/jbmmhk/auth-api) API which creates
the required groundwork such as the DynamoDB instance used for authentication. To
build the required infrastructure, follow instructions in the [User Management](https://github.com/jbmmhk/auth-api)
repository.

Installing dependencies is as simple as running `npm install`, followed by using serverless to deploy the
project to the AWS account configured on your local machine.

```
git clone https://github.com/jbmmhk/auth-api-oauth2
npm install
./node_modules/.bin/serverless deploy
```

Optionally, you may install serverless globally using `npm install -g serverless` which should add serverless
to your PATH.

```
npm install -g serverless
serverless deploy
```

Once the script has finished, you will have a functional API running through your AWS account. Towards the
end of the script's execution you should see the URLs for the endpoints attached to API Gateway through your account.

```
endpoints:
  POST - https://<my-url>.execute-api.<my-region>.amazonaws.com/dev/authorization
```

To test the functionality, you may submit a HTTP POST request to the url you recieved with `email` and `password` parameters
or invoke the function using the serverless CLI and pre-built parameters from `create.json`.

```
serverless invoke -f create -p create.json
```

If submitted with valid parameters, you should recieve a 200 response with an empty errors array.

```json
{
  "errors": []
}
```
