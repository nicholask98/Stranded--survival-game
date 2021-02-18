# Stranded: A Text-based Survival Game


## Overview:
You were left to die on a deserted island. The next opportunity to be rescued, will not be for at least 50 days. You need to survive until the opportunity arises but you also need to be looking out for people to arrive, because the exact time is uncertain. Use your time wisely.


## Ideas/Mechanics

#### Days/Game Flow:
Each day passes by with 24 hours of time to accomplish what needs to be done (including your sleep). You can use your time however you desire. You'll be prompted with options and how much time they require to accomplish. Some options will only be available during certain times in the day(ie. sleeping only available after 8PM. naps available from 1PM to 3PM. Scavenging for food only available during daylight, etc.). Each new day will update the day counter (which is essentially your score ie. "You survived X days before _________. being mauled by a bear or dying of thirst etc.").


### * Your needs:
You'll have a thirst, hunger, and health score and if any of them drop to 0 you will die. Score for each is 0 to 100
Ex. "THIRST: 48/100 || HUNGER: 90/100 || HEALTH: 25/100"

- Health: 
If you do not have a fire started before bed your health score will drop. If you do not have shelter, weather will affect your health (rain, extreme cold etc.) You can find shelter in nature (like taking shelter in a cave for the night. Which will lower your health less than being outside, but still some) or you can build a home with resources you find. Sleeping 8 hours will provide you the maximum health increase.

- Hunger:
Hunger depletes slowly over time: 2 points per 6 hours. See list of hunger values of food below.

- Thirst:
Thirst depletes more quickly than hunger: 9 points per 6 hours. See list of thirst values of food below.


### * Resources: 

- Wood:
4 wood can keep you sufficiently warm for one night, 50 wood can build a cabin. A cabin retains heat, so you only need 2 wood to keep you sufficiently warm every night.

- Water:
Can collect rain water and boil it on a fire for 30 minutes to clean it. It's not always raining so you can take advantage of the timing if it is. You can also collect water from the ocean, but you have to boil it for an hour. 

- Food:
Can forage for berries/fruits. Some fruits and vegetables have water content in them and raise your thirst score. Can hunt for wildlife for food, but the animals are about 50% likely to have diseases. Must also cook meat and it takes an hour. Cooked meat does not have water content. In order to hunt you need to build weapons(bow/arrow, sword, spear, fishing pole.)



### Food Values:
* Item: Hunger / Thirst / Health

- Healthy Cooked Meat: 15 / 0 / 0
- Diseased Meat: 15 / 0 / -30
- Apple: 5 / 4 / 3
- Pear: 5 / 4 / 4
- Banana: 4 / 1 / 5
- Red berry: 1 / 2 / 2
- Blue berry: 1 / 3 / 2
- Green berry: 1 / 0 / 2
- Black berry: 2 / 1 / 2
- Purple berry: 2 / 2 / 2


- Bucket Clean water: 0 / 50 / 10
- Bucket Half-Clean Ocean Water: 0 / 25 / -5
- Salt water: 0 / -10 / -20



##### Ideas for later implementation:
- If the player dies, record some aspects of their game (Like a shelter they built, or resources that were already taken.) and implement them into the current game. This way you can have a death counter, and the user can have more reason to keep playing after they've died.
- Include possibility for new people to arrive randomly on the island. You can choose to do whatever you want with them. Fight them, and risk dying (because they may be dangerous), befriend them and use them as a resource to complete more tasks throughout the day. They have the same needs as you: Health, hunger, thirst.
- Implement enemies: Like the above, the enemies can be other people who were already on the island before you got there. They can be animals like bears or wolves. Even giant squids or piranas for water stuff. Can use wood to build a fence to protect your camp.
-  If you find plants you like, you can take them and plant their seeds at your camp.
- Some types of foods are poisonous but you don't know until you get poisoned. Make a randomizer that changes which foods are poisonous for each new game. ex. if you've already tried the berries and got sick: "Harvest Red berries? WARNING: POSIONOUS FOOD".