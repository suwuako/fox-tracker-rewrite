# fox-tracker-rewrite
<img src="https://media.discordapp.net/attachments/777935642004553792/942833728672129094/senko_dub.png?width=1202&height=676">

## Description
Code to track activity statuses across a multitude of platforms to organise and chart data with a multitude of functions

Now includes/is planning to add functions to track user activity in general and aims to track sleep schedules, spotify activity and more.

## Dependencies

-   `discord.py`  -- library to interact with the discord API
-   `json`        -- to read json files (config & secret)
-   `asyncio`     -- to run code asynchronously 
-   `datetime`    -- time related items

## Functions

### Auto
- log all user statuses on initialization 
- log changes in user activity

### Commands
- !status to check all current activities
- !ping to check latency

## TODOs
1. add discord status tracking functions (online, dnd, idle, offline)
2. base sleep tracker on discord status tracking
3. upload logged statistics to a server, whether that is to a google spreadsheet or to a personal server via ssh & scp
4. graph data just for the sake of it
5. do some cool stuff with it maybe 

## License
Creative Commons

## Contributors
suwa
