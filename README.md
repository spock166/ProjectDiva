# ProjectDiva
## Introduction
Vivy is a discord bot that utilizes OpenAI's API.  To keep in the spirit of things the first draft of her code was written by ChatGPT.  From there she was refined and improved by human hands.  

## Setup
A JSON file is used to store sensitive information such as API tokens and can be created simply using `json.dumps` to obtain a json file of the form:

```
{
  "discord_token" : "my_discord_token",
  "openai_token" : "my_openai_token"
}
```

From there Vivy should be set to run on your Discord server.  By default she uses the `gpt-3.5-turbo` to chat, although OpenAI has more sophisticated models available.


