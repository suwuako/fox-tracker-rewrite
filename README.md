# fox-tracker-rewrite
<img src="https://cdn.discordapp.com/attachments/879261281473937451/944534159215448084/Untitled.png">

## Description
Code to track activity statuses across a multitude of platforms to organise and chart data with a multitude of functions
Now includes/is planning to add functions to track user activity in general and aims to track sleep schedules, spotify activity and more.

Ultimately, this project is for fun to track my friends and myself. However, it also as a demonstration to show what data can be used to tell about you while being limited to an extremely tiny scope.

This will only reflect a small portion of what companies that run services is able to record, tell and examine about you. 

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

## Directory Structure
- `fox_lib`       -- main library containing command cogs, events and fox_lib

  - `cogs`        -- contains all commands within the bot
  - `events`      -- contains all events within the bot
  - `libraries`   -- function libraries that are used to maintain clean code

- `json`          -- folder to contain all json files that is used
  - `secret.json` -- contains all secret values (e.g. bot-token, log-channels)
  - `config.json` -- contains all configurations for the bot

## TODOs
1. add discord status tracking functions (online, dnd, idle, offline)
2. base sleep tracker on discord status tracking
3. upload logged statistics to a server, whether that is to a google spreadsheet or to a personal server via ssh & scp
4. graph data just for the sake of it
5. do some cool stuff with it maybe 

## License
GNU GPL-3.0

## Contributors
suwa
