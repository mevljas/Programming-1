# Movie actors
This homework is being graded and you should not miss it.

For a particular grade, you must also solve all the tasks required for a lower grade. For, for example, grade 7, you also need to solve problems for grade 6 and so on.

## Score 6
We have a list of pairs of names of actors and movies in which they have played, for example

[("Ana", "From Čatež to Litija"),
 ("Berta", "From Čatež to Litija"),
 ("Ana", "Harry Potter 4"),
 ("Cilka", "Harry Potter 4"),
 ("Berta", "Star Trek DS-9"),
 ("Days", "Harry Potter 4"),
 ("Emma", "Star Trek DS-9"),
]
If an actor plays in multiple films, he appears several times; so Ana played in From Čatež to Litija and in Harry Potter 4.

Write the following functions

- players(links) receives a list like the one above and return a set of player names,
- movies(links) returns a set of movie names,
- player_plays(actor, links) returns a set of movie names in which a given actor has played,
- movie_actors(movie, links) returns a set of names of actors who appeared in the given movie,
- by_players(links) returns a dictionary whose keys are the names of the actors and the corresponding values are the sets of names of the movies in which these actors played, for example python {"Ana": {"From Čatež to Litija", "Harry Potter 4"} "Berta": {"From Čatež to Litija", "Star Trek DS-9"}, "Cilka": {"Harry Potter 4"}, "Dani": {"Harry Potter 4"}, "Emma": { "Star Trek DS-9"}}
- po_filmih(links) returns a dictionary whose keys are movies and the corresponding values are sets of player names.
## Score 7
Write functions

- teammates(players_films), which receives such a dictionary as returned by the post-players function, and as a result returns a set of pairs of actors who have ever met in a movie. Each pair should be arranged alphabetically. For the above dictionary, the function would return {("Ana", "Berta"), ("Ana", "Cilka"), ("Ana", "Dani"), ("Berta", "Ema"), ("Cilka "," Days ")}. So, for example, (“Berta” “Ema”) is in the crowd because Berta and Ema performed together in “Star Trek DS-9”.

- n_teamers(player, pairs) receives the player's name and the list of pairs returned by the previous function. Returns the number of all players a given player has ever worked with. The call of n_ teammates("Dani", couples) (where couples are the above list of couples) returns 2, as Dani played alongside Ana and Cilka.

- teammate_players(player, pairs) gets the same arguments as the previous function, and as a result returns the set of players with which the given player participated. player_ teammates("Days", pairs) returns {"Ana", "Cilka"}.

## Score 8
Write all functions for grades 6 and 7 using derived dictionaries and sets, so that the function will contain only return *something*.

## Score 9
The strength of the connection between the two actors is calculated by checking how many films they have played together. We could simply count the movies ... but we won’t, because movies with fewer actors bind stronger than ones where there are a lot of actors. The “power” of the film is equal to 2 / square the number of actors.

How strongly are Ana and Berta connected? They played in From Čatež to Litija, which has 2 players, and in Harry Potter 4, which has (as the name suggests) 4. The connection between Ana and Berta is therefore 2/2 ** 2 + 2/4 ** 2 = 2/4 + 2/16 = 10/16 = 0.625.

Write functions:

- link_power(player1, player2, links), which as an argument gets the names of two players and a list of links in the form from task for grade 6. As a result, it returns the power of the link. The call strength_connection ("Ana", "Berta", connection) returns 0.625;

- weighted_connections(links) receives only links, and as a result returns a dictionary whose keys are all pairs of player names (each pair appears only once and is arranged alphabetically), and the corresponding values are the strength of the links as returned by the previous function.

And one more thing: both functions must be written in one line.

## Grade 10
Write functions

- connected_with(player, pairs), which receives the name of the player and a list of pairs of players who have ever participated. As a result, a set of names of all the players who collaborated with any of the players who collaborated with any of the players who collaborated with any of the players ... who collaborated with a given player. The result also includes the given player himself.

Call connected_with("Ana", [("Ana", "Berta"), ("Berta", "Cilka"), ("Dani", "Ema"), ("Berta", "Fanči"), (" Greta "," Helga ")] returns the set {Ana", "Berta", "Cilka", "Fanči"}; Ana only worked directly with Berta, but she also collaborated with Cilka and Fanči.

Call connected_with("Ana", [("Ana", "Berta"), ("Berta", "Cilka"), ("Dani", "Ema"), ("Berta", "Fanči"), (" Greta "," Helga "), (" Emma "," Fanci ")]) returns {" Ana "," Berta "," Cilka "," Dani "," Emma "," Fanci "}. Compared to the previous call, we also have a couple Ema and Fanči, who with Ana (through Berta and Fanči) increase Emo, and through Ema Dani.

- islands(pairs) returns a list of all "islands" of unrelated players. Each island is represented by a crowd. The order of the islands in the list is arbitrary.

Call islands([("Ana", "Berta"), ("Berta", "Cilka"), ("Dani", "Ema"), ("Berta", "Fanči"), ("Greta", " Helga ")]) returns [{" Ana "," Berta "," Cilka "," Fanci "}, {" Dani "," Emma "}, {" Greta "," Helga "}].

Call islands([("Ana", "Berta"), ("Berta", "Cilka"), ("Dani", "Ema"), ("Berta", "Fanči"), ("Greta", " Helga "), (" Ema "," Fanci ")]) returns [{" Ana "," Berta "," Cilka "," Fanci "," Dani "," Ema "}, {" Greta "," Helga "}].

These two functions do not need to be written in one line. In fact, that would be pretty annoying.
