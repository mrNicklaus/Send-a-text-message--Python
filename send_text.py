from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "" # Enter your ac sid provided
# Your Auth Token from twilio.com/console
auth_token  = "" # Enter your hidden account auth token

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="", # Enter your verified phone number
    from_="", # Enter the generated twilio  phone number in your new account
    body="Hello from Nicks Python?")

print(message.sid)