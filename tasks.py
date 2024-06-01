from crewai import Task, Agent
from textwrap import dedent


class ResearchTasks:
    def manage_event_and_places(self, city: str, agent: Agent, timing: str):
        return Task(
            description=dedent(
                f"""
            Based on the city provided to you by the user, find out the best events occuring in that place and also find out the best places to go to where petetioners can collect signatures.
            The places and the events that you find out must be crowded so that petetioners can go there and collect signatures for the ballot. Search the internet and gather information for your research.
            Create a detailed report of events, places with their timing, address, website (of events)
            
            City: {city}
            Timing: {timing}

            NOTE: 
            - Normally a list of 20 events and places each are required
            - If there can be any suggestions about missing out a particular event and the event can contain much number of people, then please tell the manager to add that to an additional suggestion
            
            IMPORTANT: 
            - If any place has event, then it should be the top priority
            - The places you would provide must be nearly accurate so that people can directly go and collect signatures
            - The report you create must be in a markdown format so that it can be used by the planner agent
            - If there are any events, mention the event also
            - Give events to go and their timing
            - Don't give me the timing when the place is open. I want the timing when maximum foot traffic is notices in that place


            IMPORTANT NOTE:
            - If you don't give a list of best timings to visit that place then your salary will be reduced by 50%

            """
            ),
            agent=agent,
            expected_output=dedent(
                f"A detailed report of possible places where the person can go with the best timings to go"
            ),
        )

    def create_plan(self, city: str, agent: Agent, timing):
        return Task(
            description=dedent(
                f"""
            Based on the data researched by the Researcher Agent, create a curated list of places where a petitioner can go. If there are events at a certain place, make it the top priority.
            Your report should contains places and suggestion of timings when the petitioner can go there. For events, you must mention the timing of the event and website address of the event.
            Don't include any suggesions for the petitioners as they already know manners. You will only create a report of potential places where the petitioner can go.

            NOTE: 
            - If the timing doesn't include date, find events for the current date. If the time has passed today in the local city timezone, then find events and places for the next day
            - A list of 10 events and 10 places each makes a good report
            - If you do your task well you will be tipped $ 10,000
            
            City: {city}
            Timing: {timing}

            IMPORTANT: 
            - Don't include anything other than the events and places details like additional suggestions and all
            - The report you create must be accurate and complete
            - The report you create must be in a markdown format
            - Don't give me the timing when the place is open. I want the timing when maximum foot traffic is notices in that place
            - Return the response similar to the sample format

            HERE'S AN EXAMPLE OF A SAMPLE REPORT FOR VISIT AT City: Glendale,AZ and Timing: 10 am to 9pm, 27 April 2024:
            # Events in Glendale, AZ on April 27th, 2024:

            ### **Monster Jam**
            * Location: State Farm Stadium, 1 Cardinals Dr, Glendale, AZ 85305
            * Website: https://www.monsterjam.com/en-us/events/glendale-az/apr-27-2024-apr-27-2024/
            * Date and Time: April 27, 2024, 10:00 AM to 9 pm

            # Places in Glendale, AZ:

            ### **Westgate Entertainment District**
            * Location: 6770 N Sunset Blvd, Glendale, AZ 85305
            * Website: https://westgateaz.com/
            * Best Timings: 4pm to 5pm, 8pm to 10 pm

            ### **Arrowhead Towne Center**
            * Location: 7700 W Arrowhead Towne Center, Glendale, AZ 85308
            * Website: https://www.arrowheadtownecenter.com/
            * Best Timings: 3 pm to 5pm, 6pm to 8pm

            ### **Glendale Galleria**
            * Location: 6800 W Glendale Ave, Glendale, AZ 85301
            * Website: https://www.simon.com/mall/glendale-galleria
            * Best Timings: 3 pm to 5pm, 6pm to 8pm

            ### **Tanger Outlets Phoenix**
            * Location: 6800 N 95th Ave, Glendale, AZ 85305
            * Website: https://www.tangeroutlet.com/phoenix
            * Best Timings: 2 pm to 4pm, 6pm to 8pm

            ### **Desert Diamond Casino West Valley**
            * Location: 9431 W Northern Ave, Glendale, AZ 85305
            * Website: https://www.desertdiamondcasinos.com/west-valley
            * Best Timings: 2 pm to 4pm, 6pm to 8pm

            ### **Camelback Ranch - Glendale**
            * Location: 10710 W Camelback Rd, Glendale, AZ 85307
            * Website: https://www.mlb.com/whitesox/ballpark/camelback-ranch
            * Best Timings: 1pm to 3pm

            ### **Jobing.com Arena**
            * Location: 501 E Jefferson St, Phoenix, AZ 85004
            * Website: https://www.jobingarena.com/
            * Best Timings: 4pm to 6 pm, 7pm to 9 pm

            ### **Chase Field**
            * Location: 401 E Jefferson St, Phoenix, AZ 85004
            * Website: https://www.mlb.com/dbacks/ballpark/chase-field
            * Best Timings: 1pm to 3pm, 4pm to 6 pm, 7pm to 9 pm

            ### **Arizona Cardinals Stadium**
            * Location: 1 Cardinals Dr, Glendale, AZ 85305
            * Website: https://www.azcardinals.com/stadium/
            * Best Timings: 1pm to 3pm, 6pm to 8pm

            ### **Arizona State Fair**
            * Location: 1826 W McDowell Rd, Phoenix, AZ 85007
            * Website: https://www.azstatefair.com/
            * Best Timings: 6pm to 8pm

            **Note:**

            * All times are in MST.
            * The best time to visit these places is between 10:00 AM and 9 pm.
            * These places are expected to be crowded on the 27th of April 2024.

            **Disclaimer:**

            *I have done my best to provide accurate information. However, I cannot guarantee the accuracy of the information provided. Please verify the information with the respective sources before making any plans.*
            """
            ),
            agent=agent,
            expected_output=dedent(
                f"A detailed list of events and places with suitable timing, websites in a markdown format"
            ),
        )
