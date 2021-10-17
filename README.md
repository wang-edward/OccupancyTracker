# Hack the Valley 2021 Project

## Inspiration
There are many facilities with a limit of how many people can enter. Possibly because of COVID-19 (health-restrictions) or there is simply not enough space. At our high-school's library there is a 140 person limit and it inspired us to make an occupancy tracker to try and help the librarians keep track of the number of students entering and leaving, so they don't have to manually do it. This software could also be used to gather information about customers at retail stores and gain business insight such as the busiest hours.

## How we built it 
- OpenCV for reading from the input stream and drawing to the screen
- MediaPipe for pose detection and tracking
- FireBase to store our data 
- Matplotlib to create graphs

<a><img src="https://github.com/Shayan925/OccupancyTracker/blob/main/test.png" title="Tracker" /></a>

<a><img src="https://github.com/Shayan925/OccupancyTracker/blob/main/image_2021-10-16_235658.png" title="Tracker" /></a>

## Challenges we faced
Even though we used MediaPipe for the object detection and pose estimation, determining the direction at which the person was travelling proved to be quite difficult. That was the most challenging part of the program and the only other issue was a big lag spike in the video, every time we sent data to the FireBase database. We quickly resolved that issue by creating multiple threads to increase performance.

## What we learned
- There is a lot of advanced mathematics that goes into determining the direction of a moving object in computer vision.
- First time using the FireBase database in one of our projects.
- Always something to learn.
## Future additions
- We might create an embed that users could put on their website that displays
    - Current occupancy (as a % of maximum)
    - Graph of a regular business day (busiest hours)