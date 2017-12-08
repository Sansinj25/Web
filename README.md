# Title : The food symphony

# Abstract

Have you ever wondered while cooking whether these ingredients could be great together ? A good example is certainly the Hawaiian pizza, which mixes, original pizza ingredients like tomato, ham and mozzarella, with pineapple, an exotic ingredient.

Thus, using the big dataset gathering cooking recipes all around the world, our project's goal is to extract the combination of ingredients and try to find an interconnection between them.
First of all, will be to extract the essence of each ingredient in a recipe and then analyze what the ingredient bring in the recipe (sweet, spicy, ...). The second step, will be to find correlation between recipes in order to map which combinations of different ingredients blend the best together to give tasteful meals. Finally, we imagine an interface where users will give as input a series of ingredients and constraints, i.e. (vegan, with meat, with fish, etc.) and a recipe will be suggested to them. From there we can use machine learning to create new recipes from what we have learned. Theoretically, this mechanism will consider all ingredients seen in the learning phase, thus new unknown mixtures of ingredients can emerge giving rise to the best combination ever (hopefully).

Story:

We believe that ingredients in a recipe are like harmonies in music, separated they are pleasant to hear, but when perfectly combined harmonies can come up with something special (Schubert' Symphonies).
Therefore, we are convinced that some of the best combinations are still waiting to be found. Indeed, best chef in the world always tries when making a creation, to have all ingredients in osmosis. What if the best combination is a fish from Tahiti, a spice from Tierra del Fuego, some exotic vegetable from Vietnam and olive oil from Italy. How would be able to produce it?

Motivation: We are three students that enjoy cooking and eating, however, as students, it's not always easy to take the time to check for a recipe, look at the ingredients we already have and what we are missing. Also, it's not easy to have new ideas or to know whether what are left in our fridges could be cooked together.  Thus, we believe this project suit us well. We have the opportunity to work on a subject that we enjoy and to create something new that may help other people to improve all the cooking process.


# Research questions

1. Are common ingredients (like meats, rice or pasta) essential for a good meal ? Or whether exotic ingredients make it special ?

2. What is the essence of each ingredient and what do they bring in a recipe ?

3. What are the characteristics of popular recipes ?

4. What kind of correlation between ingredient will be the best to find the harmony in a recipe ?

5. What are the process of the best chef in the world to find new recipes ? And could we apply this to our project ?

6. What should we implement in our interface to make it interactive and friendly using ?

7. The cooking process does have a great importance in the preparation of the meal. We will need to find a workaround. 

# Dataset

To achieve our goals, we will use Cooking recipes dataset, where we can get the list of ingredients turn into ingredients bag of words in order to group them into categories and characterize their essence and their role in the recipe. Therefore, we will be able to determine the correlation by the number of occurrences and their role.

Besides ,the characteristics of each ingredients such as the total amount of calories and the calories by group, i.e. fat, protein, sugar, as well as the sodium and cholesterol content will be extracted to enrich our work. On one side, we will try to add the chef process in order to find new recipes and on the other side, we will try to make the distinction with common ingredients and exotic ingredients.


# A list of internal milestones up until project milestone 2

The project milestone should contain a notebook with data collection and descriptive analysis.

Week #1 :
- Agree on the dataset and what information to extract.
- Discuss with the TA about our work plan.
- Find function to handle text extraction (only important words, without articles words such as the, a, for ...)

Week #2 :
- Data collection
- Group ingredients into categories
- Characterize the essence and role of each ingredients
- Start to find correlation between them
- Work on possible combinations

Week #3 :
- Come up with a solution to measure the harmony of our recipes
- Start to work on the learning phase
- Work on chef's process to find new recipes
- Work on our data story
- Work on the descriptive analysis

Week #4
- Finalize the notebook
- Structured and informed plan for the next milestones.
- Start to work on our data story or report
- Start to discuss about the presentation for the poster

# Questions for TAa

- It would be usefull to also have the number of calories, satured fat etc in each ingredients. Can we use an external documentation for that? Or can we infer it from the data using machine learning?

- We really want to do something interactive, Would you have any recommendations (website or interface on computer) ?

- We will need powerful tools of natural language processing and machine learning to extract ingredients and come up with new combinations. Is it doable?
