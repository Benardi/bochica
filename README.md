<a href="https://github.com/Benardi/bochica">
    <img src="https://raw.githubusercontent.com/Benardi/bochica/master/bochica_wide.png"
         alt="bochica logo"
         align="center">
</a>


# Bochica 

Bochica refers primarily to the construction of an inverted index. By doing so we aim to explore concepts behind Information Retrieval and the use of a Crawler.

One of its objectives is to gather at least 100 Brazilian news starting from 01/01/2018 and export them as a CSV file following the layout below.

| Field     | Type     | Description                    |
| --------- | -------- | ------------------------------ |
| title     | String   |                                |
| sub_title | String   |                                |
| author    | String   |                                |
| date      | Datetime | dd/mm/yyyy hh:mi:ss            |
| section   | String   | Esportes, Saúde, Política, etc |
| text      | String   |                                |
| url       | String   |                                |


# Project layout

If not familiar with Scrapy one should read its [basic documentation](http://docs.scrapy.org/en/latest/intro/tutorial.html).

The project is laid out in four main directories

- frontier
- bochica
- seeds
- output

The directory `seeds` has in a JSON file the seeds of the *crawling* algorithm, in other words, the starting links to be used by the crawler. The code opearates through copies of theses files in the directory `frontier`. The directory `bochica` has the project itself.

# Commands to execute project

> ```shell
> make run # executes crawler for site brasil_elpais
> make export # exports json results json of crawler to csv format.
> ```
