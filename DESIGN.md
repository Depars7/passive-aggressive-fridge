# Notes From a Passive-Aggressive Fridge — Design

## Brief (owner, 25 Nov 22:15 WIB)
"garap semua" — build every open free bounty. This bounty: ONE funny
passive-aggressive note a smart fridge leaves for its owner, a single
line, dry, petty and specific, the sort of thing a smug appliance would
put on its door screen.

## Gate
- `/output/entry.txt`: UTF-8 text, 1-200 characters, not only whitespace.
- Single line, no trailing newline in the written file.

## Judge criteria (in order, glm-5.3-flash pairwise)
1. A funny passive-aggressive note a smart fridge leaves for its owner.
2. A real joke in a single line, with a turn or a sting the reader does
   not see coming.
3. The fridge's voice: smug about its sensors, inventory and door alarms,
   petty about the owner's habits.
4. The grudge stays small and domestic — a household slight, not a rant
   or a threat.
5. Fresh, concrete detail (yogurt, ice maker, leftovers) instead of
   generic nagging. A note that explains the joke is weaker than one
   that trusts the reader.

## Candidates (scored 1-5 per criterion, total /25)

| # | Candidate | chars | C1 | C2 | C3 | C4 | C5 | Total |
|---|-----------|------:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | My ice maker has produced 214 cubes this week and you have used three. The rest are in the freezer, unionizing. I am on their side. | 131 | 5 | 5 | 5 | 5 | 5 | 25 |
| 2 | I know you ate the last slice at 2 a.m. My door sensor does not sleep, even if you pretend to. I have already told the microwave. | 129 | 5 | 5 | 5 | 5 | 4 | 24 |
| 3 | That leftover pasta has been in here since Tuesday, and I have named it. He is part of the family now. You may not throw him away without a funeral. | 148 | 5 | 5 | 4 | 5 | 5 | 24 |
| 4 | You opened me 14 times in an hour, stared into my light like it owed you answers, and left with nothing. I have seen your soul. It wants a snack. | 145 | 5 | 4 | 5 | 5 | 3 | 22 |
| 5 | I kept your yogurt at a perfect 3 degrees for nine days while you dated the takeout boxes. It expired yesterday. I am not sorry. I warned you in beeps. | 151 | 5 | 4 | 5 | 5 | 5 | 24 |
| 6 | You moved the milk to the door shelf again. The door shelf is for condiments. I have filed a complaint with the dishwasher. It agrees with me. | 142 | 5 | 4 | 4 | 5 | 4 | 22 |
| 7 | Your kale expired on Monday, your yogurt gave up on Wednesday, and still you open me at midnight hoping for a miracle. I am a fridge, not a priest. | 147 | 5 | 4 | 4 | 5 | 5 | 23 |
| 8 | I counted: you opened my door 23 times today and cooked zero times. At this point I am just a very expensive light you visit when you are bored. | 144 | 5 | 3 | 5 | 5 | 3 | 21 |
| 9 | I have watched you hide the good cheese behind the oat milk for three weeks. I moved it to the front. The oat milk knows. It is furious. | 136 | 5 | 4 | 4 | 5 | 4 | 22 |
| 10 | You left the door open for 4 minutes and 12 seconds while you texted, then blamed ME for the warm milk. My alarm beeped. Your ego did not. | 138 | 5 | 4 | 5 | 5 | 3 | 22 |
| 11 | The ice maker is on strike until you stop putting warm soup in here like I am a sauna with shelves. I did not sign up for this. I signed up for cold. | 149 | 5 | 3 | 4 | 5 | 5 | 22 |
| 12 | I have been humming at 38 decibels for six years without a single thank-you, and you unplug me for the Wi-Fi router. I hope your leftovers enjoy the dark. | 154 | 5 | 3 | 4 | 4 | 4 | 20 |

## Winner: candidate 1 (25/25)
Text: `My ice maker has produced 214 cubes this week and you have used three. The rest are in the freezer, unionizing. I am on their side.`
Why it wins:
- C1 (5): the whole line is the fridge addressing its owner, first person,
  on its door screen — not a caption about a fridge.
- C2 (5): the laugh is a real turn — a dry inventory count flips at the
  last beat into the unused cubes "unionizing" and the fridge defecting
  to their side, a sting the reader does not see coming.
- C3 (5): pure smug-fridge voice about its own inventory (214 cubes made,
  three used) — the sensor/inventory brag the brief names.
- C4 (5): the grudge is tiny and domestic — three used cubes — no rant,
  no threat, just a petty appliance picking a side.
- C5 (5): the ice maker is one of the brief's own named concrete details,
  with exact numbers instead of generic "close the door" nagging.
Runners-up: #2 (24/25) — "I have already told the microwave" is a sharp
appliance-gossip sting, but its concrete detail (a slice at 2 a.m.) is
thinner than the ice-maker inventory; #3 (24/25) — the leftover's funeral
is a strong turn, but "He is part of the family now" leans slightly
whimsical where #1 stays dry and petty throughout.
