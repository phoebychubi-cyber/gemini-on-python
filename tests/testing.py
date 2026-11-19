from gemini import Gemini

gemini = Gemini("your api key")

response = gemini.ask("In 1809, a British statesman was shot in the buttock during a duel with a fellow Cabinet minister, later went on to serve as Prime Minister of the United Kingdom for just 119 days in 1827 before dying in office, and—according to evolutionary biologist Stephen Jay Gould—indirectly helped set the stage for Charles Darwin's voyage on HMS Beagle. Who was this statesman?")

print(response)
