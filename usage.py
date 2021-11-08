from  dash import html
import dash_tagcloud
from app import create_app, serve_app

app = create_app()

data = [
  { "text": 'Hey', "value": 1000 },
  { "text": 'lol', "value": 200 },
  { "text": 'first impression', "value": 800 },
  { "text": 'very cool', "value": 1000 },
  { "text": 'duck', "value": 10 },
]

security_data = [
  {
    "text": "Leveraged/Inverse",
    "value": 265
  },
  {
    "text": "Trading",
    "value": 265
  },
  {
    "text": "Equity",
    "value": 1481
  },
  {
    "text": "Large Cap",
    "value": 500
  },
  {
    "text": "US",
    "value": 198
  },
  {
    "text": "Blend",
    "value": 311
  },
  {
    "text": "Other",
    "value": 237
  },
  {
    "text": "Global",
    "value": 372
  },
  {
    "text": "Emerging Markets",
    "value": 125
  },
  {
    "text": "Bond",
    "value": 463
  },
  {
    "text": "USD",
    "value": 170
  },
  {
    "text": "Government",
    "value": 110
  },
  {
    "text": "Europe",
    "value": 120
  },
  {
    "text": "Sector",
    "value": 249
  },
  {
    "text": "Technology",
    "value": 64
  },
  {
    "text": "Commodities",
    "value": 192
  },
  {
    "text": "Japan",
    "value": 56
  },
  {
    "text": "Corporate",
    "value": 106
  },
  {
    "text": "Precious Metals",
    "value": 55
  },
  {
    "text": "Broad Basket",
    "value": 41
  },
  {
    "text": "Eurozone",
    "value": 55
  },
  {
    "text": "Consumer",
    "value": 27
  },
  {
    "text": "Goods",
    "value": 27
  },
  {
    "text": "Services",
    "value": 50
  },
  {
    "text": "Value",
    "value": 47
  },
  {
    "text": "Income",
    "value": 47
  },
  {
    "text": "UK",
    "value": 39
  },
  {
    "text": "ex Japan",
    "value": 47
  },
  {
    "text": "Asia",
    "value": 43
  },
  {
    "text": "EUR",
    "value": 90
  },
  {
    "text": "Energy",
    "value": 48
  },
  {
    "text": "Financial",
    "value": 23
  },
  {
    "text": "China",
    "value": 34
  },
  {
    "text": "Industrial",
    "value": 31
  },
  {
    "text": "Materials",
    "value": 20
  },
  {
    "text": "Healthcare",
    "value": 19
  },
  {
    "text": "High Yield",
    "value": 43
  },
  {
    "text": "Small Cap",
    "value": 32
  },
  {
    "text": "Pacific",
    "value": 27
  },
  {
    "text": "A Shares",
    "value": 13
  },
  {
    "text": "GBP",
    "value": 43
  },
  {
    "text": "Flex Cap",
    "value": 23
  },
  {
    "text": "India",
    "value": 12
  },
  {
    "text": "Korea",
    "value": 12
  },
  {
    "text": "Inflation Linked",
    "value": 25
  },
  {
    "text": "Brazil",
    "value": 11
  },
  {
    "text": "Broad",
    "value": 14
  },
  {
    "text": "Metals",
    "value": 11
  },
  {
    "text": "Local Currency",
    "value": 14
  },
  {
    "text": "Property",
    "value": 26
  },
  {
    "text": "Indirect",
    "value": 26
  },
  {
    "text": "Russia",
    "value": 10
  },
  {
    "text": "Communications",
    "value": 10
  },
  {
    "text": "Utilities",
    "value": 10
  },
  {
    "text": "Growth",
    "value": 16
  },
  {
    "text": "ex UK",
    "value": 9
  },
  {
    "text": "Latin",
    "value": 9
  },
  {
    "text": "America",
    "value": 12
  },
  {
    "text": "Ecology",
    "value": 9
  },
  {
    "text": "Canada",
    "value": 8
  },
  {
    "text": "Money",
    "value": 8
  },
  {
    "text": "Market",
    "value": 8
  },
  {
    "text": "Biotechnology",
    "value": 8
  },
  {
    "text": "Taiwan",
    "value": 8
  },
  {
    "text": "Fixed",
    "value": 8
  },
  {
    "text": "Grains",
    "value": 7
  },
  {
    "text": "Short Term",
    "value": 30
  },
  {
    "text": "Ultra",
    "value": 7
  },
  {
    "text": "Hedged",
    "value": 23
  },
  {
    "text": "Natural",
    "value": 7
  },
  {
    "text": "Resources",
    "value": 7
  },
  {
    "text": "Mid Cap",
    "value": 33
  },
  {
    "text": "Australia",
    "value": 6
  },
  {
    "text": "New",
    "value": 6
  },
  {
    "text": "Zealand",
    "value": 6
  },
  {
    "text": "Small/",
    "value": 11
  },
  {
    "text": "Water",
    "value": 6
  },
  {
    "text": "Turkey",
    "value": 6
  },
  {
    "text": "Softs",
    "value": 5
  },
  {
    "text": "Germany",
    "value": 6
  },
  {
    "text": "RMB",
    "value": 5
  },
  {
    "text": "Onshore",
    "value": 5
  },
  {
    "text": "Infrastructure",
    "value": 5
  },
  {
    "text": "South",
    "value": 5
  },
  {
    "text": "Africa",
    "value": 7
  },
  {
    "text": "Namibia",
    "value": 5
  },
  {
    "text": "Diversified",
    "value": 17
  },
  {
    "text": "Alt",
    "value": 13
  },
  {
    "text": "Systematic",
    "value": 4
  },
  {
    "text": "Futures",
    "value": 4
  },
  {
    "text": "ex Russia",
    "value": 4
  },
  {
    "text": "Emerging",
    "value": 6
  },
  {
    "text": "Indonesia",
    "value": 4
  },
  {
    "text": "Islamic",
    "value": 7
  },
  {
    "text": "Alternative",
    "value": 4
  },
  {
    "text": "Relative",
    "value": 3
  },
  {
    "text": "Arbitrage",
    "value": 3
  },
  {
    "text": "Agriculture",
    "value": 5
  },
  {
    "text": "Livestock",
    "value": 3
  },
  {
    "text": "Long",
    "value": 3
  },
  {
    "text": "Term",
    "value": 3
  },
  {
    "text": "Italy",
    "value": 3
  },
  {
    "text": "Not Categorised",
    "value": 3
  },
  {
    "text": "North",
    "value": 3
  },
  {
    "text": "Private",
    "value": 3
  },
  {
    "text": "Currency",
    "value": 2
  },
  {
    "text": "BRIC",
    "value": 2
  },
  {
    "text": "Convertible",
    "value": 2
  },
  {
    "text": "France",
    "value": 2
  },
  {
    "text": "Biased",
    "value": 2
  },
  {
    "text": "Frontier",
    "value": 2
  },
  {
    "text": "Markets",
    "value": 2
  },
  {
    "text": "Israel",
    "value": 2
  },
  {
    "text": "Large/",
    "value": 2
  },
  {
    "text": "Nordic",
    "value": 2
  },
  {
    "text": "Poland",
    "value": 2
  },
  {
    "text": "Switzerland",
    "value": 2
  },
  {
    "text": "Thailand",
    "value": 2
  },
  {
    "text": "Moderate",
    "value": 3
  },
  {
    "text": "Allocation",
    "value": 5
  },
  {
    "text": "Vietnam",
    "value": 2
  },
  {
    "text": "Middle",
    "value": 1
  },
  {
    "text": "East",
    "value": 1
  },
  {
    "text": "Flexible",
    "value": 1
  },
  {
    "text": "Subordinated",
    "value": 1
  },
  {
    "text": "Moderately",
    "value": 2
  },
  {
    "text": "Adventurous",
    "value": 1
  },
  {
    "text": "Cautious",
    "value": 1
  },
  {
    "text": "Netherlands",
    "value": 1
  },
  {
    "text": "Spain",
    "value": 1
  },
  {
    "text": "Sweden",
    "value": 1
  }
]



app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1('Dash Tag Cloud'),
            dash_tagcloud.DashTagcloud(data=security_data, className='tag-cloud',
                    spiral="rectangular", fontSize=4)
            ], className='app-inner')
    ], className='app-outer')
])

if __name__ == '__main__':
    serve_app(app)
