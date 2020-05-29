# Gimme AWS Creds


gimme-aws-creds is a CLI that utilizes an [Okta](https://www.okta.com/) IdP via SAML to acquire temporary AWS credentials via AWS STS.

Okta is a SAML identity provider (IdP), that can be easily set-up to do SSO to your AWS console. Okta does offer an [OSS java CLI]((https://github.com/oktadeveloper/okta-aws-cli-assume-role)) tool to obtain temporary AWS credentials, but I found it needs more information than the average Okta user would have and doesn't scale well if have more than one Okta App.

With gimme-aws-creds all you need to know is your username, password, Okta url and MFA token, if MFA is enabled. gimme-aws-creds gives you the option to select which Okta AWS application and role you want credentials for. Alternatively, you can pre-configure the app and role name by passing -c or editing the config file. This is all covered in the usage section.

## Prerequisites

[Okta SAML integration to AWS using the AWS App](https://help.okta.com/en/prod/Content/Topics/Miscellaneous/References/OktaAWSMulti-AccountConfigurationGuide.pdf)

## Installation

Build the docker image locally:

```bash
docker build -t gimme-aws-creds .
```

To make it easier you can also create an alias for the gimme-aws-creds command with docker:

```bash
# make sure you have the "~/.okta_aws_login_config" locally first!
# Get ~/.okta_aws_login_config file from https://hub.ghx.com/display/CSGHX/%5BHOWTO%5D+Use+the+AWS+CLI+with+Okta 
# update it for your AWS account and store in local ~/.okta_aws_login_config

touch ~/.okta_aws_login_config && \
alias gimme-aws-creds="docker run -it --rm \
  -v ~/.aws/credentials:/root/.aws/credentials \
  -v ~/.okta_aws_login_config:/root/.okta_aws_login_config \
  gimme-aws-creds"
```

With this config, you will be able to run further commands seamlessly!

## Configuration

## Configuration File

The config file follows a [configfile](https://docs.python.org/3/library/configparser.html) format.
By default, it is located in $HOME/.okta_aws_login_config


### Generate credentials

`gimme-aws-creds` will print out credentials in export

### Generate credentials as json

`gimme-aws-creds -o json` will print out credentials in JSON format - 1 entry per line

### Store credentials from json

`gimme-aws-creds --action-store-json-creds` will store JSON formatted credentials from `stdin` to
aws credentials file, eg: `gimme-aws-creds -o json | gimme-aws-creds --action-store-json-creds`.
Data can be modified by scripts on the way.

### Viewing Profiles

`gimme-aws-creds --action-list-profiles` will go to your okta config file and print out all profiles created and their settings.

### Viewing roles

`gimme-aws-creds --action-list-roles` will print all available roles to STDOUT without retrieving their credentials.




