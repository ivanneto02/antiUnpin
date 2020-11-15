This Slack application serves the purpose of preventing students from unpinning messages that we want preserved.

Author: Ivan Neto

Directions:
    Essentially, this process takes < num stems > steps.

1) Make an app and install it
    - Go to https://api.slack.com/ , sign in and select "Your Apps."
    - Select "Create an App"
    
    - Assign permissions
        - Head over to "OAuth & Permissions"
        - Scroll down to "Scopes" and add the following scopes to the Bot Token Scopes
            pins:read
            pins:write
            users:read
        - Add the following User Token Scopes
            admin

    - Install application to your workspace.

2) Get token and signing secret
    - Go to "OAuth & Permissions" and copy the "Bot User OAuth Access Token." This will be used by Slack to verify your bot from their end.
        - Replace the token inside "temp-commands" with the token you just copied.

    - Go to "Basic Information" and copy the "Signing Secret".
        - Replace the token inside "temp-commands" with the secret you just copied.

You're almost good to go.

3) Set up Events
    - Run main.py using "python3 main.py" on your terminal. (You must have python 3 installed on your system.)
    - Run the ngrok server using "./ngrok http 3000" on your terminal.
        - Copy the link with the following format: https://e710fb0a8a89.ngrok.io

    - Go to "Event Subscriptions"
        - Enable events and paste the link + /slack/events: https://e710fb0a8a89.ngrok.io/slack/events
            - * Make sure that both main.py and the ngrok server are running at the same time. *
        - Subscribe to the following bot events
            pin_added
            pin_removed
    
At this point, the bot should be able to pin/unpin messages from non-admin users who try to pin/unpin messages. These events will be recorded under "logs".
