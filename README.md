# snapshot_test
A project that manages AWS EC2 instances


## About
This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring
shotty uses the configuration file created by the AWS cli. e.g.

`aws configure --profile shotty`

## Running

`pipenv run python shotty/shotty.py <command> <subcommand> <--project PROJECT>`

*command* is instances, volumes, or snapshots
*subcommand* is depends on command
*project* is the project tag and it's optional
