# TeamName-SilverEmergencyResponse_SCDFXIBM
We are Team coding n00bies! We are a group of friends who have known one another since secondary school and are new to the world of coding. We signed up for this competition to learn and challenge ourselves! :) 

# **Content**
1. Short description of our solution and our idea
2. Architecture of our proposed solution
3. Our detailed solution
4. Step-by-step installation instructions
5. Technologies used to build our solution

# **Short description of our solution and our idea**
According to the Health Promotion Board Singapore, about one-third of elderly Singaporeans aged 60 and above have recurring falls. Falling down at an old age can be detrimental as older people have more fragile bones, are more likely to have complications from surgeries and have problems recovering. 

Our team has identified elderly who are living alone as a particularly vulnerable group amongst the elderly. This is because the elderly in this group do not have family members or relatives living with them who can provide help in the case of a fall or alert emergency medical services. Furthermore, we identified that bathrooms are commonplace for falls due to the slippery surfaces. Therefore, our team’s solution aims to detect such falls, alert the Singapore Civil Defence Force (SCDF) and Community First Responders (CFRs) for the elderly and collect data that is useful for the personnel arriving at the scene. 

There are two phases to our solution. Phase One encompasses data collection via motion sensors to detect a fall so that SCDF is alerted as soon as it occurs. This is of utmost importance as the elderly living alone do not have anyone else who can alert emergency medical services and may be immobilised after the fall.  

Phase Two is to maximise the effectiveness of CFRs who arrive early to the scene before SCDF personnel through Watson Translation. This is to make communication between the injured senior citizen. Clear communication will allow the CFR to make a better assessment of the situation and provide the necessary aid accordingly. This can significantly impact the outcome of the fall for the elderly. Furthermore, the communication between the CFR and the elderly can be transcribed and sent to SCDF personnel who are on the way so they can remain updated. 

# **Architecture of our proposed solution**

# **Our detailed solution**
Phase One: Detection of falls and alerting SCDF  

Phase One requires the use of motion sensors. The motion sensors will be installed on the four walls and the ceiling of the bathroom. They track movement in the bathroom and will be able to distinguish between normal activity and an actual fall by continuously measuring the speed of movements in all directions. The motion sensor can also determine the time at which a person is motionless and the position they are in (i.e. on the floor). 

When a fall is detected, a voice bot will be activated. This is made possible because the motion sensors are connected to Arduino using wires. Arduino is connected via Bluetooth to a wifi-enabled device (e.g. a mobile device), located in the elderly’s home, which can open a voice-enabled Node-RED website with a chatbot. 

The voice bot will be integrated with Watson Speech to Text and Watson Translation functions. The voice bot will communicate with the injured elderly by asking questions about their condition. Answers from the elderly will be recorded, transcribed and sent to SCDF. SCDF can assess the transcription as it arrives. This information will be valuable to SCDF personnel as it helps them analyse and understand the situation before arriving at the scene. 

Furthermore, using the answers from the elderly, the voice bot will assess the level of severity of the fall. The level of severity can be categorised as follows: false alarm, mild, intermediate, severe. Figure 1 and 2 below show how the elderly’s condition will be categorised. This assessment of the degree of severity is also sent to SCDF to determine how much manpower is to be deployed and whether it is a false alarm. 



Fig. 1


Questions
Responses that will indicate 
Code Red (Severe)
Responses that will indicate 
Code Orange (Intermediate)
Responses that will indicate 
Code Yellow (Mild)
Responses that will indicate 
Code Zero (No action required)
“Can you make a sound to indicate you are conscious?”



No response
Unintelligible sounds 
“Yes”, “ya”, “I can talk”, “I am conscious” 
“Yes”, “ya”, “I can talk”, “I am conscious” 
“Have you fallen down?”
No response
“Yes”, “Ya”
“Yes”, “Ya”
“No”, “I am okay”, 
“I am fine” 
“Are you bleeding?” 
No response
“Yes”, “bleeding”, “blood”
“No”
-
“Can you tell me where you are feeling pain?”
No response
Body parts such as the leg, head, arm, back
Any body part excluding the head, hip, and back
-
“Do you remember how you fell?”
No response
“No”, “cannot”, “I don’t know” 
“Yes”, “Ya”, “slipped”, “slippery floor”, “tripped”, “water”, “wet”
-
“Are you able to move your body?”
No response
“No”, “cannot”
“Can”, “a bit” 
-
“What is the year currently?”
No response
“No” or an incorrect response 
Correctly identifies the year
-
“Are you on any medication that makes you drowsy now?”
No response
“Yes”, “I think so”, “I don’t know”, “I can’t remember”
“No”
-

Fig. 2 




Phase 2: Maximising the effectiveness of Community First Responders (CFRs) 

CFRs can play a key role in the rescue process. After it is determined that the elderly have fallen, CFRs within 400 metres of the injured elderly’s location will be alerted via the myResponder app. CFRs will only be alerted if the level of severity is severe, intermediate or mild. CFRs will not be alerted if the voice bot has deemed the situation a false alarm. 

If CFRs are able to enter the house and attend to the elderly, they can make use of myResponder app to send on-site videos, geo-location and other useful information to SCDF. In addition to these existing features, the myResponder app will be integrated with Watson Speech to Text and Watson Translation functions. 

This is to make communication between the injured elderly and the CFR as smooth as possible given a language barrier and that the senior is conscious. Clear and accurate communication will allow the CFR to make a better assessment of the situation and provide the necessary aid accordingly during the first critical moments. For example, the senior citizen can describe where they are experiencing pain as well as the type of pain so the CFR can decide the appropriate aid to provide. This can significantly impact the outcome of the fall for the elderly. Furthermore, the communication between the CFR and the elderly can be transcribed and sent to SCDF personnel who are on the way. This would allow them to arrive at the scene fully updated and armed with as much information as possible. 

Use of Watson Speech to Text and Watson Translation functions in the chatbot and myResponder app

Our team has decided to use two IBM functions ― Watson Translation and Watson Speech to Text. 

Watson Translation is necessary to maximise the effectiveness of CFRs as it helps lower the language barrier. Singapore is a multiracial country where many languages are spoken and the elderly are often not proficient in English. It is likely that the injured elderly and the CFR will not be able to communicate in English nor have the same mother tongue. 

Watson Speech to Text is utilised so that a transcript of the conversation between the voice bot and the elderly as well as between the CFR and the elderly are sent to SCDF personnel. With textual information, it will be faster for SCDF personnel to comprehend and thus analyse the situation compared to listening to entire audio recordings. 

