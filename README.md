# WU24 2023 Power Duos!
Welcome to the summer 2023 update to this project, looking at data from the World Under 24 Championships. This project still uses Python with `bs4`, `requests`, and `pandas`, but also makes use of Python's `multiprocessing` library to speed up the process of scraping the data from hundreds of games. I also refactored the code a bit to make the project more reusable for future WFDF tournaments.

The data from this iteration of the project is housed in [this spreadsheet](https://docs.google.com/spreadsheets/d/1pimbqxY_FZxargUp5606RaP8UmOqyoQSswoxYjXYtrw/edit?usp=sharing). Worked on some sheets magic to get the team names to conditionally highlight with team division (Open, Women's, and Mixed) and have nice filtering for the scoring metrics (% vs. # of scores).

<img width="806" alt="Screen Shot 2023-07-31 at 12 22 36 PM" src="https://github.com/liliwilson/wucc2022-webscrape/assets/56806227/02a6be92-8bbb-480c-a7b2-747826dd2378">
