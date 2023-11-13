# AWM_CA1
Continuous assignment 1 for AWM 
### Basic functionality
- User Can input many Event Plan on the side panel
- Each event plan has a set of itinerary events that happen across the map
- A user clicks on the map to fill out a form on what they plan to do on that location.
- website displays a list of itinerary events ordered by date-time on cards on the main panel
- map displays when the event occurs and pop up titles as blue pins
- Displays recently pointed locations as red pins
- if geolocation is enabled map displays the users current location and coordinates of the user
- A user can delete An entire plan or individual itinerary events
- Has a login page for different users
- Itinerary and Plan tables can scroll for overflow
- It creates, store and manipulate spatial data in PostgreSQL/PostGIS database.
- It utilizes Boostrap for ease of development and user friendly design. This makes the application responsive to make usuable it on different screen sizes.
- App was deployed on an ubuntu VM on Azure using docker, nginx and has HTTPS with the help of certbot for security.
- Uses ajax for asynchronized calls


## Screen Shots of app
<img width="1434" alt="Screenshot 2023-11-13 at 14 34 33" src="https://github.com/RonnyRice/AWM_CA1/assets/82329993/956bed4d-fdb6-48a1-88ee-e26070b008c9">

- initial look of the app
- displays location

<img width="1433" alt="Screenshot 2023-11-13 at 14 41 17" src="https://github.com/RonnyRice/AWM_CA1/assets/82329993/7a230e10-04a8-400c-afac-b528f9771829">

- Displays pins itinerary event locations
- Diplays the Itinerary cards  

<img width="1438" alt="Screenshot 2023-11-13 at 14 37 11" src="https://github.com/RonnyRice/AWM_CA1/assets/82329993/218870dc-99ee-4df2-885e-d16b7cec8cfc">

- User fills in form for new itinerary

<img width="1435" alt="Screenshot 2023-11-13 at 14 44 47" src="https://github.com/RonnyRice/AWM_CA1/assets/82329993/85e6c1de-3ea7-4feb-99f0-17b8996f24e3">

- Carousel of Itenerary cards for overflow

<img width="1432" alt="Screenshot 2023-11-13 at 14 43 32" src="https://github.com/RonnyRice/AWM_CA1/assets/82329993/91021917-ce78-4198-9633-1621e020f5c9">

- Pop up titles can be seen when blue pin is selected

### Responsiveness
<img width="601" alt="Screenshot 2023-11-13 at 14 14 37" src="https://github.com/RonnyRice/AWM_CA1/assets/82329993/b8fbb810-8461-4b61-af4a-7863cb98ec3c">

## Setup

