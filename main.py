import os
import logmaker

from slack_bolt import App

SLACK_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SECRET = os.environ["SLACK_SIGNING_SECRET"]

app = App(
	token=SLACK_TOKEN,
	signing_secret=SLACK_SECRET
)

@app.event("pin_removed")
def handle_unpin(client, event, logger):
	user = event["user"]
	user_data = client.users_list()

	for member in user_data["members"]:
		if user == member["id"]:
			if not member["is_admin"]:
				message = event["item"]["message"]["text"]
				name = member["name"]
				channel = event["channel_id"]
				timestamp = event["item"]["message"]["ts"]
				logmaker.createLog(user, name, message)
				result = client.pins_add(
					channel=channel, timestamp=timestamp
				)
				logger.info(result)
				return 1

	return 0

@app.event("pin_added")
def handle_pin(client, event, logger):
	user = event["user"]
	user_data = client.users_list()
	
	for member in user_data["members"]:
		if user == member["id"]:
			if not member["is_admin"] and not member["is_bot"]:
				message = event["item"]["message"]["text"]
				name = member["name"]
				channel = event["channel_id"]
				timestamp = event["item"]["message"]["ts"]
				logmaker.createLog(user, name, message)
				result = client.pins_remove(
					channel=channel, timestamp=timestamp
				)
				logger.info(result)
				return 1

	return 0

if __name__ == "__main__":
	app.start(port=int(os.environ.get("PORT", 3000)))
