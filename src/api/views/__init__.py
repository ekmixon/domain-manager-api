"""__init__."""

CATEGORIES = [
    {
        "name": "Activist Groups",
        "proxies": [
            {"Blue Coat": "Activist Groups"},
            {"Trusted Source": "Politics/Opinion"},
            {"fortiguard": "Political Organizations"},
            {"Palo Alto Networks": "Philosophy and Political Advocacy"},
            {"Trend Micro": "Politics"},
        ],
    },
    {
        "name": "Advertising",
        "proxies": [
            {"Blue Coat": "Activist Groups"},
            {"Trusted Source": "Web Ads/Analytics"},
            {"fortiguard": "Advertising"},
            {"Palo Alto Networks": "Web Advertisements"},
            {"Trend Micro": "Web Advertisements"},
        ],
    },
    {
        "name": "Advocacy Organizations",
        "proxies": [
            {"Blue Coat": "Political/Social Advocacy"},
            {"Trusted Source": "Politics/Opinion"},
            {"fortiguard": "Advocacy Organizations"},
            {"Palo Alto Networks": "Philosophy and Political Advocacy"},
            {"Trend Micro": "Politics"},
        ],
    },
    {
        "name": "Alternative Beliefs",
        "proxies": [
            {"Trusted Source": "Religion/Ideology"},
            {"Blue Coat": "Alternative Spirituality/Belief"},
            {"fortiguard": "Alternative Beliefs"},
            {"Palo Alto Networks": "Philosophy and Political Advocacy"},
            {"Trend Micro": "Alternative Journals"},
        ],
    },
    {
        "name": "Art",
        "proxies": [
            {"Trusted Source": "Art/Culture/Heritage"},
            {"Blue Coat": "Art/Culture"},
            {"fortiguard": "Arts and Culture"},
            {"Palo Alto Networks": "Entertainment and Arts"},
            {"Trend Micro": "Arts"},
        ],
    },
    {
        "name": "Auction",
        "proxies": [
            {"Trusted Source": "Auctions/Classifieds"},
            {"Blue Coat": "Auctions"},
            {"fortiguard": "Auction"},
            {"Palo Alto Networks": "Auctions"},
            {"Trend Micro": "Auctions"},
        ],
    },
    {
        "name": "Blogs",
        "proxies": [
            {"Trusted Source": "Blogs/Wiki"},
            {"Blue Coat": "Social Networking"},
            {"fortiguard": "Social Networking"},
            {"Palo Alto Networks": "Social Networking"},
            {"Trend Micro": "Blogs / Web Communications"},
        ],
    },
    {
        "name": "Financial Brokerage",
        "proxies": [
            {"Trusted Source": "Finance/Banking"},
            {"Blue Coat": "Brokerage/Trading"},
            {"fortiguard": "Brokerage and Trading"},
            {"Palo Alto Networks": "Business and Economy"},
            {"Trend Micro": "Brokerages / Trading"},
        ],
    },
    {
        "name": "Business",
        "proxies": [
            {"Trusted Source": "Business"},
            {"Blue Coat": "Business/Economy"},
            {"fortiguard": "Business"},
            {"Palo Alto Networks": "Business and Economy"},
            {"Trend Micro": "Business / Economy"},
        ],
    },
    {
        "name": "Charitable Organizations",
        "proxies": [
            {"Trusted Source": "Business"},
            {"Blue Coat": "Charitable/Non-Profit"},
            {"fortiguard": "Charitable Organizations"},
            {"Palo Alto Networks": "Business and Economy"},
            {"Trend Micro": "Business / Economy"},
        ],
    },
    {
        "name": "Chat",
        "proxies": [
            {"Trusted Source": "Chat"},
            {"Blue Coat": "Chat (IM)/SMS"},
            {"fortiguard": "Instant Messaging"},
            {"Palo Alto Networks": "Internet Communications and Telephony"},
            {"Trend Micro": "Chat / Instant Messaging"},
        ],
    },
    {
        "name": "Computers / Internet",
        "proxies": [
            {"Trusted Source": "Internet Services"},
            {"Blue Coat": "Computer/Information Security"},
            {"fortiguard": "Information Technology"},
            {"Palo Alto Networks": "Computer and Internet Info"},
            {"Trend Micro": "Computers / Internet"},
        ],
    },
    {
        "name": "Content Delivery Networks",
        "proxies": [
            {"Trusted Source": "Content Server"},
            {"Blue Coat": "Content Delivery Networks"},
            {"fortiguard": "Content Servers"},
            {"Palo Alto Networks": "Content Delivery Networks"},
            {"Trend Micro": "Pay to Surf"},
        ],
    },
    {
        "name": "Dating",
        "proxies": [
            {"Trusted Source": "Dating/Personals"},
            {"Blue Coat": "Personals/Dating"},
            {"fortiguard": "Dating"},
            {"Palo Alto Networks": "Dating"},
            {"Trend Micro": "Personals / Dating"},
        ],
    },
    {
        "name": "Education",
        "proxies": [
            {"Trusted Source": "Education/Reference"},
            {"Blue Coat": "Education"},
            {"fortiguard": "Education"},
            {"Palo Alto Networks": "Educational Institutions"},
            {"Trend Micro": "Education"},
        ],
    },
    {
        "name": "Entertainment",
        "proxies": [
            {"Trusted Source": "Entertainment"},
            {"Blue Coat": "Entertainment"},
            {"fortiguard": "Entertainment"},
            {"Palo Alto Networks": "Entertainment and Arts"},
            {"Trend Micro": "Entertainment"},
        ],
    },
    {
        "name": "Finance",
        "proxies": [
            {"Trusted Source": "Finance/Banking"},
            {"Blue Coat": "Finance"},
            {"fortiguard": "Finance and Banking"},
            {"Palo Alto Networks": "Financial Services"},
            {"Trend Micro": "Financial Services"},
        ],
    },
    {
        "name": "For Kids",
        "proxies": [
            {"Trusted Source": "For Kids"},
            {"Blue Coat": "For Kids"},
            {"fortiguard": "Child Education"},
            {"Palo Alto Networks": "Entertainment and Arts"},
            {"Trend Micro": "For Kids"},
        ],
    },
    {
        "name": "Games",
        "proxies": [
            {"Trusted Source": "Games"},
            {"Blue Coat": "Games"},
            {"fortiguard": "Games"},
            {"Palo Alto Networks": "Games"},
            {"Trend Micro": "Games"},
        ],
    },
    {
        "name": "News",
        "proxies": [
            {"Trusted Source": "General News"},
            {"Blue Coat": "News"},
            {"fortiguard": "News and Media"},
            {"Palo Alto Networks": "News"},
            {"Trend Micro": "News / Media"},
        ],
    },
    {
        "name": "Government",
        "proxies": [
            {"Trusted Source": "Government/Military"},
            {"Blue Coat": "Government/Legal"},
            {"fortiguard": "Government and Legal Organizations"},
            {"Palo Alto Networks": "Government"},
            {"Trend Micro": "Government / Legal"},
        ],
    },
    {
        "name": "Health",
        "proxies": [
            {"Trusted Source": "Health"},
            {"Blue Coat": "Health"},
            {"fortiguard": "Health and Wellness"},
            {"Palo Alto Networks": "Health and Medicine"},
            {"Trend Micro": "Health"},
        ],
    },
    {
        "name": "Humor",
        "proxies": [
            {"Trusted Source": "Humor/Comics"},
            {"Blue Coat": "Humor/Jokes"},
            {"fortiguard": "Entertainment"},
            {"Palo Alto Networks": "Entertainment and Arts"},
            {"Trend Micro": "Humor"},
        ],
    },
    {
        "name": "Hunting and Fishing",
        "proxies": [
            {"Trusted Source": "Entertainment"},
            {"Blue Coat": "Entertainment"},
            {"fortiguard": "Entertainment"},
            {"Palo Alto Networks": "Hunting and Fishing"},
            {"Trend Micro": "Gun Clubs / Hunting"},
        ],
    },
    {
        "name": "Job Search",
        "proxies": [
            {"Trusted Source": "Job Search"},
            {"Blue Coat": "Job Search/Careers"},
            {"fortiguard": "Job Search"},
            {"Palo Alto Networks": "Job Search"},
            {"Trend Micro": "Job Search / Careers"},
        ],
    },
    {
        "name": "Military",
        "proxies": [
            {"Trusted Source": "Government/Military"},
            {"Blue Coat": "Military"},
            {"fortiguard": "Armed Forces"},
            {"Palo Alto Networks": "Military"},
            {"Trend Micro": "Military"},
        ],
    },
    {
        "name": "Politics/Opinion",
        "proxies": [
            {"Trusted Source": "Politics/Opinion"},
            {"Blue Coat": "Political/Social Advocacy"},
            {"fortiguard": "Political Organizations"},
            {"Palo Alto Networks": "Philosophy and Political Advocacy"},
            {"Trend Micro": "Politics"},
        ],
    },
    {
        "name": "Real Estate",
        "proxies": [
            {"Trusted Source": "Real Estate"},
            {"Blue Coat": "Real Estate"},
            {"fortiguard": "Real Estate"},
            {"Palo Alto Networks": "Real Estate"},
            {"Trend Micro": "Real Estate"},
        ],
    },
    {
        "name": "Religion",
        "proxies": [
            {"Trusted Source": "Religion/Ideology"},
            {"Blue Coat": "Religion"},
            {"fortiguard": "Global Religion"},
            {"Palo Alto Networks": "Religion"},
            {"Trend Micro": "Religion"},
        ],
    },
    {
        "name": "Restaurants",
        "proxies": [
            {"Trusted Source": "Restaurants"},
            {"Blue Coat": "Restaurants/Food"},
            {"fortiguard": "Restaurant and Dining"},
            {"Palo Alto Networks": "Shopping"},
            {"Trend Micro": "Restaurants / Food"},
        ],
    },
    {
        "name": "Search Engines",
        "proxies": [
            {"Trusted Source": "Search Engines"},
            {"Blue Coat": "Search Engines/Portals"},
            {"fortiguard": "Search Engines and Portals"},
            {"Palo Alto Networks": "Search Engines"},
            {"Trend Micro": "Search Engines / Portals"},
        ],
    },
    {
        "name": "Shopping",
        "proxies": [
            {"Trusted Source": "Online Shopping"},
            {"Blue Coat": "Shopping"},
            {"fortiguard": "Shopping"},
            {"Palo Alto Networks": "Shopping"},
            {"Trend Micro": "Shopping"},
        ],
    },
    {
        "name": "Social Networking",
        "proxies": [
            {"Trusted Source": "Social Networking"},
            {"Blue Coat": "Social Networking"},
            {"fortiguard": "Social Networking"},
            {"Palo Alto Networks": "Social Networking"},
            {"Trend Micro": "Social Networking"},
        ],
    },
    {
        "name": "Sports",
        "proxies": [
            {"Trusted Source": "Sports"},
            {"Blue Coat": "Sports/Recreation"},
            {"fortiguard": "Sports"},
            {"Palo Alto Networks": "Sports"},
            {"Trend Micro": "Sports"},
        ],
    },
    {
        "name": "Travel",
        "proxies": [
            {"Trusted Source": "Travel"},
            {"Blue Coat": "Travel"},
            {"fortiguard": "Travel"},
            {"Palo Alto Networks": "Travel"},
            {"Trend Micro": "Travel"},
        ],
    },
    {
        "name": "Web Hosting",
        "proxies": [
            {"Trusted Source": "Internet Services"},
            {"Blue Coat": "Web Hosting"},
            {"fortiguard": "Web Hosting"},
            {"Palo Alto Networks": "Web Hosting"},
            {"Trend Micro": "Web Hosting"},
        ],
    },
]
