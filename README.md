# AWS EC2 Controller Discord Bot
This is still a large WIP, currently being used to turn a Feed the Beast server on and off from Discord. End goal is to have a larger amount of commands, easier integration with your own AWS account and not having just one hard coded instance.

## Tools Used
* Python 3 and pip3
* AWS CLI : ```pip3 install awscli ```
* AWS BOTO library : ``` pip3 install boto3 ```
* Discord Bot library : ``` pip3 install discord ```

## Usage | Installation
1. Install and setup the required tools above
2. Setup AWS CLI with ``` aws configure ```
3. Go to Discord's developer site and setup a bot (here)[https://discordapp.com/developers]
4. Clone this repo into a desired folder
5. Set the discord token environment variable with the name 'AWSDISCORDTOKEN'
6. python3 bot.py :)

For easy and reliable usage I reccomend using upstart to restart on error and start on system startup
