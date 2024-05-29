# Simpplr_Movielist
Simpplr Movie List
Overview
The Simpplr Movie List is a web application designed to help users manage a list of movies. It provides functionality for viewing, adding, updating, and deleting movies stored in a database. The frontend interface is developed using HTML, CSS (Bootstrap), and JavaScript, while the backend is built using Django.
Features
Navigation
Navigation Bar: Allows users to switch between different sections of the application, such as viewing all movies, adding new movies, filtering movies, and retrieving movie counts by language.
Viewing All Movies
Movie List: Displays all movies in a table format, showing details such as movie name, director, year of release, language, and rating.
Pagination: Helps manage large datasets by breaking the list into manageable pages.
Update Movie: Users can edit existing movie details by clicking an "Update" button, which opens a modal window with pre-filled fields. Changes are saved back to the database upon submission.
Delete Movie: Users can remove movies from the list by clicking a "Delete" button, which deletes the movie entry from the database.
Adding Movies
Add Movie Form: Users can add new movies by filling out a form with fields for movie name, director, year of release, language, and rating.
Filtering Movies
Filter Options: Users can filter movies based on specific criteria to narrow down the movie list according to their preferences.

Bonus Feature: Get Movie Counts by Language
Language Count: Provides the number of movies available in a particular language, offering insights into the distribution of movies across different languages.
Technologies Used
Frontend
HTML: Used for creating the structure of web pages.
CSS (Bootstrap): Enhances the visual appearance of the application using a styling framework.
JavaScript: Adds interactivity and dynamic behavior to web pages.
Backend
Django: A high-level Python web framework used to build robust web applications.
Python: The programming language for server-side logic and data manipulation.
Database
Excel (xlsx) File: Used as the storage mechanism for maintaining movie data. The OpenPyXL library is employed for reading and writing Excel files.
Project Structure
HTML Templates
index.html: The main template displaying the movie list and navigation.
add_movies.html: Template for the page where users can add new movies.
filter_movies.html: Template for the page where users can filter movies.
search_movie_by_language.html: Template for the page where users can search for movies by language.
JavaScript (Client-side)
Internal js code: Manages client-side functionality such as fetching movie data, updating the table, pagination, search, and handling modal interactions.
Django Views
submit_form: Handles the form submission for adding new movies.
index: Renders the main page with the movie list.
filter_movies: Renders the filtering page.
add_movies: Renders the page for adding new movies.
search_movie_by_language: Renders the page for searching movies by language.
movie_list: Retrieves movie data from the database and returns it as JSON.
delete_movie: Handles deleting a movie from the database.
update_movie: Handles updating movie details in the database.
CSS Styles
Inline Styles and Bootstrap Classes: Used for styling elements.


Screenshots

Add Movies page

We can add the movie through this “Add Movies” page, we will click on submit button, then we will get a message that the form has been successfully submitted.
As soon as we click on the OK button, all this data will start appearing on the All Movies page.
![1](https://github.com/Vraag0056/Simpplr_Movielist/assets/60671266/24d190d6-d647-4780-8162-3fa731b3ecc4)


All Movies Page

This screenshot is the home page of a movie list application. This page shows the list of all the movies. Every movie has an action buttons through which we can update or delete the movie.
Whenever we add movies, all the data of that movie will be shown on this page.
As we can see in the above screenshot we have add a movie which we can see in this table.
![2](https://github.com/Vraag0056/Simpplr_Movielist/assets/60671266/8887976a-ab49-4ea6-9622-b0f0ccc52eca)


2.1 Search a movie Bar
We can search any movie by its name.
![3](https://github.com/Vraag0056/Simpplr_Movielist/assets/60671266/7ed84aec-975a-493a-88cc-1ee75a0c8ad2)

2.2 Update Button
We can update the data of any movie by clicking on the update button. As soon as we click on the update button, a form will come to us in which the previous data has already filled, we will have to replace the data with new data and click on save changes.
By the above process we can update any data.
![4](https://github.com/Vraag0056/Simpplr_Movielist/assets/60671266/ea6962b2-b4c7-45e9-9018-8986d6ce678f)

2.3 Delete Button
We can delete the data of any movie by clicking on the delete button.
As soon as we click on the delete button, a message will appear and we will see that as soon as we click on OK button, the data will be deleted.
![5](https://github.com/Vraag0056/Simpplr_Movielist/assets/60671266/ba358572-0ef5-403d-95ef-0442834ee6ae)

Filter Movies
We can filter movies on this page in different ways, such as by movie name, director name,year, rating, or language.
The following screenshot explains that director name is a filter and we can searching for any director.
![7](https://github.com/Vraag0056/Simpplr_Movielist/assets/60671266/b845ae83-7dd0-4280-a4ba-09d1c5c4adc9)
![8](https://github.com/Vraag0056/Simpplr_Movielist/assets/60671266/65b9233e-a5a3-49c1-8206-92ea5b933aba)
![9](https://github.com/Vraag0056/Simpplr_Movielist/assets/60671266/a7261165-a942-4449-864c-594106f1d1e8)

BONUS Question Page - (Get Movies Count)
By this page we can get the number of movies in the specified language.
The following screenshot shows how this page works. Firstly we have the dropdown by which we can select any language.
![10](https://github.com/Vraag0056/Simpplr_Movielist/assets/60671266/ab5e85d1-50c8-4a4d-a4f2-6bca6a168e9e)
After selecting and clicking submit button we can show the result which is shown in the following image.
![Screenshot 2024-05-29 172646](https://github.com/Vraag0056/Simpplr_Movielist/assets/60671266/5305bc83-cdac-4bbf-b314-5ef169ac44e6)







