import gradio as gr
import json

# Generate Markdown history from JSON history
def process_json_history(json_file):
    '''
    json_history is a JSON string with the following format:
    json_history =
    {
        "0": {
            "episodeIdx": 0,
            "history": {
                "history": [
                    {
                        "action": "look around",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta lighter\n\ta oven, which is turned off. The oven door is closed. \n\ta painting\n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: a glass cup (containing nothing).\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta lighter\n\ta oven, which is turned off. The oven door is closed. \n\ta painting\n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: a glass cup (containing nothing).\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)",
                        "score": "0.0"
                    },
                    {
                        "action": "look around",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta lighter\n\ta oven, which is turned off. The oven door is closed. \n\ta painting\n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: a glass cup (containing nothing).\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta lighter\n\ta oven, which is turned off. The oven door is closed. \n\ta painting\n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: a glass cup (containing nothing).\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)",
                        "score": "0.0"
                    },
                    {
                        "action": "move sewer to kitchen",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta lighter\n\ta oven, which is turned off. The oven door is closed. \n\ta painting\n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: a glass cup (containing nothing).\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "No known action matches that input.",
                        "score": "0.0"
                    },
                    {
                        "action": "move lighter to bowl",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta lighter\n\ta oven, which is turned off. The oven door is closed. \n\ta painting\n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: a glass cup (containing nothing).\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "You move the lighter to the bowl.",
                        "score": "0.0"
                    },
                    {
                        "action": "pour ceramic cup into chair",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, a lighter, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta oven, which is turned off. The oven door is closed. \n\ta painting\n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: a glass cup (containing nothing).\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "No known action matches that input.",
                        "score": "0.0"
                    },
                    {
                        "action": "pour metal pot into ceramic cup",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, a lighter, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta oven, which is turned off. The oven door is closed. \n\ta painting\n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: a glass cup (containing nothing).\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "No known action matches that input.",
                        "score": "0.0"
                    },
                    {
                        "action": "pour table into bowl",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, a lighter, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta oven, which is turned off. The oven door is closed. \n\ta painting\n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: a glass cup (containing nothing).\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "You pour the contents of the table into the bowl.",
                        "score": "0.0"
                    },
                    {
                        "action": "move painting to bathroom",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, a glass cup (containing nothing), a lighter, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta oven, which is turned off. The oven door is closed. \n\ta painting\n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: nothing.\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "You move the painting to the bathroom.",
                        "score": "0.0"
                    },
                    {
                        "action": "mix cup containing orange juice",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, a glass cup (containing nothing), a lighter, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta oven, which is turned off. The oven door is closed. \n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: nothing.\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "No known action matches that input.",
                        "score": "0.0"
                    },
                    {
                        "action": "look at sodium chloride",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, a glass cup (containing nothing), a lighter, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta oven, which is turned off. The oven door is closed. \n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: nothing.\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "No known action matches that input.",
                        "score": "0.0"
                    },
                    {
                        "action": "move glass jar to metal pot",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, a glass cup (containing nothing), a lighter, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta oven, which is turned off. The oven door is closed. \n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: nothing.\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "No known action matches that input.",
                        "score": "0.0"
                    },
                    {
                        "action": "pour counter into bowl",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, a glass cup (containing nothing), a lighter, an orange, a potato), a drawer.\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta oven, which is turned off. The oven door is closed. \n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: nothing.\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "You pour the contents of the counter into the bowl.",
                        "score": "0.0"
                    },
                    {
                        "action": "pick up drawer in bowl",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, a drawer, a glass cup (containing nothing), a lighter, an orange, a potato).\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta oven, which is turned off. The oven door is closed. \n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: nothing.\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "You move the drawer to the inventory.",
                        "score": "0.0"
                    },
                    {
                        "action": "mix freezer",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, a glass cup (containing nothing), a lighter, an orange, a potato).\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta oven, which is turned off. The oven door is closed. \n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: nothing.\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\ta drawer.  The drawer is closed.\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "That container is empty, so there are no items to mix.",
                        "score": "0.0"
                    },
                    {
                        "action": "move stopwatch to metal pot",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, a glass cup (containing nothing), a lighter, an orange, a potato).\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta oven, which is turned off. The oven door is closed. \n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: nothing.\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\ta drawer.  The drawer is closed.\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "No known action matches that input.",
                        "score": "0.0"
                    },
                    {
                        "action": "focus on door to hallway",
                        "freelook": "This room is called the kitchen. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta counter. On the counter is: a bowl (containing a red apple, a banana, a glass cup (containing nothing), a lighter, an orange, a potato).\n\ta cupboard. The cupboard door is closed. \n\ta freezer. The freezer door is closed. \n\ta fridge. The fridge door is closed. \n\ta glass jar (containing a substance called sodium chloride)\n\ta oven, which is turned off. The oven door is closed. \n\ta sink, which is turned off. In the sink is: nothing.\n\ta substance called soap\n\ta stopwatch, which is deactivated. \n\ta stove, which is turned off. On the stove is: nothing.\n\ta table. On the table is: nothing.\n\ta thermometer, currently reading a temperature of 10 degrees celsius\nYou also see:\n\tA door to the bathroom (that is open)\n\tA door to the hallway (that is open)\n\tA door to the outside (that is open)\n",
                        "inventory": "In your inventory, you see:\n\ta drawer.  The drawer is closed.\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "You focus on the door between kitchen and hallway.",
                        "score": "-1.0"
                    }
                ],
                "simplifications": "easy",
                "taskDescription": "Your task is to focus on the life stages of the avocado plant, starting from earliest to latest. The plants are located outside.",
                "taskIdx": "13",
                "taskName": "identify-life-stages-2",
                "variationIdx": "2"
            },
            "notes": {
                "text": "my notes here"
            }
        },
        "1": {
            "episodeIdx": 1,
            "history": {
                "history": [
                    {
                        "action": "look around",
                        "freelook": "This room is called the hallway. In it, you see: \n\tthe agent\n\ta substance called air\n\ta picture\nYou also see:\n\tA door to the art studio (that is open)\n\tA door to the bedroom (that is open)\n\tA door to the greenhouse (that is open)\n\tA door to the kitchen (that is open)\n\tA door to the living room (that is open)\n\tA door to the workshop (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "This room is called the hallway. In it, you see: \n\tthe agent\n\ta substance called air\n\ta picture\nYou also see:\n\tA door to the art studio (that is open)\n\tA door to the bedroom (that is open)\n\tA door to the greenhouse (that is open)\n\tA door to the kitchen (that is open)\n\tA door to the living room (that is open)\n\tA door to the workshop (that is open)",
                        "score": "0.0"
                    },
                    {
                        "action": "look around",
                        "freelook": "This room is called the hallway. In it, you see: \n\tthe agent\n\ta substance called air\n\ta picture\nYou also see:\n\tA door to the art studio (that is open)\n\tA door to the bedroom (that is open)\n\tA door to the greenhouse (that is open)\n\tA door to the kitchen (that is open)\n\tA door to the living room (that is open)\n\tA door to the workshop (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "This room is called the hallway. In it, you see: \n\tthe agent\n\ta substance called air\n\ta picture\nYou also see:\n\tA door to the art studio (that is open)\n\tA door to the bedroom (that is open)\n\tA door to the greenhouse (that is open)\n\tA door to the kitchen (that is open)\n\tA door to the living room (that is open)\n\tA door to the workshop (that is open)",
                        "score": "0.0"
                    },
                    {
                        "action": "close door to workshop",
                        "freelook": "This room is called the hallway. In it, you see: \n\tthe agent\n\ta substance called air\n\ta picture\nYou also see:\n\tA door to the art studio (that is open)\n\tA door to the bedroom (that is open)\n\tA door to the greenhouse (that is open)\n\tA door to the kitchen (that is open)\n\tA door to the living room (that is open)\n\tA door to the workshop (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "The door is now closed.",
                        "score": "0.0"
                    },
                    {
                        "action": "go to living room",
                        "freelook": "This room is called the hallway. In it, you see: \n\tthe agent\n\ta substance called air\n\ta picture\nYou also see:\n\tA door to the art studio (that is open)\n\tA door to the bedroom (that is open)\n\tA door to the greenhouse (that is open)\n\tA door to the kitchen (that is open)\n\tA door to the living room (that is open)\n\tA door to the workshop (that is closed)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "You move to the living room.",
                        "score": "0.04"
                    },
                    {
                        "action": "move drawer to cloth sittable",
                        "freelook": "This room is called the living room. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta couch. On the couch is: a white pillow.\n\ta desk. On the desk is: a drawer.\n\ta painting\nYou also see:\n\tA door to the hallway (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "You move the drawer to the couch.",
                        "score": "0.04"
                    },
                    {
                        "action": "focus on object",
                        "freelook": "This room is called the living room. In it, you see: \n\tthe agent\n\ta substance called air\n\ta chair. On the chair is: nothing.\n\ta couch. On the couch is: a drawer, a white pillow.\n\ta desk. On the desk is: nothing.\n\ta painting\nYou also see:\n\tA door to the hallway (that is open)\n",
                        "inventory": "In your inventory, you see:\n\tan orange\n",
                        "isCompleted": "false",
                        "observation": "You focus on the pillow.",
                        "score": "-1.0"
                    }
                ],
                "simplifications": "easy",
                "taskDescription": "Your task is to focus on the life stages of the apple plant, starting from earliest to latest. The plants are located outside.",
                "taskIdx": "13",
                "taskName": "identify-life-stages-2",
                "variationIdx": "0"
            },
            "notes": {
                "text": "my notes here"
            }
        }
    }
    '''
    with open(json_file, "r") as f:
        json_history = json.load(f)
    markdown_history = ""
    for episode in json_history.values():
        markdown_history += f"## Episode {episode['episodeIdx']}\n"
        for history in episode['history']['history']:
            markdown_history += f"### Action: {history['action']}\n"
            markdown_history += f"#### Freelook: {history['freelook']}\n"
            markdown_history += f"#### Inventory: {history['inventory']}\n"
            markdown_history += f"#### Is Completed: {history['isCompleted']}\n"
            markdown_history += f"#### Observation: {history['observation']}\n"
            markdown_history += f"#### Score: {history['score']}\n\n"
    return gr.update(value=markdown_history)

# Create Gradio blocks interface
with gr.Blocks() as demo:
    gr.Markdown("# ScienceWorld Explorer")

    with gr.Row():
        with gr.Column():
            json_file = gr.File(label="History JSON", file_types=["json"], type="filepath")
            submit_button = gr.Button("Submit")

        with gr.Column():
            history_output = gr.Markdown(label="History Markdown", value="")

    submit_button.click(process_json_history, json_file, history_output)

# Launch the Gradio interface
demo.launch()
