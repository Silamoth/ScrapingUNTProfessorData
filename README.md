# ScrapingUNTProfessorData

This is a project I made early on during the Spring 2020 semester.  It had to have been around January or February of 2020.  At this time, I was getting into some data science stuff.  I really should have uploaded and written about this project earlier, but better late than never.  I thought it would be cool to scrape and analyze some data about UNT professors from RateMyProfessors.com.  So, I went ahead and did that.

<h2>Getting the Data</h2>

Since RateMyProfessors doesn't provide any API endpoint (that I know of), I knew I had to scrape data from their website.  No big deal; it's just parsing some HTML.  After doing a little bit of research, I decided to use Selenium WebDriver to help with the web scraping.  Selenium WebDriver is library that lets you hook into a browser via code.  It's actually designed for testing web apps, but it also works for web scraping.

Getting started was fairly simple.  I pointed WebDriver at the right URL (the search for UNT professors was embedded into the URL), and it opened a browser window with that webpage.  I was able to then start grabbing and messing with different HTML elements on the webpage (sort of).  However, there were some issues.

<h3>The First Roadblock: Pop-Ups</h3>

As soon as the desired webpage opened, a pop-up about cookies showed up, taking focus.  This is a problem (you'll see why in a minute).  I needed to get this to go away.  So, I grabbed the pop-up in code, founded the button with code, and clicked it with code.  This was the first thing I'd ever done with WebDriver, so it took me a little bit.  However, it wasn't all that difficult.

<h3>The Second Roadblock: Loading Professors</h3>

I also ran into a second issue: by default, RateMyProfessors only loads in 20 professors.  You need to click "Load More" to see more professors.  So, I had to tell WebDriver to keep clicking on "Load More" until all the professors were loaded in.  This is why I needed the cookies pop-up to go away; with that pop-up present, nothing else could be clicked.

<h3>What I Scraped</h3>

I ended up scraping data on each professor's name, average rating, and number of ratings since this data could easily be scraped from the search results.  At one point, I had thought about going into each professor's individual page to scrape even more data, but I ended up getting busy with the semester before I could get to that.

<h2>Analyzing the Data</h2>

Once I had all the data I wanted, I then needed to analyze it.  Specifically, I wanted to analyze average ratings for professors across the university.  I didn't end up doing anything with the rating counts, although I could have done a weighted average if I had thought of it at the time.  Instead, I focused on the distribution of average ratings.

To summarize the ratings, I calculated the mean and median average ratings.  I found the mean average rating to be 3.699 and the median average rating to be 4.0.  I then decided to visualize this distribution of average ratings in a histogram since the ratings are quantitative (although RateMyProfessors only allows discrete rating values, the averages do not necessarily fit into these discrete categories).  I probably should have calculated the standard deviation and IQR as well, but at least the distribution is fairly clear from the histogram.

![UNT Professor Ratings]
(https://raw.githubusercontent.com/Silamoth/ScrapingUNTProfessorData/master/UNT%20Professor%20Ratings.jpeg)

<h3>The Challenge: Unrated Professors</h3>

One challenge I ran into during analysis was dealing with professors that were unrated.  For whatever reason, RateMyProfessors does list some professors without ratings, so I needed to clean the data and deal with this problem.  I decided to simply ignore these professors and drop them from the analysis.  I believe this was the right decision because professors who aren't rated probably haven't taught much, if at all, so it's not important to consider them in the analysis.

<h2>What I Learned</h2>

On a directly practical level, working on this project helped me a learn a bit about web scraping, which is something I had never done before.  It also gave me the opportunity to sharpen my analytics and visualization skills.  However, I think the most valuable part of working on this project was getting to see how a (simple) data science project works from start to finish.  I had to gather my data, organize it, clean it, analyze it, and visualize it.  Along the way, I had to make decisions about the data, like how to handle professors without ratings.  Although this project was rather simplistic, it taught me how to deal with real data.
