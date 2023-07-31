# Project Overview
Hi! I made this project after noticing that the World Flying Disc Federation (WFDF) reports scores from its international tournaments in a very webscrapable manner. I was curious abou using these scores to calculate new stats that I was interested in, and thus WUCC 2022 Power Duos was born!

I adapted the code again in June 2023 to work with the World Under-24 championship data, and while doing so, also improved the code's efficiency using Python's inbuilt parallelization tools :). You can check out this code on the [WU24 branch][https://github.com/liliwilson/wucc2022-webscrape/tree/wu24].

# WUCC 2022 Power Duos!
Webscraping mini-project using data from the [2022 World Ultimate Club Championships]([https://wucc.sport](https://wfdf.sport/event/wfdf-2022-world-ultimate-club-championships/)). Using Python with `bs4`, `requests`, and `pandas`. 

I was curious about whether or not there were pairs of players absolutely dominating at Worlds, and wanted to find some way I could use the really awesome data that WFDF was putting out for each game (see an example of data [here](https://results.wfdf.sport/wucc/?view=gameplay&game=1)) I ended up with this project that tracks the scoring of pairs of players (where one person throws the assist to the other for the goal, or vice versa), ranking them by absolute number of scores or by the pairs' contribution to their team's overall goal count. 

The data from the project is housed in [this spreadsheet](https://docs.google.com/spreadsheets/d/1cKhtEw4KwD05jiI-_Dl2B8FLxahZKvGYRzJJf1rpPkI/edit?usp=sharing), and may be adapted to a website format later on. Worked on some sheets magic to get the team names to conditionally highlight with team division (Open, Women's, and Mixed) and have nice filtering for the scoring metrics (% vs. # of scores).

<img width="1256" alt="Screen Shot 2022-07-30 at 10 39 24 PM" src="https://user-images.githubusercontent.com/56806227/182007370-bda08e38-53ca-41fd-9d4b-4a9cfef3272f.png">
