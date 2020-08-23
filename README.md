# ScrapingUNTProfessorData
Scraping and analyzing some basic data about UNT professors from RateMyProfessors.com

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

Once I had all the data I wanted, I then needed to analyze it.  

<h3>The Challenge: Unrated Professors</h3>

<h2>The Result</h2>
